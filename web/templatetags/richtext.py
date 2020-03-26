from django import template
from rich_text_renderer import RichTextRenderer

register = template.Library()

renderer = RichTextRenderer()

@register.filter
def render(input):
    return renderer.render(input)
