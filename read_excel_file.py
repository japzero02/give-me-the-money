import pandas as pd


def save_file():
    data_frame = pd.read_excel("excel/student_booking.xlsx")
    writer = pd.ExcelWriter('student_booking.xlsx')
    data_frame.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
