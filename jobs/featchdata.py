import os
import sys
import django
import json

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

# Import your models
from jobs.models import Freelancer, Business

def list_all_data():
    # Get Freelancers
    freelancers = Freelancer.objects.all()
    freelancer_list = []

    for freelancer in freelancers:
        freelancer_data = {
            "id": freelancer.id,
            "name": freelancer.name,
            "tagline": freelancer.tagline,
            "bio": freelancer.bio,
            "website": freelancer.website or "",
            "profile_pic": f"http://127.0.0.1:8000{freelancer.profile_pic.url}" if freelancer.profile_pic else ""
        }
        freelancer_list.append(freelancer_data)

    # Get Businesses
    businesses = Business.objects.all()
    business_list = []

    for business in businesses:
        business_data = {
            "id": business.id,
            "name": business.name,
            "bio": business.bio,
            "profile_pic": f"http://127.0.0.1:8000{business.profile_pic.url}" if business.profile_pic else ""
        }
        business_list.append(business_data)

    # Combine all data
    all_data = {
        "freelancers": freelancer_list,
        "businesses": business_list
    }

    # Print as formatted JSON
    formatted_json = json.dumps(all_data, indent=4)
    print(formatted_json)
    print(f'\nTotal Freelancers: {len(freelancer_list)}')
    print(f'Total Businesses: {len(business_list)}')

if __name__ == '__main__':
    list_all_data()