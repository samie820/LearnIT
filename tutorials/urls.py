from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^series/(?P<slug>[-\w]+)/$',views.tutorial_series_detail,name='tutorial_series_detail'),
    url(r'^series/$',views.TutoriialSeriesList.as_view(),name='tutorial_series_List'),
    url(r'^series/(?P<tutorial_series>[-\w]+)/(?P<slug>[-\w]+)/$',views.lessons_detail,name='lesson_detail')
]