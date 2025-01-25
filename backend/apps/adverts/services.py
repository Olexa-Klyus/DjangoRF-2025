from locale import currency

from django.db.models import Avg, Case, Count, F, Q, Sum, When

from apps.adverts.models import AdvertModel
from apps.currency.models import CurrencyModel


def get_avg_prices(advert, user):
    avg_prices = {}
    if hasattr(user, 'profile'):
        if user.profile.premium_acc:
            qs = (AdvertModel.objects.filter(brand=advert.brand, mark=advert.mark)).select_related('currency').values(
                'currency__saleRate', 'price').annotate(sum_as_UAH=F('currency__saleRate') * F('price'))

            if advert.region:
                avg_region = qs.filter(region=advert.region).aggregate(avg_price_region=Avg('sum_as_UAH'),
                                                                       counter=Count('price'))

            if advert.city:
                avg_city = qs.filter(city=advert.city).aggregate(avg_price_city=Avg('sum_as_UAH'),
                                                                 counter=Count('price'))

            avg_all = qs.aggregate(avg_price_all=Avg('sum_as_UAH'), counter=Count('price'))

            # print('all_qqssss', avg_all)


            # потрібно ще поділити на курс і видати в int
            avg_prices['ccy'] = advert.currency.name
            avg_prices['avg_all'] = round(avg_all['avg_price_all']/advert.currency.saleRate, 0)




    return avg_prices
