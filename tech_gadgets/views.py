from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from django.utils.text import slugify
import json
from django.urls import reverse

from django.views import View

from .dummy_data import gadgets
# Create your views here.
# wearabletracker-x10

from django.views.generic.base import RedirectView


def start_page_view(request):
    return HttpResponse("me: Welcome too Views")


class RedirectToGadgetView(RedirectView):
    pattern_name = "gadget_slug_url"

    def get_redirect_url(self, *args, **kwargs):
        slug = slugify(gadgets[kwargs.get("gadget_id", 0)]["name"])
        new_kwargs = {"gadget_slug": slug}
        return super().get_redirect_url(*args, **new_kwargs)


def single_gadget_int_view(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]["name"])
        new_url = reverse("gadget_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound("Gadget not found")


class GadgetView(View):
    def get(self, request, gadget_slug):
        gadget_match = None
        for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget
        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data["test"]}")
            return JsonResponse({"response": "Valid data"})
        except:
            return JsonResponse({"response": "Invalid data"})


def single_gadget_view(request, gadget_slug=""):

    if request.method == "GET":
        gadget_match = None
        for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget
        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"recieved data: {data["test"]}")
            return JsonResponse({"response": "Valid data"})
        except:
            return JsonResponse({"response": "Invalid data"})
