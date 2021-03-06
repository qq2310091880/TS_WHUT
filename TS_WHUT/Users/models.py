"""
数据模板
"""
from django.db import models
from datetime import datetime  # 导入当前时间
from django.contrib.auth.models import AbstractUser  # 这个model是数据库默认的user
from utils.storage import ImageStorage
from easy_thumbnails.fields import ThumbnailerImageField
from PIL import Image, ImageDraw, ImageFont
from TS_WHUT.settings import LOGO_ROOT, BASE_DIR


class EmailVerifyRecord(models.Model):
    # 邮箱验证
    code = models.CharField(max_length=20, verbose_name="验证码")
    send_email = models.EmailField(max_length=50, verbose_name="邮箱")
    send_type = models.CharField(choices=(("register", "注册"), ("forget", "找回密码"), ("update_email", "修改邮箱")),
                                 max_length=30, verbose_name="验证码类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.send_email)


class UserProfile(AbstractUser):
    # 用户
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(max_length=7, null=True, blank=True,
                              choices=(("male", "男"), ("female", "女")),
                              default="female", verbose_name="性别")
    mobile = models.CharField(max_length=11, null=True,
                              blank=True, verbose_name="手机号码")
    number = models.CharField(max_length=20, verbose_name="学号",
                              null=True, blank=True)
    image = models.ImageField(upload_to="heads/%Y/%m", default="heads/default.png", null=True, blank=True,
                              storage=ImageStorage(), max_length=100, verbose_name="头像")
    if_sign = models.BooleanField(verbose_name="签约", default=False)
    follow_nums = models.IntegerField(verbose_name="关注者量", default=0)
    fan_nums = models.IntegerField(verbose_name="粉丝量", default=0)
    upload_nums = models.IntegerField(verbose_name="上传量", default=0)
    like_nums = models.IntegerField(verbose_name="总点赞量", default=0)
    collection_nums = models.IntegerField(verbose_name="总收藏量", default=0)
    download_nums = models.IntegerField(verbose_name="总被下载量", default=0)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Follow(models.Model):
    # 关注关系
    follow = models.ForeignKey(UserProfile, related_name="follow_user",
                               on_delete=models.SET_NULL, null=True, verbose_name="被关注者")
    fan = models.ForeignKey(UserProfile, related_name="fan_user",
                            on_delete=models.SET_NULL, null=True, verbose_name="粉丝")
    add_time = models.DateField(default=datetime.now, verbose_name="关注时间")

    class Meta:
        verbose_name = "关注关系"
        verbose_name_plural = verbose_name


class BannerModel(models.Model):
    # 轮播图
    title = models.CharField(max_length=100, verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y/%m", storage=ImageStorage(),
                              verbose_name="轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name="访问地址")
    if_show = models.BooleanField(default=False, verbose_name="是否显示")
    index = models.IntegerField(default=100, verbose_name="顺序")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ImageModel(models.Model):
    # 图片
    image = ThumbnailerImageField(upload_to="images/%Y/%m", storage=ImageStorage(),
                                  verbose_name="图片", max_length=100, null=True, blank=True)
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    if_active = models.BooleanField(default=False, verbose_name="是否通过审核")
    desc = models.CharField(max_length=200, verbose_name="描述",
                            null=True, blank=True)
    user = models.ForeignKey(UserProfile, models.SET_NULL,
                             null=True, verbose_name="上传人")
    pattern = models.CharField(max_length=10, verbose_name="格式", default="png")
    like_nums = models.IntegerField(default=0, verbose_name="点赞数")
    cates = models.CharField(max_length=200, verbose_name="种类字符串", default="")
    collection_nums = models.IntegerField(default=0, verbose_name="收藏数")
    download_nums = models.IntegerField(default=0, verbose_name="下载量")
    name = models.CharField(max_length=20, verbose_name="名字", default="")

    class Meta:
        verbose_name = "图片"
        verbose_name_plural = verbose_name


class GroupImage(models.Model):
    # 图片种类
    name = models.CharField(verbose_name="图片分类", max_length=20)
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    image = models.ForeignKey(ImageModel, models.SET_NULL,
                              null=True, verbose_name="图片")

    class Meta:
        verbose_name = "图片分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class LikeShip(models.Model):
    # 点赞关系
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                             null=True, verbose_name="用户名")
    image = models.ForeignKey(ImageModel, on_delete=models.SET_NULL,
                              null=True, verbose_name="图片")
    add_time = models.DateField(default=datetime.now, verbose_name="点赞时间")

    class Meta:
        verbose_name = "点赞"
        verbose_name_plural = verbose_name


class DownloadShip(models.Model):
    # 下载关系
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                             null=True, verbose_name="用户名")
    image = models.ForeignKey(ImageModel, on_delete=models.SET_NULL,
                              null=True, verbose_name="图片")
    add_time = models.DateField(default=datetime.now, verbose_name="下载时间")

    class Meta:
        verbose_name = "下载"
        verbose_name_plural = verbose_name


class Folder(models.Model):
    name = models.CharField(max_length=20, verbose_name="收藏文件夹",
                            default="默认文件夹")
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                             null=True, verbose_name="用户")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    nums = models.IntegerField(default=0, verbose_name="数量")

    class Meta:
        verbose_name = '收藏夹'
        verbose_name_plural = verbose_name


class FolderImage(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.SET_NULL,
                               null=True, verbose_name="文件夹")
    image = models.ForeignKey(ImageModel, on_delete=models.SET_NULL,
                              null=True, verbose_name="图片")
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                             null=True, verbose_name="用户")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "图片文件夹关系"
        verbose_name_plural = verbose_name


class Comment(models.Model):
    image = models.ForeignKey(ImageModel, on_delete=models.SET_NULL,
                              null=True, verbose_name="图片")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                             null=True, verbose_name="用户", related_name="speaker")
    reply = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                              null=True, verbose_name="回复人", related_name="listen")
    content = models.CharField(max_length=200, verbose_name="评论")
    like = models.IntegerField(default=0, verbose_name="点赞数")

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.SET_NULL,
                                null=True, verbose_name="评论")
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                             null=True, verbose_name="用户")
    add_time = models.DateField(default=datetime.now, verbose_name="添加时间")
