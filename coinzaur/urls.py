from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from django.views.generic import CreateView

from coinzaur.forms import UserCreationForm


urlpatterns = [
    # Admin site
    url(r'^admin/', include(admin.site.urls)),

    # User Auth
    url(r'^login/$', views.login, {'template_name': 'index/auth/login.html'}, name="login"),
    url(r'^logout/$', views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^register/$', CreateView.as_view(
        template_name="index/auth/register.html",
        form_class=UserCreationForm,
        success_url="/login"), name='register'),
    url(r'^password_change/$', views.password_change, name='password_change'),
    url(r'^password_change/done/$', views.password_change_done, name='password_change_done'),
    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', views.password_reset_complete, name='password_reset_complete'),

    # Front page
    url(r'^', include('index.urls')),
]