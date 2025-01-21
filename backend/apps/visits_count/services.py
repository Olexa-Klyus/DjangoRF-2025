from itertools import count

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

    obj, created = VisitCountModel.objects.get_or_create(ip=ip, advert=advert, user=user.id)

    return f'visit is add = {created}'


def get_visit_count(advert, user):
    counter = 0

    if hasattr(user, 'profile'):
        if user.profile.premium_acc:
            counter = VisitCountModel.objects.filter(advert=advert).count()

    return counter
