from django.urls import path,re_path

from . import views

from api_shop import ApiShop,Api


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

app_name='api'

urlpatterns = [
    path('api_data', af.get_api_data, name='api_data'),
    path('document/', af.render_documents, name='document'),
    re_path(r'([\s\S]*)', af.api_entry, name='index')
]

