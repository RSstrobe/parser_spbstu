import pytest
from lib.parsing import parsing


class TestUnitParser:
    @pytest.fixture
    def set_up(self):
        """
        Prepares info for reference input file(s)
        @return: None
        """
        self.input_file = 'input_data_test/test_schedule.inc'  # Входные данные для парсинга

        self.parse_list_output_reference = [
            [None, 'W1', None, '10', '10', '1', '3', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '1.0'],
            [None, 'W2', None, '32', '10', '1', '3', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '2.0'],
            [None, 'W3', None, '5', '36', '2', '2', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '3.0'],
            [None, 'W4', None, '40', '30', '1', '3', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '4.0'],
            [None, 'W5', None, '21', '21', '4', '4', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '5.0'],
            ['01 JUN 2018', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            ['01 JUL 2018', 'W3', None, '32', '10', '1', '1', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '1.0718'],
            ['01 JUL 2018', 'W5', None, '21', '21', '1', '3', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '5.0'],
            ['01 AUG 2018', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            ['01 SEP 2018', 'W1', None, '10', '10', '2', '3', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '1.0918'],
            ['01 SEP 2018', 'W2', None, '32', '10', '1', '2', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '2.0'],
            ['01 SEP 2018', 'W3', 'LGR1', '10', '10', '2', '2', 'OPEN', 'DEFAULT', '1', '2', '1', 'DEFAULT', 'DEFAULT',
             'DEFAULT', '1.0918'],
            ['01 OCT 2018', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            ['01 NOV 2018', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            ['01 DEC 2018', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]

    def test_parse_schedule(self, set_up):
        """
        Check the correctness of the parser output
        :param set_up:
        :return:
        """
        assert parsing(self.input_file).values.tolist() == self.parse_list_output_reference