# Humpty Dumpty
Convert between V1 and V2 but keep learning cards intact.  

(Except filtered decks in V1)

## Warning!!
Backup! Backup! Backup!


## merge_and_remap_stat_buttons:
true or false, Anki's default is true. Turn this off if you don't want your grades merged.


### Grade Merging Explained:
V1 uses 2/3/4 buttons, while V2 uses 4 buttons.

During upgrade, V1 button2 (good) is remapped to V2 button3 (good). And the reverse when you downgrade. If you are playing around switching back and forth between V1 and V2, V2 and V1, then your buttons are merged into one big stack. This remapping screws up the stats as it merges hard with good grades.

Setting "merge_and_remap_stat_buttons" to false will also allow you to switch between V1 and V2 without screwing up your stats.

