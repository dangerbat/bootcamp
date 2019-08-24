from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ArticlesConfig(AppConfig):
    name = 'applications.articles'
    verbose_name = _('Articles')
