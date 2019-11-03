from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image
from .forms import UploadImageForm

ANSWER = False
FORM = None

# Create your views here.
def index(request):
	return render(request, 'main.html')

def handle_uploaded_file(f):
	# process ML model and receive output
	ANSWER = True

def upload(request):
	if request.method == 'POST':
		FORM = UploadImageForm(request.POST, request.FILES)
		if FORM.is_valid():
			handle_uploaded_file(request.FILES['img'])
			return HttpResponseRedirect('/success/')
	else:
		FORM = UploadImageForm()
	return render(request, 'main.html', {'form': FORM})

def output(request):
	return render(request, 'main.html', {'answer': ANSWER,
										 'form': FORM})
