import onestep.views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    # path('', onestep.views.get_index_page),
    path('sJxfwApi/',onestep.views.sJxfwApi),
    path('tabpanelApi/',onestep.views.tabpanelApi),
    path('cardApi/',onestep.views.cardApi),
    path('bannerApi/',onestep.views.bannerApi),
    path('newsApi/',onestep.views.NewsApi),

]
