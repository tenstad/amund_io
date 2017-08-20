from django import template
import markdown2

register = template.Library()

@register.filter(name='markdown')
def markdown(text):
    result = ''
    while '</' in text:
        start = text.index('<')
        end = text.index('</')
        end = text.index('>', end) + 1
        start_end = text.index('>', start) + 1
        end_start = text.index('<', start_end)
        result += markdown2.markdown(text[:start])
        result += text[start:start_end]
        result += markdown2.markdown(text[start_end:end_start])
        result += text[end_start:end]
        text = text[end:]
    result += markdown2.markdown(text)

    while '<p><img' in result:
        start = result.index('<p><img')
        end = result.index('>', start + 3) + 1
        result = result[:start] + result[start + 3:end] + result[end + 4:]

    return result
