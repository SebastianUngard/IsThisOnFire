from django import forms
from .models import ImageUpload

class UploadImageForm(forms.ModelForm):
	class Meta:
		model = ImageUpload
		fields = ['img']

