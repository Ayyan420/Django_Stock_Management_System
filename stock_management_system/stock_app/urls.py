from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from django.urls import include


from django.conf import settings



from django.conf.urls.static import static

#now import the views.py file into this code

from . import views

urlpatterns=[
    path('',views.list_items , name = "List Items"),
    path('list_items/',views.list_items , name = "List Items"),
    path('send_e_mail/',views.send_e_mail , name = "Send E-Mail"),
    path('send_ee_mail/',views.send_ee_mail , name = "send_ee_mail"),
    path('add_items/',views.add_items , name = "Add Items"),
    path('update_items/<int:id_get>',views.update_items , name = "Update_Items"),
    path('del_items/<int:id_get>',views.del_items , name = "Del_Items"),
    path('stock_detail/<int:id_pk>',views.stock_detail, name = "Stock_detail"),
    path('issue_items/<int:id_pk>',views.issue_items, name = "Issue_items"),
    path('receive_items/<int:id_pk>',views.receive_items, name = "Receive_items"),
    path('reorder_items/<int:id_pk>',views.reorder_items, name = "Reorder_items"),
    path('list_history/',views.list_history, name = "List_history"),
    path('create_category/',views.create_category, name = "Create_category"),
    path('del_categories/<int:id_get>',views.del_categories , name = "Del_categories"),
]







# for file handlein

# run only in debug mode



# pip install repotlab
# pip install django-registration-redux

# then after addd in settings add in sett then migrate