from django.conf.urls import url

from . import views

app_name = "parking"

urlpatterns = [
    url(r'^$', views.request_msg, name='request_msg'),
]
