# Humpty Dumpty
Keeps learning cards status while converting between V1-V2 or importing apkgs.

(except filtered decks in V1)


## About:
This addon converts between V1 and V2 while keeping learning cards intact. There should be no problems upgrading from V1 to V2, however, downgrading back to V1 from V2 requires some missing values to be recalculated.

If you're not playing around, then you only need to use it once, from V1 to V2 and can safely remove this addon. (Hence the title...)

Please read the source code first before deciding if this is the right addon for you.

Update:
It turns out that V2 has poor support for apkg with scheduling info. A user is asked to downgrade to V1 before importing/exporting a shared deck. So this addon might turn out more useful than I thought.

Update2:
Ironically, importing and exporting V2 shared decks requires down converting to V1. This addon actually helps to keep the learning status. Definitely more useful than I thought.


## Instruction:
Preferences > Experimental V2 scheduler


## Filtered Decks in V1:
Filtered decks are emptied first before converting to V2. In V1, all learning cards in a filtered deck will loose their learning status when returning to the original deck.


## Naming:
Humpty Dumpty has been used to demonstrate the second law of thermodynamics. In the same way, this conversion is lossy, the odue value will never return to the original form. But it is not used in most cases except by filtered decks.
