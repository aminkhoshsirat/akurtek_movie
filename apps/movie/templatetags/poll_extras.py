from django import template

register = template.Library()


@register.filter()
def money_format(value):
    if value is None:
        value = 0
    return f'{value:,}'
