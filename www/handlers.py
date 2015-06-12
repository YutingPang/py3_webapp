#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__='Yuting Pang'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from coreweb import get, post

from models import User, Comment, Blog, next_id

@get('/')
def index(request):
    summary = 'fasdjflsajf df jdsaf dsajf lidus fnsaldf ids fnsda hfhrewu hasdoif hsaf hhea sdfh.'
    blogs = [
        Blog(id='1', name='test blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='HAHAHAHAH', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='LOLOLOLOLO', summary=summary, created_at=time.time()-7255)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }
