from django.conf.urls import url, include
from django.contrib import admin

from edc_base.views import LoginView, LogoutView

from .views import HomeView

urlpatterns = [
    url(r'login', LoginView.as_view(), name='login_url'),
    url(r'logout', LogoutView.as_view(pattern_name='login_url'), name='logout_url'),
    url(r'^admin/', admin.site.urls),
    url(r'^call/', include('edc_call_manager.urls', namespace='edc-call-manager')),
    url(r'^consent/', include('edc_consent.urls', namespace='edc-consent')),
    url(r'^label/', include('edc_label.urls', namespace='edc-label')),
    url(r'^lab/', include('edc_lab.urls', namespace='edc-lab')),
    url(r'^visit_schedule/', include('edc_visit_schedule.urls', namespace='edc-visit-schedule')),
    url(r'^edc/', include('edc_base.urls', namespace='edc-base')),
    url(r'^', HomeView.as_view(), name='home_url'),
]
