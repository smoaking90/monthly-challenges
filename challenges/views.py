from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'Don\'t drink alcohol for the month.'
    elif month == 'february':
        challenge_text = 'Don\'t eat meat for the month.'
    elif month == 'march':
        challenge_text = 'Learn Django for 20 minutes every day.'
    else:
        return HttpResponseNotFound('This month is not supported.')
    return HttpResponse(challenge_text)
