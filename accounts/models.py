from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from extensions.utils import jalali_converter
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings

from posts.models import Post
from accounts.validators import PHONE_VALIDATOR


class User(AbstractUser):

    first_name = None
    last_name = None
    last_login = None
    username = models.CharField(
        'شماره تلفن',
        validators=[PHONE_VALIDATOR],
        max_length=11,
        unique=True
    )
    expired = models.DateTimeField('تاریخ انقضا', auto_now=True, null=True)

    def get_full_name(self):
        pass

    def get_short_name(self):
        pass
    
    def __str__(self):
        return self.username


class Cart(models.Model):
    STATUS_CHOICES = (
        ('1', 'جاری'),
        ('2', 'تحویل شده'),
        ('3', 'لغو شده'),
    )
    id = models.BigAutoField('کد سفارش', primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='carts', verbose_name='کاربر')
    publish = models.DateField('زمان ثبت سفارش', auto_now_add=True)
    status = models.CharField('وضعیت سفارش', max_length=1, default='1', choices=STATUS_CHOICES)
    whats = models.BooleanField('ارتباط در وانساپ', default=False)
    
    class Meta:
        verbose_name = 'لیست سفارش'
        verbose_name_plural = 'لیست سفارشات'

    def __str__(self):
        return 'کد ' + str(self.id)

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = 'زمان ثبت سفارش'
    

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='cart_items', verbose_name='سبد خرید')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='cart_items', verbose_name='محصول')
    quantity = models.SmallIntegerField('تعداد', default=1)
    off = models.CharField('تخفیف', max_length=2, blank=True)

    class Meta:
        verbose_name = 'آیتم سفارش'
        verbose_name_plural = 'آیتم های سفارش'

    def __str__(self):
        return self.post.title

class BasketItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket_items', verbose_name='کاربر')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='basket_items', verbose_name='محصول')  
    quantity = models.SmallIntegerField('تعداد', default=1)

    class Meta:
        verbose_name = 'آیتم سبد خرید'
        verbose_name_plural = 'آیتم های سبد خرید'

    def __str__(self):
        return self.post.title

    @receiver(pre_save, sender=Post)
    def delete_basket_items_has_not_avail_post(sender, instance, **kwargs):
        if instance.id is not None:
            previous_avail = sender.objects.only('avail').get(id=instance.id).avail
            if previous_avail != instance.avail and previous_avail == True:
                instance.basket_items.all().delete()