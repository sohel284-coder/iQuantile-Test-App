from django.shortcuts import render, redirect
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from filemanagementapp.forms import *

from filemanagementapp.models import *
from filemanagementapp.serializers import *

@login_required(login_url='login_page')
def file_management(request, ):
    user = request.user
    return render(request, 'file_management.html', {'user':user})

def edit_file(request, ):
    return render(request, 'edit_file.html', )
   

def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account has been Created for ' + user)
            return redirect('login_page')
    return render(request, 'register_page.html', {'form':form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('file_management')
        else:
            messages.info(request, 'Username or password is incorrect')
    return render(request, 'login_page.html',   )

def logout_user(request):
    logout(request)
    return redirect('login_page')


class FileManagementListCreateAPIView(ListCreateAPIView):
    queryset = FileManagement.objects.filter()
    # parser_classes = (MultiPartParser, FormParser,)
    permission_class = (permissions.AllowAny(), )
    serializer_class = FileManagementSerializer

class FileListAPIView(ListAPIView):
    queryset = FileManagement.objects.filter()
    def get(self, request):
        products = FileManagement.objects.filter(user=request.user)
        return Response(FileManagementSerializer(products, many=True).data)

class FileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FileManagement.objects.all()
    serializer_class = FileManagementSerializer
    lookup_field = 'id'






