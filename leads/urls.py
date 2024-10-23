from django.urls import path
from leads.views import lead_list,lead_detail,lead_create

app_name="leads"

urlpatterns = [

    path("",lead_list),
    path('<int:pk>/',lead_detail),
    path("create/",lead_create),

]