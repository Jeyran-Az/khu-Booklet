from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import File, Category, Comment
from .forms import FileForm
from django.contrib.auth.decorators import login_required




def index(request):
	return render(request, 'BookletApp/index.html')

#def base(request):
    #return render(request, 'BookletApp/base.html')

@login_required
def files_list(request):
    files= File.objects.filter(owner=request.user).order_by('uploaded_date')
    context= {'files': files,}
    return render(request, 'BookletApp/files_list.html', context= context)

@login_required
def categories_list(request):
    categories= Category.objects.all()
    context= {'categories': categories}
    return render(request, 'BookletApp/categories_list.html', context= context)

@login_required
def file_create_form(request):
    form= FileForm(request.POST)
    if form.is_valid():
       form.save()
    context= {"form":form}
    return render(request,'BookletApp/file_create.html',context)

'''
def category_detail(request, category_id):
    try:
       category= Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
       return HttpResponseNotFound("Category doesn't exist!")
       

    comments= Comment.objects.filter(category=category)
    context= {'category':category, 'comments':comments}
    return render(request, 'BookletApp/category_detail.html', context=context)
'''    

def new_category(request):
	return render(request, 'BookletApp/new_category.html')

def new_file(request):
	return render(request, 'BookletApp/new_file.html')

def about(request):
	return render(request, 'BookletApp/about.html')

def contact(request):
	return render(request, 'BookletApp/contact.html')


def randomprocesses(request):
	return render(request, 'BookletApp/randomprocesses.html')

def fuzzy(request):
	return render(request, 'BookletApp/fuzzy.html')

def graph(request):
	return render(request, 'BookletApp/graph.html')

def stat_methods(request):
	return render(request, 'BookletApp/stat_methods.html')

def probability1(request):
	return render(request, 'BookletApp/probability1.html')

def math_softwares(request):
	return render(request, 'BookletApp/math_softwares.html')


def ad_programming(request):
	return render(request, 'BookletApp/ad_programming.html')

def ranalysis(request):
	return render(request, 'BookletApp/ranalysis.html')

def coding(request):
	return render(request, 'BookletApp/coding.html')

def lopt(request):
	return render(request, 'BookletApp/lopt.html')


def comfunc(request):
	return render(request, 'BookletApp/comfunc.html')

def numth(request):
	return render(request, 'BookletApp/numth.html')


@login_required
def general(request):
    #categories= Category.objects.all()
    #context= {'categories': categories}
    return render(request, 'BookletApp/general.html')#, context= context)	

def defa(request):
	return render(request, 'BookletApp/defa.html')

def help(request):
	return render(request, 'BookletApp/help.html')

#def test(request):
	#return render(request, 'BookletApp/test.html')

#def comfunc(request):
	#return render(request, 'BookletApp/comfunc.html')    











