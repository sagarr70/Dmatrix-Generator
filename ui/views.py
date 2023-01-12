from django.http import HttpResponse
from django.shortcuts import render
from requests import request

from . import GetPinCodes
# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'sagar'});

def saveexcel(request):
    pincodes = GetPinCodes.main(request.FILES["excel_file"],str(request.POST["cname"]))
    if(len(pincodes)>0):
        return render(request,'downloadsvg.html',{"pincodes":pincodes,"length":len(pincodes)})
    else:
        return render(request,'error.html')