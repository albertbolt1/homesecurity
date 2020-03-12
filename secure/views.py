import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static

def second(request):

    return render(request, 'secure/second.html')


def live(request):

	from secure import live1
	try:
		live1.foo()
	except:
		return render(request,'secure/live.html')



def facecrop(request):

	from secure import facecrop
	try:
		facecrop.facecrop1()
	except:
		return render(request,'secure/live.html')



def detectedfaces(request):

    return render(request, 'secure/detectedfaces.html')

def proximity(request):

	from secure import proximity
	try:
		proximity.prox()
	except:
		return render(request,'secure/live.html')

def light(request):

	from secure import light
	try:
		light.light()
	except:
		return render(request,'secure/live.html')

def battery(request):

	from secure import battery
	try:
		battery.battery()
	except:
		return render(request,'secure/live.html')


def home(request):
	return render(request,'secure/home.html')



def home1(request):
	return render(request,'secure/start.html')

def home2(request):
	return render(request,'secure/twomain.html')


def motion(request):

	from secure import motiondetection
	try:
		motiondetection.motiondetection()
	except:
		return render(request,'secure/live.html')


def missing(request):

	from secure import substract
	substract.substract()
	return render(request,'secure/live.html')



def outof(request):
	from secure import email
	try:
		email.motiondetection()
		return render(request,'secure/live23.html')
	except:
		return render(request,'secure/live.html')



