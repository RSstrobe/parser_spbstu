from lib.parsing import parsing

filename = 'data/input_data/test_schedule.inc'

if __name__ == '__main__':
    output_dataframe = parsing(filename)
    output_dataframe.to_excel('data/output_data/output.xlsx')
