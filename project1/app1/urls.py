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
    path('buy/<int:ice_id>/',views.buy, name='buy'),
    # path('ice_av/<int:avalible_ice>/',views.total_ice, name='t-ice')
      # admin

    path('admin/', views.admin_login, name='admin_login'),
    path('admin_home/', views.admin_home, name='admin_home'),  # ✅ name now matches redirect
    path('update/<int:id>/', views.update, name='update'),
    path('add/', views.add, name='add'), 
    path('add_store/', views.add_store, name='add'),
    path('delete_cus/', views.delete_cus, name='delete_cus'),
    path('logout/', views.logout, name='logout')
    # path('delete_cus/', views.delete_cus, name='delete_cus'),

  




    # path('admin/',views.prodects, name='login')
]
