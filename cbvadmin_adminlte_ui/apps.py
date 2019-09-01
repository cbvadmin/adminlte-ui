from django.apps import AppConfig
from cbvadmin.sites import site


class CBVAdminConfig(AppConfig):
    name = 'cbvadmin_adminlte_ui'
    verbose_name = 'AdminLTE'

    def ready(self):
        super(CBVAdminConfig, self).ready()
        site.register('adminlte', self, 'template_pack')
