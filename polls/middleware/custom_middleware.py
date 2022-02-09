from django.conf import settings
from django.shortcuts import redirect

class registredUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path == "/login/" or request.user.is_authenticated and request.path == "/signup":
            return redirect("/")      
            
        response = self.get_response(request)
        return response
