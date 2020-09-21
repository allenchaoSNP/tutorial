# -*- coding: utf-8 -*-
{
    'name': 'AllenAddons'
    , 'version': '1.0.0'
    , 'category': 'Extra Tools'#分類
    , 'author': "Allen"#作者
    , 'license': 'LGPL-3'
    , 'depends': ['base'] #依賴模塊
    , 'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/view.xml',
        'views/menu.xml',
        'controllers/controllers.py',
        ],
    #, 'images': ['static/description/connect_mssql.png'], #應該是單純的圖式
    'installable': True, #可安裝
    'auto_install': False, #自動安裝
    'application': True, #是否為應用
}