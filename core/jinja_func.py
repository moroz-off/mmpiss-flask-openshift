# -*- coding: utf-8 -*-
from settings import SETTINGS


def create_url(**kwargs):
    return '{url}/{name}'.format(**kwargs)


def static_js(name):
    return create_url(url=SETTINGS['static_js_url'], name=name)


def static_css(name):
    return create_url(url=SETTINGS['static_css_url'], name=name)
