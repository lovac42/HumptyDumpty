# Humpty Dumpty
Keeps learning cards status while converting between V1-V2 or importing apkgs.

(except filtered decks in V1)


## Naming:
Humpty Dumpty has been used to demonstrate the second law of thermodynamics. In the same way, this conversion is lossy, the odue value will never return to the original form. But it is not used in most cases except by filtered decks.


## About:
This addon converts between V1 and V2 while keeping learning cards intact. There should be no problems upgrading from V1 to V2, however, downgrading back to V1 from V2 requires some missing values to be recalculated.

Update:
It turns out that V2 has poor support for apkg with scheduling info. A user is asked to downgrade to V1 before importing/exporting a shared deck. So this addon might turn out more useful than I thought.

Update2:
Ironically, importing and exporting V2 shared decks requires down converting to V1. This addon actually helps to keep the learning status. Definitely more useful than I thought.


### Grade Merging Explained:
V1 uses 2/3/4 buttons, while V2 uses 4 buttons.

During upgrade, V1 button2 (good) is remapped to V2 button3 (good). And the reverse when you downgrade. If you are playing around switching back and forth between V1 and V2, V2 and V1, then your buttons are merged into one big stack. This remapping screws up the stats as it merges hard with good grades.

Setting "merge_and_remap_stat_buttons" to false will also allow you to switch between V1 and V2 without screwing up your stats.

<img src="https://github.com/lovac42/HumptyDumpty/blob/master/screenshots/merged.png?raw=true">  


## Instruction:
Preferences > Experimental V2 scheduler


## Filtered Decks in V1:
Filtered decks are emptied first before converting to V2. In V1, all learning cards in a filtered deck will loose their learning status when returning to the original deck.
