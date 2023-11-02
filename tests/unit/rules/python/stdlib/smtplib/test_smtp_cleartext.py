# Copyright 2023 Secure Saurce LLC
import os

from precli.core.level import Level
from precli.rules import Rule
from tests.unit.rules.python import test_case


class SmtpCleartextTests(test_case.TestCase):
    def setUp(self):
        super().setUp()
        self.base_path = os.path.join(
            "tests",
            "unit",
            "rules",
            "python",
            "stdlib",
            "smtplib",
            "examples",
        )

    def test_smtp_cleartext_rule_meta(self):
        rule = Rule.get_by_id("PRE0015")
        self.assertEqual("PRE0015", rule.id)
        self.assertEqual("cleartext_transmission", rule.name)
        self.assertEqual(
            "https://docs.securesauce.dev/rules/PRE0015", rule.help_url
        )
        self.assertEqual(True, rule.default_config.enabled)
        self.assertEqual(Level.WARNING, rule.default_config.level)
        self.assertEqual(-1.0, rule.default_config.rank)
        self.assertEqual("319", rule.cwe.cwe_id)

    def test_smtplib_smtp_auth(self):
        results = self.parser.parse(
            os.path.join(self.base_path, "smtplib_smtp_auth.py")
        )
        self.assertEqual(1, len(results))
        result = results[0]
        self.assertEqual("PRE0015", result.rule_id)
        self.assertEqual(27, result.location.start_line)
        self.assertEqual(27, result.location.end_line)
        self.assertEqual(7, result.location.start_column)
        self.assertEqual(11, result.location.end_column)
        self.assertEqual(Level.ERROR, result.level)
        self.assertEqual(-1.0, result.rank)

    def test_smtplib_smtp_context_mgr(self):
        results = self.parser.parse(
            os.path.join(self.base_path, "smtplib_smtp_context_mgr.py")
        )
        self.assertEqual(1, len(results))
        result = results[0]
        self.assertEqual("PRE0015", result.rule_id)
        self.assertEqual(6, result.location.start_line)
        self.assertEqual(6, result.location.end_line)
        self.assertEqual(9, result.location.start_column)
        self.assertEqual(14, result.location.end_column)
        self.assertEqual(Level.ERROR, result.level)
        self.assertEqual(-1.0, result.rank)

    def test_smtplib_smtp_login(self):
        results = self.parser.parse(
            os.path.join(self.base_path, "smtplib_smtp_login.py")
        )
        self.assertEqual(1, len(results))
        result = results[0]
        self.assertEqual("PRE0015", result.rule_id)
        self.assertEqual(26, result.location.start_line)
        self.assertEqual(26, result.location.end_line)
        self.assertEqual(7, result.location.start_column)
        self.assertEqual(12, result.location.end_column)
        self.assertEqual(Level.ERROR, result.level)
        self.assertEqual(-1.0, result.rank)

    def test_smtplib_smtp_ssl(self):
        results = self.parser.parse(
            os.path.join(self.base_path, "smtplib_smtp_ssl.py")
        )
        self.assertEqual(0, len(results))

    def test_smtplib_smtp_starttls(self):
        results = self.parser.parse(
            os.path.join(self.base_path, "smtplib_smtp_starttls.py")
        )
        self.assertEqual(0, len(results))
