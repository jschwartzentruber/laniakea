'''
Tests

@author:     Christian Holler (:decoder)

@license:

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

@contact:    choller@mozilla.com
'''

from collections import OrderedDict
import unittest

from laniakea import LaniakeaCommandLine

test_macros = OrderedDict()
test_macros["FOO"] = "FOOVAL"
test_macros["BAR"] = "BARVAL"
test_macros["BAZ"] = "BAZVAL"

userdata_test_macros = """
#!/bin/bash

# This is a sample userdata script with macros

FOO="@FOO@"
BAR=@BAR@
BAZ=some@BAZ@thing

# End
"""

userdata_test_macros_expected = """
#!/bin/bash

# This is a sample userdata script with macros

FOO="FOOVAL"
BAR=BARVAL
BAZ=someBAZVALthing

# End
"""

userdata_test_macro_export = """
#!/bin/bash

# This is a sample userdata script with macro export

@!all_macros_export@

# End
"""

userdata_test_macro_export_expected = """
#!/bin/bash

# This is a sample userdata script with macro export

export FOO='FOOVAL'
export BAR='BARVAL'
export BAZ='BAZVAL'

# End
"""

class LaniakeaTestMacroReplacement(unittest.TestCase):
    def runTest(self):
        self.assertEqual(LaniakeaCommandLine.handle_tags(userdata_test_macros, test_macros), userdata_test_macros_expected)

class LaniakeaTestMacroListExport(unittest.TestCase):
    def runTest(self):
        self.assertEqual(LaniakeaCommandLine.handle_tags(userdata_test_macro_export, test_macros), userdata_test_macro_export_expected)
