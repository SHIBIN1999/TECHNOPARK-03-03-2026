
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('add_company/',views.add_Company,name='add_company'),
    path('add_job/',views.add_job,name='add_job'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit_job,name='edit_job'),
    path('home_company',views.home_company,name='home_company'),
    path('edit_company/<int:id>',views.edit_company,name='edit_company'),
    path('delete_company/<int:id>',views.delete_company,name='delete_company')
    

]