from django.urls import path 
from . import views

app_name = "myMovieReviews"

urlpatterns = [
    path ('', views.movie_list, name="list"),
    path("<int:pk>/", views.movie_detail, name="detail"),
    path('create/', views.movie_create, name="create"),
    path("<int:pk>/update", views.movie_update, name="update"),
    path("<int:pk>/delete", views.movie_delete, name="delete"),
]