from typing import ContextManager
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def Home(request):
    context= {'success':False, 'name':'saloni'}
    if request.method == "POST":
        print("This is Post request")
        tasks= request.POST['tasks']
        desc= request.POST['desc']
        ins=Task(tasks=tasks, desc=desc)
        ins.save()
        context= {'success':True}
        print("Saved in Db")
    return render(request,'index.html',context)

def Tasks(request):
    alltasks= Task.objects.all()
    context={'Tasks':alltasks}
    return render(request,'about.html',context)