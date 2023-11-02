# Extra type annotations for world-wall-clock dependencies

This subdirectory contains stub files providing type annotations for
dependencies that are not fully compliant with mypy type-checking (presently
just urwid). The stub files were generated with mypy's `stubgen` tool and
manually tweaked where necessary to provide more complete type information
about methods used in world-wall-clock. Wherever these stub files themselves
generated errors in mypy, they have been exempted from mypy checks altogether
using `# mypy: ignore-errors` at the top of the file, because the goal of these
stub files is to provide more thorough type-checking for world-wall-clock, not
to resolve type inconsistencies in external libraries.

urwid's developers have been gradually annotating its types with the goal of
full compliance with mypy checks, so these stubs may become unnecessary in the
future.