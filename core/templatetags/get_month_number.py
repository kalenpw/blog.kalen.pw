from django import template

register = template.Library()


@register.filter
def get_month_number(month):
    months = [
        'Jan.',
        'Feb.',
        'Mar.',
        'Apr.',
        'May.',
        'Jun.',
        'Jul.',
        'Aug.',
        'Sep.',
        'Oct.',
        'Nov.',
        'Dec.'
    ]
    return str(months.index(month) + 1).zfill(2)
