from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about1'),
    path('show/',views.show, name='show'),
    path('rev/',views.rev,name='rev'),
    path('cat/',views.cat,name='cat'),
    path('stores/',views.other_stores, name="stores"),
    path('ice_dec/<int:ice_id>/', views.ice_dec, name="ice_dec"),
    path('buy/<int:ice_id>/',views.buy, name='buy')
    # path('ice_av/<int:avalible_ice>/',views.total_ice, name='t-ice')
]
