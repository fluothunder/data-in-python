import psda.io_data.input
from pandas._testing import assert_frame_equal
from variables_for_test_input import *
import os


def test_excel_to_df_school():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    df1 = psda.io_data.input.excel_to_df_school(dir_path+"/data/input_schools.xlsx")
    assert_frame_equal(df1, expected_df1)


def test_excel_to_df_population():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    df2 = psda.io_data.input.excel_to_df_population(dir_path+"/data/input_population.xls")
    assert_frame_equal(df2, expected_df2)
