# -*- coding: utf-8 -*-
import sys
import os.path

# Save the API_KEY to your home directory as a file named
# SANDCAGE_API_KEY
api_key_dir = os.path.expanduser('~')
api_key_file = os.path.join(api_key_dir, 'SANDCAGE_API_KEY')
with open(api_key_file, 'r') as f:
    api_key = f.readline()
    

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))
from sandcage import SandCage

sc = SandCage(api_key=api_key)
result = sc.schedule_files_service(
    {'jobs': [
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
         'tasks': [
             {'actions': 'resize',
              'height': 30}]}]})

if result.status_code != 200:
    print('Http error occured with status code {}.'.format(result.status_code))
else:
    result_dict = result.json()
    print('Status: {}'.format(result_dict['status']))
    print('Request id: {}'.format(result_dict['request_id']))
    # Success or warning
    if result_dict['status'] == 'success' or result_dict['status'] == 'warning':
        # In case of warning, print out the warning messages
        if result_dict['status'] == 'warning':
            for msg in result_dict['warning_msg']:
                for (key, value) in msg.items():
                    print('{}: {}'.format(key, value))
                print('')
            
        # Print out the tasks
        for task in result_dict['tasks']:
            for (key, value) in task.items():
                print('{}: {}'.format(key, value))
            print('')
    # In case of an error, print out the messages messages
    elif result_dict['status'] == 'error':
        for msg in result_dict['error_msg']:
            for (key, value) in msg.items():
                print('{}: {}'.format(key, value))
            print('')
    else:
        print('Unexpected status.')
