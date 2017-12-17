#!/usr/bin/env python
from toapi import Item, Css


class Question(Item):
    __base_url__ = "http://wufazhuce.com"

    title = Css("div.one-cuestion > h4")
    editor = Css("div.one-cuestion p.cuestion-editor")
    content = Css("div.one-cuestion div.cuestion-contenido")

    def clean_title(self, title):
        if isinstance(title, list):
            return ''.join([i.text.strip() for i in title])
        return title.strip()

    def clean_content(self, abstract):
        if isinstance(abstract, list):
            result = []
            for i in abstract:
                text = ''
                for node in i.itertext():
                    text += node.strip()
                value = text
                result.append(value)
            return result

        return [abstract.strip()]

    class Meta:
        source = None
        route = '/question/.*?'
