# argparser

import argparse


class args(object):
    _prog_name: str = "Cowboys"
    _desc: str = ""
    _epilog: str = ""

    def __init__(self) -> None:
        self._parser = argparse.ArgumentParser(
            prog=self._prog_name,
            description=self._desc,
            epilog=self._epilog)
        self._parser.add_argument('-n', '--number', default=5)
        self.args: argparse.Namespace = self._parser.parse_args()
