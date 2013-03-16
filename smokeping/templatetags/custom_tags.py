from django import template

register = template.Library()

@register.filter
def tag(list, tag):
    new_list = [a.name + ':/' + tag for a in list]
    return ' '.join(new_list)
