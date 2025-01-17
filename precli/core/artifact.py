# Copyright 2024 Secure Sauce LLC
from typing import Optional


class Artifact:
    def __init__(self, file_name: str, uri: Optional[str] = None):
        self._file_name = file_name
        # TODO: if uri is None, use file:///
        self._uri = uri
        self._contents = None
        self._encoding = "utf-8"
        self._language = None

    @property
    def file_name(self) -> str:
        """The name of the file."""
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Set the file name"""
        self._file_name = file_name

    @property
    def uri(self) -> Optional[str]:
        """The URI of the artifact."""
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Set the artifact URI."""
        self._uri = uri

    @property
    def encoding(self) -> str:
        """The encoding of the file."""
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Set the encoding of the file."""
        self._encoding = encoding

    @property
    def contents(self) -> str | None:
        """The contents of the artifact."""
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Set the contents (for typically the file)."""
        self._contents = contents

    @property
    def language(self) -> str | None:
        """The programming language for this artifact."""
        return self._language

    @language.setter
    def language(self, language):
        """Set the programming language."""
        self._language = language
