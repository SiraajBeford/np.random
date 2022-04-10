class DataCategoriser():

    def __init__(self,cleaned_data_list):
        super(DataCategoriser, self).__init__()
        self.data = cleaned_data_list
        self.category = [0,0,0,0,0]
        self.current_file_categories = []
        
    def get_all_sizes(self, input_file):
        sizes = []
        for i in range(len(input_file['Size'])):
            sizes.append(input_file['Size'][i])
        return sizes

    def split_item_size(self, look_up_size):
        look_up_sizep = []
        for item in range(len(look_up_size)):
            look_up_sizep.append(look_up_size[item].split('-'))
        return look_up_sizep

    def get_width_height(self,widths_heights):
        widths = []
        heights = []
        for d in range(len(widths_heights)):
            new_widths_heights = widths_heights[d].split('x')
            widths.append(new_widths_heights[0])
            heights.append(new_widths_heights[1])
        return widths,heights

    def category_selection(self,split_item_size,input_file, file_number):
        category = [0,0,0,0,0]
        cat = []
        for dimensions in range(len(split_item_size)):
            widths_heights = split_item_size[dimensions]
            w,h = self.get_width_height(widths_heights)
            wmax = int(max(w))
            wmin = int(min(w))
            hmax = int(max(h))
            hmin = int(min(h))
            
            if wmax<750 or hmax<750 and wmin+hmin<=1150: 
                self.category[0] += 1 
                category[0] += 1
                cat.append(1) 
            elif wmax<750 or hmax<750 and wmin+hmin>1150: 
                self.category[1] += 1 
                category[1] += 1
                cat.append(2) 
            elif wmax>=750 or hmax>=750 and wmax<1350 or hmax<1350: 
                self.category[2] += 1 
                category[2] += 1
                cat.append(3) 
            elif wmax>=1350 or hmax>=1350 and wmax<2100 or hmax<2100: 
                self.category[3] += 1 
                category[3] += 1
                cat.append(4) 
            elif wmax>2100 or hmax>2100: 
                self.category[4] += 1 
                category[4] += 1
                cat.append(5) 
        self.current_file_categories = cat
        # print('Items in categories for file number',str(file_number+1) + ':',category) # must remove

    def categorization_steps(self):
        for file_number in range(len(self.data)):
            input_file = self.data[file_number]
            look_up_size = self.get_all_sizes(input_file)
            split_item_size = self.split_item_size(look_up_size)
            self.category_selection(split_item_size,input_file,file_number)
            input_file['Category'] = self.current_file_categories

    def categorise(self):
        self.categorization_steps()
        # print('Items in categories:',self.category)
        
    def data_with_categories(self):
        return self.data
        
