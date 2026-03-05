from django.shortcuts import render,redirect
from . models import Company,Job
from . forms import CompanyForm,JobForm 

# Create your views here.
def home(request):
    jobs=Job.objects.all()
    
    return render(request,'home.html',{'jobs':jobs})

def add_Company(request):
    if request.method=='POST':
        frm=CompanyForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect('home')
    frm=CompanyForm()
    return render(request,'add_company.html',{'frm':frm})

def add_job(request):
    if request.method=='POST':
        frm=JobForm(request.POST)
        print(frm)
        if frm.is_valid():
            frm.save()
            return redirect('home')
         
    frm=JobForm()
    return render(request,'add_job.html',{'frm':frm})

def delete(request,id):
    obj=Job.objects.get(id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('home')  
    return render(request,'delete.html',{'obj':obj})



def edit_job(request,id):
    obj=Job.objects.get(id=id)
    frm=JobForm(instance=obj)
    if request.method=='POST':
        frm=JobForm(request.POST,instance=obj)
        if frm.is_valid():
            frm.save()
            return redirect('home')
    return render(request,'add_job.html',{'frm':frm})


def home_company(request):
    company=Company.objects.all()
    return render(request,'home_company.html',{'company':company})


def edit_company(request,id):
    obj=Company.objects.get(id=id)
    frm=CompanyForm(instance=obj)
    if request.method=='POST':
        frm=CompanyForm(request.POST,instance=obj)
        if frm.is_valid():
            frm.save()
            return redirect('home_company')
    
    return render(request,'add_company.html',{'frm':frm})

def delete_company(request,id):
    obj=Company.objects.get(id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('home_company')
    return render(request,'delete.html',{'obj':obj})