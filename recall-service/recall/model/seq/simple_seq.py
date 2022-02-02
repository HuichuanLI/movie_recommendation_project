# -*- coding:utf-8 -*-
# @Time : 2022/2/2 3:33 下午
# @Author : huichuan LI
# @File : simple_seq.py
# @Software: PyCharm
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col, collect_list, udf


def build_seq(rating_df: DataFrame, spark):
    return rating_df \
        .groupBy('user_id') \
        .agg( \
            collect_list(col('anime_id').cast('string')).alias('anime_ids') \
        )
