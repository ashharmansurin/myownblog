from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import Post,Profile,Photo
from django.contrib.auth.models import User
from .forms import UserRegisterationForm,PostCreateForm,UserUpdateForm,ProfileForm,UserPasswordForm,GallaryForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required



# Create your views here.
class PostListView(ListView):
    model = Post
    ordering =['-timestamp']
    template_name='crud/home.html'
    context_object_name ='posts'


class PostDetailView(DetailView):
    model = Post
    ordering =['-timestamp']
    template_name ='crud/post_detail.html'  
    context_object_name ='post'

    def get_context_data(self,*args ,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['latest_post']= self.model.objects.all().order_by('-timestamp')[:5]
        return context

@login_required(login_url='login')
def PostCreateView(request):
    fm = PostCreateForm()
    if request.method=="POST":
        fm = PostCreateForm(request.POST,request.FILES)
        if fm.is_valid():
            user_post =fm.save(commit=False)
            user_post.author = request.user
            user_post.save()
            messages.success(request,'you have made post succesfully')
            return redirect('home')
    context ={'form':fm}
    return render(request,'crud/post_create.html',context)
    

@login_required(login_url='login')
def PostUpdateView(request,pk):
    post = Post.objects.get(id=pk)
    fm = PostCreateForm(instance=post)
    if request.method=="POST":
        fm = PostCreateForm(request.POST,request.FILES,instance=post)
        if fm.is_valid():
            user_post=fm.save(commit=False)
            user_post.author = request.user
            user_post.save()
            messages.success(request,'you have Updated post succesfully')
            return redirect('home')

    context ={'form':fm}
    return render(request,'crud/post_create.html',context)

@login_required(login_url='login')
def PostDeleteView(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    messages.danger(request ,'You have deleted Your Post')
    return redirect('dashboard')



def PostSearchView(request):
    search_query = request.GET.get('search-query')

    allpoststitle = Post.objects.filter(title__icontains=search_query)
    allpostsdesc = Post.objects.filter(short_description__icontains=search_query)
    allposts = allpoststitle.union(allpostsdesc)

    context = {'posts':allposts,'search_query':search_query}
    return render(request, 'crud/post_search.html',context)



def ContactView(request):
    
    return render(request,'crud/contactus.html')


def Account_Settings(request):
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileForm(instance= request.user.profile)

    if request.method=='POST':
        
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        # photos = request.FILES.getlist('photo_gallary')
        # current_user = request.user
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            messages.success(request,'Your Profile has been Updated')
            return HttpResponseRedirect(reverse('user-profile',args=[int(request.user.id)]))
       
    context ={'user_form':user_form,'profile_form':profile_form}
    return render(request,'crud/account_settings.html',context)



def photos_gallary(request):
    user_images = Photo.objects.filter(uploaded_by = request.user)
    gallary_form = GallaryForm()
    if request.method=="POST":
        gallary_form = GallaryForm(request.POST,request.FILES)
        files = request.FILES.getlist('gallary')
        gallary_form.save(commit=False)
        
        if gallary_form.is_valid():
            for f  in files:
                current_user = request.user
                images = Photo(uploaded_by=current_user,gallary=f)
                user_photo=images.save()
    context ={'g_form':gallary_form,'user_photos':user_images}
    # print(user_images)
    return render(request,'crud/upload_photos.html',context)


def user_photos_gallary(request,pk):
  images = Photo.objects.filter(uploaded_by = pk)
  context ={'user_photos':images}
  print('images:',images)
  return render(request,'crud/user-upload-photos.html',context)



@login_required(login_url='login')
def Dashboard(request):
    current_user = request.user
    count = Post.objects.filter(author=current_user).count()
    user_post = Post.objects.filter(author=current_user).order_by('-timestamp')
    context = {'posts':user_post,'counts':count}
    return render(request,'crud/dashboard.html',context)

def User_Profile(request,pk):
    user = User.objects.get(id=pk)
    context ={'user_info':user}
    return render(request,'crud/user_profile.html',context)



def UserPasswordChange(request):
    form = UserPasswordForm(request.user)
    if request.method=="POST":
        form = UserPasswordForm(request.user,request.POST)
        if form.is_valid():
            pc= form.save()
            
            update_session_auth_hash(request,pc)
            messages.info(request,'Password Changed successfully')
            return redirect('password-change')

    context ={'pass_form':form}
    return render(request,'crud/password_change.html',context)


def User_Registration(request):
    fm = UserRegisterationForm()
    if request.method == 'POST':
        fm = UserRegisterationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'User has been registered succesfully')
            return redirect('login')
    context ={'form':fm}
    return render(request,'accounts/register.html',context)


def User_Login(request):
    if request.method =='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'You are logged in succesfully')
            return redirect('dashboard')
            
    return render(request,'accounts/login.html')    


def User_Logout(request):
    logout(request)
    messages.info(request, 'You are logged out succesfully')
    return redirect('login')