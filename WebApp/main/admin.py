from django.contrib import admin
from .models import Image, ImageUpload

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
	list_display = ('is_fire', 'is_training', 'url')

class ImageUploadAdmin(admin.ModelAdmin):
	list_display = ('img',)

admin.site.register(ImageUpload, ImageUploadAdmin)
admin.site.register(Image, ImageAdmin)