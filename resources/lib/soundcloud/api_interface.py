from future.utils import with_metaclass
from abc import ABCMeta, abstractmethod


class ApiInterface(with_metaclass(ABCMeta)):
    @abstractmethod
    def search(self, query, kind): pass

    @abstractmethod
    def call(self, url): pass

    @abstractmethod
    def discover(self, selection): pass

    @abstractmethod
    def resolve_url(self, url): pass