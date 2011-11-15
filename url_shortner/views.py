# Create your views here.
import django.contrib.staticfiles

from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from url_shortner.models import Url
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import os, random

def index(request):
    return render_to_response('url_shortner/index.html', context_instance = RequestContext(request))

def detail(request):
    ip_url=request.POST['url']
    s = Url.objects.filter(input_url=ip_url)
    if s:
        appended_url = s[0].appended_url
        word = s[0].string
        return render_to_response('url_shortner/index.html', {'appended_url':appended_url, 'word':word, 'show_url':True}, context_instance = RequestContext(request))
        
    else:
        char_array = "abcdefgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_"
        word = "".join(random.choice(char_array) for i in range(4))
        appended_url = 'http://127.0.0.1:8000/'+word
        p=Url(input_url = ip_url, string = word, appended_url = appended_url )
        p.save()
        return render_to_response('url_shortner/index.html', {'appended_url':appended_url, 'word':word, 'show_url':True}, context_instance = RequestContext(request))

def results(request,p):
    s = Url.objects.filter(string=p)
    url = s[0].input_url
    return HttpResponsePermanentRedirect(url)
    #return HttpResponse(url)

def redirect(request,p):
    s = Url.objects.filter(string=p)
    url = s[0].input_url
    return HttpResponsePermanentRedirect(url)
 
