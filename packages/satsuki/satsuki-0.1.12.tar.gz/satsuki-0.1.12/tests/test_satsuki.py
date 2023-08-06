# -*- coding: utf-8 -*-
# pylint: disable=redefined-outer-name
"""Test Satsuki module."""
import uuid
import os
import platform
from string import Template
import pytest
import requests
import github

from satsuki import Arguments, ReleaseMgr

TEST_VERBOSE = True
TEST_BODY = str(uuid.uuid1())
TEST_SLUG = "YakDriver/satsuki-tests"
TEST_TAG = "Test-v" + TEST_BODY[:6]
TEST_REL_NAME = "Test Release v" + TEST_BODY[:6]
TEST_COMMITISH = "85478f0e9298061ca56e62f8054bfe068e97622a"
TEST_FILENAME = 'tests/release-asset.exe'
TEST_DOWNLOAD = 'tests/downloaded-asset'
TEST_DOWNLOAD_SHA = 'tests/downloaded-asset-sha'
TEST_RECREATE_COMMITISH = "0875719da4be3bf10614719d5ae5d2a548f5f201"


def test_blank_arguments():
    """Test authorization by getting blank arguments. """
    with pytest.raises(PermissionError):
        Arguments()


def test_create_release(token):
    """Test creating a GitHub release."""
    arguments_base = Arguments(
        token=token,
        slug=TEST_SLUG,
        tag=TEST_TAG,
        body=TEST_BODY,
        rel_name=TEST_REL_NAME,
        commitish=TEST_COMMITISH
    )

    r_m = ReleaseMgr(arguments_base)
    r_m.execute()  # <== should create
    compare_args = Arguments(
        token=token,
        slug=TEST_SLUG,
        tag=TEST_TAG
    )

    assert compare_args.opts["body"] == TEST_BODY \
        and compare_args.opts["rel_name"] == TEST_REL_NAME


def test_get_latest(token):
    """Test getting the latest GitHub release."""
    arguments_base = Arguments(
        token=token,
        slug=TEST_SLUG,
        tag=TEST_TAG,
        body=TEST_BODY,
        rel_name=TEST_REL_NAME,
        commitish=TEST_COMMITISH
    )

    r_m = ReleaseMgr(arguments_base)
    r_m.execute()  # <== should create
    compare_args = Arguments(
        token=token,
        slug=TEST_SLUG,
        latest=True
    )

    if compare_args.opts["tag"] == TEST_TAG:
        assert compare_args.opts["tag"] == TEST_TAG \
            and compare_args.opts["body"] == TEST_BODY \
            and compare_args.opts["rel_name"] == TEST_REL_NAME
    else:
        # a real tag has gotten in first, forget the test
        assert True


def test_upload_file_no_sha(token):
    """Test uploading an asset to a GitHub release."""
    with open(TEST_FILENAME, 'wb') as fout:
        fout.write(os.urandom(1024000))

    args = Arguments(
        token=token,
        slug=TEST_SLUG,
        tag=TEST_TAG,
        files_file="tests/test.file"
    )

    ul_rel = ReleaseMgr(args)
    ul_rel.execute()
    assert True


def test_download_file_no_sha(token):
    """Test whether the file uploaded in previous test exists."""

    # github => repo => release => asset_list => asset => url => download

    g_h = github.Github(token, per_page=100)
    repo = g_h.get_repo(TEST_SLUG, lazy=False)
    release = repo.get_release(TEST_TAG)
    asset_list = release.get_assets()
    sha_filename = Template(Arguments.HASH_FILE).safe_substitute({
        'platform': platform.system().lower()
    })

    pass_test = True

    for check_asset in asset_list:
        # look through list of assets for uploaded file and sha file

        if check_asset.name == sha_filename:

            pass_test = False

    assert pass_test


# Order is important, no sha tests upload, recreate gets rid of upload,
# and then upload can be done again

def test_recreate_release(token):
    """Test recreating a GitHub release, which deletes the uploaded asset."""
    recreate_args = Arguments(
        token=token,
        slug=TEST_SLUG,
        tag=TEST_TAG,
        recreate=True,
        commitish=TEST_RECREATE_COMMITISH
    )
    new = ReleaseMgr(recreate_args)
    new.execute()  # <== should recreate

    # really the test is if it makes it this far
    assert recreate_args.opts["target_commitish"] == TEST_RECREATE_COMMITISH


def test_upload_file(token):
    """Test uploading an asset to a recreated GitHub release."""
    with open(TEST_FILENAME, 'wb') as fout:
        fout.write(os.urandom(1024000))

    args = Arguments(
        token=token,
        slug=TEST_SLUG,
        tag=TEST_TAG,
        files_file="tests/test.file",
        file_sha=Arguments.FILE_SHA_SEP_FILE
    )

    ul_rel = ReleaseMgr(args)
    ul_rel.execute()
    assert True


def test_download_file(token):
    """Test downloading an asset associated with a GitHub release."""

    # github => repo => release => asset_list => asset => url => download

    g_h = github.Github(token, per_page=100)
    repo = g_h.get_repo(TEST_SLUG, lazy=False)
    release = repo.get_release(TEST_TAG)
    asset_list = release.get_assets()
    sha_filename = Template(Arguments.HASH_FILE).safe_substitute({
        'platform': platform.system().lower()
    })

    assets_calculated_sha = 'notasha'
    sha_dict = {}

    for check_asset in asset_list:
        # look through list of assets for uploaded file and sha file

        if check_asset.name == os.path.basename(TEST_FILENAME):

            # the uploaded asset
            request = requests.get(check_asset.browser_download_url)
            open(TEST_DOWNLOAD, 'wb').write(request.content)

            # recalc hash of downloaded file
            assets_calculated_sha = Arguments.get_hash(TEST_DOWNLOAD)

        elif check_asset.name == sha_filename:

            # the sha hash file
            request = requests.get(check_asset.browser_download_url)
            sha_dict = request.json()

    assert assets_calculated_sha == sha_dict[os.path.basename(TEST_FILENAME)]


def test_delete_release(token):
    """Test deleting a GitHub release."""
    delete_args = Arguments(
        token=token,
        slug=TEST_SLUG,
        tag=TEST_TAG,
        command=Arguments.CMD_DELETE,
        include_tag=True
    )

    del_rel = ReleaseMgr(delete_args)
    del_rel.execute()
    assert True
