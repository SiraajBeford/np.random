from soupsieve import select
from src.data_cleaning import DataCleaner

# Clean the data
cleaner = DataCleaner()
cleaner.clean_all_schedules()
cleaner.print_current_data()
cleaner.export_cleaned_schedules()