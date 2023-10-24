# selective-submodule-cloner
A python script which selectively clones submodules even if they are nested

# setup
Clone a repository which has submodules, inside of `selected_submodules.json` add the paths of the submodules you want to initialize and update. If the submodules are nested, put them in an order that would not result in error if they are initialized and updated in the top to bottom order in `selected_submodules.json`, then run `python main.py` and your submodules should there.
