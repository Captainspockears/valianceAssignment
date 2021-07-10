from django.shortcuts import render
from django.http.response import HttpResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def index(request):
    return HttpResponse("Welcome to Valiance Solution's Temperature API!")
