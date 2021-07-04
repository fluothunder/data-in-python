import pandas as pd
import numpy as np


def create_dict_of_districts(df_population: pd.DataFrame) -> dict:
    """
    creates dictionary of DataFrames consisting information how many students born in each year 1999-2015
    from each district go to schools of the same type

    :param df_population: dataframe with information about population in 2020 for each district in Poland
    :return: dictionary with district id's as keys and dataframes as values
    """
    types_born = {"Szkoła podstawowa": {2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011},
                  "Przedszkole": {2012, 2013, 2014, 2015},
                  "Liceum ogólnokształcące": {2000, 2001, 2002},
                  "Technikum": {1999, 2000, 2001, 2002},
                  "Gimnazjum": {2003}}
    dict_of_districts = {}
    for distr, g in df_population.groupby(["voivo", "county", "district"]):
        for tp in types_born:
            years = types_born[tp]
            mask = g.born.isin(years)
            g_valid = g[mask]
            total = g_valid.qty.sum()
            g.loc[mask, tp] = g_valid.qty / total
        dict_of_districts[distr] = g.set_index("born")
    return dict_of_districts


def compute_ratio(df_schools: pd.DataFrame) -> pd.DataFrame:
    """
    computes ratio students per teacher

    :param df_schools: dataframe with schools in Poland in 2018
    :return: df_schools with column 'ratio_students_per_teacher' adjoined
    """
    df_schools["ratio_students_per_teacher"] = df_schools[["students", "teachers"]].apply(
        lambda x: x.students / x.teachers, axis=1)
    return df_schools


def compute_students_per_school(df_schools: pd.DataFrame, dict_of_districts: dict) -> pd.DataFrame:
    """
    estimates number of students per school broken down by their year of birth

    :param df_schools: dataframe with schools in Poland in 2018
    :param dict_of_districts: dictionary with district id's as keys and dataframes as values
    :return: dataframe with estimated number of students per school broken by their year of birth
    """
    df_schools[list(range(1999, 2016))] = df_schools[["voivo", "county", "district", "students", "school_type"]].apply(
        lambda x: np.ceil(x.students * dict_of_districts[(x.voivo, x.county, x.district)].loc[:, x.school_type]),
        axis=1)
    return df_schools


# All together
def process_school(df_schools: pd.DataFrame, dict_of_districts: dict):
    """
    function to process dataframe with schools; it consists of some component functions

    :param df_schools: dataframe with schools in Poland in 2018
    :param dict_of_districts: dictionary with district id's as keys and dataframes as values
    :return: dataframe with estimated number of students per school broken by their year of birth
    """
    return compute_students_per_school(compute_ratio(df_schools), dict_of_districts)
