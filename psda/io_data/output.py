import pandas as pd
import os
from math import ceil


def output_csv(df: pd.DataFrame, file_name: str):
    """
    exports dataframe to .csv file. creates directory './results' if necessary

    :param df: dataframe to be exported
    :param file_name: name of the .csv file (adding format extension is unnecessary)
    :return:
    """
    cwd = os.getcwd()
    if not os.path.exists(cwd+"/results"):
        os.makedirs(cwd+"/results")
    df.to_csv(path_or_buf=cwd+"/results/"+file_name+".csv")


def output_report(df_schools, df_schools_processed: pd.DataFrame, file_name: str):
    """
    creates a report .txt from data analysis

    :param df_schools: unprocessed dataframe
    :param df_schools_processed: processed dataframe
    :param file_name: name of the .txt file (adding format extension is unnecessary)
    """
    students_total = df_schools.students.sum()
    students_dropped = students_total - df_schools_processed.students.sum()
    perc = ceil((students_dropped / students_total)*10000) / 100
    cwd = os.getcwd()
    if not os.path.exists(cwd + "/results"):
        os.makedirs(cwd + "/results")
    with open(cwd+"/results/"+file_name+".txt", "w") as f_p:
        f_p.write(f"There is lost not more than {perc}% information about students.\n\n")
        f_p.write(f"There are a total of {students_total} students in statistics before processing them.\n")
        f_p.write(f"During processing data {students_dropped} of them have to be dropped due to "
                  f"incomplete or imperfect information about their schools. There were also chosen only "
                  f"most important types of schools in Poland.")
