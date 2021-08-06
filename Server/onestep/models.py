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
    mSrc = models.ImageField(upload_to='menuimg', verbose_name='商铺图片', null=True)
    class Meta:
        db_table='o_tabpanel'

    def __str__(self):
        return f'{self.label}'
#商品表
class card(models.Model):
    spID = models.AutoField(primary_key=True)
    imgSrc = models.ImageField(upload_to='menuimg', verbose_name='商品图片', null=True)
    sName = models.CharField(max_length=30,null=False)
    sPrice = models.CharField(max_length=30,null=False)
    sDesc = models.CharField(max_length=512,null=False)
    cName = models.ForeignKey(tabpanel,on_delete=models.CASCADE,db_constraint=False)
    class Meta:
        db_table='o_card'


#banner表
class banner(models.Model):
    ID = models.AutoField(primary_key=True)
    bSrc = models.ImageField(upload_to='banner', verbose_name='banner', null=True)
    class Meta:
        db_table:'banner'

#新闻表
class NewsLine(models.Model):
    title = models.CharField(max_length=255,null=False)
    subtitle = models.CharField(max_length=255,null=False)
    body = models.CharField(max_length=888,null=False)
    class Meta:
        db_table:'NewsLine'