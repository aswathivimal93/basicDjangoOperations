from django.http import HttpResponse

from .forms import movieForm
from .models import Movie

from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,"index.html",context)

def details(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        des=request.POST.get('des')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie=Movie(name=name,des=des,year=year,img=img)
        movie.save()
        return redirect('/')
    return render(request,'add.html')
def update_movie(request,id):
    movie=Movie.objects.get(id=id)
    form=movieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')


