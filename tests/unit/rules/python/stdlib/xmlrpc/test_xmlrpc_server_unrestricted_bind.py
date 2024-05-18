# Copyright 2024 Secure Saurce LLC
import os

import pytest

from precli.core.level import Level
from precli.parsers import python
from precli.rules import Rule
from tests.unit.rules import test_case


class TestXmlrpcServerUnrestrictedBind(test_case.TestCase):
    @classmethod
    def setup_class(cls):
        cls.rule_id = "PY032"
        cls.parser = python.Python()
        cls.base_path = os.path.join(
            "tests",
            "unit",
            "rules",
            "python",
            "stdlib",
            "xmlrpc",
            "examples",
        )

    def test_rule_meta(self):
        rule = Rule.get_by_id(self.rule_id)
        assert rule.id == self.rule_id
        assert rule.name == "unrestricted_bind"
        assert (
            rule.help_url
            == f"https://docs.securesauce.dev/rules/{self.rule_id}"
        )
        assert rule.default_config.enabled is True
        assert rule.default_config.level == Level.WARNING
        assert rule.default_config.rank == -1.0
        assert rule.cwe.cwe_id == "1327"

    @pytest.mark.parametrize(
        "filename",
        [
            "xmlrpc_server_doc_xml_rpc_server.py",
            "xmlrpc_server_simple_xml_rpc_server.py",
        ],
    )
    def test(self, filename):
        self.check(filename)
