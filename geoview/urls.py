from django.conf.urls import url
from django.views.generic import TemplateView
from .views import index

urlpatterns = [
    url(r'^$', index, name='home'),
]
