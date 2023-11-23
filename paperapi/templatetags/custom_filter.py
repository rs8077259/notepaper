from django import template
register=template.Library()
@register.filter
def split(value,delimiter):
    return value.split(delimiter)
@register.filter
def is_img(text):
    return True if text.split('=')[0]=='img' else False
@register.filter
def is_video(text):
    return True if text.split('=')[0]=='video' else False
@register.filter
def media(text):
    return 'media/'+text.split('=')[1]
