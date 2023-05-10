from pandas import read_csv

class DatabaseParser:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.cat_lst = None
        self.data_dict = None

    def load(self,file_path = None):
        if file_path != None:
            self.file_path = file_path

        self.data_frame = read_csv(self.file_path, delimiter=';', encoding='utf-8', header=0)
        self.data_frame = self.data_frame.dropna(how='all')

        self.parse()

    def parse(self):
        self.data_dict = {}
        self.unit_prompt = ['Material', 'unknown1','unknown2']
        has_unit = False
        category = ''
        # Iterate over the rows of the DataFrame
        for _, row in self.data_frame.iterrows():
            nan_count = row.isnull().sum()  # Count the NaN values in the row
            if nan_count == 2:
                category = row['Materials']
            elif nan_count == 1 and has_unit == False:
                self.unit_prompt[1] = row[1]
                self.unit_prompt[2] = row[2]
                has_unit = True
            elif nan_count == 0:
                if category not in self.data_dict:
                    self.data_dict[category] = []
                    
                self.data_dict[category].append([row['Materials'], [float(row[1]),float(row[2])]])

    def get_categories_list(self):
        if self.cat_lst != None and self.data_dict != None and len(self.cat_lst) == len(self.data_dict):
            return self.cat_lst

        self.cat_lst = []

        for cat,_ in self.data_dict.items():
            self.cat_lst.append(cat)

        return self.cat_lst

    def get_materials_list(self, category, plain_text = False, unit_header = False):
        if category in self.data_dict:
            if plain_text:
                result = []

                if unit_header:
                    result.append(self.unit_prompt)
                
                for item in self.data_dict[category]:
                    plain_text_lst = [item[0]] + [str(x) for x in item[1]]
                    result.append(plain_text_lst)
                return result
            else:
                return self.data_dict[category]