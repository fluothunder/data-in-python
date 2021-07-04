import psda.io_data.output
import os
import filecmp
from variables_for_test_output import *


def test_output_csv():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    psda.io_data.output.output_csv(df1, "output_test")
    assert os.path.exists("./results/output_test.csv")
    assert filecmp.cmp(dir_path+"/data/expected_output_csv.csv", "./results/output_test.csv")
    cwd = os.getcwd()
    os.remove(cwd+"/results/output_test.csv")
