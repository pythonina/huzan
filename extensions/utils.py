from . import jalali
from django.conf import settings
import ghasedakpack
from django.http.response import JsonResponse
from posts.models import Limiter
from django.utils import timezone
from functools import wraps

sms = ghasedakpack.Ghasedak(settings.SMS_APIKEY)

def jalali_converter(time):
    jmonths = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    
    time_to_tuple = jalali.Gregorian(time).persian_tuple()
    time_to_list = list(time_to_tuple)
    time_to_list[1] = jmonths[time_to_list[1] - 1]

    output = "{} {} {}".format(
        time_to_list[2],
        time_to_list[1],
        time_to_list[0]
    )

    return output


def send_sms(**kwargs):
    res = sms.verification({**kwargs})
    if res == False:
        return JsonResponse({}, status=500)
    

def _get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def check_limit(func):
    @wraps(func)
    def wrapper(instance, request, *args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            ip = _get_client_ip(request)
            path = ip + request.path
            count = Limiter.objects.filter(path=path, date__gt=timezone.now() - timezone.timedelta(minutes=2)).count()
            if count > 5:
                return JsonResponse({'msg': 'متاسفیم، تعداد درخواست بیش از حد مجاز'}, status=400)
            Limiter.objects.create(path=path)
            return func(instance, request, *args,**kwargs)
    return wrapper

