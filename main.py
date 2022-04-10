# from soupsieve import select
from bleach import clean
from src.data_cleaning import DataCleaner
from src.data_catagorising import DataCategoriser
from src.data_quantifying import Quantifier
import time

now = float(time.time())
# Clean the data
cleaner = DataCleaner()
cleaner.clean_all_schedules()
cleaner.export_cleaned_schedules()

# Categorise the data
categoriser = DataCategoriser(cleaner.clean())
categoriser.categorise()

# Quantify data and calculate costs
quantifer = Quantifier(categoriser.data_with_categories())
quantifer.quantify()

# Get runtime
nownow = float(time.time())
print(nownow-now)
