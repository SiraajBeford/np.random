import pandas as pd
import os

class Quantifier():

    def __init__(self,data_with_categories):
        super(Quantifier, self).__init__()
        self.data = data_with_categories[0]
        self.file_names = data_with_categories[1]
        self.sum_of_area_of_category = [0,0,0,0,0]
        self.main_dir = str(os.getcwd()).replace('\data','')

    def quantity(self,input_file):
        self.sum_of_area_of_category = [0,0,0,0,0]
        for item in range(len(input_file)):
            new_area = str(list(input_file['Area'])[item])
            for category in range(len(self.sum_of_area_of_category)): 
                if list(input_file['Category'])[item] == category+1: 
                    if new_area != 0:
                        self.sum_of_area_of_category[category] += float(new_area)*float(list(input_file['Count'])[item])
                    else:
                        new_area = list(input_file['Surface Area'])[item]
                        self.sum_of_area_of_category[category] += float(new_area)*float(list(input_file['Count'])[item])

    def quantify(self):
        for file_number in range(len(self.data)):
            input_file = self.data[file_number]
            self.quantity(input_file)
            self.make_csv_excel(file_number)
        print('BOQs updated')
        
    def get_rates(self):
        return [1,2.5,4,5,6]

    def get_cost(self,sum):
        cost = []
        total_cost = 0; 
        for index in range(len(sum)):
            cost.append(sum[index]*self.get_rates()[index])
            total_cost += cost[index]
        return cost, total_cost

    def make_csv_excel(self,file_number):
        data = []
        for category in range(5):
            row = []
            row.append(category+1)
            row.append(self.sum_of_area_of_category[category])
            row.append(self.get_rates()[category])
            row.append(self.get_cost(self.sum_of_area_of_category)[0][category])
            data.append(row)
        data.append(['total',self.get_cost(self.sum_of_area_of_category)[1]])
        file = pd.DataFrame(data,columns=['category','quantity','rate','cost'])
        file.to_csv(self.main_dir + '\output\csv\BOQ_'+str(self.file_names[file_number])+'.csv',index=False)
        


