from django import template

register = template.Library()


@register.filter
def money(value, currency='$'):
    """
    Custom filter: 1234.5 -> "$1 234.50", 29 -> "$29".
    The currency symbol is optional: {{ price|money:"EUR " }}
    """
    try:
        number = float(value)
    except (TypeError, ValueError):
        return value
    text = f'{number:,.2f}'.replace(',', ' ')
    if text.endswith('.00'):
        text = text[:-3]
    return f'{currency}{text}'
