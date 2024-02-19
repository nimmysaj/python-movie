from django.shortcuts import render, redirect

from movieapp.forms import movieForm
from movieapp.models import movie
from django.http import HttpResponse

# Create your views here.
def index(request):
    m=movie.objects.all()
    context={'movie_list':m}
    return render(request,'index.html',context)
def detail(request,movie_id):
    #return HttpResponse('this movie id is %s' %movie_id)
    m = movie.objects.get(id=movie_id)
    context = {'movie_list': m}
    return render(request, 'detail.html', context)

def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year=request.POST.get('year')
        img = request.FILES['img']
        movie(name=name,desc=desc,year=year,img=img).save()
    return render(request,'add.html')

def update(request,id):
    m=movie.objects.get(id=id)
    form=movieForm(request.POST or None,request.FILES,instance=m)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':m})


def delete(request,id):
    if request.method=="POST":
        m=movie.objects.get(id=id)
        m.delete()
        return redirect('/')
    return render(request,'delete.html')