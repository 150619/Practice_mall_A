from django.db import models


class BookInfo(models.Model):
    """图书信息：演示一对多，一方"""
    btitle = models.CharField(max_length=20, verbose_name='书名')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        """模型类的元类：用于修改、配置模型类对应的数据表"""
        db_table = 'tb_books'  # 自定义数据库表名

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle  # 输出该模型数据对象时，只输出书名


class HeroInfo(models.Model):
    """英雄信息：演示一对多，多方"""
    # 确定性别字段的取值范围
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='英雄属于的图书')
    hname = models.CharField(max_length=20, verbose_name='人名')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heros'

    def __str__(self):
        return self.hname
