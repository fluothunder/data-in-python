from pandas._testing import assert_frame_equal
import psda.process.fix_data
from variables_for_test_fix_data import *


def test_del_nan():
    assert_frame_equal(psda.process.fix_data.del_nan(df1), expected_df1)


def test_del_schools_from_non_existing_districts():
    assert_frame_equal(psda.process.fix_data.del_schools_from_non_existing_districts(df2, dict2), expected_df2)


def test_del_zs():
    assert_frame_equal(psda.process.fix_data.del_zs(df3), expected_df3)


def test_del_zero():
    assert_frame_equal(psda.process.fix_data.del_zero(df4), expected_df4)


def test_filter_key_types_of_schools():
    assert_frame_equal(psda.process.fix_data.filter_key_types_of_schools(df5), expected_df5)


def test_fix_school():
    assert_frame_equal(psda.process.fix_data.fix_school(df6, dict6), expected_df6)
