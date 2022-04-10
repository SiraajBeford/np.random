from distutils import extension
from matplotlib.pyplot import axis
import pandas as pd
import numpy as np
import os
import data
import glob
from datetime import datetime

class DataCombiner:
    
    def __init__(self):
        self.main_path = os.getcwd()
        self.data_dir = os.getcwd() + "\data"
<<<<<<< HEAD
        self.file_names = []
=======
        self.used_files = []
>>>>>>> 4961fce386261e39daf87c8a068d7a7d64ea1429

    def find_valid_input_data(self):
        os.chdir(self.data_dir)
        extension = 'csv'
        self.used_files = glob.glob('*.{}'.format(extension))    
        return self.used_files

    def find_valid_input_paths(self):
        valid_inputs =  self.find_valid_input_data()
        valid_input_paths = []
        for i in valid_inputs:
            valid_input_paths.append(self.data_dir + "\\" + i)
            self.file_names.append(i.replace('.csv',''))
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
        self.uncleaned_data_list = self.segment_data_in_frame()
        self.cleaned_data_list = []
        self.export_schedules = {}
        self.export_path_for_schedules = self.main_path + '\\' + 'output' + '\\' + 'csv'

    def clean_all_schedules(self):
        for schedule in self.uncleaned_data_list:
            self.cleaned_data_list.append(self.clean_schedule(schedule))

    def clean_schedule(self,schedule):
        schedule = self.clean_empty_rows(schedule)
        schedule = self.remove_if_empty_size(schedule)
        schedule = self.clean_units(schedule)
        schedule = self.clean_area_and_surface_area_zero(schedule)

        return schedule

    def clean_empty_rows(self, schedule):
        empty_row_indices = schedule[schedule.isna().all(axis=1)].index
        schedule = schedule.drop(index=empty_row_indices)
        return schedule

    def clean_units(self, schedule):
        schedule["Area"] = schedule["Area"].astype(str)
        schedule["Area"] = schedule["Area"].str.replace(" m²","")
        schedule["Surface Area"] = schedule["Surface Area"].astype(str)
        schedule["Surface Area"] = schedule["Surface Area"].str.replace(" m²","")
        return schedule

    def clean_area_and_surface_area_zero(self, schedule):
        schedule["Area"] = schedule["Area"].astype(float)
        schedule["Surface Area"] = schedule["Surface Area"].astype(float)
        zero_indices_area = schedule.index[schedule['Area']==0.0]
        zero_indices_surface_area = schedule.index[schedule['Surface Area']==0.0]
        common_indices = list(set(zero_indices_area).intersection(zero_indices_surface_area))
        schedule = schedule.drop(index=common_indices)
        return schedule

    def pack_results(self):
        self.export_schedules = dict(zip(self.used_files, self.cleaned_data_list))

    def export_cleaned_schedules(self):
        self.check_if_dir_empty()
        self.pack_results()
        for key, value in self.export_schedules.items():
            value.to_csv(self.export_path_for_schedules + '\\' + key, encoding='utf-8-sig', index = False)

    def remove_if_empty_size(self, schedule):
        no_size_rows_indices = schedule[schedule['Size'].isna()].index
        schedule = schedule.drop(index=no_size_rows_indices)
        return schedule

    def print_original_data(self):
        print(self.segment_data_in_frame())

<<<<<<< HEAD
    def clean(self):
        uncleaned_data_list = self.segment_data_in_frame()
        return uncleaned_data_list,self.file_names
=======
    def print_current_data(self):
        print(self.cleaned_data_list[0])

    def check_if_dir_empty(self):
        if len(os.listdir(self.export_path_for_schedules) ) == 0:
            pass
        else:    
            for file_name in os.listdir(self.export_path_for_schedules):
                # construct full file path
                file = self.export_path_for_schedules + file_name
                if os.path.isfile(file):
                    print('Deleting file:', file)
                    os.remove(file)
>>>>>>> 4961fce386261e39daf87c8a068d7a7d64ea1429
