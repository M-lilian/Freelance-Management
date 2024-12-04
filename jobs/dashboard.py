from django.shortcuts import render
from .models import Freelancer, Business

def dashboard_view(request):
    freelancers_count = Freelancer.objects.count()
    businesses_count = Business.objects.count()

    # Pass data to the template
    data = {
        'freelancers_count': freelancers_count,
        'businesses_count': businesses_count,
    }
    return render(request, 'dashboard.html', data)
