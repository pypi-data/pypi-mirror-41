from dataclasses import dataclass
from typing import List


@dataclass()
class FritzPath:
    path: str

    def __post_init__(self) -> None:
        self._fragments: List[str] = self.path.split('/')

    @property
    def fragments(self) -> List[str]:
        return self._fragments


@dataclass()
class FritzInput:
    id: str
    value: str


@dataclass()
class FritzButton:
    selector: str
    by_type: str


@dataclass()
class FritzWifiProfileSelect:
    device_name: str
    profile: str


class FritzPages(object):
    _child_lock = FritzPath('inet/filter')
    _child_profiles = FritzPath('inet/filter/kidPro')

    @property
    def child_lock(self) -> FritzPath:
        return self._child_lock

    @property
    def child_profiles(self) -> FritzPath:
        return self._child_profiles

