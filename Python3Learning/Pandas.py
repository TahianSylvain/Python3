import matplotlib.pyplot as pyplot
import numpy as numpy
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]


def csv(input_file, output_file):
    """
        sample_input.csv sample_output.csv
    """
    data_frame = pd.read_csv(input_file)
    data_frame.to_csv(output_file, index=False)
    return None


def excel(input_file, output_file):
    """
        sample_input.xlsx sample_output.xls
    """
    data_frame=pd.read_excel(input_file, sheet_name="OnJANUARY", index_col=None)
    writer=pd.ExcelWriter(output_file)
    #result_data = conditionning(data_frame)
    result_data.to_ecxel(writer, sheet_nam="OnFEBRUARY", index=False)
    writer.save()
    return None