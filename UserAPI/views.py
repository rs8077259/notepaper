from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.contrib.auth.models import User
from rest_framework import status
from threading import Thread
from notepaper.settings import DEFAULT_FROM_EMAIL,EMAIL_HOST_USER,EMAIL_HOST_PASSWORD




# views

@api_view(["POST"])
def register(request):
    username = request.POST.get('username',None)
    password = request.POST.get('password',None)
    email = request.POST.get('email',None)
    if username and password and email:
        User.objects.create_user(username=username,email=email,password=password)
        emailArgs={
            "subject" : "Registration Successfull",
            "message" : '',
            "html_message" :  f"Dear {username}\nThanks for being  a member of our community\nYour email address:<b>{email}</b> has been registered succesfully",
            "fail_silently" : False,
            "recipient_list" : [email],
            "from_email" : DEFAULT_FROM_EMAIL,
            "auth_user" : EMAIL_HOST_USER,
            "auth_password" : EMAIL_HOST_PASSWORD
        }

        Thread(target=send_mail,kwargs=emailArgs).start()
        return Response({"status":"Registration Success"},status=status.HTTP_200_OK)

    return Response({"status" : 206},status=status.HTTP_206_PARTIAL_CONTENT)



