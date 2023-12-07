from django.shortcuts import render,HttpResponse
from home.models    import Task

def home(request):
    context ={'success':False}
    if request.method=='POST':
        title= request.POST['titile']
        desc = request.POST['desc']
        print(title,desc)
        ins = Task(taskTitle = 'title',taskdesc= 'desc ')
        context = {'success':True}
    return render(request,'index.html',context)

def tasks(request):
    return render(request,'tasks.html')

# Create your views here.
