# Copyright 2023 Secure Saurce LLC
from precli.core.level import Level
from precli.core.result import Result
from precli.core.rule import Rule


class PycryptoWeakHash(Rule):
    def __init__(self):
        super().__init__(
            id="PRE312",
            name="reversible_one-way_hash",
            full_descr=__doc__,
            cwe=328,
            message="Use of weak hash function {} does not meet security "
            "expectations.",
        )

    def analyze(self, context: dict) -> Result:
        if Rule.match_calls(
            context,
            [
                "Crypto.Hash.MD2.new",
                "Crypto.Hash.MD4.new",
                "Crypto.Hash.MD5.new",
                "Crypto.Hash.RIPEMD.new",
                "Crypto.Hash.SHA.new",
            ],
        ):
            return Result(
                rule_id=self.id,
                context=context,
                level=Level.ERROR,
                message=self.message.format(context["func_call_qual"]),
            )