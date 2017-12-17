#!/usr/bin/env python
from toapi import Item, Css


class Article(Item):
    __base_url__ = "http://wufazhuce.com"

    title = Css("h2.articulo-titulo")
    author = Css("p.articulo-autor")
    abstract = Css("div.comilla-cerrar")
    content = Css("div.articulo-contenido")

    def clean_title(self, title):
        return title.strip()

    def clean_author(self, author):
        return author.strip()

    def clean_abstract(self, abstract):
        return abstract.strip()

    class Meta:
        source = None
        route = '/article/.*?'
