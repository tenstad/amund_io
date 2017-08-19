from django import template
import markdown2

register = template.Library()

@register.filter(name='markdown')
def markdown(text):
    return markdown2.markdown(text)
