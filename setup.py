# -*- coding:utf-8 -*-
from setuptools import setup, find_packages


packages = find_packages('Myblog')
print(packages)

setup(
    name='Myblog',
    version='0.1',
    description='Blog System base on Django',
    author='treehl',
    author_email='treehl93@gmail.com',
    packages=find_packages('Myblog'),
    package_dir={'': 'Myblog'}, # 从根目录Myblog寻找
    # package_data={'': [
    #     'themes/default/static/js/*.js',# 方法一、从路径中寻找要打包的js
    #     'themes/default/template/*/*.html',
    # ]},
    # 方法二、增加MANIFEST.in
    include_package_data=True,
    install_requires=[
        'django==1.11.3',
    ],
    scripts=[
        'Myblog/manage.py',
    ],

)