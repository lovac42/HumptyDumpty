# -*- coding: utf-8 -*-
# Copyright 2019-2020 Lovac42
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Support: https://github.com/lovac42/HumptyDumpty


import aqt.preferences
from anki.lang import _
from anki.hooks import wrap

from .dumpty import conf


def setupUi(self, Preferences):
    msg = self.newSched.text()
    tf = conf.get("merge_and_remap_stat_buttons", True)
    msg += "  [button_remap = %s]" % tf
    self.newSched.setText(_(msg))


aqt.forms.preferences.Ui_Preferences.setupUi = wrap(
    aqt.forms.preferences.Ui_Preferences.setupUi, setupUi, "after"
)
