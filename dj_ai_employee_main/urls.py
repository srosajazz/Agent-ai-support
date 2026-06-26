from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Django's built-in admin panel
    path("admin/", admin.site.urls),
    # Login page — uses Django's built-in LoginView with a custom template
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    # Logout — uses Django's built-in LogoutView, redirects to LOGOUT_REDIRECT_URL in settings.py
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # All orders-related URLs are handled in orders/urls.py
    path("orders/", include("orders.urls")),
]
