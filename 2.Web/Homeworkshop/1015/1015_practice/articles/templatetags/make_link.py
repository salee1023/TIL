from django import template

register = template.Library()

@register.filter()
def hashlink(what):
    new_content = ''
    for word in what.split():
        if word.startswith('#'):
            word = '<a href="#">'+word+'</a>'
            new_content += word
            # new_content += ' '+'<a href="#">'+word+'</a>'
        else:
            new_content += word
    return new_content
            


