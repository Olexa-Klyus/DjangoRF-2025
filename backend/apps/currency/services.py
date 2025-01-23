import datetime as dt

from apps.currency.models import CurrencyModel


def get_currency_points():
    query_set = CurrencyModel.objects.all()[1:2]
    points = []
    for item in query_set:
        points.append({
            "currency_id": item.id,
            "currency_name": item.name,
            'saleRate': item.saleRate,
            'purchaseRate': item.purchaseRate,
            "currency_point_date": item.update_at,
        })
    return points


def point_is_actual():
    last_point = CurrencyModel.objects.all()
    point = False

    if last_point:
        point = True
        # до 10 години ранку курс вчорашній, після 10 год. оновлюється на першому запиті з АРІ банку, далі вже тягнем з бази
        if dt.datetime.now().hour >= 10:
            res = last_point[1].update_at
            last_date_point = dt.date(res.year, res.month, res.day)

            today = dt.date.today()
            if last_date_point == today:
                point = True
            else:
                point = False

    return point


def get_calculated_prices(price, currency_id):
    points = list(CurrencyModel.objects.all())

    prices = [{"UAH": 0},
              {"USD": 0},
              {"EUR": 0}]

    match currency_id:
        case 1:  # UAH
            prices = [{"UAH": price},
                      {"USD": price / points[1].saleRate},
                      {"EUR": price / points[2].saleRate}]
        case 2:  # USD
            prices = [{"USD": price},
                      {"UAH": price * points[1].saleRate},
                      {"EUR": price * points[1].saleRate / points[2].saleRate}]
        case 3:  # EUR
            prices = [{"EUR": price},
                      {"UAH": price * points[2].saleRate},
                      {"USD": price * points[2].saleRate / points[1].saleRate}]

    return prices
