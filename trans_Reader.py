import csv
from DataBase import DB

class Trans_Reader():
    def __init__(self):
        self.niet_gepland = []
        self.wel_gepland = []
        self.wel_gepland_prv = []  
        self.geen_mail = []
        self.headers = []
        self.data = []
        
    def planning_reader(self, file_name):
        DB.clear_table()
        with open(file_name, 'r') as file:
            self.CSV_read = csv.reader(file, delimiter=';')
            for line in self.CSV_read:
                new_record = tuple(line)
                DB.insert_transport_data(new_record)

    def p4f_reader(self, file_name):
        with open(file_name, 'r') as file:
            self.CSV_read = csv.reader(file, delimiter=';')
            for line in self.CSV_read:
                try:
                    DB.update_transport_data(int(line[1]),line[20], line[25])
                except:
                    pass
            
#    def data_combine(self, dictionary):
#        for line in self.data:
#            if '@' and '.' in dictionary[line[0]][0]:
#                new_line = line + dictionary[line[0]]
#                self.data_combined.append(new_line)
#
    def data_split(self):
        data = DB.get_data()
        self.headers = data[0]
        del data[0]
        for line in data:
            if line[10] == None:
                self.geen_mail.append(line)                
            elif '@' and '.' not in line[10]:
                self.geen_mail.append(line)                
            elif line[6] == 'Niet gepland':
                self.niet_gepland.append(line)
            elif line[5] == 'privé':
                self.wel_gepland_prv.append(line)
            else :
                self.wel_gepland.append(line)
    
if __name__ == '__main__':    
    file_name = 'P4F.csv'                              

    z = Trans_Reader() 
    z.planning_reader('transport.csv')
    z.p4f_reader('P4F.csv')
    z.data_split()
    
    niet_gepland=z.niet_gepland
    wel_gepland=z.wel_gepland
    wel_gepland_prv=z.wel_gepland_prv
    geen_mail=z.geen_mail
    
    data = z.data