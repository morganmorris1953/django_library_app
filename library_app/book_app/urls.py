from django.urls import path, include
from .views import *    #third version, makes it so i don't have to type "views.index" below


urlpatterns = [
    # path('', ),
    path("", index, name='book_list'),
    path("new", book_create, name="book_create"),
    path('<int:book_id>', book_view, name='book_details'),
    path('<int:book_id>/update', book_update, name='book_update'),
    path('<int:book_id>/delete', book_delete, name='book_delete'),
]