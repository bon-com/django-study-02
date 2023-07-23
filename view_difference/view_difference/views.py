from django.views.generic import TemplateView
from django.shortcuts import render


class HelloWorldClass(TemplateView):
    """class-based viewで実装"""

    template_name = "hello1.html"


def hello2(request):
    """function-based viewで実装"""
    return render(request, "hello2.html")
