import datetime as dt

from django.db.models import Count

from apps.visits_count.models import VisitCountModel

# from apps.visits_count.serializers import VisitCountCreateSerializer

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def visit_add(request, advert):
    ip = get_client_ip(request)
    user = request.user

    # варіант без накруток
    obj, created = VisitCountModel.objects.get_or_create(ip=ip, advert=advert, user=user.id)

    return f'visit is add = {created}'


def get_visit_count(advert, user):
    count_all, count_day, count_week, count_month = [0, 0, 0, 0]

    if hasattr(user, 'profile'):
        if user.profile.premium_acc:
            # qs = VisitCountModel.objects.values('advert', 'created_at').filter(advert=advert)
            qs = VisitCountModel.objects.filter(advert=advert)
            today_date = dt.date.today()
            today_datetime = dt.datetime.today()
            print(today_date, today_datetime)
            print(today_date - dt.timedelta(days=7))
            print(today_datetime - dt.timedelta(days=7))

            count_all = qs.count()
            count_day = qs.filter(created_at__gte=today_datetime - dt.timedelta(hours=1)).aggregate(
                count_day=Count('advert'))
            count_week = qs.count()
            count_month = qs.count()
            print(count_day)

    return count_all
