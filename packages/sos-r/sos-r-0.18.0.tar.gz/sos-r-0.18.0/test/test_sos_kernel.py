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
import sys
import unittest
from ipykernel.tests.utils import execute, wait_for_idle
from sos_notebook.test_utils import sos_kernel, get_result, get_display_data, get_std_output

class TestSoSKernel(unittest.TestCase):
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

    def testMagicUse(self):
        with sos_kernel() as kc:
            iopub = kc.iopub_channel
            execute(kc=kc, code="%use R0 -l sos_r.kernel:sos_R -c #CCCCCC")
            _, stderr = get_std_output(iopub)
            self.assertEqual(stderr, '')
            execute(kc=kc, code="%use R1 -l sos_r.kernel:sos_R -k ir -c #CCCCCC")
            _, stderr = get_std_output(iopub)
            self.assertEqual(stderr, '')
            execute(kc=kc, code="%use R2 -k ir")
            _, stderr = get_std_output(iopub)
            self.assertEqual(stderr, '')
            execute(kc=kc, code="a <- 1024")
            wait_for_idle(kc)
            execute(kc=kc, code="a")
            res = get_display_data(iopub)
            self.assertEqual(res, '[1] 1024')
            execute(kc=kc, code="%use R3 -k ir -l R")
            _, stderr = get_std_output(iopub)
            self.assertEqual(stderr, '')
            execute(kc=kc, code="a <- 233")
            wait_for_idle(kc)
            execute(kc=kc, code="a")
            res = get_display_data(iopub)
            self.assertEqual(res, '[1] 233')
            execute(kc=kc, code="%use R2 -c red")
            _, stderr = get_std_output(iopub)
            self.assertEqual(stderr, '')
            execute(kc=kc, code="a")
            res = get_display_data(iopub)
            self.assertEqual(res, '[1] 1024')
            execute(kc=kc, code="%use sos")
            wait_for_idle(kc)

    def testSubKernel(self):
        with sos_kernel() as kc:
            iopub = kc.iopub_channel
            execute(kc=kc, code="%use R")
            _, stderr = get_std_output(iopub)
            self.assertEqual(stderr, '')
            execute(kc=kc, code="a <- 1024")
            wait_for_idle(kc)
            execute(kc=kc, code="a")
            res = get_display_data(iopub)
            self.assertEqual(res, '[1] 1024')
            execute(kc=kc, code="%use sos")
            wait_for_idle(kc)

    def testMagicPut(self):
        with sos_kernel() as kc:
            iopub = kc.iopub_channel
            execute(kc=kc, code="%use R")
            _, stderr = get_std_output(iopub)
            self.assertEqual(stderr, '')
            execute(kc=kc, code="a <- 1024")
            wait_for_idle(kc)
            execute(kc=kc, code="%put a")
            wait_for_idle(kc)
            #execute(kc=kc, code="%put __k_k")
            #wait_for_idle(kc)
            execute(kc=kc, code="%use sos")
            wait_for_idle(kc)
            execute(kc=kc, code="a")
            res = get_result(iopub)
            self.assertEqual(res, 1024)
            # strange name
            execute(kc=kc, code="%use R")
            wait_for_idle(kc)
            execute(kc=kc, code=".a.b <- 22")
            wait_for_idle(kc)
            execute(kc=kc, code="%put .a.b")
            wait_for_idle(kc)
            execute(kc=kc, code="%use sos")
            wait_for_idle(kc)
            execute(kc=kc, code="_a_b")
            res = get_result(iopub)
            self.assertEqual(res, 22)
            #
            # test to yet another kernel
            #
            execute(kc=kc, code="%put --to Python3 _a_b")
            wait_for_idle(kc)
            execute(kc=kc, code="%use Python3")
            wait_for_idle(kc)
            execute(kc=kc, code="_a_b")
            res = get_result(iopub)
            self.assertEqual(res, 22)
            #
            execute(kc=kc, code="kkk = 'ast'")
            wait_for_idle(kc)
            execute(kc=kc, code="%put --to R kkk")
            res = get_result(iopub)
            execute(kc=kc, code="%use R")
            wait_for_idle(kc)
            execute(kc=kc, code="kkk <- paste0(kkk, '1')")
            wait_for_idle(kc)
            execute(kc=kc, code="%put --to Python3 kkk")
            wait_for_idle(kc)
            execute(kc=kc, code="%use Python3")
            wait_for_idle(kc)
            execute(kc=kc, code="kkk")
            res = get_result(iopub)
            self.assertEqual(res, 'ast1')
            execute(kc=kc, code="%use sos")
            wait_for_idle(kc)


    def testMagicGet(self):
        with sos_kernel() as kc:
            iopub = kc.iopub_channel
            execute(kc=kc, code="a = 1025")
            wait_for_idle(kc)
            execute(kc=kc, code="_b_a = 22")
            wait_for_idle(kc)
            execute(kc=kc, code="%use R")
            _, stderr = get_std_output(iopub)
            self.assertEqual(stderr, '')
            execute(kc=kc, code="%get a")
            wait_for_idle(kc)
            execute(kc=kc, code="a")
            res = get_display_data(iopub)
            self.assertEqual(res, '[1] 1025')
            execute(kc=kc, code="b <- 122\nc<-555")
            wait_for_idle(kc)
            #
            execute(kc=kc, code="%get _b_a")
            wait_for_idle(kc)
            execute(kc=kc, code=".b_a")
            res = get_display_data(iopub)
            self.assertEqual(res, '[1] 22')
            execute(kc=kc, code="%use sos")
            wait_for_idle(kc)
            #
            # get from a sub kernel
            execute(kc=kc, code="%get --from R b")
            wait_for_idle(kc)
            execute(kc=kc, code="b")
            res = get_result(iopub)
            self.assertEqual(res, 122)
            # get from a third kernel
            execute(kc=kc, code="%use Python3")
            wait_for_idle(kc)
            execute(kc=kc, code="%get --from R c")
            wait_for_idle(kc)
            execute(kc=kc, code="c")
            res = get_result(iopub)
            self.assertEqual(res, 555)
            execute(kc=kc, code="%use sos")
            wait_for_idle(kc)


    def testAutoSharedVars(self):
        with sos_kernel() as kc:
            iopub = kc.iopub_channel
            execute(kc=kc, code="sos_null = None")
            wait_for_idle(kc)
            execute(kc=kc, code="sos_num = 123")
            wait_for_idle(kc)
            execute(kc=kc, code="%use R")
            wait_for_idle(kc)
            execute(kc=kc, code="sos_num")
            res = get_display_data(iopub)
            self.assertEqual(res, '[1] 123')
            execute(kc=kc, code="sos_num = sos_num + 10")
            wait_for_idle(kc)
            execute(kc=kc, code="%use sos")
            wait_for_idle(kc)
            execute(kc=kc, code="sos_num")
            res = get_display_data(iopub)
            self.assertEqual(res, '133')

    def testNewKernel(self):
        '''Test magic use to create new kernels'''
        with sos_kernel() as kc:
            iopub = kc.iopub_channel
            # create a data frame
            execute(kc=kc, code='%use R2 -l R')
            wait_for_idle(kc)
            execute(kc=kc, code='%use R3 -l R -c black')
            wait_for_idle(kc)
            execute(kc=kc, code='%use R4 -k ir -l R -c green')
            wait_for_idle(kc)
            execute(kc=kc, code='%use R4 -c cyan')
            wait_for_idle(kc)
            execute(kc=kc, code='%with R5 -l sos_r.kernel:sos_R -c default')
            wait_for_idle(kc)
            execute(kc=kc, code='%with R6 -l unknown -c default')
            _, stderr = get_std_output(iopub)
            self.assertTrue('Failed to switch' in stderr, 'expect error {}'.format(stderr))
            execute(kc=kc, code="%use sos")
            wait_for_idle(kc)

    def testWith(self):
        '''Test magic with'''
        with sos_kernel() as kc:
            iopub = kc.iopub_channel
            # create a data frame
            execute(kc=kc, code='var = [1, 2, 3, 4]')
            wait_for_idle(kc)
            execute(kc=kc, code='%with R -i var -o m\nm=mean(var)')
            wait_for_idle(kc)
            execute(kc=kc, code="%dict m")
            res = get_result(iopub)
            self.assertEqual(res['m'], 2.5)
            execute(kc=kc, code="%use sos")
            wait_for_idle(kc)


if __name__ == '__main__':
    unittest.main()
