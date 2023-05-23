from django.urls import path
from . import views

urlpatterns=[
    path('',views.book_create),
    path('list/',views.book_list),
]