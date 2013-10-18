#!/usr/bin/python

import ctypes
import os

from datatypes import XScreenSaverInfo

xlib = ctypes.cdll.LoadLibrary( 'libX11.so.6')
xss = ctypes.cdll.LoadLibrary( 'libXss.so.1')

def idle_time_ms(display=None):

    '''Return the current X idle time in milliseconds.'''

    global xlib
    global xss

    if display is None:
        display = os.environ.get('DISPLAY')

    assert display is not None

    dpy = xlib.XOpenDisplay( os.environ['DISPLAY'])
    root = xlib.XDefaultRootWindow( dpy)
    xss.XScreenSaverAllocInfo.restype = ctypes.POINTER(XScreenSaverInfo)
    xss_info = xss.XScreenSaverAllocInfo()
    xss.XScreenSaverQueryInfo( dpy, root, xss_info)

    return xss_info.contents.idle

