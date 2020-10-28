import re
from django import template
from ..models import client
from rich_text_renderer import RichTextRenderer

from rich_text_renderer.base_node_renderer import BaseNodeRenderer

register = template.Library()

renderer = RichTextRenderer({})

@register.filter
def render(input):
    return renderer.render(input)
