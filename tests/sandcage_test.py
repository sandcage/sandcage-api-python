import sys
import os.path
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from sandcage import SandCage


class SandCageTest(unittest.TestCase):

    def setUp(self):
        # This test is run without API_KEY
        self.sc = SandCage()
        
    def test_list_files(self):
        payload = {}
        result = self.sc.list_files_service(payload)
        
        self.assertEqual(result.status_code, 200)

        # The following keys are expected in the response json
        expected = ('status', 'request_id', 'error_msg')
        for key in result.json():
            self.assertTrue(key in expected)

    def test_list_files_with_page(self):
        payload = {'page': 2}
        result = self.sc.list_files_service(payload)
        
        self.assertEqual(result.status_code, 200)
    
        # The following keys are expected in the response json
        expected = ('status', 'request_id', 'error_msg')
        for key in result.json():
            self.assertTrue(key in expected)
	
        
    def test_list_files_with_page_and_results_per_page(self):
        payload = {'page': 1,
                   'results_per_page': 10}
        
        result = self.sc.list_files_service(payload)
        
        self.assertEqual(result.status_code, 200)
    
        # The following keys are expected in the response json
        expected = ('status', 'request_id', 'error_msg')
        for key in result.json():
            self.assertTrue(key in expected)
		

    def test_get_info_with_request_id(self):
        payload = {'request_id': '[request_id]'}
        
        result = self.sc.get_info_service(payload)
        
        self.assertEqual(result.status_code, 200)
    
        # The following keys are expected in the response json
        expected = ('status', 'request_id', 'error_msg')
        for key in result.json():
            self.assertTrue(key in expected)
		

    def test_get_info_with_file_tokens(self):
        payload = {'files': [{'file_token': '[file_token 1]'},
                             {'file_token': '[file_token 2]'},
                             {'file_token': '[file_token 3]'}]}
        
        result = self.sc.get_info_service(payload)
        
        self.assertEqual(result.status_code, 200)
        
        # The following keys are expected in the response json
        expected = ('status', 'request_id', 'error_msg')
        for key in result.json():
            self.assertTrue(key in expected)
            

    def test_schedule_files(self):
        payload = {'jobs': [
            {'url': 'http://cdn.sandcage.com/p/a/img/logo.jpg',
             'tasks': [
                 {'actions': 'save'},
                 {'actions': 'resize',
                  'filename': 'hello_world.jpg',
                  'width': 200},
                 {'actions': 'crop',
                  'coords': '10,10,50,50'},
                 {'reference_id': '1234567890',
                  'actions': 'rotate',
                  'degrees': 90},
                 {'actions': 'cover',
                  'width': 60,
                  'height': 60,
                  'cover': 'middle,center'}]},
            {'url': 'http://cdn.sandcage.com/p/a/img/header_404.png',
             'tasks': [{'actions': 'resize',
                        'height': 30}]}]}

        result = self.sc.schedule_files_service(payload)
        
        self.assertEqual(result.status_code, 200)
        
        # The following keys are expected in the response json
        expected = ('status', 'request_id', 'error_msg')
        for key in result.json():
            self.assertTrue(key in expected)
            

    def test_destroy_files(self):
        payload = {'files': [{'reference_id': '[reference_id]',
                             'file_token': '[file_token]'}]}
        
        result = self.sc.destroy_files_service(payload)
        
        self.assertEqual(result.status_code, 200)
        
        # The following keys are expected in the response json
        expected = ('status', 'request_id', 'error_msg')
        for key in result.json():
            self.assertTrue(key in expected)

        
if __name__ == '__main__':
    unittest.main()
