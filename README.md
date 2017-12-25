## toapi-one

### What is toapi-one?

This project uses [Toapi](https://github.com/gaojiuli/toapi) to build a friendly and robust API from [one](http://wufazhuce.com/).


``` shell

# or git clone https://github.com/toapi/toapi-one
toapi new toapi/toapi-one
cd toapi-one
# toapi run
python wsgi.py
```

Then, everything is done, the following content will show on screen:

![RUN](./docs/00.png)

### Usage:

Once the server is started, you can get JSON data from toapi-one, now toapi-one can:

- index
    - article
    - one
    - question
- article_info
- one_info
- question_info

``` json

{
    "/one/": [
        "IndexOne",
        "IndexArticle",
        "IndexQuestion"
    ],
    "/one/article/:path": [
        "Article"
    ],
    "/one/one/:path": [
        "One"
    ],
    "/one/question/:path": [
        "Question"
    ]
}

```

Visit `http://0.0.0.0:5000/_items/`

#### index_info

> http://0.0.0.0:5000/one/

``` json

{
    "IndexArticle": {
        "one_article_index": "VOL.1897",
        "one_article_list": [
            {
                "one_article_url": "http://127.0.0.1:5000/one/article/2975",
                "one_index": "VOL.1896",
                "one_title": "结婚后，你的朋友是不是变少了？"
            },
            {
                "one_article_url": "http://127.0.0.1:5000/one/article/2976",
                "one_index": "VOL.1895",
                "one_title": "文学性"
            },
            {
                "one_article_url": "http://127.0.0.1:5000/one/article/2968",
                "one_index": "VOL.1894",
                "one_title": "第一批90后还能活到2018年吗？"
            },
            {
                "one_article_url": "http://127.0.0.1:5000/one/article/2969",
                "one_index": "VOL.1893",
                "one_title": "母亲，或安娜"
            },
            {
                "one_article_url": "http://127.0.0.1:5000/one/article/2970",
                "one_index": "VOL.1892",
                "one_title": "那你能给我个好评吗？"
            },
            {
                "one_article_url": "http://127.0.0.1:5000/one/article/2964",
                "one_index": "VOL.1891",
                "one_title": "第三者"
            }
        ],
        "one_article_title": "我穷，可是我有想象力啊                                - 李开春",
        "one_article_url": "http://127.0.0.1:5000/one/article/2971"
    },
    "IndexOne": {
        "one_item_list": [
            {
                "date": "16 Dec 2017",
                "one_abstract": "我的眼睛很大很大    装得下高山    装得下大海    装得下蓝天    我的眼睛很小很小    有时遇到心事    就连两行泪    也装不下",
                "one_index": "VOL.1897",
                "one_type": "摄影",
                "one_url": "http://127.0.0.1:5000/one/one/1926"
            },
            {
                "date": "15 Dec 2017",
                "one_abstract": "海在远方怀孕，今夜    黑猫在瓦上诵经    恋月狂和恐月症    苍白的美妇人    大眼睛的脸，贴在窗上        我也忙了一整夜，把月光    掬在掌，注在瓶    分析化学的成份    分析回忆，分析悲伤    恐月症和恋月狂，月光光",
                "one_index": "VOL.1896",
                "one_type": "插画",
                "one_url": "http://127.0.0.1:5000/one/one/1925"
            },
            {
                "date": "14 Dec 2017",
                "one_abstract": "一般人都不是他们想要做的那种人，而是他们不得不做的那种人。",
                "one_index": "VOL.1895",
                "one_type": "摄影",
                "one_url": "http://127.0.0.1:5000/one/one/1924"
            },
            {
                "date": "13 Dec 2017",
                "one_abstract": "人生每个阶段，需要的爱情也不同。两个人会走在一起，是因为需要同类的爱情。激荡、安定、忘我、平淡、执迷、踏实，人生走在同一条时间轴，看天空的颜色、呼吸的频率，都一样，就会在一起。",
                "one_index": "VOL.1894",
                "one_type": "摄影",
                "one_url": "http://127.0.0.1:5000/one/one/1923"
            },
            {
                "date": "12 Dec 2017",
                "one_abstract": "我们以为计划好了一切，可命运只有在这种时候开玩笑，才会让人真正意识到它的存在。",
                "one_index": "VOL.1893",
                "one_type": "插画",
                "one_url": "http://127.0.0.1:5000/one/one/1922"
            },
            {
                "date": "11 Dec 2017",
                "one_abstract": "后来，在无数的“醉时同交欢，醒后各分散”中长大，收敛了太多期待。得到的就是得与到，斩钉截铁的锵锵二字。而能够失去的，是欲言又止、望而却步、再三思量的能够，与命中注定的失去。",
                "one_index": "VOL.1892",
                "one_type": "摄影",
                "one_url": "http://127.0.0.1:5000/one/one/1921"
            },
            {
                "date": "10 Dec 2017",
                "one_abstract": "人若是动了感情，就并不要求一件事情有道理。情人之间就说不上什么道理。",
                "one_index": "VOL.1891",
                "one_type": "插画",
                "one_url": "http://127.0.0.1:5000/one/one/1920"
            }
        ]
    },
    "IndexQuestion": {
        "one_question_index": "VOL.1897",
        "one_question_list": [
            {
                "one_index": "VOL.1896",
                "one_question_url": "http://127.0.0.1:5000/one/question/1947",
                "one_title": "贫穷能激发人的哪些潜能？"
            },
            {
                "one_index": "VOL.1895",
                "one_question_url": "http://127.0.0.1:5000/one/question/1939",
                "one_title": "跟亲密的人产生矛盾，要不要找别人诉苦？"
            },
            {
                "one_index": "VOL.1894",
                "one_question_url": "http://127.0.0.1:5000/one/question/1944",
                "one_title": "让人欲罢不能的奶茶，究竟是怎么来的？"
            },
            {
                "one_index": "VOL.1893",
                "one_question_url": "http://127.0.0.1:5000/one/question/1945",
                "one_title": "为什么中国的老人特别爱给孩子喂饭？"
            },
            {
                "one_index": "VOL.1892",
                "one_question_url": "http://127.0.0.1:5000/one/question/1943",
                "one_title": "街头小广告为什么能存在？"
            },
            {
                "one_index": "VOL.1891",
                "one_question_url": "http://127.0.0.1:5000/one/question/1942",
                "one_title": "那些你点了收藏的东西，后来都怎么样了？"
            }
        ],
        "one_question_title": "佛系恋爱是怎么样的？",
        "one_question_url": "http://127.0.0.1:5000/one/question/1949"
    }
}

```

#### article_info

> http://127.0.0.1:5000/one/article/2975

``` json

{
    "Article": {
        "abstract": "结婚是为了让人变成辽阔的大陆，而不是变成孤岛。",
        "author": "作者/韩松落",
        "content": "****",
        "title": "结婚后，你的朋友是不是变少了？"
    }
}

```

#### one_info

> http://127.0.0.1:5000/one/one/1925

``` json

{
    "One": {
        "abstract": "海在远方怀孕，今夜\n黑猫在瓦上诵经\n恋月狂和恐月症\n苍白的美妇人\n大眼睛的脸，贴在窗上\n\n我也忙了一整夜，把月光\n掬在掌，注在瓶\n分析化学的成份\n分析回忆，分析悲伤\n恐月症和恋月狂，月光光",
        "date": "15 Dec 2017",
        "image": "http://image.wufazhuce.com/FoHVUKQU_N-9ag5Z8tNd_BkzB9uc",
        "index": "VOL.1896",
        "type": "\n\t\t\t\t\t\t插画\n\t\t\t\t\t"
    }
}

```

#### question_info

> http://127.0.0.1:5000/one/question/1947

``` json

{
    "Question": {
        "content": [
            "虽然贫穷限制我们的想象力，但是贫穷可以激发我们的很多潜能啊，因为穷，你都做过哪些事情？",
            "每个人都有兜比脸干净的时候，贫穷使我复古，使我节能……贫穷使我勤奋每用完一次共享单车，我都会不厌其烦地把押金取出来存入余额宝，下次要骑车再充进去。发现评价订单可以拿到返现优惠券后，我爱上了这个锻炼文笔的机会。贫穷锻炼了我的动手能力公司有咖啡机和咖啡豆，买一盒牛奶就可以自制和星爸爸差不多的拿铁了。眼镜腿不小心压断了，我用透明胶粘上又戴了半年。攒钱买了一次贵妇级护肤品，用完之后舍不得扔掉瓶子，买了大宝挤进去。贫穷激发了我的智慧外卖优惠规则是满60减25,120块的单子分两单下，就能优惠50块了！是不是很机智！PS：然而今天发现我们经常拆单点外卖的店取消了满减优惠……白条是个好东西，买100块的东西也不能放过。加班狗在家装网太浪费了，不如在公司下好电影电视剧再回家看。下雨了，我终于可以免费洗车了。我觉得吧，现场听演唱会也看不清明星的脸，在演唱会场馆门口单纯地听听歌也蛮好的。化妆品断货了没钱补，厚着脸皮去丝芙兰逛了一圈，全妆化好了。贫穷鼓励我去社交跟朋友们组建了多个专门发外卖红包的微信群，领取红包之后要自觉汇报还差几个到最大红包。买衣服为了凑满打折，满场子找陌生人拼单。贫穷决定了我的偏好连续一礼拜的晚饭是家里寄的柚子，问我为什么？大概因为我喜欢吃柚子。出门吃饭选餐厅，团购券决定了我今天想吃什么。我是闲置物品交易APP的资深用户。晚上八点之后打折的面包最最好吃了！贫穷也带来了一些小窘迫最近，我感觉我家的猫都瘦了。坐红眼航班到魔都，为了省钱在机场坐了一夜，等第二天的首班地铁回家。脚趾天赋异禀，新的连裤袜第一天就能穿出一个洞，其他部位都很新根本舍不得扔……不要叫我去需要脱鞋的地方玩谢谢……爹妈给我买了一辆小破车，但我基本不用，就停在公司。为啥？因为公司停车不要钱。贫穷会给我们带来很多窘迫和心酸，但同时也给了我们苦中作乐的机会。不是含着金钥匙出生的我们，走向独立的路上都会经历一段捉襟见肘的时期。不妨用乐观轻松的态度看待贫穷，脚踩大地也能仰望星空。"
        ],
        "editor": "\n\t\t\t\t\t\t责任编辑：阿芙拉\t\t\t  \t\t",
        "title": "贫穷能激发人的哪些潜能？"
    }
}

```

### Deploy:

We recommend that you use Caddy(Nginx) + Gunicorn
