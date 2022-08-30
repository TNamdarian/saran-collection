"""
Forum Models including Thread and Comment
The majority of this app was generally influenced by Selmi Tech's
youtube tutorial series on how to create a Forum App but it
was used to understand general principles of how to work with
Django and Python including Views and Modals. Reference:
https://www.youtube.com/watch?v=knGk9aUr4Do
"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Thread(models.Model):
    """
    Model for threads in forum app. There field that links to
    the User model by foreign key. The fields include a Thread,
    title, who created it, the description and dates for when the
    thread was created and edited.
    """
    title = models.CharField(max_length=60)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    # Represents the class objects as a string
    # To return a string of the thread title the creator of it
    # https://www.python-course.eu/python3_magic_methods.php
    def __str__(self):
        return self.title + ' by ' + str(self.creator)

    # To handle named arguments not yet defined from:
    # https://docs.python.org/2/tutorial/controlflow.html#keyword-arguments
    def get_absolute_url(self):
        """
        Function to return the url with the thread and the pk
        """
        return reverse('thread', kwargs={'pk': self.pk})


class Comment(models.Model):
    """
    Model for comments related a thread. There field that links to
    the Thread model by foreign key. It also links to the User
    model with foreign key. There is also a field for the date
    the comment was created and edited.
    """
    thread = models.ForeignKey(Thread, related_name="comments",
                               on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.TextField(max_length=1200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        # From: https://www.geeksforgeeks.org/python-string-format-method/
        return 'On {} by {}'.format(self.thread, self.creator)
