# durham-hacknight-20180612
Code for Durham GGDOT Hacknight 18 October 2018

Before the hacknight, please download the NDNS data - if you haven't done this yet then please read the README_PREHACK file.

If you have low system memory or otherwise want to avoid executing the computationally intensive first cell of the notebook that makes the combined csv files, then do the following (replacing "[path/to...]" with your NDNS data directory):

python3
import ndns_to_csv as nc
nc.mash_files  (ndns_dir  =  '[path/to...]/UKDA-6533-tab/tab/', tag  =  '_20180612')"

or EDIT the very last line of ndns_to_csv.py and then TYPE 'python3 ndns_to_csv.py' at the command line

