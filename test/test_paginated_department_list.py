"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergeATSClient
from MergeATSClient.model.department import Department
globals()['Department'] = Department
from MergeATSClient.model.paginated_department_list import PaginatedDepartmentList
from MergeATSClient.api_client import ApiClient


class TestPaginatedDepartmentList(unittest.TestCase):
    """PaginatedDepartmentList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedDepartmentList(self):
        """Test PaginatedDepartmentList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedDepartmentList()  # noqa: E501

        """
        No test json responses were defined for PaginatedDepartmentList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedDepartmentList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
