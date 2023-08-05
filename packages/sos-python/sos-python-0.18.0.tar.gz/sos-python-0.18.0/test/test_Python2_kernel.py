#!/usr/bin/env python3
#
# Copyright (c) Bo Peng and the University of Texas MD Anderson Cancer Center
# Distributed under the terms of the 3-clause BSD License.

#
# NOTE: for some namespace reason, this test can only be tested using
# nose.
#
# % nosetests test_kernel.py
#
#
import os
import unittest
from ipykernel.tests.utils import execute, wait_for_idle, assemble_output
from sos_notebook.test_utils import sos_kernel, get_result, clear_channels

try:
    import feather
    feather
    with_feather = True
except ImportError:
    with_feather = False

class TestPython2Kernel(unittest.TestCase):
    #
    # Beacuse these tests would be called from sos/test, we
    # should switch to this directory so that some location
    # dependent tests could run successfully
    #
    def setUp(self):
        self.olddir = os.getcwd()
        if os.path.dirname(__file__):
            os.chdir(os.path.dirname(__file__))

    def tearDown(self):
        os.chdir(self.olddir)

    def testPutGet(self):
        with sos_kernel() as kc:
            iopub = kc.iopub_channel
            # create a data frame

            execute(kc=kc, code='''
null_var = None
num_var = 123
logic_var = True
logic_arr_var = [True, False, True]
char_var = '123'
char_arr_var = ['1', '2', '3']
list_var = [1, 2, '3']
dict_var = dict(a=1, b=2, c='3')
set_var = {1, 2, '3'}

import numpy
num_arr_var = numpy.array([1, 2, 3])
mat_var = numpy.matrix([[1,2],[3,4]])
import pandas as pd
import numpy as np
arr = np.random.randn(1000)
arr[::10] = np.nan
df_var = pd.DataFrame({'column_{0}'.format(i): arr for i in range(10)})
''')
            clear_channels(iopub)
            #
            execute(kc=kc, code='''
%use Python2
%get null_var num_var num_arr_var logic_var logic_arr_var char_var char_arr_var mat_var set_var list_var dict_var df_var
%dict -r
%put null_var num_var logic_var logic_arr_var char_var char_arr_var set_var list_var dict_var
''')
            wait_for_idle(kc)
            execute(kc=kc, code="%use sos")
            wait_for_idle(kc)
            execute(kc=kc, code="%dict null_var num_var logic_var logic_arr_var char_var char_arr_var set_var list_var dict_var")
            res = get_result(iopub)
            self.assertEqual(res['null_var'], None)
            self.assertEqual(res['num_var'], 123)
            self.assertEqual(res['logic_var'], True)
            self.assertEqual(res['logic_arr_var'], [True, False, True])
            self.assertEqual(res['char_var'], '123')
            self.assertEqual(res['char_arr_var'], ['1', '2', '3'])
            self.assertEqual(res['list_var'], [1,2,'3'])
            self.assertEqual(res['dict_var'], {'a': 1, 'b': 2, 'c': '3'})


    def testDirectExchangeWithPython2(self):
        '''Test getting data from another instance of Python3 (bypassing sos)'''
        with sos_kernel() as kc:
            iopub = kc.iopub_channel
            # create a data frame
            execute(kc=kc, code='''
%use Python2
ddvar = 3
''')
            wait_for_idle(kc)
            #
            execute(kc=kc, code='''
%use P3 -l Python2
%get ddvar --from Python2
''')
            wait_for_idle(kc)
            execute(kc=kc, code="print(ddvar)")
            stdout, _ = assemble_output(iopub)
            self.assertEqual(stdout.strip(), '3', 'Expect {}'.format(stdout))
            execute(kc=kc, code="%use sos")
            wait_for_idle(kc)
            execute(kc=kc, code="%dict -k")
            res = get_result(iopub)
            self.assertTrue('ddvar' not in res)

if __name__ == '__main__':
    unittest.main()
