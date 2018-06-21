# -*- coding: utf-8 -*-
"""

MIT License
Copyright (c) 2017-2018, Germán Méndez. Bravo (Kronuz). All Rights Reserved.

"""
from __future__ import absolute_import, print_function

VERSION = "1.0.1"

import sublime

from .stacktraces import StackTraces


def plugin_loaded():
    global tracer
    try:
        if tracer:
            try:
                tracer.stop()
            except RuntimeWarning:
                pass
    except NameError:
        pass
    tracer = StackTraces(traceback_path='/tmp/SublimeStackTracer{ext}', traceback_interval=5)
    tracer.start()


# ST3 features a plugin_loaded hook which is called when ST's API is ready.
#
# We must therefore call our init callback manually on ST2. It must be the last
# thing in this plugin (thanks, beloved contributors!).
if int(sublime.version()) < 3000:
    plugin_loaded()
