# {{LICENCE}}

from recordclass.test.test_memoryslots import *
from recordclass.test.test_recordclass import *
from recordclass.test.test_structclass import *
from recordclass.test.test_arrayclass import *

import sys
_PY36 = sys.version_info[:2] >= (3, 6)

if _PY36:
    from recordclass.test.typing.test_recordclass import *
    from recordclass.test.typing.test_structclass import *

def test_all():
    import unittest
    unittest.main(verbosity=2)
