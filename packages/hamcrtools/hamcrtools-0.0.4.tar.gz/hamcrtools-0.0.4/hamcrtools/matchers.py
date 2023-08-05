# -*- coding: utf-8 -*-

import json
import os

import requests
from hamcrest import less_than_or_equal_to
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.string_description import StringDescription
from jsonschema import validate, ValidationError
from requests import Response


class JsonschemaMatcher(BaseMatcher):
    def __init__(self, jsonschema_path):
        self.jsonschema_path = jsonschema_path
        with open(jsonschema_path) as jsonschema_descriptor:
            self.jsonschema = json.load(jsonschema_descriptor)

    def _matches(self, item):
        try:
            validate(item, self.jsonschema)
        except ValidationError as e:
            self.message = e.message
            return False
        return True

    def describe_to(self, description):
        description.append_text(f'Content should correspond to schema located at {self.jsonschema_path}')

    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append_text('Json is not correspond to schema.')
        mismatch_description.append_text(os.linesep)
        mismatch_description.append_text(self.message)


def matched_schema(jsonschema_path):
    return JsonschemaMatcher(jsonschema_path)


def object_itself(obj):
    return obj


class ListSortedMatcher(BaseMatcher):
    @staticmethod
    def _less_or_equal(left, right):
        return left <= right

    @staticmethod
    def _greater_or_equal(left, right):
        return left >= right

    def __init__(self, pair_matcher=less_than_or_equal_to, criteria=object_itself):
        self.pair_matcher = pair_matcher
        self.criteria = criteria
        self.messages = []

    def _matches(self, item):
        if not (isinstance(item, list) or isinstance(item, tuple)):
            self.messages.append(f'Can\'t perform ListSorted matcher on {type(item)} object.')

        pairs = [(item[i], item[i + 1]) for i in range(len(item) - 1)]
        for i, (left, right) in enumerate(pairs):
            matcher = self.pair_matcher(self.criteria(right))
            if not matcher.matches(self.criteria(left)):
                description = StringDescription()
                matcher.describe_to(description)
                description.append_text(' expected, but ')
                matcher.describe_mismatch(self.criteria(left), description)
                description.append(f'. items indexes are {i}, and {i + 1}')
                self.messages.append(str(description))
                return False
        return True

    def describe_to(self, description):
        pass

    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append_text('List is not correctly sorted.')
        mismatch_description.append(os.linesep)
        mismatch_description.append_text(f'Comparator = {self.pair_matcher} ; criteria = {self.criteria}.')
        mismatch_description.append_text(os.linesep)
        for m in self.messages:
            mismatch_description.append_text(m)
            mismatch_description.append_text(os.linesep)


def is_sorted(pair_matcher=less_than_or_equal_to, criteria=object_itself):
    return ListSortedMatcher(pair_matcher, criteria)


class ResponseCodeMatcher(BaseMatcher):
    def __init__(self, code):
        self.expected_code = requests.codes[code] if isinstance(code, str) else code
        if not isinstance(self.expected_code, int):
            raise ValueError('Code is expected to be either string or integer or "requests.codes.{name}" object.')

    def _matches(self, item):
        self.actual_code = item
        if isinstance(item, Response):
            self.actual_code = item.status_code
        if isinstance(item, str):
            self.actual_code = requests.codes[item]
        if not isinstance(self.actual_code, int):
            raise ValueError('Item is expected to be either requests.Response object '
                             'or string or integer or "requests.codes.{name}" object.')

        return self.expected_code == self.actual_code

    def describe_to(self, description):
        description.append_text(f'Response code should be equal to {self.expected_code}.')

    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append_text(f'Response code was {self.actual_code}.')


def has_code(code):
    return ResponseCodeMatcher(code)
