# -*- coding:UTF-8 -*-

from flask import jsonify
from flask_cors import CORS
from . import main, filename
from load_data import Algorithm


# 跨域插件
CORS(main,resource=r'/*')


@main.route('/', methods=['GET', 'POST'])
def get_result():
    net_pre = Algorithm(filename)
    y_real = net_pre.y_real.tolist()
    y_pre = net_pre.y_pre.tolist()
    return jsonify({'y_pre':y_pre,'y_real':y_real})









