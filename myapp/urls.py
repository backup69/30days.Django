from django.urls import path
from . import views
urlpatterns=[
    #specify new url
    # as a back end developer my focus is 

    path('', views.index, name='index'),
    # path('counter', views.counter ,name='counter')
    path('counter',views.counter,name='counter')
]
    
