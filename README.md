# GGDOT Data Hack

This is a set of tools to help you play with nutrition and emissions data from the UK diet. It is based on the UK National Diet and Nutrition Survey (NDNS) combined with greenhouse gas emissions data (see the CO2eRef field for the source of each emissions estimate).

To use this repository you first need to download the NDNS data (accepting their licences) - see the README_PREHACK file for information on how to do this. 

If you have low system memory or otherwise want to avoid executing the computationally intensive first cell of the notebook that makes the combined csv files, then do the following (replacing "[path/to...]" with your NDNS data directory):

python3
import ndns_to_csv as nc
nc.mash_files  (ndns_dir  =  '[path/to...]/UKDA-6533-tab/tab/', tag  =  '_20180612')"

or EDIT the very last line of ndns_to_csv.py and then TYPE 'python3 ndns_to_csv.py' at the command line

Happy hacking! 

Please remember that in addition to the licence on this toolkit, you are bound by the licences for each dataset you use. These include:
1) The National Diet and Nutrition Survey hosted by the UK National Data Service
2) Greenhouse gas emissions data from Intake24 https://intake24.co.uk/info/open-source#content 

