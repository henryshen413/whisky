from django import template
from whiskydatabase.models import Menu
from django.db.models import Q

register = template.Library()

@register.inclusion_tag('nav_menu.html', takes_context=True)
def load_menu(context):

    hierarchy = {}
    title_mapping = {}
    context['menu'] = Menu.objects.filter(parent=None, status=True).order_by("lvl")
    submenus = Menu.objects.filter(~Q(parent=None), status=True)
    context['latest_articles'] = {}

    for i in context['menu']:
        hierarchy[i.title] = []
        title_mapping[i.id] = i.title

    for i in submenus:
        hierarchy[title_mapping[i.parent_id]].append(i)

    return context

@register.filter
def show_username(user):

    return user.username


@register.filter
def convert_rate(rate):
    
    return int(rate*10)

@register.filter
def round_rate(rate):
    
    return round(rate, 1)
