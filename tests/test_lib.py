import pytest

from lib.data_cleaning import data_cleaning
from lib.prepare_list_for_dataframe import prepare_list_for_dataframe


@pytest.mark.parametrize('filename', [('input_data_test/test_schedule.inc')])
def test_data_cleaning(filename):
    """
    Проверить правильность работы функции data_cleaning()
    :param filename:
    :return:
    """
    with open(filename, encoding='UTF-8') as f:
        lines_from_document = f.read().splitlines()

    list_after_clean = [['COMPDAT',
                         'W1 10 10 1 3 OPEN DEFAULT 1 2 1 DEFAULT DEFAULT DEFAULT 1.0',
                         'W2 32 10 1 3 OPEN DEFAULT 1 2 1 DEFAULT DEFAULT DEFAULT 2.0',
                         'COMPDAT',
                         'W3 5 36 2 2 OPEN DEFAULT 1 2 1 DEFAULT DEFAULT DEFAULT 3.0',
                         'W4 40 30 1 3 OPEN DEFAULT 1 2 1 DEFAULT DEFAULT DEFAULT 4.0',
                         'COMPDAT',
                         'W5 21 21 4 4 OPEN DEFAULT 1 2 1 DEFAULT DEFAULT DEFAULT 5.0'],
                        ['DATES', '01 JUN 2018'],
                        ['DATES',
                         '01 JUL 2018',
                         'COMPDAT',
                         'W3 32 10 1 1 OPEN DEFAULT 1 2 1 DEFAULT DEFAULT DEFAULT 1.0718',
                         'W5 21 21 1 3 OPEN DEFAULT 1 2 1 DEFAULT DEFAULT DEFAULT 5.0'],
                        ['DATES', '01 AUG 2018'],
                        ['DATES',
                         '01 SEP 2018',
                         'COMPDAT',
                         'W1 10 10 2 3 OPEN DEFAULT 1 2 1 DEFAULT DEFAULT DEFAULT 1.0918',
                         'W2 32 10 1 2 OPEN DEFAULT 1 2 1 DEFAULT DEFAULT DEFAULT 2.0',
                         'COMPDATL',
                         'W3 LGR1 10 10 2 2 OPEN DEFAULT 1 2 1 DEFAULT DEFAULT DEFAULT 1.0918'],
                        ['DATES', '01 OCT 2018'],
                        ['DATES', '01 NOV 2018'],
                        ['DATES', '01 DEC 2018']]

    assert data_cleaning(lines_from_document) == list_after_clean


@pytest.mark.parametrize('filename', [('input_data_test/test_schedule.inc')])
def test_prepare_list_for_dataframe(filename):
    """
    Проверить правильность работы функции prepare_list_for_dataframe()
    :param filename:
    :return:
    """
    with open(filename, encoding='UTF-8') as f:
        lines_from_document = f.read().splitlines()
    clean_list = data_cleaning(lines_from_document)
    list_for_df = prepare_list_for_dataframe(clean_list)
    assert type(list_for_df) == list
