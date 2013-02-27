from django.http import HttpResponse
from django.views.generic.simple import direct_to_template


def index(request):
	return direct_to_template(request, "index.html")

def rings(request):
	return direct_to_template(request, "rings.html")

def earrings(request):
	return direct_to_template(request, "earrings.html")

def pendants(request):
	return direct_to_template(request, "pendants.html")

def photo_rings1(request):
	return direct_to_template(request, "photo_rings1.html")

def photo_earrings1(request):
	return direct_to_template(request, "photo_earrings1.html")

def enter(request):
	return direct_to_template(request, "enter.html")

def registration(request):
	return direct_to_template(request, "registration.html")

def photo1(request):
	return direct_to_template(request, "photo1.html")

def employees(request):
	return direct_to_template(request, "employees.html")