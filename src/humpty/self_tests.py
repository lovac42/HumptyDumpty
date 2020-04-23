# -*- coding: utf-8 -*-
# Copyright 2020 Lovac42
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Support: https://github.com/lovac42/HumptyDumpty


# This only tests for correct wrapping.
# It does not account for other changes.


from anki.hooks import addHook
from anki.utils import namedtmp
from anki.storage import Collection


class Test:
    def reset(self):
        self.state = 0

    def setTestState(self, s):
        self.state = s


run_test = Test()


def testWrap():
    from anki.schedv2 import Scheduler
    path = namedtmp("humpty_dumpty_tmp.anki2")
    dummy_col = Collection(path)
    v2_sched = Scheduler(dummy_col)

    try:
        run_test.reset()
        v2_sched.moveToV1()
        assert run_test.state == 1, "The addon HumptyDumpty was not patched correctly. Error code 1"

        run_test.reset()
        v2_sched.moveToV2()
        assert run_test.state == 2, "The addon HumptyDumpty was not patched correctly. Error code 2"

        run_test.setTestState(-1) #for pref menu
        # print("HumptyDumpty was patched correctly.")

    finally:
        dummy_col.close()
        del dummy_col


addHook("profileLoaded", testWrap)
