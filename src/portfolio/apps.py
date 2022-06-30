""" fichero apps de portfolio """

from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    """
    PortfolioConfig: configuraciones de la app portfolio
    para el admin site
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
    verbose_name = 'Portafolio'
