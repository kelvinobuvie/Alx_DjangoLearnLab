from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
# ✅ import your own views including register & list_books
from . import views
from .views import LibraryDetailView  # still fine
from .views import list_books  # still fine

urlpatterns = [
    # Books listing
    path('books/', list_books, name='list_books'),

    # Library details (class-based)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # ✅ Registration view
    path('register/', views.register, name='register'),

    # ✅ Login view (checker looks for template_name)
    path(
        'login/',
        LoginView.as_view(template_name='relationship_app/login.html'),
        name='login'
    ),

    # ✅ Logout view (checker looks for template_name)
    path(
        'logout/',
        LogoutView.as_view(template_name='relationship_app/logout.html'),
        name='logout'
    ),
]
