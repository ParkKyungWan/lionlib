from django.shortcuts import render, redirect
from .models import AuthUser #유저 정보 db 
from django.contrib.auth import authenticate #로그인 인증을 위해
from django.contrib import auth #로그인을 위해 
from argon2 import PasswordHasher
import datetime

# index, login, register

def index( request ):
    return render( request, 'index/index.html')

    
def login( request ):
    
    if request.session.get('user'):
            return redirect( 'trend' )
    else:
        return render( request, 'index/login.html')

def logout( request ):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect( 'index' )
    
def register( request ):
    return render( request, 'index/register.html')


# trend, my, new

def trend( request ):
    return render( request, 'main/trend.html')

    
def my( request ):
    return render( request, 'main/my.html')

    
def new( request ):
    return render( request, 'main/new.html')

#all books
  
def all( request ):
    return render( request, 'main/all.html')

#show post
def show( request ):
    return render( request, 'main/show.html')

#posting
def new( request ):
    return render( request, 'main/new.html')



##### 기능 구현 ######

#회원가입 버튼 클릭 시
def user_create( request ):
    mail, pw = request.POST.get('email','') , request.POST.get('password','')
    if request.method == 'POST' and mail and pw:
        if AuthUser.objects.filter( email = mail ).exists():
            return render( request, 'etc/alert.html', { 'title' : "오류", 'text' : "이미 가입된 메일입니다"} )
        user = AuthUser()
        user.username = mail
        user.email = mail
        user.password = PasswordHasher().hash(pw)
        user.is_superuser = 0
        user.is_staff = 0
        user.is_active = 1
        user.date_joined = datetime.datetime.now()
        user.save()
        return render( request, 'etc/alert.html', { 'title' : "메일 인증", 'text' : "발송된 인증 메일을 확인해주세요"} )
    else:
        return render( request, 'etc/alert.html', { 'title' : "오류", 'text' : "올바른 경로가 아닙니다"} )

#로그인 버튼 클릭 시
def user_login( request ):
    mail, pw = request.POST.get('email','') , request.POST.get('password','')
    if request.method == 'POST' and mail and pw:
        is_user_exsist = AuthUser.objects.filter( email = mail ).exists()
        if is_user_exsist:
            user = AuthUser.objects.get( email = mail )
            if PasswordHasher().verify( user.password , pw ):
                request.session['user'] =  user.username
                return redirect('trend')
            else:
                return render( request, 'etc/alert.html', { 'title' : "로그인 실패", 'text' : "비밀번호를 확인하세요"})
        else:
            return render( request, 'etc/alert.html', { 'title' : "로그인 실패", 'text' : "존재하지 않는 계정입니다"})
    else:
        return render( request, 'etc/alert.html', { 'title' : "오류", 'text' : "올바른 경로가 아닙니다"} )