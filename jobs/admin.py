from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Freelancer, Business

class AdminDashboardLinkMixin:
    def admin_dashboard(self, obj):
        url = reverse('admin-dashboard')
        return format_html('<a href="{}">Go to Dashboard</a>', url)

class FreelancerAdmin(admin.ModelAdmin, AdminDashboardLinkMixin):
    list_display = ('name', 'email', 'admin_dashboard')  # Example fields

class BusinessAdmin(admin.ModelAdmin, AdminDashboardLinkMixin):
    list_display = ('name', 'type', 'admin_dashboard')  # Example fields

admin.site.register(Freelancer, FreelancerAdmin)
admin.site.register(Business, BusinessAdmin)
