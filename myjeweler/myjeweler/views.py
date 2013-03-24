from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from myjeweler.apps.silver_adornment.models import SilverRings


def index(request):
	return render(request, "index.html")

def rings(request):
	rings = SilverRings.objects.all()
	return render(request, "rings.html", {
		'rings': rings
		})

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
	