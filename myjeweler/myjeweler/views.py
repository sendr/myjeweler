# -*- coding: utf-8 -*-
from datetime import datetime 

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from myjeweler.apps.silver_adornment.models import SilverRings, SilverEarrings, TypeEarrings
from django import forms
from django.core.mail import send_mail
from django.template.loader import render_to_string


def index(request):
	return render(request, "index.html")

def rings(request):
	rings = SilverRings.objects.all()
	return render(request, "rings.html", {
		'rings': rings
		})


class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	text = forms.CharField(widget=forms.Textarea)


def feedback_view(request):

	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():			
			data = form.cleaned_data
			data['date'] = datetime.now()
			message = render_to_string('my_feedback.txt', data)
			send_mail("Message form from Myjewelry", message, data['email'], ["sendr84@gmail.com"] )
			messages.success(request, u'Сообщение было успешно отправлено')
			return redirect(reverse("feedback"))
	else:
		form = ContactForm()
	return render(request, "feedback.html",{
						'form': form})

def earrings(request):
	earrings = SilverEarrings.objects.all() 
	return render(request, "earrings.html", {
		'earrings': earrings,
		})

def pendants(request):
	return render(request, "pendants.html")

def photo_rings1(request):
	return render(request, "photo_rings1.html")

def photo_earrings1(request):
	return render(request, "photo_earrings1.html")

def photo1(request):
	return render(request, "photo1.html")
	