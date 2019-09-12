from django.contrib import admin

# Register your models here.

from .models import Grades,Students

#注册
class GradesAdmin(admin.ModelAdmin):
    #列表页属性
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5

    #修改、添加页属性
    fieldsets = [
        ('num',{'fields':['ggirlnum','gboynum']}),
        ('base',{'fields':['gname','gdate','isDelete']})
    ]
admin.site.register(Grades,GradesAdmin)

class StudentsAdmin(admin.ModelAdmin):
    #列表页属性
    list_display = ['pk','sname','sgender','sage','sxontend','sgrade','isDelete']

    list_per_page = 2


admin.site.register(Students,StudentsAdmin)