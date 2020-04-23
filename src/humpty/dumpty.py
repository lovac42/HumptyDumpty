# -*- coding: utf-8 -*-
# Copyright 2019-2020 Lovac42
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Support: https://github.com/lovac42/HumptyDumpty
# Version: 0.0.3


# Anki maps button2 to good for learning cards on V1.
# On V2, button2 is mapped to hard.

# If you are playing around switching back and forth
# between V1 and V2, V2 and V1, then your buttons
# are merged into one big stack.

# For alternative schedulers addons such as:
# Plan9, Plan0, or PimsEmu, they are mapped correctly to
# 4 buttons. So this remapping screws up the stats for
# alternative schedulers, as it merges hard with good grades.

# If you are using mixed schedulers, like I do,
# you'll need to separate and export each deck into
# separate profiles, upgrade each separately, then
# import these decks back into one.


# Turn this off if you don't want your grades merged.

MERGE_AND_REMAP_BUTTONS = False  #Anki's Default is True

# Setting this to false will also allow you to switch
# between V1 and V2 without screwing up your stats.
# But when you are ready to make the switch
# and you are not using alternative schedulers,
# make sure to turn this back on.





from anki import schedv2
from aqt import mw
from anki.utils import intTime


def moveToV1(sched):
    # For old versions of anki before 2.1.16
    mw.col.clearUndo()

    # All cards return to their original deck
    sched._emptyAllFiltered()

    # Change type 3 to 2, recalculate odue
    updateAllFromLearning(sched, toSchedVer=2)

    # Convert queue -3 to -2
    sched._moveManuallyBuried()

    # Convert suspended learning cards to new/review
    # WARNING: Learning status is lost for suspended cards.
    sched._resetSuspendedLearning()

    # Anki defaults to True
    if MERGE_AND_REMAP_BUTTONS:
        # This migrates btn4 to btn3.
        # It condenses btn3 with btn2!!
        # If you also have btn2 data, they are merged with btn3.
        sched._remapLearningAnswers("ease=ease-1 where ease in (3,4)")


def moveToV2(sched):
    # For old versions of anki before 2.1.16
    mw.col.clearUndo()

    # Warning:
    # Learning cards in V1 filtered decks will
    # loose their learning status.
    sched._emptyAllFiltered()

    # Change type 2 to 3, remove odue
    updateAllFromLearning(sched, toSchedVer=1)

    # Anki defaults to True
    if MERGE_AND_REMAP_BUTTONS:
        #This migrates btn2 to btn3, and btn3 to btn4
        sched._remapLearningAnswers("ease=ease+1 where ease in (2,3)")



def updateAllFromLearning(sched, toSchedVer=2):
    """
        Converts type 2 to type 3
        V2 sets odue = 0
        V1 sets odue = due at the time a card lapses
    """

    if toSchedVer==1: #to V1
        # LOSSY ODUE:
        # The real odue values was lost.
        # We calculate a new number in case
        # the user bury/suspends the card.
        # But otherwise, this value is useless.
        odue=", odue=ivl+%d"%sched.today
        type=2

    else: #to V2
        odue=", odue=0"
        type=3

    sched.col.db.execute("""
update cards set
type = %d, mod = %d, usn = %d %s
where queue in (1,3) and type in (2,3)
""" % (type, intTime(), sched.col.usn(), odue))




# ========= Wrap ================
schedv2.Scheduler.moveToV1 = moveToV1
schedv2.Scheduler.moveToV2 = moveToV2




# ========= GUI ================
import aqt.preferences
from anki.lang import _
from anki.hooks import wrap

def setupUi(self, Preferences):
    msg="Experimental V2 scheduler \
[button_remap = %s]"%MERGE_AND_REMAP_BUTTONS
    self.newSched.setText(_(msg))

aqt.forms.preferences.Ui_Preferences.setupUi = wrap(aqt.forms.preferences.Ui_Preferences.setupUi, setupUi, "after")
