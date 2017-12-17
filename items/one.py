#!/usr/bin/env python
from toapi import Item, Css


class One(Item):
    __base_url__ = "http://wufazhuce.com"

    index = Css("div.tab-content div.one-titulo")
    image = Css("div.tab-content div.one-imagen img", attr='src')
    abstract = Css("div.tab-content div.one-cita")
    type = Css("div.tab-content div.one-imagen-leyenda")
    date = Css("div.tab-content div.one-pubdate p")

    def clean_index(self, index):
        return index.strip()

    def clean_abstract(self, abstract):
        return abstract.strip()

    def clean_date(self, date):
        if isinstance(date, list):
            return ' '.join([i.text.strip() for i in date])

    class Meta:
        source = None
        route = '/one/.*?'
