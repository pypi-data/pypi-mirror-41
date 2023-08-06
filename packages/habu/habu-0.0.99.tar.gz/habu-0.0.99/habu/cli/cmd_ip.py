#!/usr/bin/env python3

import click

from habu.lib.ip import get_ip


@click.command()
def cmd_ip():
    """Print your current public IP based on the response from https://api.ipify.org

    Example:

    \b
    $ habu.ip
    182.26.32.246"""

    print(get_ip())


if __name__ == '__main__':
    cmd_ip()
