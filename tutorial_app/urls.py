from django.conf.urls import url
from tutorial_app import views

urlpatterns = [
	url(r'^categories/$', views.category_list),
	url(r'^language/(?P<pk>[0-9]+)$', views.category_detail),
]
