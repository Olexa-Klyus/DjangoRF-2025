from locale import currency

from django.db.models import Avg, Case, When

from apps.adverts.models import AdvertModel
from apps.currency.services import get_last_points


def get_avg_prices(advert, user):
    avg_prices = {}
    if hasattr(user, 'profile'):
        if user.profile.premium_acc:
            currency_points = [1, 42, 45]

            qs = (AdvertModel.objects.filter(brand=advert.brand, mark=advert.mark)).select_related('currency').values(
                'currency__id', 'currency__name')

            qs_all = qs.annotate(avg_price_all=Avg('price'))
            if advert.region:
                qs_region = qs.filter(region=advert.region).annotate(avg_price_region=Avg('price'))
                print('region-------------', qs_region)
            print('all-------------', qs_all)

    return avg_prices


def get_calculated_prices(price, currency_id):
    points = get_last_points()

    prices = [{"UAH": 0},
              {"USD": 0},
              {"EUR": 0}]

    if points:
        match currency_id:
            case 1:  # UAH
                prices = [{"UAH": price},
                          {"USD": price / points[0]["saleRate"]},
                          {"EUR": price / points[1]["saleRate"]}]
            case 2:  # USD
                prices = [{"USD": price},
                          {"UAH": price * points[0]["saleRate"]},
                          {"EUR": price * points[0]["saleRate"] / points[1]["saleRate"]}]
            case 3:  # EUR
                prices = [{"EUR": price},
                          {"UAH": price * points[1]["saleRate"]},
                          {"USD": price * points[1]["saleRate"] / points[0]["saleRate"]}]

    return prices
