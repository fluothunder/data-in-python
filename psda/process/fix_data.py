import pandas as pd


# 1. Deleting rows with NaN's
def del_nan(df: pd.DataFrame) -> pd.DataFrame:
    """
    deleting rows with NaN's

    :param df: dataframe
    :return: dataframe df without rows with NaN's
    """
    mask = df.isnull().any(axis=1)
    return df[~mask]


# 2. Deleting schools from non-existing districts in 2020
def del_schools_from_non_existing_districts(df_schools: pd.DataFrame, dict_of_districts: dict) -> pd.DataFrame:
    """
    deleting schools from non-existing districts in 2020

    :param df_schools: dataframe with schools in 2018
    :param dict_of_districts: dictionary that keys are id's of districts in Poland in 2020
    :return: refined df_schools
    """
    keys = dict_of_districts.keys()
    mask = df_schools[["voivo", "county", "district"]].apply(lambda x: (x.voivo, x.county, x.district) in keys, axis=1)
    return df_schools[mask]


# 3. Dealing with ZS's
def del_zs(df_schools: pd.DataFrame) -> pd.DataFrame:
    """
    dealing with ZS's (pol. 'Zespół szkół i placówek oświatowych')

    :param df_schools: dataframe with some ZS's which should be processed
    :return: refined df_schools
    """
    list_of_groups = []
    for _, g in df_schools.groupby(["rspo"]):
        if "Zespół szkół i placówek oświatowych" in set(g.school_type):
            teachers_total = list(g.loc[g.school_type == "Zespół szkół i placówek oświatowych"].teachers)[0]
            df_ = g[g.school_type != "Zespół szkół i placówek oświatowych"].copy()
            sections_total = df_.sections.sum()
            if sections_total != 0:
                df_.teachers = df_.sections.apply(lambda x: (teachers_total * x) // sections_total)
            list_of_groups.append(df_)
        else:
            list_of_groups.append(g)
    return pd.concat(list_of_groups, ignore_index=True)


# 4. Deleting rows with 0 teachers or 0 students
def del_zero(df_schools: pd.DataFrame) -> pd.DataFrame:
    """
    deleting rows with 0 teachers or 0 students

    :param df_schools: dataframe
    :return: refined df_schools
    """
    mask = (df_schools.teachers != 0) & (df_schools.students != 0)
    return df_schools[mask]


# 5. Filtering key types of schools
# ==== (don't run it before applying del_zs function do DataFrame with schools!) ====
def filter_key_types_of_schools(df: pd.DataFrame) -> pd.DataFrame:
    """
    filtering key types of schools: 'Szkoła podstawowa', 'Przedszkole', 'Liceum ogólnokształcące' and 'Gimnazjum'

    :param df: dataframe with many types of schools
    :return: dataframe with key types of schools only
    """
    types_born = {"Szkoła podstawowa": {2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011},
                  "Przedszkole": {2012, 2013, 2014, 2015},
                  "Liceum ogólnokształcące": {2000, 2001, 2002},
                  "Technikum": {1999, 2000, 2001, 2002},
                  "Gimnazjum": {2003}}
    types_of_schools = types_born.keys()
    mask = df.school_type.isin(types_of_schools)
    return df[mask]


# All together
def fix_school(df_schools: pd.DataFrame, dict_of_districts: dict) -> pd.DataFrame:
    """
    function to fix dataframe with schools; it consists of some component functions

    :param df_schools: dataframe with schools which should be fixed
    :param dict_of_districts: dictionary with data about districts in Poland in 2020
    :return: refined dataframe
    """
    return filter_key_types_of_schools(
        del_zero(
            del_zs(
                del_schools_from_non_existing_districts(
                    del_nan(df_schools), dict_of_districts))))
