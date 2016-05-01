from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_users', views.get_users),
    url(r'^get_foods', views.get_foods),
    url(r'^$', views.home),
    url(r'^new_food/(?P<name>[\w\-]+)/(?P<calorific_value>[\d\-]+)/(?P<diabetes>\d)/(?P<hypertension>\d)/(?P<high_cholesterol>\d)/(?P<anemia>\d)/$',
        views.new_food),

]
