from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_entry/", views.add_entry, name="add_entry"),
    path("search/", views.search, name="search"),
    path("wiki/<str:title>/", views.entry, name="entry"),
    path("save_entry/", views.save_entry, name="save_entry"),
    path("edit_entry/<str:title>/", views.edit_entry, name="edit_entry"),
    path("save_edit/<str:title>/", views.save_edit, name="save_edit"),
    path("random_page/", views.random_page, name="random_page")
]
