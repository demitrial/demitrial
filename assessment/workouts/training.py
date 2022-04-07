di = {}
normal = {'event': {'event_type': 'signature_request_sent', 'event_time': '1647692106',
                    'event_hash': 'cc35446ac3557014fe8aa9a7827df990d4e75fcf4734d1f4b177a6a13f4bc56b',
                    'event_metadata': {'related_signature_id': None,
                                       'reported_for_account_id': '1f920cadd0118efbe1b45a97ce74c063863ebe37',
                                       'reported_for_app_id': None}},
          'account_guid': '1f920cadd0118efbe1b45a97ce74c063863ebe37', 'client_id': None,
          'signature_request': {'signature_request_id': '8aa4b4ff829b0e5a493bfe4bb361d6431d72758e', 'test_mode': True,
                                'title': 'Task_sign_request', 'original_title': 'This is testing request',
                                'subject': 'This is testing request',
                                'message': 'Hi, This is the message for send request',
                                'metadata': {}, 'created_at': 1647692097, 'is_complete': False, 'is_declined': False,
                                'has_error': False, 'custom_fields': [], 'response_data': [],
                                'signing_url': 'https://app.hellosign.com/sign/8aa4b4ff829b0e5a493bfe4bb361d6431d72758e',
                                'signing_redirect_url': None,
                                'final_copy_uri': '/v3/signature_request/final_copy/8aa4b4ff829b0e5a493bfe4bb361d6431d72758e',
                                'files_url': 'https://api.hellosign.com/v3/signature_request/files/8aa4b4ff829b0e5a493bfe4bb361d6431d72758e',
                                'details_url': 'https://app.hellosign.com/home/manage?guid=8aa4b4ff829b0e5a493bfe4bb361d6431d72758e',
                                'requester_email_address': 'demitrial@dorustree.in', 'signatures': [
                  {'signature_id': 'e57b999ffb753c76e233cb775f796a6c', 'has_pin': False, 'has_sms_auth': False,
                   'signer_email_address': 'demitrial.dorustree@gmail.com', 'signer_name': 'user', 'signer_role': None,
                   'order': None, 'status_code': 'awaiting_signature', 'signed_at': None, 'last_viewed_at': None,
                   'last_reminded_at': None, 'error': None}], 'cc_email_addresses': [], 'template_ids': None}}

print(normal['client_id'])

embd = {'event': {'event_type': 'signature_request_sent', 'event_time': '1647692477',
                  'event_hash': 'ea97486f91f4f5d1e17055331afb7de360140e4c968dd85deff6eb808856f559',
                  'event_metadata': {'related_signature_id': None,
                                     'reported_for_account_id': '1f920cadd0118efbe1b45a97ce74c063863ebe37',
                                     'reported_for_app_id': 'a5b2d38378281f6ea3c7788ad500ffd6'}},
        'account_guid': '1f920cadd0118efbe1b45a97ce74c063863ebe37', 'client_id': 'a5b2d38378281f6ea3c7788ad500ffd6',
        'signature_request': {'signature_request_id': '6969b99c0f88b9037bef447e4091dc7662b7f8d5', 'test_mode': True,
                              'title': 'Task_sign_request', 'original_title': 'This is testing request',
                              'subject': 'This is testing request',
                              'message': 'Hi, This is the message for send request',
                              'metadata': {}, 'created_at': 1647692470, 'is_complete': False, 'is_declined': False,
                              'has_error': False, 'custom_fields': [], 'response_data': [], 'signing_url': None,
                              'signing_redirect_url': None,
                              'final_copy_uri': '/v3/signature_request/final_copy/6969b99c0f88b9037bef447e4091dc7662b7f8d5',
                              'files_url': 'https://api.hellosign.com/v3/signature_request/files/6969b99c0f88b9037bef447e4091dc7662b7f8d5',
                              'details_url': 'https://app.hellosign.com/home/manage?guid=6969b99c0f88b9037bef447e4091dc7662b7f8d5',
                              'requester_email_address': 'demitrial@dorustree.in', 'signatures': [
                {'signature_id': 'c20f22fe1f6af3d981617d8163a04410', 'has_pin': False, 'has_sms_auth': False,
                 'signer_email_address': 'demitrial.dorustree@gmail.com', 'signer_name': 'user', 'signer_role': None,
                 'order': None, 'status_code': 'awaiting_signature', 'signed_at': None, 'last_viewed_at': None,
                 'last_reminded_at': None, 'error': None}], 'cc_email_addresses': [], 'template_ids': None,
                              'client_id': 'a5b2d38378281f6ea3c7788ad500ffd6'}}

if embd['signature_request']['client_id']:
    di['signature_type'] = 'Embedded'
else:
    di['signature_type'] = 'Normal'
