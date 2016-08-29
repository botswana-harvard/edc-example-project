from django.contrib import admin

from edc_example.models import SubjectConsent

from .admin_site import edc_example_project_admin


@admin.register(SubjectConsent, site=edc_example_project_admin)
class SubjectConsentAdmin(admin.ModelAdmin):
    pass
