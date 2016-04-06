#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def testing():
        assert True

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        #from fycotcp.fycotcp import Pyco
        #from fycotcp.fycotcp import DeviceInfo
        #from fycotcp.fycotcp import Socket
        #from fycotcp.picotcpadapter import PicoTCPAdapter
    else:
        #from ..fycotcp.fycotcp import Pyco
        #from ..fycotcp.fycotcp import DeviceInfo
        #from ..fycotcp.fycotcp import Socket
        #from ..fycorcp.picotcpadapter import PicoTCPAdapter
        pass

    unittest.main()


#if __name__ == "__main__":
#   main(sys.argv[1:])

