from src.data_cleaning import DataCleaner
from src.data_catagorising import DataCategoriser
from src.data_quantifying import Quantifier

# Clean the data
cleaner = DataCleaner()

# Categorise the data
categoriser = DataCategoriser(cleaner.clean())
categoriser.categorise()
quantifer = Quantifier(categoriser.data_with_categories())
quantifer.quantify()
