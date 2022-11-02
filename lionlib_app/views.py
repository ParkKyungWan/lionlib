from django.shortcuts import render

# index, login, register

def index( request ):
    return render( request, 'index/index.html');

    
def login( request ):
    return render( request, 'index/login.html');

    
def register( request ):
    return render( request, 'index/register.html');

def register2( request ):
    return render( request, 'index/register2.html');


# trend, my, new

def trend( request ):
    return render( request, 'main/trend.html');

    
def my( request ):
    return render( request, 'main/my.html');

    
def new( request ):
    return render( request, 'main/new.html');

#all books
  
def all( request ):
    return render( request, 'main/all.html');

#show post
def show( request ):
    return render( request, 'main/show.html');

#posting
def new( request ):
    return render( request, 'main/new.html');