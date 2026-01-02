from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

app_name = "ideas"

urlpatterns = [
    path('', views.idea_list, name="idea_list"),
    path("<int:pk>/", views.idea_detail, name="idea_detail"),
    path('create/', views.idea_create, name="idea_create"),
    path("<int:pk>/update", views.idea_update, name="idea_update"),
    path("<int:pk>/delete", views.idea_delete, name="idea_delete"),
    path('devtools/', views.devtool_list, name="devtool_list"),
    path('devtools/create/', views.devtool_create, name="devtool_create"),
    path('devtools/<int:pk>/', views.devtool_detail, name="devtool_detail"),
    path('devtools/<int:pk>/update/', views.devtool_update, name="devtool_update"),
    path('devtools/<int:pk>/delete/', views.devtool_delete, name="devtool_delete"),
    path('idea-star/<int:pk>/', views.idea_star, name='idea_star'),
    path('idea/<int:pk>/interest/', views.adjust_interest, name='adjust_interest'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)