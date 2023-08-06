# -*- coding: utf-8 -*-
"""
Find testcases that are missing in Polarion.
"""

from __future__ import absolute_import, unicode_literals

import logging
import os

from cfme_testcases import testcases, utils
from cfme_testcases.collector import testcases_svn
from cfme_testcases.exceptions import TestcasesException
from dump2polarion import parselogs

# pylint: disable=invalid-name
logger = logging.getLogger(__name__)


class MissingTestcases(object):
    """Testcases missing in Polarion."""

    def __init__(self, config, all_testcases, init_logname, svn_dir):
        self.config = config
        self.all_testcases = all_testcases
        self.init_logname = init_logname or ""
        self.svn_dir = svn_dir

    def get_missing_from_log(self):
        """Gets missing testcases from log file."""
        lookup_method = self.config.get("xunit_import_properties") or {}
        lookup_method = lookup_method.get("polarion-lookup-method") or "id"
        parsed_log = parselogs.parse(self.init_logname)

        if lookup_method == "name":
            missing = [item.name for item in parsed_log.new_items]
        elif lookup_method == "custom":
            missing = [item.custom_id for item in parsed_log.new_items]
        elif lookup_method == "id":
            missing = [item.id for item in parsed_log.new_items]

        return set(missing)

    def get_missing_from_svn(self, all_testcases, repo_dir):
        """Gets missing testcases using SVN repo."""
        import_props = self.config.get("testcase_import_properties") or {}
        lookup_by = import_props.get("lookup-method") or "id"
        if lookup_by == "name":
            lookup_by = "title"
        elif lookup_by == "custom":
            lookup_by = import_props.get("polarion-custom-lookup-method-field-id") or "testCaseID"
        elif lookup_by == "id":
            lookup_by = "work_item_id"

        missing = testcases_svn.get_missing(repo_dir, all_testcases, lookup_by=lookup_by)
        return set(missing)

    def get_missing(self):
        """Returns list of missing testcases."""
        utils.check_lookup_methods(self.config)
        log_exists = os.path.isfile(self.init_logname)
        if self.svn_dir and not log_exists:
            missing = self.get_missing_from_svn(self.all_testcases, self.svn_dir)
        elif not log_exists:
            raise TestcasesException(
                "The submit log file `{}` doesn't exist.".format(self.init_logname)
            )
        else:
            missing = self.get_missing_from_log()
        return missing


def get_missing(config, testcases_root, init_logname, svn_dir):
    """Returns list of missing testcases."""
    all_testcases = testcases.get_all_testcases(testcases_root)
    return MissingTestcases(config, all_testcases, init_logname, svn_dir).get_missing()
