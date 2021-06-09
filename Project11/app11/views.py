from django.shortcuts import render
def showIndex(request):
    return render(request,"main.html")
def loginCheck(request):
    username=request.POST.get("t1")
    password=request.POST.get("t2")
    if username=="ravi" and password=="kumar":
        return render(request,"welcome.html")
    else:
        return render(request,"error.html")
# Create your views here.
