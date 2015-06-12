#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations
'''

__author__ = 'Yuting Pang'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'py3_webapp',
        'password': 'py3_webapp',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}
