import onestep.views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', onestep.views.get_index_page),
    path('submit/',onestep.views.submit),
    path('sJxfwApi/',onestep.views.sJxfwApi)

]
