from django.contrib import admin
from django.db.models import indexes
from django.urls import path,include
from django_email_verification import urls as email_urls
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    # path('',views.landing,name = 'landing'),
    path('register/',views.RegisterPage, name = 'register'),
    # path('',views.index,name="index"),
    path('login/',views.loginPage,name = 'login'),
    path('home/',views.home,name='home'),
    path('logout/', views.logoutUser, name="logout"),
    path('sendEmail/',views.sendEmail,name="sendEmanil"),
    path('email/', include(email_urls)),
    path('OrgS/',views.mydemo,name='mydemo'),
    
    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name ="P1/password_reset.html"),
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name ="P1/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name ="P1/password_reset_done.html"), 
        name="password_reset_complete"),
    

]



'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''