"""Convenience module for accessing settings relating to the attachments app,
providing default values where configuration is not specified."""

from django.conf import settings

ATTACHMENTS_UPLOAD_PATH = getattr(settings, "ATTACHMENTS_UPLOAD_PATH", "attachments/")
