import pandas as pd


def read_file():
    data_frame = pd.read_excel("excel/student_booking.xlsx")
    return data_frame
