from django.db import models

# Create your models here.

#班级
class Grades(models.Model):
    gname = models.CharField(max_length=20)
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    def _str_(self):
        return "%s-%d-%d"%(self.gname,self.ggirlnum,self.gboynum)

#学生
class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    sxontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    #关联外键
    sgrade = models.ForeignKey("Grades")
    def _str_(self):
        return "%s-%d-%d"%(self.gname,self.ggirlnum,self.gboynum)

