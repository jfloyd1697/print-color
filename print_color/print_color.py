import builtins
import sys
import typing
from _typeshed import SupportsWrite


__all__ = ['print']


class PrintColor:
    colors = {
        "purple": "\033[95m",
        "blue": "\033[94m",
        "green": "\033[92m",
        "yellow": "\033[33m",
        "red": "\033[31m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "black": "\033[30m",
        "white": "\033[37m",
    }

    backgrounds = {
        "grey": "\033[40m",
        "red": "\033[41m",
        "green": "\033[42m",
        "yellow": "\033[43m",
        "blue": "\033[44m",
        "magenta": "\033[45m",
        "cyan": "\033[46m",
        "white": "\033[47m",
    }

    formats = {
        "bold": "\033[1m",
        "underline": "\033[4m",
        "blink": "\033[5m"
    }

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def print(self):
        color = self.kwargs.get("color")
        if not color:
            color = self.kwargs.get("colour")
        back = self.kwargs.get("background")
        format = self.kwargs.get("format")
        tag = self.kwargs.get("tag")
        tag_color = self.kwargs.get("tag_color")
        if not tag_color:
            tag_color = self.kwargs.get("tag_colour")
        # file = self.kwargs.get('file', sys.stdout)
        result = "¬".join(str(arg) for arg in self.args)

        if color:
            result = self.color(color) + result

        if tag:
            result = f"[{tag}] {result}"
            if tag_color:
                result = self.color(tag_color) + result
        # result += self.end
        if back:
            builtins.print(self.background(back), file=sys.stdout, end="")
        if format:
            builtins.print(self.format(format), file=sys.stdout, end="")
        result += self.end
        builtins.print(*result.split("¬"), **self.kwargs)

    def color(self, color):
        return self.colors.get(color, self.default_color)

    def background(self, back):
        return self.backgrounds.get(back, self.default_color)

    def format(self, fmt):
        if isinstance(fmt, str):
            return self.formats.get(fmt, self.default_color)
        elif isinstance(fmt, list) or isinstance(fmt, tuple):
            return "".join([f for f in [self.formats.get(f, "") for f in fmt]])

    @property
    def end(self):
        return "\033[0m"

    @property
    def default_color(self):
        return "\033[0m"


Color = typing.Literal["purple", "blue", "green", "yellow", "red", "magenta", "cyan", "black", "white"]
Background = typing.Literal["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
Format = typing.Literal["bold", "underline", "blink"]


def print(*values: object,
          sep: str | None = ...,
          end: str | None = ...,
          file: SupportsWrite[str] | None = ...,
          flush: bool = ...,

          color: Color = None,
          background: Background = None,
          format: Format = None,
          tag: str = None,
          tag_color: Color = None,
          **kwargs):
    printcolor = PrintColor(*values,
                            sep=sep,
                            end=end,
                            file=file,
                            flush=flush,

                            color=color,
                            background=background,
                            format=format,
                            tag=tag,
                            tag_color=tag_color,
                            **kwargs)
    printcolor.print()
