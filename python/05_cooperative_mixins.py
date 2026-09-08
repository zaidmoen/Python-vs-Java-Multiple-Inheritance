"""Reusable, cooperative mixins that compose through super()."""


class BaseRequest:
    def handle(self, request: dict[str, object]) -> list[str]:
        return [f"handled {request['path']}"]


class AuthenticationMixin(BaseRequest):
    def handle(self, request: dict[str, object]) -> list[str]:
        if not request.get("authenticated"):
            raise PermissionError("Authentication is required")
        return ["authenticated", *super().handle(request)]


class TimingMixin(BaseRequest):
    def handle(self, request: dict[str, object]) -> list[str]:
        return ["timed", *super().handle(request)]


class ApiHandler(AuthenticationMixin, TimingMixin):
    pass


def main() -> None:
    request = {"path": "/profile", "authenticated": True}
    print("MRO:", " -> ".join(cls.__name__ for cls in ApiHandler.__mro__))
    print("Pipeline:", " -> ".join(ApiHandler().handle(request)))

    try:
        ApiHandler().handle({"path": "/profile", "authenticated": False})
    except PermissionError as error:
        print("Rejected request:", error)


if __name__ == "__main__":
    main()

