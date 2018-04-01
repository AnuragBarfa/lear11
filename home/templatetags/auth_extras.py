from django import template
from django.contrib.auth.models import Group

register = template.Library()
#   load this file in the html page where you want to use this {% load auth_extras %} to load
@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False