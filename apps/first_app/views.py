from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return HttpResponse("placeholder to later display all the list of blogs")

def new(request):
	return HttpResponse("placeholder to display a new form to create a new blog")
	#  /new   - display "placeholder to display a new form to create a new blog" via HttpResponse


def create(request):
	return redirect('/')
	#  /create  -  For now, have this url redirect to /

def show(request):
	print blog_id
	return HttpResponse("placeholder to display blog {}".format(blog_id))
	#  /{{number}} - display 'placeholder to display blog {{number}}'.  For example /15 should display a message 'placeholder to display blog 15'.

def edit(request):
	return HttpResponse("placeholder to edit blog {}".format(blog_id))
	#  /{{number}}/edit - display 'placeholder to edit blog {{number}}'

def destroy(request):
	return redirect('/')
	#  /{{number}}/delete - redirect to /	


# Create your views here.
