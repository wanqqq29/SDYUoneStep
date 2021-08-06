from django.contrib import admin
from onestep.models import Service, tabpanel, card,banner,NewsLine


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('label', 'href', 'color', 'icon', 'type')


# Register your models here.
admin.site.register(Service, ServiceAdmin)

class tabPanelAdmin(admin.ModelAdmin):
    list_display = ('ckID', 'label', 'pos', 'loc')

admin.site.register(tabpanel,tabPanelAdmin)

class cardAdmin(admin.ModelAdmin):
    list_display = ('spID','imgSrc','sName','sPrice','sDesc','cName')
admin.site.register(card,cardAdmin)

class bannerAdmin(admin.ModelAdmin):
    list_display = ('ID','bSrc')
admin.site.register(banner,bannerAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','subtitle','body')
admin.site.register(NewsLine,NewsAdmin)