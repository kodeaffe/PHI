from django import template

from django.core.urlresolvers import translate_url

register = template.Library()


@register.simple_tag(takes_context=True)
def change_lang(context, lang: str, *args, **kwargs):
    """Returns a URL for the current page in given language (code)"""
    path = context['request'].path
    return translate_url(path, lang)
