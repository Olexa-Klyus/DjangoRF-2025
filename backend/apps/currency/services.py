import datetime as dt

from apps.currency.models import CurrencyPointModel


def get_last_points():
    query_set = CurrencyPointModel.objects.all().select_related('currency')[:2]
    points = []
    for item in query_set:
        points.append({
            "currency_point_date": item.date_point,
            "currency_id": item.currency.id,
            "currency_name": item.currency.name,
            'saleRate': item.saleRate,
            'purchaseRate': item.purchaseRate,
        })
    return points


def point_is_actual():
    last_point = CurrencyPointModel.objects.values('updated_at')
    point = False

    if last_point:
        point = True
        # до 10 години ранку курс вчорашній, після 10 год. оновлюється на першому запиті з АРІ банку, далі вже тягнем з бази
        if dt.datetime.now().hour >= 10:
            res = last_point[0]['updated_at']
            last_date_point = dt.date(res.year, res.month, res.day)

            today = dt.date.today()
            if last_date_point == today:
                point = True
            else:
                point = False

    return point
