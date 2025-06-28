from  django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('accounts/password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)