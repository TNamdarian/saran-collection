"""
Views for Forum, including threads and comments,
also to add, edit and delete threads and comments.
The majority of this app was generally influenced by Selmi Tech's
youtube tutorial series on how to create a Forum App but it
was used to understand general principles of how to work with
Django and Python including Views and Modals. Reference:
https://www.youtube.com/watch?v=knGk9aUr4Do
"""

from django.shortcuts import render, redirect, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import ThreadForm, CommentForm
from .models import Thread, Comment


@login_required
def forum_view(request):
    """
    This renders the forum page. To access this page, a user needs
    to be logged in. All the current threads will display.
    """
    if not request.user.is_authenticated:
        messages.error(
            request, 'You must be logged in to see the Coffee Forum')
        return redirect(reverse('login'))

    threads = Thread.objects.all().order_by('-date_created')

    # Pagination: https://docs.djangoproject.com/en/3.2/topics/pagination/
    paginator = Paginator(threads, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    threads_page = True

    context = {
        'page_obj': page_obj,
        'threads_page': threads_page,
    }

    return render(request, 'forum/forum.html', context)


# Class Based views: https://bit.ly/3p0oH2F
# Login & Security: https://bit.ly/3iVyCma
# https://stackoverflow.com/questions/42698197/is-there-django-list-view-model-sort

# --- THREAD VIEW FUNCTION --- #
class ThreadView(LoginRequiredMixin, DetailView):
    """
    This renders the thread page for a single thread. To access
    this page, a user needs to be logged in.
    """
    model = Thread
    template_name = "forum/thread.html"

    def get_context_data(self, **kwargs):
        """
        This function is to show number and the actual comments related to a
        specific thread. To access this page, a user needs to be logged in.
        """
        context = super(ThreadView, self).get_context_data(**kwargs)
        # For presenting extra content via context: https://bit.ly/3v97u8e
        context['comments'] = self.object.comments.all()
        context['comments_count'] = self.object.comments.count()
        return context


# --- ADD A THREAD FUNCTION --- #
class AddThreadView(LoginRequiredMixin, CreateView, SuccessMessageMixin):
    """
    This renders the page to add a new thread. It has a form with feedback
    and a success message with SuccessMessageMixin. Use of LoginRequiredMixin
    to access this page, a user needs to be logged in. Use of CreateView to
    display a form for creating an object.
    """
    model = Thread
    form_class = ThreadForm
    success_message = "Thread '%(title)s' was created successfully"
    template_name = "forum/add_thread.html"

    # Exclude creator field from form https://bit.ly/3v7p3Fn
    def form_valid(self, form):
        """
        To ensure that the creator field is not included in the list of fields
        to edit, and override form_valid() to add the user.
        """
        form.instance.creator = self.request.user
        return super().form_valid(form)


# --- EDIT A THREAD FUNCTION --- #
class EditThreadView(LoginRequiredMixin, UpdateView, UserPassesTestMixin,
                     SuccessMessageMixin):
    """
    This renders the page to edit a thread. It has a form with feedback
    and a success message with SuccessMessageMixin. Use of LoginRequiredMixin
    to access this page, a user needs to be logged in. Use of
    UserPassesTestMixin to limit access to logged-in users that pass a test
    namely, they should have created the thread or they are an admin user.
    """
    model = Thread
    form_class = ThreadForm
    success_message = "Thread '%(title)s' was updated successfully"
    template_name = "forum/edit_thread.html"

    # User permissions: https://bit.ly/3mSsegO
    def test_func(self):
        """
        This makes sure only the creator of the thread and superusers can edit
        the thread.
        """
        thread = self.get_object()
        if self.request.user == thread.creator:
            return True
        elif self.request.user.is_superuser:
            return True
        return False


# --- DELETE A THREAD FUNCTION --- #
class DeleteThreadView(LoginRequiredMixin, DeleteView, UserPassesTestMixin,
                       SuccessMessageMixin):
    """
    This renders the page to delete a thread. This is to bring in defensive
    coding to make sure user wants to delete a thread. On deletion there
    is feedback with a success message with SuccessMessageMixin. Use of
    LoginRequiredMixin to access this page, a user needs to be logged in. Use
    of UserPassesTestMixin to limit access to logged-in users that pass a test
    namely, they should have created the thread or they are an admin user. Use
    of DeleteView which is built-in Django to assist with deleting.
    """
    model = Thread
    template_name = "forum/delete_thread.html"
    success_message = "The Thread was successfully deleted."
    success_url = reverse_lazy('forum')

    # User permissions: https://bit.ly/3mSsegO
    def test_func(self):
        """
        This is to set the paramaters for UserPassesTestMixin so that only
        users who created the thread or if they are an admin user can delete
        a thread.
        """
        thread = self.get_object()
        if self.request.user == thread.creator:
            return True
        elif self.request.user.is_superuser:
            return True
        return False

    # Success message in DeleteView: https://bit.ly/3oRYlzG
    def delete(self, request, *args, **kwargs):
        """
        This renders a feedback success message related to SuccessMessageMixin
        once the thread is successfully deleted.
        """
        messages.success(self.request, self.success_message)
        return super(DeleteThreadView, self).delete(request, *args, **kwargs)


# --- ADD A COMMENT FUNCTION --- #
class AddCommentView(LoginRequiredMixin, CreateView, SuccessMessageMixin):
    """
    This renders the page to add a new comment to a thread. It has a form with
    feedback and a success message with SuccessMessageMixin. Use of
    LoginRequiredMixin to access this page, a user needs to be logged in. Use
    of CreateView to display a form for creating an object.
    """
    model = Comment
    template_name = "forum/add_comment.html"
    success_message = "Your comment was added successfully the Thread."
    form_class = CommentForm

    # Function to set the ridirect page https://bit.ly/3BPwunz
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('forum'))

    # Exclude creator field from form https://bit.ly/3v7p3Fn
    def form_valid(self, form):
        """
        This overrides form_valid() to add the logged in user as the creator of
        the comment.
        """
        form.instance.thread_id = self.kwargs['pk']
        form.instance.creator = self.request.user
        return super().form_valid(form)


# --- EDIT A COMMENT FUNCTION --- #
class EditCommentView(LoginRequiredMixin, UpdateView, UserPassesTestMixin,
                      SuccessMessageMixin):
    """
    This renders the page to edit a comment. It has a form with feedback
    and a success message with SuccessMessageMixin. Use of LoginRequiredMixin
    to access this page, a user needs to be logged in. Use of
    UserPassesTestMixin to limit access to logged-in users that pass a test
    namely, they should have created the thread or they are an admin user.
    """
    model = Comment
    template_name = "forum/edit_comment.html"
    success_message = "Your comment was updated successfully"
    form_class = CommentForm

    # Function to set the ridirect page https://bit.ly/3BPwunz
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('forum'))

    # User permissions: https://bit.ly/3mSsegO
    def test_func(self):
        """
        This makes sure only the creator of the comment and superusers can edit
        the comment.
        """
        comment = self.get_object()
        if self.request.user == comment.creator:
            return True
        elif self.request.user.is_superuser:
            return True
        return False


# --- DELETE A COMMENT FUNCTION --- #

class DeleteCommentView(LoginRequiredMixin, DeleteView, UserPassesTestMixin,
                        SuccessMessageMixin):
    """
    This renders the page to delete a comment. This is to bring in defensive
    coding to make sure user wants to delete a comment. On deletion there
    is feedback with a success message with SuccessMessageMixin. Use of
    LoginRequiredMixin to access this page, a user needs to be logged in. Use
    of UserPassesTestMixin to limit access to logged-in users that pass a test
    namely, they should have created the comment or they are an admin user. Use
    of DeleteView which is built-in Django to assist with deleting.
    """
    model = Comment
    success_message = "Your comment was successfully deleted"
    template_name = "forum/delete_comment.html"

    # Function to set the ridirect page https://bit.ly/3BPwunz
    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('forum'))

    # User permissions: https://bit.ly/3mSsegO
    def test_func(self):
        """
        This is to set the paramaters for UserPassesTestMixin so that only
        users who created the comment or if they are an admin user can delete
        a comment.
        """
        comment = self.get_object()
        if self.request.user == comment.creator:
            return True
        elif self.request.user.is_superuser:
            return True
        return False

    # Success message in DeleteView: https://bit.ly/3oRYlzG
    def delete(self, request, *args, **kwargs):
        """
        This renders a feedback success message related to SuccessMessageMixin
        once the comment for the thread is successfully deleted.
        """
        messages.success(self.request, self.success_message)
        return super(DeleteCommentView, self).delete(request, *args, **kwargs)