from soupsieve import select
from src.data_cleaning import DataCleaner
from src.data_catagorising import DataCategoriser
from src.data_quantifying import Quantifier
import time

now = float(time.time())
# Clean the data
cleaner = DataCleaner()
<<<<<<< HEAD

# Categorise the data
categoriser = DataCategoriser(cleaner.clean())
categoriser.categorise()

# Quantify data and calculate costs
quantifer = Quantifier(categoriser.data_with_categories())
quantifer.quantify()

# Get runtime
nownow = float(time.time())
print(nownow-now)
=======
cleaner.clean_all_schedules()
cleaner.print_current_data()
cleaner.export_cleaned_schedules()
>>>>>>> 4961fce386261e39daf87c8a068d7a7d64ea1429
