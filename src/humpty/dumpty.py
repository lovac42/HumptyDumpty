# -*- coding: utf-8 -*-
# Copyright 2019-2020 Lovac42
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Support: https://github.com/lovac42/HumptyDumpty


from anki import schedv2
from aqt import mw
from anki.utils import intTime

from .const import ADDON_NAME
from .config import Config

conf = Config(ADDON_NAME)


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

    if conf.get("merge_and_remap_stat_buttons", True):
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

    if conf.get("merge_and_remap_stat_buttons", True):
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

# Using assignment instead of wrap to prevent unknown conflicts.
schedv2.Scheduler.moveToV1 = moveToV1
schedv2.Scheduler.moveToV2 = moveToV2
