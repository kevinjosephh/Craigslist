import requests
from django.shortcuts import render
from bs4 import BeautifulSoup

# Create your views here.
cragUrl ='https://mumbai.craigslist.org/d/jobs/search/jjj?query=job'

def home(request):
    return render(request,'base.html')

def search(request):
    results= request.POST.get('search')
    response = requests.get(cragUrl)
    data = response.text
    context= {'search' : results,}
    return render(request,'search.html',context)
