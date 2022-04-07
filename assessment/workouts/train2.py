# import json
#
# x = """{
#     "data": "Jennifer Smith",
#     "Contact Number": 7867567898,
#     "meta": "jen123@gmail.com",
#     "Hobbies":["Reading", "Sketching", "Horse Riding"]
#     }"""
#
# # parse x:
# y = json.loads(x)
# print(y)
#
# send_dict: dict = y['data']
# meta_dict: dict = send_dict['meta']
#
from datetime import datetime
import datetime
from sqlalchemy import null, false, true

dd = {"event": {"event_type": "signature_request_sent", "event_time": "1647519901",
                "event_hash": "4a659737738c16fd347ce5363457146baa41f3dc7418c70ee971f466dc191a75",
                "event_metadata": {"related_signature_id": null,
                                   "reported_for_account_id": "1f920cadd0118efbe1b45a97ce74c063863ebe37",
                                   "reported_for_app_id": "a5b2d38378281f6ea3c7788ad500ffd6"}},
      "account_guid": "1f920cadd0118efbe1b45a97ce74c063863ebe37", "client_id": "a5b2d38378281f6ea3c7788ad500ffd6",
      "signature_request": {"signature_request_id": "e02932c7e549ec9ebb319cb78370d686db6c4252", "test_mode": true,
                            "title": "Embedded callback_url", "original_title": "Embedded signature",
                            "subject": "Embedded signature", "message": "Please sign for Callback url", "metadata": {},
                            "created_at": 1647519894, "is_complete": false, "is_declined": false, "has_error": false,
                            "custom_fields": [], "response_data": [], "signing_url": null, "signing_redirect_url": null,
                            "final_copy_uri": "\\/v3\\/signature_request\\/final_copy\\/e02932c7e549ec9ebb319cb78370d686db6c4252",
                            "files_url": "https:\\/\\/api.hellosign.com\\/v3\\/signature_request\\/files\\/e02932c7e549ec9ebb319cb78370d686db6c4252",
                            "details_url": "https:\\/\\/app.hellosign.com\\/home\\/manage?guid=e02932c7e549ec9ebb319cb78370d686db6c4252",
                            "requester_email_address": "demitrial@dorustree.in", "signatures": [
              {"signature_id": "6c77a4ae085f2d963c7e77cd408cabaf", "has_pin": false, "has_sms_auth": false,
               "signer_email_address": "demitrial.dorustree@gmail.com", "signer_name": "Jack", "signer_role": null,
               "order": null, "status_code": "awaiting_signature", "signed_at": null, "last_viewed_at": null,
               "last_reminded_at": null, "error": null}], "cc_email_addresses": [], "template_ids": null,
                            "client_id": "a5b2d38378281f6ea3c7788ad500ffd6"}}
# event_time = dd['event']['event_time']
# ts = int(event_time)
# actual_time = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
actual_time = '2022-03-17 12:25:01'

# date_time_obj = datetime.datetime.strptime(actual_time, '%Y-%m-%d %H:%M:%S.%f')
# print('Date:', date_time_obj.date())
# print(date_time_obj)

op = open('/home/pc/PycharmProjects/flaskcrud/embd_sign_media/Python Training Road Map.pdf')
print(op)
