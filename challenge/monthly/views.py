from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthdic={
    "january":"Teja-17",
    "february":"Bhaagi-26,Sriks-5",
    "march":"Me-1,Radha-25",
    "april":None,
    "may":"harshey-7",
    "june":"Puvva-21",
    "july":None,
    "august":"Lohitha-18",
    "september":"Rosh-28",
    "october":None,
    "november":None,
    "december":"Karim-5",
}

def index(request):
    months=list(monthdic.keys())
    return render(request,"index.html",{
        "months":months
    })

def monthly_bynumber(request,month):
    months=list(monthdic.keys())
    if month<=12:
        redirect=months[month-1]
        redirect_url=reverse("chal",args=[redirect])
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound("No month")

def monthlyc(request,month):
    # try:
        return render(request,"monthly.html",{
             "text":monthdic[month],
             "m":month
        })
    # except:
    #     return HttpResponseNotFound("No month")

