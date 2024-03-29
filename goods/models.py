from django.db import models


class Category(models.Model):  # 商品类别
    cname = models.CharField(max_length=10)

    def __unicode__(self):       #python 3 用  def__str__(sef):
        return u'Category:%s' % self.cname


class Goods(models.Model):
    gname = models.CharField(max_length=100)
    gdesc = models.CharField(max_length=100)
    oldprice = models.DecimalField(max_digits=5, decimal_places=2)  # 小数最大长度，保留位数
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey('Category', models.DO_NOTHING)

    def __unicode__(self):
        return u'Goods:%s' % self.gname

    # 获取商品图
    def getGImg(self):
        return self.inventory_set.first().color.colorurl

        # 获取商品所有颜色对象
    def getColorList(self):
        colorList = []
        for inventory in self.inventory_set.all():
            color = inventory.color
            if color not in colorList:
                colorList.append(color)
                # print(colorList)
        return colorList
    # 取商品所有尺寸对象
    def getSizeList(self):
        sizeList = []
        for inventory in self.inventory_set.all():
            size = inventory.size
            if size not in sizeList:
                sizeList.append(size)
                # print(sizeList)
        return sizeList
    # 获取所有的详情信息
    def getDetailList(self):
        import collections
        # 创建一个有序字典用于存放详情信息（key:详情名称value:图片列表）
        datas = collections.OrderedDict()
        for goodsdetail in self.goodsdetail_set.all():
            # 获取详情名称
            gdname = goodsdetail.name()
            if not gdname in datas:
                datas[gdname] = [goodsdetail.gdurl]
            else:
                datas[gdname].append(goodsdetail.gdurl)
        return datas

class GoodsDetailName(models.Model):     #详情名称
    gdname = models.CharField(max_length=30)

    def __unicode__(self):
        return u'GoodsDetailName:%s' % self.gdname


class GoodsDetail(models.Model):   #商品详情
    gdurl = models.ImageField(upload_to='')
    gdname = models.ForeignKey('GoodsDetailName', models.DO_NOTHING)
    goods = models.ForeignKey('Goods', models.DO_NOTHING)

    def name(self):
        return self.gdname.gdname

class Size(models.Model):
    sname = models.CharField(max_length=10)

    def __unicode__(self):
        return u'Size:%s' % self.sname


class Color(models.Model):
    colorname = models.CharField(max_length=100)
    colorurl = models.ImageField(upload_to='media/color/')

    def __unicode__(self):
        return u'Color:%s' % self.colorname


class Inventory(models.Model):  # 库存
    count = models.PositiveIntegerField()
    color = models.ForeignKey('Color', models.DO_NOTHING)
    goods = models.ForeignKey('Goods', models.DO_NOTHING)
    size = models.ForeignKey('Size', models.DO_NOTHING)
