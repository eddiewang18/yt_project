from django.db import models
from account.models import MyUser

# Create your models here.
class Yt_Stat(models.Model):
    stat_id = models.BigAutoField(db_column="stat_id",primary_key=True)
    yt_url = models.TextField(db_column='yt_url')
    yt_title = models.CharField(max_length = 200, db_column='yt_title')
    convert_type  = models.CharField(max_length = 5,db_column='convert_type')
    cuser = models.ForeignKey(MyUser, on_delete=models.CASCADE,to_field='email',db_column='cuser',null=True,blank=True)
    cdate = models.DateField(auto_now=False, auto_now_add=True,db_column='cdate',null=True)
    ctime  = models.TimeField(auto_now=False, auto_now_add=True,db_column='ctime',null=True)
    img_url  = models.TextField(db_column='img_url',null=True)
    

    class Meta:
        db_table = 'Yt_Stat'


class Yt_Stat_tags(models.Model):
    stat_did = models.BigAutoField(primary_key=True,db_column='stat_did')
    stat_id = models.ForeignKey(Yt_Stat, on_delete=models.CASCADE,to_field='stat_id',db_column='stat_id')
    tag_name  = models.CharField(db_column='tag_name',max_length = 150)
    cdate = models.DateField(auto_now=False, auto_now_add=True,db_column='cdate',null=True)
    ctime  = models.TimeField(auto_now=False, auto_now_add=True,db_column='ctime',null=True)

    class Meta:
        db_table = 'Yt_Stat_tags'


    
    



    
    