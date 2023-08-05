# coding=utf-8
# Licensed Materials - Property of IBM
# Copyright IBM Corp. 2017
from typing import Any, Dict

import enum

def domain_id() -> str: ...
def instance_id() -> str: ...
def is_standalone() -> bool: ...
def get_application_directory() -> str: ...
def get_application_configuration(name : str) -> Dict[str,str]: ...
def channel(obj) -> int: ...
def local_channel(obj) -> int: ...
def max_channels(obj) -> int: ...
def local_max_channels(obj) -> int: ...


class MetricKind(enum.Enum):
    Counter=0
    Gauge=1
    Time=2


class CustomMetric(object):
    def __init__(self, obj: Any, name: str, description: str=None, kind: MetricKind=MetricKind.Counter, initialValue: int=0) -> None: ...
    @property
    def value(self) -> int: ...
