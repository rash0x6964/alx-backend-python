#!/usr/bin/env python3
""" A module for testing the client module """

import unittest
from parameterized import parameterized
from unittest.mock import MagicMock, patch

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Tests the GithubOrgClient class """

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json",)
    def test_org(self, org, res, mocked_fn) -> None:
        """ Tests the org method """

        mocked_fn.return_value = MagicMock(return_value=res)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), res)
        mocked_fn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )
