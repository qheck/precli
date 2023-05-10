# Copyright 2023 Secure Saurce LLC
from precli.core.result import Result
from precli.core.rule import Rule


class MarshalLoad(Rule):
    def __init__(self, id: str):
        super().__init__(
            id=id,
            name="deserialization_of_untrusted_data",
            full_descr=__doc__,
            cwe_id=502,
            message="Potential unsafe usage of {} that can allow "
            "instantiation of arbitrary objects.",
            targets=("call"),
            wildcards={
                "marshal.*": [
                    "load",
                    "loads",
                ]
            },
        )

    def analyze(self, context: dict) -> Result:
        if Rule.match_calls(context, ["marshal.load", "marshal.loads"]):
            return Result(
                rule_id=self.id,
                context=context,
                message=self.message.format(context["func_call_qual"]),
            )