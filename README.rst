====================
CBVadmin AdminLTE UI
====================

Template pack for CBVadmin using AdminLTE.io css framework


Installing and configuring
==========================

Install from PyPi

``pip install cbvadmin-adminlte-ui``

Install from Git

``pip install git+https://github.com/cbvadmin/adminlte-ui.git``

Add the following to django settings.py

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'cbvadmin_adminlte_ui',
    ]
    ...
    CBVADMIN_TEMPLATE_PACK': 'adminlte',
    CRISPY_TEMPLATE_PACK': 'bootstrap3',
    CRISPY_ALLOWED_TEMPLATE_PACKS': ('bootstrap3',)
