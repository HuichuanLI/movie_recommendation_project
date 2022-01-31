# -*- coding:utf-8 -*-
# @Time : 2022/1/31 11:15 下午
# @Author : huichuan LI
# @File : config.py
# @Software: PyCharm
import os

config = {
    'rank_endpoint': os.environ['RANK_ENDPOINT'],
    'recall_endpoint': os.environ['RECALL_ENDPOINT'],
    'dataset_path': os.environ['DATASET_PATH']
}