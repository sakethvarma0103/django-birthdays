from django.urls import path
from . import views
urlpatterns = [
    path("",views.index , name="index"),
    path("<int:month>",views.monthly_bynumber),
    path("<str:month>",views.monthlyc,name="chal")
]
