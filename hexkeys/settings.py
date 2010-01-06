"""
Convenience module for access of custom application settings,
which enforces default settings when the main settings module does not
contain the appropriate settings.
"""
from django.conf import settings

ENCODING_ALPHABET = getattr(settings, 'HEXKEYS_ENCODING_ALPHABET', 
		"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
