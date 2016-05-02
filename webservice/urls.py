from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_users', views.get_users),
    url(r'^get_foods', views.get_foods),
    url(r'^$', views.home),
    url(
        r'^new_food/(?P<name>[\w\-]+)/(?P<calorific_value>[\d\-]+)/(?P<diabetes>\d)/(?P<hypertension>\d)/(?P<high_cholesterol>\d)/(?P<anemia>\d)/$',
        views.new_food),
    url(
        r'^new_user/(?P<username>[\w\-]+)/(?P<password>[\w\-]+)/(?P<name>[\w\-]+)/(?P<email>[\w.-]+@[\w.-]+)/(?P<photo>[\w.-]+)/(?P<level>[\d\-]+)/(?P<age>[\d\-]+)/(?P<height>[\d\-]+)/(?P<weight>[\d\-]+)/(?P<score>[\d\-]+)/(?P<diabetes>\d)/(?P<hypertension>\d)/(?P<high_cholesterol>\d)/(?P<anemia>\d)/$',
        views.new_user),
    url(
        r'^update_food/(?P<pk>[\d\-]+)/(?P<name>[\w\-]+)/(?P<calorific_value>[\d\-]+)/(?P<diabetes>\d)/(?P<hypertension>\d)/(?P<high_cholesterol>\d)/(?P<anemia>\d)/$',
        views.update_food),
    url(
        r'^update_user/(?P<pk>[\d\-]+)/(?P<username>[\w\-]+)/(?P<password>[\w\-]+)/(?P<name>[\w\-]+)/(?P<email>[\w.-]+@[\w.-]+)/(?P<photo>[\w.-]+)/(?P<level>[\d\-]+)/(?P<age>[\d\-]+)/(?P<height>[\d\-]+)/(?P<weight>[\d\-]+)/(?P<score>[\d\-]+)/(?P<diabetes>\d)/(?P<hypertension>\d)/(?P<high_cholesterol>\d)/(?P<anemia>\d)/$',
        views.update_user)

]
