"""Show that super() follows the MRO rather than a hard-coded parent."""


class Root:
    def process(self, events: list[str]) -> None:
        events.append("Root")


class LoggingMixin(Root):
    def process(self, events: list[str]) -> None:
        events.append("LoggingMixin")
        super().process(events)


class ValidationMixin(Root):
    def process(self, events: list[str]) -> None:
        events.append("ValidationMixin")
        super().process(events)


class Service(LoggingMixin, ValidationMixin):
    def process(self, events: list[str]) -> None:
        events.append("Service")
        super().process(events)


def main() -> None:
    events: list[str] = []
    Service().process(events)

    print("MRO:", " -> ".join(cls.__name__ for cls in Service.__mro__))
    print("Execution:", " -> ".join(events))


if __name__ == "__main__":
    main()

