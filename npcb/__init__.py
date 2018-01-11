import numpy as np
import re
import ast

__all__ = ["array"]


def _tkinter_wrapper(Tk):
    def inner():
        t = Tk()
        cb = t.clipboard_get()
        t.withdraw()
        t.destroy()
        return cb
    return inner


class _Clipboard(object):
    def __init__(self):
        """Try to load a function that is able to read the clipboard.

        Probably the most lightweight is pyperclip so try that one first, if
        that's not available try pandas (because it's a very common package)
        and finally try tkinter which needs a Tk() instance which will open
        a window (and is slower).
        """
        try:
            from pyperclip import paste
        except ImportError:
            pass
        else:
            self.get = paste
            return

        try:
            from pandas.io.clipboard import clipboard_get
        except ImportError:
            pass
        else:
            self.get = clipboard_get
            return

        try:
            from tkinter import Tk  # python 3
        except ImportError:
            pass
        else:
            self.get = _tkinter_wrapper(Tk)
            return

        try:
            from Tkinter import Tk  # python 2
        except ImportError:
            pass
        else:
            self.get = _tkinter_wrapper(Tk)
            return

        raise ImportError('npcb needs one of pandas/pyperclip/tkinter installed'
                          'to read from the clipboard')

# Create an instance of the object because we don't need to initialize it more
# than once.
_Clipboard = _Clipboard()

def array():
    """Returns the current clipboard content as NumPy array.
    """
    inp = _Clipboard.get()
    inp = inp.strip()
    # if it starts with "array(" we just need to remove the
    # leading "array(" and remove the optional ", dtype=xxx)"
    if inp.startswith('array('):
        inp = re.sub(r'^array\(', '', inp)
        dtype = re.search(r', dtype=(\w+)\)$', inp)
        if dtype:
            return np.array(ast.literal_eval(inp[:dtype.start()]), dtype=dtype.group(1))
        else:
            return np.array(ast.literal_eval(inp[:-1]))
    else:
        # In case it's the string representation it's a bit harder.
        # We need to remove all spaces between closing and opening brackets
        inp = re.sub(r'\]\s+\[', '],[', inp)
        # We need to remove all whitespaces following an opening bracket
        inp = re.sub(r'\[\s+', '[', inp)
        # and all leading whitespaces before closing brackets
        inp = re.sub(r'\s+\]', ']', inp)
        # replace all remaining whitespaces with ","
        inp = re.sub(r'\s+', ',', inp)
        return np.array(ast.literal_eval(inp))
