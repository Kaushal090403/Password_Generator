from django.shortcuts import render
from random import *

def home(request):
    return render(request,"home.html")

def show(request):
    length=int(request.GET.get("le"))
    pw=""
    text="qazxswedcvfrtgbnhyujmlopki"
    if request.GET.get("uc"):
        text=text+text.upper()
    if request.GET.get("dc"):
        text=text+"1234567890"
    for i in range(length):
        r=randrange(len(text))
        pw=pw+text[r]
    msg="Password is "+str(pw)
    return render(request,"show.html",{"msg":msg})
