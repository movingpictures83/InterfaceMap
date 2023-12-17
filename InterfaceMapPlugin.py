import sys

from dataset import PISToN_dataset
import os
import numpy as np

class InterfaceMapPlugin:
    def input(self, inputfile):
       self.GRID_DIR = inputfile#'data/masif_test/prepare_energies_16R/07-grid/'
    def run(self):
        pass
    def output(self, outputfile):
       ppi_list = os.listdir(self.GRID_DIR)
       ppi_list = [x.split('.npy')[0] for x in ppi_list if 'resnames' not in x and '.ref' not in x]

       labels = [0 if 'neg' in x else 1 for x in ppi_list]


       print(f"Extracted {len(ppi_list)} complexes.")
       print(f"{np.sum(labels)} acceptable and {len(labels) -np.sum(labels) } incorrect.")
       masif_test_dataset = PISToN_dataset(self.GRID_DIR, ppi_list)
       masif_test_dataset.vis_patch('1YY9-pos_A_D', html_path=outputfile+".patch.html")

       outfile2 = open(outputfile+".labels.txt", 'w')
       for label in labels:
           outfile2.write(str(label)+"\n")

