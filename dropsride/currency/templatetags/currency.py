from decimal import Decimal

from django import template

register = template.Library()


def exchange(value, request):
    """
    This converts any given price to the users selected currency of choice. The base currency is dollar ($)

    eg: {{value|exchange:arg}}

    {arg} can be any symbol "$ N" etc as defined in the Currency model symbol field
    """
    user = request.user
    cur = user.wallet.currency if user.wallet else None
    if cur.symbol != "$" and user.is_authenticated:
        result = Decimal(value) * Decimal(cur.price)
        return round(result, 2)
    return round(Decimal(value), 2)


register.filter("exchange", exchange)
