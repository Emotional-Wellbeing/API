import json

import unittest


class TestProcess(unittest.TestCase):
    def test_process_user_data(self):
        with open('../json/user_data_full_data.json') as json_file:
            data = json.load(json_file)
        self.assertTrue()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
