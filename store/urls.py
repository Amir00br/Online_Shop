from django.urls import path
from . import views

urlpatterns = [
    path('createcus', views.createcus , name='createcus'),
    path('logcus', views.logcus,name='logcus'),
    path('deletecus', views.deletecus,name='deletecus'),
    path('updatacus', views.updatacus,name='updatacus'),
    path('allcus', views.allcus,name='allcus'),


    path('logadmin', views.logadmin,name='logadmin'),

    path('createpro', views.createpro,name='createpro'),
    path('allpro', views.allpro,name='allpro'),
    path('deletepro', views.deletepro,name='deletepro'),
    path('updatapro', views.updatapro,name='updatapro'),




    path('createcate', views.createcate,name='createcate'),
    path('allcate', views.allcate,name='allcate'),
    path('deletecate', views.deletecate,name='deletecate'),
    path('updatacate', views.updatacate,name='updatacate'),

    path('createorder', views.createorder,name='createorder'),
    path('deleteorder', views.deleteorder,name='deleteorder'),
    path('allorder', views.allorder,name='allorder'),




   

    path('brow', views.brow,name='brow'),
    path('addcart', views.addcart,name='addcart'),










  
    
   # path('data/login', views.login , name='login'),
]