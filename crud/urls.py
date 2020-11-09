
from django.urls import path
from .import views


urlpatterns = [
    path('',views.PostListView.as_view(),name='home'),
    path('contact',views.ContactView,name='contact'),
    path('post-detail/<int:pk>',views.PostDetailView.as_view(),name='post-detail'),
    path('post-create',views.PostCreateView,name='post-create'),
    path('post-edit/<int:pk>',views.PostUpdateView,name='post-update'),
    path('post-delete/<int:pk>',views.PostDeleteView,name='post-delete'),
    path('post-search',views.PostSearchView,name='post-search'),
    
    path('account-settings',views.Account_Settings,name='account-settings'),
    path('dashboard',views.Dashboard,name='dashboard'),
    path('user-profile/<int:pk>',views.User_Profile,name='user-profile'),
    path('user-password-change',views.UserPasswordChange,name='password-change'),
    path('photos-gallary',views.photos_gallary,name='photos-gallary'),
    path('user-photos-gallary/<int:pk>',views.user_photos_gallary,name='user-photos-gallary'),

    path('register',views.User_Registration,name='register'),
    path('login',views.User_Login,name='login'),
    path('logout',views.User_Logout,name='logout'),
]
