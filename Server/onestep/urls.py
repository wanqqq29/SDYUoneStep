import onestep.views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', onestep.views.get_index_page),
    path('serviceSubmit/',onestep.views.serviceSubmit),
    path('tabpanelSubmit/',onestep.views.tabpanelSubmit),
    path('sJxfwApi/',onestep.views.sJxfwApi),
    path('tabpanelApi/',onestep.views.tabpanelApi),
    path('cardApi/',onestep.views.cardApi),
    path('submitApi/',onestep.views.submitApi),

]
