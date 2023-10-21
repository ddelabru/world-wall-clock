# world-wall-clock

**world-wall-clock** is a TUI application that provides a multi-timezone
graphical clock in a terminal environment.

![Screeenshot of world-wall-clock](./screenshot.png)

## Installing world-wall-clock

You can install world-wall-clock with the Python packaging tool
[pip](https://pip.pypa.io/en/stable/). It is recommended to do so in a
[virtual environment](https://docs.python.org/3/library/venv.html).

### From PyPI

```sh
python -m pip install world-wall-clock
```

### From the top level of the source repo.

```sh
python -m pip install .
```

## Running world-wall-clock

In an environment with world-wall-clock installed, start it from the command
line with:

```sh
wwclock
```

or

```sh
python -m world_wall_clock
```

## Usage

world-wall-clock is a graphical application. By default it shows a live view of
one local clock (the system time) and clocks for several time zones scattered
around the world. By navigating using arrow keys and selecting or deselecting
items from the sidebar of available timezones using the `Enter` or `Space` key,
you can customize the list of displayed clocks. This is silently stored in the
application configuration directory for the next time you launch
world-wall-clock.

Using the "Custom time" radio button, you can switch the application into custom
time mode

## Dependencies

world-wall-clock is a Python 3 application that relies on
[urwid](https://urwid.org/) as its terminal widget toolkit,
[xdg-base-dirs](https://github.com/srstevenson/xdg-base-dirs) to determine where
to keep the application configuration, and
[tzdata](https://github.com/python/tzdata) to provide backup timezone
information if this is not already present on the system.

## Development

world-wall-clock uses [Poetry](https://python-poetry.org/) to manage builds and
dependencies. The Python code is formatted using
[Black](https://github.com/psf/black).
