import pandas as pd


def excel_to_df_school(path: str) -> pd.DataFrame:
    """
    loads and convert data about schools from excel to pandas DataFrame

    :param path: path to data with schools
    :return: dataframe with information about schools
    """
    df = pd.read_excel(path,
                       skiprows=(1,),
                       usecols=(
                            "woj",
                            "pow",
                            "gm",
                            "Typ gminy",
                            "Nazwa typu",
                            "Uczniowie, wychow., słuchacze",
                            "Oddziały",
                            "Nauczyciele pełnozatrudnieni",
                            "Nauczyciele niepełnozatrudnieni (stos.pracy)",
                            "Nr RSPO jednostki sprawozdawczej")
                       )
    df = df.rename(columns={
                            "woj": "voivo",
                            "pow": "county",
                            "gm": "district",
                            "Typ gminy": "district_type",
                            "Nazwa typu": "school_type",
                            "Uczniowie, wychow., słuchacze": "students",
                            "Oddziały": "sections",
                            "Nauczyciele pełnozatrudnieni": "full_time_teachers",
                            "Nauczyciele niepełnozatrudnieni (stos.pracy)": "not_full_time_teachers",
                            "Nr RSPO jednostki sprawozdawczej": "rspo"})
    df["teachers"] = df.full_time_teachers + df.not_full_time_teachers
    df = df.drop(["full_time_teachers", "not_full_time_teachers"], axis=1)
    return df


# some auxiliary functions used in excel_to_df_population
def get_voivo(x: float) -> int:
    y = str(int(x))
    if len(y) == 7:
        return int(y[0] + y[1])
    else:
        return int(y[0])


def get_county(x: float) -> int:
    y = str(int(x))
    if len(y) == 7:
        return int(y[2] + y[3])
    else:
        return int(y[1] + y[2])


def get_district(x: float) -> int:
    y = str(int(x))
    if len(y) == 7:
        return int(y[4] + y[5])
    else:
        return int(y[3] + y[4])


def excel_to_df_population(path: str) -> pd.DataFrame:
    """
    loads and convert data about population from excel to pandas DataFrame

    :param path: path to data with population info
    :return: dataframe with information about population
    """
    df = pd.concat(pd.read_excel(path,
                                 skiprows=(0, 1, 2, 3, 4, 5, 6),
                                 usecols=[0, 1, 2],
                                 sheet_name=None))
    df.columns = ["age", "district_id", "qty"]
    df = df.apply(pd.to_numeric, errors="coerce")
    df = df[(~df.age.isnull()) | (~df.district_id.isnull())]
    df = df.fillna(method='ffill')[~df.age.isnull()]
    df = df.reset_index(drop=True)
    df["born"] = 2020 - df.age
    df = df[df.born.isin(range(1999, 2016))]
    df["voivo"] = df["district_id"].apply(get_voivo)
    df["county"] = df["district_id"].apply(get_county)
    df["district"] = df["district_id"].apply(get_district)
    df = df.drop(["district_id", "age"], axis=1)
    return df
