#!/usr/bin/env python3
""" A module for testing the client module """

import unittest
from parameterized import parameterized
from unittest.mock import MagicMock, PropertyMock, patch

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Tests the GithubOrgClient class """

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json",)
    def test_org(self, org, res, mocked_fn):
        """ Tests the org method """

        mocked_fn.return_value = MagicMock(return_value=res)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), res)
        mocked_fn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self):
        """ Tests the _public_repos_url property """

        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos"
            )

    @patch("client.get_json")
    def test_public_repos(self, mocked_fn):
        """ Tests the public_repos method """

        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [{"name": "repo_1"}, {"name": "repo_2"}]
        }
        mocked_fn.return_value = test_payload["repos"]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
                ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                ["repo_1", "repo_2"],
            )
            mock_public_repos_url.assert_called_once()
        mocked_fn.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "my_license"}}, "my_license", True),
        ({'license': {'key': "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, key, expected):
        """Tests the `has_license` method."""
        gh_org_client = GithubOrgClient("google")
        client_has_licence = gh_org_client.has_license(repo, key)
        self.assertEqual(client_has_licence, expected)
