#!/usr/bin/env python
from toapi import Item, Css


class IndexOne(Item):
    __base_url__ = "http://wufazhuce.com"

    # One
    one_item_list = Css("div#carousel-one div.item")

    def clean_one_item_list(self, one_item):
        item_list = []
        for item in one_item:
            each_item = {}
            each_item['one_index'] = item.cssselect('div.fp-one-titulo-pubdate p.titulo')[0].text.strip()
            each_item['one_type'] = item.cssselect('div.fp-one-imagen-footer')[0].text.strip()
            each_item['one_url'] = 'http://127.0.0.1:5000/' + item.cssselect('div.fp-one-cita a')[0].get('href')
            abstract = ''
            for node in item.cssselect('div.fp-one-cita a')[0].itertext():
                abstract += node.strip() + "    "
            each_item['one_abstract'] = abstract
            each_item['date'] = item.cssselect('div.fp-one-titulo-pubdate p.dom')[0].text + " " + \
                                item.cssselect('div.fp-one-titulo-pubdate p.may')[0].text
            item_list.append(each_item)
        return item_list

    class Meta:
        source = None
        route = '/$'


class IndexArticle(Item):
    __base_url__ = "http://wufazhuce.com"

    # Article
    one_article_index = Css(".fp-one-articulo p.one-titulo")
    one_article_title = Css(".fp-one-articulo p.one-articulo-titulo a")
    one_article_url = Css(".fp-one-articulo p.one-articulo-titulo a", attr='href')
    one_article_list = Css(".fp-one-articulo ul li")

    def clean_one_article_url(self, one_article_url):
        return 'http://127.0.0.1:5000/' + one_article_url

    def clean_one_article_list(self, one_article_list):
        article_list = []
        for article in one_article_list:
            each_article = {}
            each_article['one_index'] = article.cssselect('span')[0].text.strip()
            each_article['one_title'] = article.cssselect('a')[0].text.strip()
            each_article['one_article_url'] = 'http://127.0.0.1:5000/' + article.cssselect('a')[0].get('href')
            article_list.append(each_article)
        return article_list

    class Meta:
        source = None
        route = '/$'


class IndexQuestion(Item):
    __base_url__ = "http://wufazhuce.com"

    # Question
    one_question_index = Css(".fp-one-cuestion p.one-titulo")
    one_question_title = Css(".fp-one-cuestion p.one-cuestion-titulo a")
    one_question_url = Css(".fp-one-cuestion p.one-cuestion-titulo a", attr='href')
    one_question_list = Css(".fp-one-cuestion ul li")

    def clean_one_question_url(self, one_question_url):
        return 'http://127.0.0.1:5000/' + one_question_url

    def clean_one_question_list(self, one_question_list):
        question_list = []
        for question in one_question_list:
            each_question = {}
            each_question['one_index'] = question.cssselect('span')[0].text.strip()
            each_question['one_title'] = question.cssselect('a')[0].text.strip()
            each_question['one_question_url'] = 'http://127.0.0.1:5000/' + question.cssselect('a')[0].get('href')
            question_list.append(each_question)
        return question_list

    class Meta:
        source = None
        route = '/$'
