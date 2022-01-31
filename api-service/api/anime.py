# -*- coding:utf-8 -*-
# @Time : 2022/1/31 11:15 下午
# @Author : huichuan LI
# @File : anime.py
# @Software: PyCharm
import csv
import os.path
from api.config import config


anime_file = open(os.path.join(config['dataset_path'], 'merged_anime.csv'))
reader = csv.DictReader(anime_file)
animes = { row['anime_id']: row for row in reader }


def get_anime(id):
    id = str(id)
    if id not in animes:
        return None

    return animes[id]