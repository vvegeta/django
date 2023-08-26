from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.profiles, name="profiles"),
    path('login/',views.userLogin, name="login"),
    path('logout/',views.userLogout, name="logout"),
    path('register/',views.registerUser, name="register"),
    path('<str:pk>/', views.profile, name="profile")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )