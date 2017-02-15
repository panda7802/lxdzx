from django.shortcuts import render


from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
import logging
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def t_index_view(req):
    res = render_to_response('index.html')
    return res


