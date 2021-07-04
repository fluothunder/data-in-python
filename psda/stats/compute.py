import pandas as pd
import numpy as np
from typing import List


def stat_students_per_teacher(df_schools: pd.DataFrame, columns: List) -> pd.DataFrame:
    """
    :param df_schools: input dataframe
    :param columns: columns of df_schools which should be used to .groupby
    :return: dataframe with statistics
    """
    df_stat = df_schools.groupby(columns).agg(
        min_ratio=("ratio_students_per_teacher", min),
        max_ratio=("ratio_students_per_teacher", max),
        avg_ratio=("ratio_students_per_teacher", np.mean)
    )
    return df_stat


def stat_students_per_school(df_schools: pd.DataFrame, columns: List) -> pd. DataFrame:
    """
    :param df_schools: input dataframe
    :param columns: columns of df_schools which should be used to .groupby
    :return: dataframe with statistics
    """
    df = df_schools.groupby(columns)[list(range(1999, 2016))]
    df_min = df.min()
    df_max = df.max()
    df_avg = df.mean()
    return pd.concat({"min": df_min, "max": df_max, "avg": df_avg}).T
