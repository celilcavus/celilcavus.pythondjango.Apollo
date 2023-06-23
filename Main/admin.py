from django.contrib import admin
from . import models
# Register your models here.


class AdminModelA(admin.ModelAdmin):
    list_display = ('id','title','description')

class AdminModelP(admin.ModelAdmin):
    list_display = ('id','title','description','insta','face','twitter','pintrest')

class AdminModelO(admin.ModelAdmin):
    list_display = ('id','image1','image2','image3')

class AdminModelL(admin.ModelAdmin):
    list_display = ('id','title','description')
    

class AdminModelL2(admin.ModelAdmin):
    list_display = ('id','image1','image2','image3')

class AdminModelO2(admin.ModelAdmin):
    list_display = ('id','mail','subject','message')



admin.site.register(models.ApolloModelA,AdminModelA)
admin.site.register(models.ApolloModelP,AdminModelP)
admin.site.register(models.ApolloModelO,AdminModelO)
admin.site.register(models.ApolloModelL2,AdminModelL2)
admin.site.register(models.ApolloModelO2,AdminModelO2)