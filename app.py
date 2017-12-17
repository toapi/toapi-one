#!/usr/bin/env python
from toapi import Api

from items.index import IndexOne, IndexArticle, IndexQuestion
from items.article import Article
from items.question import Question
from items.one import One
from settings import MySettings

api = Api(settings=MySettings)

api.register(IndexOne)
api.register(IndexArticle)
api.register(IndexQuestion)
api.register(Article)
api.register(Question)
api.register(One)

api.serve(ip='0.0.0.0', port='5000')
