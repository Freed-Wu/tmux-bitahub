r"""This module can be called by
`python -m <https://docs.python.org/3/library/__main__.html>`_.
"""
from shlex import split
from subprocess import check_output  # nosec: B404
from typing import Callable

from . import RESOURCE, get_gpu_status

BEGIN = "#{bitahub_status_"
END = "}"


def do_interpolation(option: str) -> str:
    r"""Do interpolation.

    :param option:
    :type option: str
    :rtype: str
    """
    resource = option.lstrip(BEGIN).rstrip(END)
    return get_gpu_status(resource)  # type: ignore


def update_tmux_option(
    option: str,
    command: str,
    do_interpolation: Callable[[str], str] = do_interpolation,
) -> None:
    r"""Update tmux option.

    :param option:
    :type option: str
    :param command:
    :type command: str
    :param do_interpolation:
    :type do_interpolation: Callable[[str], str]
    :rtype: None
    """
    value = check_output(  # nosec: B603
        split("tmux show-option -gqv") + [option], universal_newlines=True
    )
    value = value.replace(command, do_interpolation(command))
    check_output(split("tmux set-option -gq") + [option, value])  # nosec: B603


def main() -> None:
    r"""Run main function.

    :rtype: None
    """
    for option in ["status-left", "status-right"]:
        for resource in RESOURCE.__args__:  # type: ignore
            command = BEGIN + resource + END
            update_tmux_option(option, command)


if __name__ == "__main__":
    main()
