# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *

#admin account details
#username: admin
#email: speckleAdmin@speckle.com
#password: djangotest

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
