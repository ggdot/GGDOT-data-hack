# Greenhouse Gas and Dietary choices Open-source Toolkit

To use this repository you first need to download the NDNS data (accepting their licences) - see the README_PREHACK file for information on how to do this. 

If you have low system memory or otherwise want to avoid executing the computationally intensive first cell of the notebook that makes the combined csv files, then do the following (replacing "[path/to...]" with your NDNS data directory):

python3
import ndns_to_csv as nc
nc.mash_files  (ndns_dir  =  '[path/to...]/UKDA-6533-tab/tab/', tag  =  '_20180612')"

or EDIT the very last line of ndns_to_csv.py and then TYPE 'python3 ndns_to_csv.py' at the command line

