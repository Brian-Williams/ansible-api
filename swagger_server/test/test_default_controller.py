# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.playbook_input import PlaybookInput  # noqa: E501
from swagger_server.models.playbook_result import PlaybookResult  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_playbook_post(self):
        """Test case for playbook_post

        run a playbook
        """
        body = PlaybookInput()
        response = self.client.open(
            '/Brian-Williams/microansible/1.0.0/playbook',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
