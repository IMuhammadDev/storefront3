from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from rest_framework.views import APIView
import requests
import logging

logger = logging.getLogger(__name__)


class HelloView(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        try:
            logger.info("calling httpbin")
            response = requests.get("https://httpbin.org/delay/2")
            logger.info("recived the responce")
            data = response.json()
        except requests.ConnectionError:
            logger.critical("httpbin is ofline")
        return render(request, "hello.html", {"name": "Mosh"})
