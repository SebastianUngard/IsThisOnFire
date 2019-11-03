from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image
from .forms import UploadImageForm
from .apps import WebappConfig 


# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .apps import WebappConfig

ANSWER = False
FORM = None

# Create your views here.
def index(request):
	return render(request, 'main.html')

def handle_uploaded_file(f):
	# process ML model and receive output
	ANSWER = True


def populate():
	train_fire = os.listdir('../data/training/fire')
	train_not_fire = os.listdir('../data/training/not_fire')
	valid_fire = os.listdir('../data/validation/fire')
	valid_not_fire = os.listdir('../data/validation/not_fire')

	for image in train_fire:
		img = Image(url = image, is_fire = 1, is_training = 1)
		img.save()
	for image in train_not_fire:		
		img = Image(url = image, is_fire = 0, is_training = 1)
		img.save()
	for image in valid_fire:
		img = Image(url = image, is_fire = 1, is_training = 0)
		img.save()
	for image in valid_not_fire:		
		img = Image(url = image, is_fire = 0, is_training = 0)
		img.save()
# class call_model(APIView):
# 	def get(self,request):
# 	    if request.method == 'GET':
	        
# 	        # sentence is the query we want to get the prediction for
# 	        params =  request.GET.get('sentence')
	        
# 	        # predict method used to get the prediction
# 	        response = WebappConfig.predictor.predict(sentence)
	        
# 	        # returning JSON response
# 	        return JsonResponse(response)

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
