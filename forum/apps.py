"""
Forum Config class
"""
from django.apps import AppConfig


class ForumConfig(AppConfig):
    """
    Forum config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forum'