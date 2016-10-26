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

# Payload with conditional request_id
payload = {'request_id': '[INSERT_REQ_ID]'}

# Payload with conditional file_token
payload = {
    'files': [{'file_token': '[INSERT_FILE_TOKEN]'}]
}

result = sc.get_info_service()
if result.status_code != 200:
    print("Http error occured with status code {}.".format(result.status_code))
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
        for file_info in result_dict['files']:
            for (key, value) in file_info.items():
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
