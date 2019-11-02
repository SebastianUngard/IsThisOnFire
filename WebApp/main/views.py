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

# Create your views here.
def index(request):
	return HttpResponse('Is this on fire?')


def popu
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
		form = UploadImageForm(title=request.POST, img=request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['img'])
			return HttpResponseRedirect('/success/url/')
	else:
		form = UploadImageForm()
	return render(request, 'main.html', {'form': form})
