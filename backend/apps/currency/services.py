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


def get_calculated_prices(price, currency_id):
    points = get_last_points()
    prices = []

    match currency_id:
        case 1:  # UAH
            prices = [{"UAH": str(price)},
                      {"USD": price / points[0]["saleRate"]},
                      {"EUR": price / points[1]["saleRate"]}]
        case 2:  # USD
            prices = [{"USD": str(price)},
                      {"UAH": price * points[0]["saleRate"]},
                      {"EUR": price * points[0]["saleRate"] / points[1]["saleRate"]}]
        case 3:  # EUR
            prices = [{"EUR": str(price)},
                      {"UAH": price * points[1]["saleRate"]},
                      {"USD": price * points[1]["saleRate"] / points[0]["saleRate"]}]

    return prices
