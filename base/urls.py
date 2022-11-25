from django.urls import path

from base import views

app_name = 'base'
urlpatterns = [

    path('', views.home, name='home'),
    path('addlisting', views.addlisting, name='listing'),
    path('listingpage', views.listpage, name='listpage'),
    path('listingpage/<str:pk>', views.listpage, name='page'),
    path('Updatelistingpage/<str:pk>', views.updatelistpage, name='updatelistpage')
]
