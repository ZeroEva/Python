#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import re

src_1 = '<img src="https://i.pinimg.com/originals/2f/a3/99/2fa399fdeead87343f570d0bb467cc4f.jpaeg" />'

search = re.search(r'(jp[e]?g)|(png)', src_1)
print(search)
print(not None)

