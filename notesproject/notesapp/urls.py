from django.urls import path

from . import views

urlpatterns = [
    path('notes-table', views.notesTable, name='notes-table'),
    path('notes-create', views.notesCreate, name='notes-create'),
    path('notes-update/<int:id>', views.notesUpdate, name='notes-update'),
    path('notes-delete/<int:id>', views.notesDelete, name='notes-delete')
]
