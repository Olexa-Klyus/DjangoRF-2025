from locale import currency

from django.db.models import Avg, Case, Q, When

from apps.adverts.models import AdvertModel
from apps.currency.models import CurrencyModel


def get_avg_prices(advert, user):
    avg_prices = {}
    if hasattr(user, 'profile'):
        if user.profile.premium_acc:

            qs = (AdvertModel.objects.filter(brand=advert.brand, mark=advert.mark)).select_related('currency').values(
                "price", 'currency__name', 'currency__saleRate')

            # qs_all = qs.aggregate(Avg(Q('price * 2')))
            if advert.region:
                qs_region = qs.filter(region=advert.region).annotate(avg_price_region=Avg('price'))
                print('region-------------', qs_region)
            print('all_qqssss', qs)
            # print('all_qq44444444444444', qs_all)

    return avg_prices
