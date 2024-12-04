from django.urls import path
from .views import (
    FreelancerListView,
    FreelancerDetailView,
    FreelancerCreateView,
    BusinessCreateView, 
    handle_login,
    FreelancerListAPIView,
    BusinessListAPIView,
    get_csrf_token
)
from .dashboard import dashboard_view  # Import your dashboard view
from django.urls import path

urlpatterns = [
    path('', FreelancerListView.as_view(), name='freelancer-list'),
    path('account-setup/', handle_login, name='handle-login'),
    path('developer/<int:pk>/', FreelancerDetailView.as_view(), name='freelancer-detail'),
    path('developer/create/', FreelancerCreateView.as_view(), name="freelancer-create"),
    path('business/create/', BusinessCreateView.as_view(), name="business-create"),
    path('dashboard/', dashboard_view, name="admin-dashboard"),  # Add the dashboard URL here
    path('api/freelancers/', FreelancerListAPIView.as_view(), name='freelancer-list-api'),
    path('api/businesses/', BusinessListAPIView.as_view(), name='business-list-api'),
    path('accounts/csrf/', get_csrf_token, name='csrf_token'),
]
