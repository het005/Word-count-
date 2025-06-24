from django.shortcuts import render

# Create your views here.
name="het!"
def home(request):
    return render(request,'index.html',{'name':name})
def counter(request):
    textarea = request.POST.get('textarea', '')
    res=len(textarea.split())
    return render(request,'counter.html',{'res':res})