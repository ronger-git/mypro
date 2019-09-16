from django.contrib import admin

# Register your models here.

from .models import Grades,Students

#注册
class StudentsInfo(admin.TabularInline):   #SimpleListFilter
    model = Students
    extra = 2

class GradesAdmin(admin.ModelAdmin):

    inlines = [StudentsInfo]

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
    def gender(self):
        if self.sgender:
            return 'nan'
        else:
            return 'nv'
    #原页面列的名称
    gender.short_description ='性别'

    #列表页属性
    list_display = ['pk','sname','sage',gender,'sxontend','sgrade','isDelete']
    list_per_page = 2

admin.site.register(Students,StudentsAdmin)