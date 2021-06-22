from django.conf.urls import url
from tutorial_app import views

urlpatterns = [
	url(r'^language/$', views.language_list),
	url(r'^language/(?P<pk>[0-9]+)$', views.language_detail),
]
