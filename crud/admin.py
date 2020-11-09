from django.contrib import admin
from .models import Post,Profile,Photo
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display=['id','title','content','author','short_description','post_image','timestamp']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display=['id','user','pro_image','bio','birthday','works','education','cover']    


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display=['uploaded_by','gallary','upload_time']