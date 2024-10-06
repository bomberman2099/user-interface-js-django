from django.shortcuts import render, HttpResponse
from django.http import Http404


def index(request):
    return render(request, 'home/index.html')


# no database used
text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'


def sections(request, num):
    if 1 <= num <= 3:  
        response_text = f'{text} Page {num}'
        return HttpResponse(response_text)
    else:
        raise Http404('No page found')
