from django.shortcuts import render
from datetime import *
# Create your views here.

def set(request):
    data = render(request,'app/set.html')
    data.set_cookie('name','Neeraj') # by default
    # data.set_cookie('name','Neeraj', expires=datetime.utcnow()+timedelta(days=1)) # by default
    data.set_cookie('age','37',max_age=20*60*60) # by default
    data.set_cookie('City','Bhopal',httponly=True,secure=True) # by default
    # data.set_cookie('name','Neeraj',max_age=60*60*24,) # set maximum time for your cookies.
    # data.set_cookie('name','Neeraj',expires=datetime.utcnow()+timedelta(days=1)) # set expire time for your cookies.
    return data

def get(request):
    name = request.COOKIES['name'] 
    age = request.COOKIES['age'] 
    City = request.COOKIES['City']  
    # name = request.COOKIES['city']   # through error because we do not set any cookie against this key.       
    # name = request.COOKIES.get('name')
    # name = request.COOKIES.get('city') # O/P---None
    # name = request.COOKIES.get('city','Guest') # O/P---Guest
    # name = request.COOKIES.get('City','Bhopal')
    print(name)   
    print(age)
    print(City)
    name={
        'name':name,
        'age':age,
        'City':City
    }
    return render(request,'app/get.html',{'data':name})

def delete(request):
    data = render(request,'app/delete.html')
    data.delete_cookie('name')
    data.delete_cookie('age')
    data.delete_cookie('City')
    return data          