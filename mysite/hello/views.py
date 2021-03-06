from django.shortcuts import render
from django.http import HttpResponse

# https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpRequest.COOKIES
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/',
#     domain=None, secure=None, httponly=False, samesite=None)
def cookie(request):
    print(request.COOKIES)
    resp = HttpResponse('My cookie... f19c44d0 ')
    resp.set_cookie('dj4e_cookie', 'f19c44d0', max_age=1000)
    return resp

# Create your views here.
def sessfun(request) :
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])

    #resp = HttpResponse('view count='+str(num_visits))
    ctx = {'num_visits' : num_visits}
    resp = render(request, "hello/hello.html", ctx)
    resp.set_cookie('dj4e_cookie', 'f19c44d0', max_age=1000)
    return resp

