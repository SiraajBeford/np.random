from distutils import extension
import pandas as pd
import numpy as np
import os
import data
import glob

class DataCombiner:
    
    def __init__(self):
        self.data_dir = os.getcwd() + "\data"

    def find_valid_input_data(self):
        os.chdir(self.data_dir)
        extension = 'csv'
        return glob.glob('*.{}'.format(extension))    

    def find_valid_input_paths(self):
        valid_inputs =  self.find_valid_input_data()
        valid_input_paths = []
        for i in valid_inputs:
            valid_input_paths.append(self.data_dir + "\\" + i)
        return valid_input_paths

    def segment_data_in_frame(self):
        schedule_list = []
        valid_files = self.find_valid_input_paths()
        for i in valid_files:
            schedule_list.append(pd.read_csv(i))
        return schedule_list

class DataCleaner(DataCombiner):

    def __init__(self):
        super(DataCleaner, self).__init__()
        
    def report_original_data(self):
        print(self.segment_data_in_frame())

    def clean(self):
        uncleaned_data_list = self.segment_data_in_frame()
        return uncleaned_data_list
