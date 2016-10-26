import sys
import os.path
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from sandcage import SandCage


class SandCageTestWithApiKey(unittest.TestCase):

    def setUp(self):
        # Save the API_KEY to your home directory into file named
        # SANDCAGE_API_KEY
        api_key_dir = os.path.expanduser("~")
        api_key_file = os.path.join(api_key_dir, 'SANDCAGE_API_KEY')
        with open(api_key_file, 'r') as f:
            api_key = f.readline()
        
        self.sc = SandCage(api_key)
        
    def test_list_files(self):
        payload = {}
        result = self.sc.list_files_service(payload)
        
        self.assertEqual(result.status_code, 200)

        # The following keys are not expected in the response json
        not_expected = ('error_msg')
        for key in result.json():
            self.assertFalse(key in not_expected)

        # The following keys are expected in the response json
        expected = ('status', 'request_id', 'pages', 'files')
        for key in result.json():
            self.assertTrue(key in expected)

    def test_list_files_with_page(self):
        payload = {'page': 2}
        result = self.sc.list_files_service(payload)
        
        self.assertEqual(result.status_code, 200)

        # The following keys are not expected in the response json
        not_expected = ('error_msg')
        for key in result.json():
            self.assertFalse(key in not_expected)

        # The following keys are expected in the response json
        expected = ('status', 'request_id', 'pages', 'files')
        for key in result.json():
            self.assertTrue(key in expected)

        
    def test_list_files_with_page_and_results_per_page(self):
        payload = {'page': 1,
                   'results_per_page': 10}

        result = self.sc.list_files_service(payload)
        
        self.assertEqual(result.status_code, 200)

        # The following keys are not expected in the response json
        not_expected = ('error_msg')
        for key in result.json():
            self.assertFalse(key in not_expected)

        # The following keys are expected in the response json
        expected = ('status', 'request_id', 'pages', 'files')
        for key in result.json():
            self.assertTrue(key in expected)
        
if __name__ == '__main__':
    unittest.main()
