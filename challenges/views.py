from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    'january': 'Don\'t drink alcohol for the month.',
    'february': 'Don\'t eat meat for the month.',
    'march': 'Learn Django for 20 minutes every day.',
    'april': 'Study OOP for an hour a day.',
    'may': 'Go on a walk everyday',
    'june': 'Don\'t watch TV for the whole month.',
    'july': 'Start learning Javascript.',
    'august': 'Start playing guitar again. Learn a riff a day.',
    'september': 'Learn to solo on guitar',
    'october': '100 push ups a day.',
    'november': 'Write 1 minute of standup.',
    'december': 'Learn PHP.'
}

# Create your views here.

def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse('month-challenge', args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid Month.')

    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f'<h1>{challenge_text}</h1>'
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('<h1>Month not found.</h1>')
