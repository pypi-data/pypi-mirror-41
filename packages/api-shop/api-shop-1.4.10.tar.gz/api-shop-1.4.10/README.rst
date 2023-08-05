api-shop api商店
================

什么是api-shop：提供易用的、轻量化的restful-api接口工具包，基于django或者flask框架。
------------------------------------------------------------------------------------

核心功能：
----------

1、配置化api生成。
~~~~~~~~~~~~~~~~~~

2、根据配置自动校验request提交的数据，并转换成制定格式。
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

3、根据配置自动生成api文档，并提供一个web页面可供查询和mock数据演示，方便和前端开发人员沟通。
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

4、兼容django 和 flask
~~~~~~~~~~~~~~~~~~~~~~

5、更多兼容格式转换：list、set、dict、tuple均可以自动转换。还有data\_format.datetime的格式转换类，可以将'2019-01-18 23:25:25'这样的字符串日期转换成日期格式。你当然也可以很方便的制作一个格式转换器
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

自定义格式转换器
^^^^^^^^^^^^^^^^

.. code:: python

    # 使用自定义格式转换器的时候，min和max也会自动加载这个转换器转换了进行比较
    from datetime import datetime as dt

    class datetime():
        '''将str转换成datetime格式'''

        def __new__(self, string):
            if ':' in string:
                return dt.strptime(string, '%Y-%m-%d %H:%M:%S')
            else:
                return dt.strptime(string, '%Y-%m-%d')

demo 图片
=========

.. figure:: /static/demo.png
   :alt: demo

   demo
使用方法：
----------

安装：
~~~~~~

.. code:: sh

    sudo pip install api-shop

引入：
~~~~~~

.. code:: python

    from api_shop from ApiShop,Api
    # ApiShop 是构造类
    # Api是接口类
    # ap = ApiShop(conf, options)
    # options = {
    #    # 基础url，用以组合给前端的api url
    #   'base_url':'/api/',
    #    # 参数bad_request如果是真，发生错误返回一个坏请求给前端，否则都返回200的response，里面附带status=error和msg附带错误信息
    #   'bad_request': True,  
    #    # 文档路由渲染的模板，也可以不用写到这里，你自己随便找个喜欢的路由绑定一个页面，ajax拿ApiShop实例化后的get_api_data方法
    #   'document': BASE_DIR + '/api_shop/static/document.html'  
    # }

`Django例子 <https://github.com/pcloth/api-shop/tree/master/django_demo>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    ## urls.py
    from api_shop import ApiShop

    ## 接口配置数据
    conf = [
        {
            'url': 'login',
            'class': 'account.views.api_login', #需要引入的api类，继承于上面说的Api接口类
            'name': '账户登录',
            'methods': {
                'POST': [
                    {'name':'username', 'type': str, 'required': True, 'min': 3, 'max': 24, 'description': '用户名'},
                    {'name':'password', 'type': str, 'required': True, 'min': 3, 'max': 24, 'description': '密码'},
                ]
                ## 这里可以插入更多的methods，比如GET,DELETE,POST,PATCH
            }
        },
        ## 这里可以插入更多的api接口

    ]

    ## api-shop参数设置：

    options = {
                'base_url':'/api/',# 基础url，用以组合给前端的api url 可默认
                # 'document':BASE_DIR+'/api_shop/static/document.html', # 文档路由渲染的模板 可默认
                'bad_request':True, # 参数bad_request如果是真，发生错误返回一个坏请求给前端，否则都返回200的response，里面附带status=error和msg附带错误信息 可默认
            }


    ap = ApiShop(conf,options)

    app_name='api'

    urlpatterns = [
        path('api_data', ap.get_api_data, name='api_data'), # api文档需要的接口
        path('document/', ap.render_documents, name='document'), #api文档渲染的路由
        re_path(r'([\s\S]*)', ap.api_entry, name='index') # 接管api/下面其他的全部路由到api_entry入口方法
    ]

.. code:: python

    ## account/views.py
    from api_shop from Api

    class api_login(Api):
        def post(self,request,data=None):
            '''api登陆接口，方便微信用户绑定账户'''
            username = data.username
            password = data.password
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                token = TokenBackend.make_token(user).decode('utf-8')
                return JsonResponse({'status': 'success', 'msg': '执行成功', 'token': token})
            
            return JsonResponse({'status': 'error', 'msg': '用户登录失败'})

`flask例子 <https://github.com/pcloth/api-shop/tree/master/flask_demo>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    from flask import Flask,request,render_template_string

    from werkzeug.routing import BaseConverter

    from api_shop import ApiShop,Api

    class RegexConverter(BaseConverter):
        def __init__(self, map, *args):
            self.map = map
            self.regex = args[0]

    app = Flask(__name__)
    # 如果使用蓝图，添加正则处理器必须是在注册蓝图之前使用。
    app.url_map.converters['regex'] = RegexConverter

    conf = [
        {
            'url': 'login',
            'class': 'api.views.api_login',
            'name': '账户登录',
            'methods': {
                'POST': [
                    {'name':'username', 'type': str, 'required': True, 'min': 3, 'max': 24, 'description': '用户名'},
                    {'name':'password', 'type': str, 'required': True, 'min': 3, 'max': 24, 'description': '密码'},
                ]
            }
        },
        {
            'url': 'test',
            'class': 'api.views.test',
            'name': '测试数据',
            'methods': {
                'GET':[{'name':'bb', 'type': int, 'required': True, 'min': 0, 'max': 100, 'description': '百分比','default':95},],
                'POST': [
                    {'name':'add', 'type': str, 'required': True, 'min': 3, 'max': 24, 'description': '地址'},
                    {'name':'bb', 'type': int, 'required': True, 'min': 0, 'max': 100, 'description': '百分比','default':95},
                    {'name':'list', 'type': list, 'description': '列表'},
                ],
                'DELETE':[
                    {'name':'id', 'type': int, 'required': True, 'min': 1,'description': '编号'},
                ]
            }
        },

    ]


    af = ApiShop(conf)



    @app.route('/api/<regex("([\s\S]*)"):url>',methods=['GET', 'POST','PUT','DELETE','PATCH'])
    def hello_world(url):
        print(url)
        if url=='document/':
            return af.render_documents(request,url)
        if url=='api_data':
            return af.get_api_data(request,url)

        return af.api_entry(request,url)

    if __name__ == '__main__':
        app.run(host="0.0.0.0",debug=True)
