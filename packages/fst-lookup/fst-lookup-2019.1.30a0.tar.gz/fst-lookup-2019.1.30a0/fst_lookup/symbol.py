#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Copyright 2019 Eddie Antonio Santos <easantos@ualberta.ca>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABC, abstractmethod


class Symbol(ABC):
    """
    A symbol in the FST.
    """
    @abstractmethod
    def accepts(self, other: 'Symbol') -> bool:
        raise NotImplementedError


class EpsilonType(Symbol):
    def accepts(self, other: 'Symbol') -> bool:
        return True

    def __repr__(self) -> str:
        return 'Epsilon'

    def __str__(self) -> str:
        # Print an epsilon in reverse video, to distinguish it from a literal epsilon.
        return '\033[7m' 'ε' '\033[27m'


class UnknownType(Symbol):
    def accepts(self, other: 'Symbol') -> bool:
        raise NotImplementedError


class IdentityType(Symbol):
    def accepts(self, other: 'Symbol') -> bool:
        raise NotImplementedError


Unknown = UnknownType()
Identity = IdentityType()
Epsilon = EpsilonType()


class GraphicalSymbol(Symbol):
    __slots__ = '_value',

    def __init__(self, value: str) -> None:
        self._value = value

    def accepts(self, other: Symbol) -> bool:
        if isinstance(other, type(self)):
            return other._value == self._value
        return False

    def __str__(self) -> str:
        return self._value

    def __repr__(self) -> str:
        return '{:}({!r})'.format(type(self).__name__, self._value)


class Grapheme(GraphicalSymbol):
    """
    Represents a single graphical character.
    """

    def __init__(self, char: str) -> None:
        assert len(char) == 1
        super().__init__(char)


class MultiCharacterSymbol(GraphicalSymbol):
    """
    Usually represents a tag or a feature.
    """

    def __init__(self, tag: str) -> None:
        assert len(tag) > 1
        super().__init__(tag)
