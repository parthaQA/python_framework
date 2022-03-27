import json
import traceback
from pprint import pprint

import pytest
import requests
import jsonpath

from utils.CommonUtils import CommonUtils
from utils.DB_Utils import DB_Utils

@pytest.mark.usefixtures("fetch_test_data_generate_token")
class Test_Generate_Token:



    def test_generate_token(self, request, fetch_test_data_generate_token ):
        global response
        global local_id
        test_name = request.node.name
        config = CommonUtils.read_prop_file()
        url = config.get('details', 'tokenUrl')
        print(fetch_test_data_generate_token['tenantId'])
        response = requests.post(url, json=fetch_test_data_generate_token)
        print(response.status_code)
        pprint(response.json())
        json_response = json.loads(response.text)
        try:
            assert response.status_code == 200
            if response.status_code == 200:
                local_id = jsonpath.jsonpath(json_response, "idToken")
                print(local_id[0])
                assert response.status_code == 200
                print(f"{test_name} is passed")
        except AssertionError:
            print(f" status code is :{response.status_code}, hence {test_name} is failed")
            raise

    def test_file_monitoring_file(self, request, fetch_test_data_generate_token):
        test_name = request.node.name
        config = CommonUtils.read_prop_file()
        headers = {"Authorization" : 'Bearer ' + local_id[0],
        "tenant": fetch_test_data_generate_token['tenantId']}
        url = config.get('details', 'fileMonitoring_file')
        response = requests.get(url, headers=headers)

        json_response = json.loads(response.text)
        j = response.json()
        try:

            if response.status_code == 200:
                for i in range(len(j["data"])):
                    print(j["data"][i]["file_name"])
        except AssertionError:
            print("Empty body returned")
        expected_siteId = url.split("/")
        json_re = jsonpath.jsonpath(json_response, "data[0].site_id")
        site_id= " ".join(map(str, json_re))
        print(site_id)
        print(response.status_code)
        print(response.content)
        assert site_id == expected_siteId[5]
