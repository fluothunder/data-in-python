from pandas._testing import assert_frame_equal
import psda.process.process_data
from variables_for_test_process_data import *


def test_create_dict_of_districts():
    new_dict = psda.process.process_data.create_dict_of_districts(df1)
    # compare to expected_dict1:
    assert new_dict.keys() == expected_dict1.keys()
    keys_of_dicts = new_dict.keys()
    for ky in keys_of_dicts:
        assert_frame_equal(new_dict[ky], expected_dict1[ky])


def test_compute_ratio():
    assert_frame_equal(psda.process.process_data.compute_ratio(df2), expected_df2)
