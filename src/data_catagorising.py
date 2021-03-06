class DataCategoriser():

    def __init__(self,cleaned_data_list):
        super(DataCategoriser, self).__init__()
        
        self.data = cleaned_data_list[0]
        self.file_names = cleaned_data_list[1]
        self.category = [0,0,0,0,0]
        self.current_file_categories = []
        
    def get_all_sizes(self, input_file):
        sizes = []
        for i in range(len(input_file['Size'])):
            sizes.append(list(input_file['Size'])[i])
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
            wmin = int(min(w))
            hmin = int(min(h))
            
            if max(wmin,hmin)<750 and wmin+hmin<=1150: 
                self.category[0] += 1 
                category[0] += 1
                cat.append(1) 
            if max(wmin,hmin)<750 and wmin+hmin>1150: 
                self.category[1] += 1 
                category[1] += 1
                cat.append(2) 
            if max(wmin,hmin)>=750 and max(wmin,hmin)<1350: 
                self.category[2] += 1 
                category[2] += 1
                cat.append(3) 
            if max(wmin,hmin)>=1350 and max(wmin,hmin)<2100: 
                self.category[3] += 1 
                category[3] += 1
                cat.append(4) 
            if max(wmin,hmin)>=2100: 
                self.category[4] += 1 
                category[4] += 1
                cat.append(5) 
        self.current_file_categories = cat
        
    def categorization_steps(self):
        for file_number in range(len(self.data)):
            input_file = self.data[file_number]
            look_up_size = self.get_all_sizes(input_file)
            split_item_size = self.split_item_size(look_up_size)
            self.category_selection(split_item_size,input_file,file_number)
            input_file['Category'] = self.current_file_categories

    def categorise(self):
        self.categorization_steps()
        
    def data_with_categories(self):
        return self.data,self.file_names
        
