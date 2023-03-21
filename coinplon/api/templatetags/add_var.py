from django import template

register = template.Library()

@register.filter(name='var')
def var_gen(info, arg):
    for k in info.keys():
        k = k
    for j in info[k]['quote'].keys():
        j = j
    return info[k]['quote'][j][arg]

