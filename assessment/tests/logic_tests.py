import unittest

from flask import jsonify

from services.logics import add_user, getuserinfo, login, prod_type, wasteprods, plastictype_add, \
    shape_add, selling_prod, user_things_cost, sampleorder


class ServiceTests(unittest.TestCase):

    def test_add_user(self):
        input_data = {
            "username": "Droidy",
            "password": "mictest",
            "address": "france"
        }
        send_req = add_user()
        self.assertEqual(send_req, "User Added Successfully!")
        return send_req

