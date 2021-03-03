from rich.console import Console


class Response:
    def __init__(self, data):
        self._data = data

    def render(self):
        console = Console()
        console.print(self._data, style="bold green")
