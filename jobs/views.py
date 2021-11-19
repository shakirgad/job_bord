from django.shortcuts import render,redirect
from .models import*
from django.core.paginator import Paginator
from .forms import APlayForm,AddJobForm
from .filters import JobsFilter



def job_list(request):
    job_list=Jobs.objects.all()
    myFilter = JobsFilter(request.GET ,queryset=job_list)
    #job_lis=myFilter.qs
    
    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request ,'job_list.html',{
        'job_list':page_obj ,
        'myFilter':myFilter
    })

def job_detail(request , slug ):
    job_detail=Jobs.objects.get(slug=slug)
    if request.method=='POST':
        form = APlayForm(request.POST, request.FILES) 
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    
    else:
        form = APlayForm()
    return render(request ,'job_detail.html',{
        'job_detail':job_detail,
        'form':form
        })
        
def addjob(request):
    
    if request.method=='POST':
        form2 = AddJobForm(request.POST,request.FILES)
        if form2.is_valid():
            myform2=form2.save(commit=False)
            myform2.addman = request.user
            myform2.save()
            return redirect('jobs:home')
        
    else:
        form2 = AddJobForm()
    
    return render(request,'add_job.html',{'form2':form2 })
    

