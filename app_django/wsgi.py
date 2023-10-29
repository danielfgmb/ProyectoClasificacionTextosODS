"""
WSGI config for app_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from ods_translator.load_joblib import df_preprocess, tokenize_df

from django.core.wsgi import get_wsgi_application
import joblib

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_django.settings')


application = get_wsgi_application()
