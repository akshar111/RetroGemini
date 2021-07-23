from django.contrib import admin
import debug_toolbar
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import dashboard_view, login_view, logout_view, registerPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard_view, name='dashboard'),
    path('my_profile/', include('profiles.urls', namespace='profiles')),
    path('boards/', include('board.urls', namespace='board')),
    path('__debug__/', include(debug_toolbar.urls)),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registerPage, name="register"),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="auth/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="auth/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="auth/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="auth/password_reset_done.html"),
         name="password_reset_complete"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
