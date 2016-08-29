from django.contrib.admin import AdminSite


class EdcExampleProjectAdminSite(AdminSite):
    site_header = 'Example Project'
    site_title = 'Example Project'
    index_title = 'Example Project Administration'
    site_url = '/'
edc_example_project_admin = EdcExampleProjectAdminSite(name='edc_example_project_admin')
