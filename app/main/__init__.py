# -*- coding:UTF-8 -*-

from flask import Blueprint
import os
# 蓝本
main = Blueprint('main', __name__)
filename = os.path.dirname(os.path.realpath(__file__))+'/a23.xls'
from. import views


