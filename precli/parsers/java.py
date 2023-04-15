# Copyright 2023 Secure Saurce LLC
from precli.core.parser import Parser
from precli.core.result import Result


class Java(Parser):
    def __init__(self):
        super().__init__("java")

    def file_extension(self) -> str:
        return ".java"

    def parse(self, file_name: str, data: bytes) -> list[Result]:
        self.parser.parse(file_name, data)
