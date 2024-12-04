from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Freelancer, Business
from .serializers import FreelancerSerializer, BusinessSerializer

class FreelancerListView(ListView):
    model = Freelancer
    template_name = 'jobs/freelancer_list.html'

class FreelancerDetailView(LoginRequiredMixin, DetailView):
    model = Freelancer
    # template 'freelancer_detail.html'

# def freelancer_detail(request, pk):
#     freelancer = Freelancer.objects.get(pk=pk) #get_object_or_404
#     context = {
#         "objects": freelancer
#     }
#     return render(request, 'jobs/freelancer_detail/html', context)

class FreelancerCreateView(LoginRequiredMixin, CreateView):
    model = Freelancer
    fields = ['name', 'profile_pic', 'tagline', 'bio', 'website']
    success_url = reverse_lazy('freelancer-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(FreelancerCreateView, self).form_valid(form)

class BusinessCreateView(LoginRequiredMixin, CreateView):
    model = Business
    fields = ['name', 'profile_pic', 'bio']
    success_url = reverse_lazy('freelancer-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BusinessCreateView, self).form_valid(form)

@login_required
def handle_login(request):
    # if the user has a freelance/biz acct -> take them to home
    print(request.user)
    print(request.user.get_freelancer())
    if request.user.get_freelancer() or request.user.get_business():
        return redirect(reverse_lazy('freelancer-list'))

    return render(request, 'jobs/choose_account.html', {})

    


class FreelancerListAPIView(generics.ListCreateAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelancerSerializer

class BusinessListAPIView(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

@csrf_exempt
def freelancer_list(request):
    freelancers = Freelancer.objects.all()
    data = [{
        'id': f.id,
        'name': f.name,
        'tagline': f.tagline,
        'bio': f.bio,
        'website': f.website or "",
        'profile_pic': f"http://127.0.0.1:8000{f.profile_pic.url}" if f.profile_pic else ""
    } for f in freelancers]
    return JsonResponse(data, safe=False)

@csrf_exempt
def business_list(request):
    businesses = Business.objects.all()
    data = [{
        'id': b.id,
        'name': b.name,
        'bio': b.bio,
        'profile_pic': f"http://127.0.0.1:8000{b.profile_pic.url}" if b.profile_pic else ""
    } for b in businesses]
    return JsonResponse(data, safe=False)

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})

@csrf_exempt
def login_view(request):
    # Your login logic here
    pass

@csrf_exempt
def signup_view(request):
    # Your signup logic here
    pass
