from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse


def index(request):
	return render(request, "index.html")

def rings(request):
	return render(request, "rings.html")

def earrings(request):
	return render(request, "earrings.html")

def pendants(request):
	return render(request, "pendants.html")

def photo_rings1(request):
	return render(request, "photo_rings1.html")

def photo_earrings1(request):
	return render(request, "photo_earrings1.html")

def photo1(request):
	return render(request, "photo1.html")
	