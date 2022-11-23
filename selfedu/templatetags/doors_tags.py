from django import template

from selfedu.models import *
from selfedu.views import menu
register = template.Library()


@register.simple_tag(name='getdoors')
def get_doors(filter=None):
    if not filter:
        return Doors.objects.all()
    else:
        return Doors.objects.filter(pk=filter)



@register.inclusion_tag('selfedu/list_doors.html')
def show_doors(sort=None, door_selected=0):
    if not sort:
        doors = Doors.objects.all()
    else:
        doors = Doors.objects.order_by(sort)

    return {"doors": doors, "door_selected": door_selected}


@register.inclusion_tag('selfedu/list_menu.html')
def show_menu(item_selected=0):
        return {"menu": menu, "item_selected": item_selected}
