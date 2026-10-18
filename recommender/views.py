from django.shortcuts import render, get_object_or_404
from recommender.models import Domain
from recommender.services import recommend_domains
from recommender.roadmap_data import STEP_DETAILS


def home(request):
    return render(request, 'home.html')


def results(request):
    query = request.GET.get('query')

    recommendations = recommend_domains(query)

    return render(request, 'results.html', {
        'recommendations': recommendations,
        'query': query
    })



def get_step_details(step):
    title = step.strip()
    data = STEP_DETAILS.get(title, {
        'description': f"Master the core concepts of {title} with this comprehensive roadmap phase.",
        'learn': [
            f'Explore foundational ideas of {title}',
            f'Practice hands-on {title} projects',
            f'Apply {title} in real-world contexts'
        ],
        'video_link': f"https://www.youtube.com/results?search_query={title.replace(' ', '+')}+full+course+english"
    })
    return {
        'title': title,
        'description': data['description'],
        'learn': data['learn'],
        'video_link': data.get('video_link', f"https://www.youtube.com/results?search_query={title.replace(' ', '+')}+full+course+english")
    }


def domain_detail(request, id):
    domain = get_object_or_404(Domain, id=id)
    skills = [s.strip() for s in domain.skills.split(',') if s.strip()]
    steps = [get_step_details(s) for s in domain.learning_path.split(',') if s.strip()]
    platforms = [p.strip() for p in domain.platforms.split(',') if p.strip()]

    return render(request, 'domain_detail.html', {
        'domain': domain,
        'skills': skills,
        'steps': steps,
        'platforms': platforms
    })


def dashboard(request):
    domains = Domain.objects.all()
    return render(request, 'dashboard.html', {
        'domains': domains,
        'count': domains.count()
    })