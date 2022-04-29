from django.contrib import admin
from .models import Publicidad,empleo,perfil,comentarios

# Register your models here.
class PublicidadAdmin (admin.ModelAdmin):
    list_display =  ["nombre_publicidad","descripcion_publicidad","nombre_video"]
    list_editable = ["nombre_video"]
    search_fields = ["nombre_publicidad"]
    list_filters = ["nombre_publicidad"]
    list_per_page = 1
   # list_filters = ["costo"]

   
class empleoAdmin (admin.ModelAdmin):
    list_display =  ["nombre_empleo","dirrecion","jornada"]
    list_editable = ["jornada"]
    search_fields = ["jornada"]
    list_filters = ["jornada"]
    list_per_page = 1

class perfilAdmin (admin.ModelAdmin):
    list_display =  ["nombre","descripcion","sitio","dirrecion"]
    list_editable = ["sitio","descripcion","dirrecion"]
    search_fields = ["nombre"]
    list_filters = ["nombre"]
    list_per_page = 1


   


admin.site.register(Publicidad,PublicidadAdmin)
admin.site.register(empleo,empleoAdmin)
admin.site.register(perfil,perfilAdmin)
admin.site.register(comentarios)


