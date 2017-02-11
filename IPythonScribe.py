from __future__ import print_function

import io
import os

from IPython.core.magic import (Magics, magics_class, line_magic)
from IPython import get_ipython


@magics_class
class IPythonScribe(Magics):

    def __init__(self, shell, filename, separator=None):
        super(IPythonScribe, self).__init__(shell)
        self.filename = filename
        self.separator = separator

    @line_magic
    def scr(self, cells):
        "my line magic"
        self.write_separator()
        if not cells:
            previous_cell = str(self.shell.execution_count - 1)
            cells = previous_cell
        save_command = ('save -a {filename} {cells}'
                        .format(filename=self.filename, cells=cells))
        self.shell.magic(save_command)

    def write_separator(self):
        if self.cell_divider is not None and os.path.isfile(self.filename):
            with io.open(self.filename, 'a', encoding='utf-8') as f:
                f.write(self.cell_divider)
                # make sure we end on a newline
                if not self.cell_divider.endswith(u'\n'):
                    f.write(u'\n')


def start(filename, separator=None):
    """Start using IPythonScribe to append to given filename"""
    ip = get_ipython()
    magic = IPythonScribe(ip, filename, separator=separator)
    ip.register_magics(magic)
