from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image
from .forms import UploadImageForm

# Create your views here.
def index(request):
	return HttpResponse('You are at the index!')

def handle_uploaded_file(f):
	# process ML model and receive output
	pass

def upload(request):
	if request.method == 'POST':
		form = UploadImageForm(title=request.POST, img=request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['img'])
			return HttpResponseRedirect('/success/url/')
	else:
		form = UploadImageForm()
	return render(request, 'upload.html', {'form': form})
