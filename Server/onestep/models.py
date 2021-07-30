from django.db import models

# Create your models here.
# 服务表
class Service(models.Model):
    # id 自增 主键
    sID = models.AutoField(primary_key=True)
    #color
    color = models.CharField(max_length=30,null=False)
    label = models.CharField(max_length=30,null=False)
    icon = models.CharField(max_length=30,null=False)
    href = models.CharField(max_length=512,null=False)
    type = models.IntegerField(null=False)
    createTime = models.DateTimeField(auto_now_add=True)
    modifyTime = models.DateTimeField(auto_now=True)
    class Meta:
        db_table='o_service'

#窗口表
class tabpanel(models.Model):
    ckID = models.AutoField(primary_key=True)
    label = models.CharField(max_length=30,null=False)
    pos = models.CharField(max_length=30,null=False)
    loc = models.IntegerField(null=False)
    class Meta:
        db_table='o_tabpanel'

#商品表
class card(models.Model):
    spID = models.AutoField(primary_key=True)
    imgSrc = models.CharField(max_length=512,null=False)
    sName = models.CharField(max_length=30,null=False)
    sPrice = models.CharField(max_length=30,null=False)
    sDesc = models.CharField(max_length=512,null=False)
    cName = models.CharField(max_length=30,null=False)
    class Meta:
        db_table='o_card'