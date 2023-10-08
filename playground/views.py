from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from rest_framework.views import APIView
import requests


class HelloView(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        response = request.get("https://httpbin.org/delay/2")
        data = response.json()
        return render(request, "hello.html", {"name": "Mosh"})
