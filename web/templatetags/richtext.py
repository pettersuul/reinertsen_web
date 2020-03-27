import re
from django import template
from ..models import client
from rich_text_renderer import RichTextRenderer

from rich_text_renderer.base_node_renderer import BaseNodeRenderer

class entry_renderer(BaseNodeRenderer):
    def render(self, node):
        entry = node['data']['target']

        return '<div><h3>{0}</h3><a href="{0}">Les mer</a></div>'.format(
            entry.title,
            entry.slug
        )

class ol_renderer(BaseNodeRenderer):
    def render(self, node):
        list = ['<ol>']
        for item in node['content']:
            list.append('<li>' + item['content'][0]['content'][0]['value'] + '</li>')
        list.append('</ol>')
        s = ''.join(list)
        return s

class ul_renderer(BaseNodeRenderer):
    def render(self, node):
        list = ['<ul>']
        for item in node['content']:
            list.append('<li>' + item['content'][0]['content'][0]['value'] + '</li>')
        list.append('</ul>')
        s = ''.join(list)
        return s

class entrylink_renderer(BaseNodeRenderer):
    def render(self, node):
        target = str(node['data']['target'])
        text = str(node['content'][0]['value'])

        id = re.search('id=\'(.+?)\'', target).group(1)

        entry = client.entry(id)
        return '<a href="{0}">{1}</a>'.format(
            entry.slug,
            text
        )

register = template.Library()

renderer = RichTextRenderer({
    'embedded-entry-block': entry_renderer,
    'entry-hyperlink': entrylink_renderer,
    'ordered-list': ol_renderer,
    'unordered-list': ul_renderer
})

@register.filter
def render(input):
    return renderer.render(input)
