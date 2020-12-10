from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import List


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Event) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Event) -> None:
        pass

    @abstractmethod
    def notify(self, key, value) -> None:
        pass

    @abstractmethod
    def save_add(self):
        pass

    @abstractmethod
    def save_remove(self):
        pass


class Observer(Subject):
    _state: List = None
    _key: str = None
    _observers: List[Event] = []

    def attach(self, observer: Event) -> None:
        self._observers.append(observer)

    def detach(self, observer: Event) -> None:
        self._observers.remove(observer)

    def notify(self, key, value) -> None:
        self._key = key
        self._state = value
        for observer in self._observers:
            observer.on_change(self)

    def save_add(self) -> None:
        file = open("History.txt", "a")
        file.write("Add: ")
        file.write(List.LinkedList.return_str_list(self._state))
        file.write("\n")
        file.close()
        return None

    def save_remove(self) -> None:
        file = open("History.txt", "a")
        file.write("Remove: ")
        file.write(List.LinkedList.return_str_list(self._state))
        file.write("\n")
        file.close()
        return None


class Event(ABC):
    @abstractmethod
    def on_change(self, subject: Subject):
        pass


class EventAdd(Event):
    def on_change(self, subject: Subject) -> None:
        if subject._key == "Add":
            Observer.save_add(subject)


class EventRemove(Event):
    def on_change(self, subject: Subject) -> None:
        if subject._key == "Remove":
            Observer.save_remove(subject)
