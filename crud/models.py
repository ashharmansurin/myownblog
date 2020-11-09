from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=100)
    content= RichTextField(blank=True,null=True)
    short_description = models.TextField(max_length=200,blank=True)
    post_image = models.ImageField(upload_to='postimages')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.title


class Profile(models.Model):

    EDUCATION_CHOICE =(
    ('M.C.A','M.C.A'),
    ('B.C.A','B.C.A'),
    ('B.A','B.A'),
    ('M.A','M.A'),
    ('P.G','P.G'),
    ('HIGH SCHOOL','HIGH SCOOL'),
    ('SECONDARY','SECONDARY'),
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pro_image = models.ImageField(default='default.png',upload_to='profileimage',blank=True)
    bio = models.CharField(max_length=250, blank=True)
    works = models.CharField(max_length=100,blank=True)
    cover = models.ImageField(default='default.png',upload_to='coverimage',blank=True)   
    birthday = models.DateField(null=True, blank=True)
    education = models.CharField(max_length=50,choices= EDUCATION_CHOICE,blank=True)


class Photo(models.Model):
    uploaded_by = models.ForeignKey(User,on_delete=models.CASCADE)
    gallary = models.FileField(upload_to='gallaries',blank=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.uploaded_by.username




















 
  
#signals
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('profile created')

post_save.connect(create_user_profile,sender=User)


def update_user_profile(sender, instance,created ,**kwargs):
    if created == False:
     instance.profile.save()
     print('updated created')

post_save.connect(update_user_profile,sender=User)         