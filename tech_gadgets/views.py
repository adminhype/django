from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import json

from .dummy_data import gadgets
# Create your views here.


def start_page_view(request):
    return HttpResponse("me: Welcome too Views")


def single_gadget_view(request):
    return JsonResponse(gadgets[0])
