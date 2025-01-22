from apps.currency.services import get_last_points


def get_avg_prices(advert):
    pass


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
