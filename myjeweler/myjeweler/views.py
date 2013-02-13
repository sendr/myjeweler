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