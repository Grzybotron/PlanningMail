import sys
from PyQt5 import QtWidgets
from trans_Reader import Trans_Reader
from sendmail import Plan_mail
import smtplib
import datetime
from DataBase import DB

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__() 
        self.init_interface()
        self.openedfile = 'None'
        self.login = login_window.login
        self.password = login_window.password
        self.Trans_Reader = Trans_Reader()
        
    def init_interface(self):
        self.setWindowTitle('FlexiTransport') 
        self.setGeometry(500,300,360,0)
                
        self.login_lable = QtWidgets.QLabel('Logged as: '+login_window.login)
        
        self.tabs = QtWidgets.QTabWidget()
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()
        self.tabs.addTab(self.tab1, "Data Load")
        self.tabs.addTab(self.tab2, "Rapports")
        
        self.tomorrowdate = datetime.date.today() + datetime.timedelta(days=1)
        self.dateedit = QtWidgets.QLineEdit()
        self.dateedit.setText(str(self.tomorrowdate.strftime("%d-%m-%Y")))
        self.date_btn = QtWidgets.QPushButton('Set')
        self.datelable = QtWidgets.QLabel('Date is not set yet')
        self.date = ''
        
        self.load_P4F_lable = QtWidgets.QLabel('P4F data not loaded')
        self.load_P4F_btn = QtWidgets.QPushButton('Load P4F data')
        self.load_P4F_btn.setDisabled(True)

        self.loadlable = QtWidgets.QLabel('Plan not loaded')
        self.load_file_btn = QtWidgets.QPushButton('Load Plan')
        self.load_file_btn.setDisabled(True)

        self.add_attachmentlable = QtWidgets.QLabel('Attachment not loaded')
        self.add_attachment_btn = QtWidgets.QPushButton('Load Attachment')
        
#        self.send_prv = QtWidgets.QPushButton('Send Mail (prive)')
#        self.send_wolne = QtWidgets.QPushButton('Send Mail (vrij)')
#        self.send_work = QtWidgets.QPushButton('Send Mail (gepland)')
        
        self.send_all = QtWidgets.QPushButton('Send Mail to ALL')
        self.send_all.setDisabled(True)
        self.send_all.setGeometry(0,0,200,300)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.login_lable)
        v_box.addSpacing(10)
        v_box.addWidget(self.tabs)
        v_box.addSpacing(20)
        v_box.addWidget(self.send_all)
#        v_box.addWidget(self.send_work)
#        v_box.addWidget(self.send_prv)
#        v_box.addWidget(self.send_wolne)  
        
        tab1_box = QtWidgets.QVBoxLayout()

        tab1_box.addWidget(self.datelable)
        tab1_box.addWidget(self.dateedit)
        tab1_box.addWidget(self.date_btn)
        tab1_box.addSpacing(10)
        tab1_box.addWidget(self.loadlable) 
        tab1_box.addWidget(self.load_file_btn)
        tab1_box.addSpacing(10)
        tab1_box.addWidget(self.load_P4F_lable) 
        tab1_box.addWidget(self.load_P4F_btn)
        tab1_box.addSpacing(10)
        tab1_box.addWidget(self.add_attachmentlable) 
        tab1_box.addWidget(self.add_attachment_btn)
        
        self.tab1.setLayout(tab1_box)        
        self.setLayout(v_box)
        
        self.tab2_box = QtWidgets.QVBoxLayout()
        
        self.date_btn.clicked.connect(self.date_btnclick)
        self.load_file_btn.clicked.connect(self.load_btnclick)
        self.load_P4F_btn.clicked.connect(self.load_P4F_btnclick)         
        self.add_attachment_btn.clicked.connect(self.add_attachment_clk)  
        self.send_all.clicked.connect(self.send_all_clk)  
#        self.send_prv.clicked.connect(self.send_prv_clk)
#        self.send_work.clicked.connect(self.send_work_clk)  
#        self.send_wolne.clicked.connect(self.send_wolne_clk)
        
        self.show()

    def date_btnclick(self):
        self.date = self.dateedit.text()
        self.datelable.setText('Date is set to '+ str(self.date))
        self.load_file_btn.setDisabled(False)

    def load_btnclick(self):
        try:
            directory = QtWidgets.QFileDialog.getOpenFileName() 
            self.Trans_Reader.planning_reader(directory[0])
        except Exception:
            self.loadlable.setText('Loading Failed')
            self.load_P4F_btn.setDisabled(True)
            pass
        finally:
            self.loadlable.setText('Plan Loaded')
            self.load_P4F_btn.setDisabled(False) 
            self.send_all.setDisabled(True)
            #Ponizsza linijka do edycji
#            new_win = Table()
#            self.tab2_box.addWidget(new_win)
#            self.tab2.setLayout(self.tab2_box)

    def load_P4F_btnclick(self):
        try:
            directory = QtWidgets.QFileDialog.getOpenFileName()             
            self.Trans_Reader.p4f_reader(directory[0])
            self.Trans_Reader.data_split()
        except Exception:
            self.load_P4F_lable.setText('Loading Failed')
            self.send_all.setDisabled(True)
            pass
        finally:
            self.load_P4F_lable.setText('P4F data Loaded')
            self.send_all.setDisabled(False)  
    
    def add_attachment_clk(self):
        directory = QtWidgets.QFileDialog.getOpenFileName()
        with open(directory[0], "rb") as opened:
            self.openedfile = opened.read()
        self.add_attachmentlable.setText('Attachment Loaded')    

    def send_all_clk(self): 
        self.mail = Plan_mail(self.date,self.login,self.password)
        if self.openedfile == 'None':
            self.mail.sendmail_prv(self.Trans_Reader.wel_gepland_prv)
            self.mail.sendmail_wel_gepland(self.Trans_Reader.wel_gepland)
            self.mail.sendmail_niet_gepland(self.Trans_Reader.niet_gepland)
            self.mail.make_raport('Send Mail to ALL _rapport_',self.Trans_Reader.geen_mail)
        else:
            self.mail.sendmail_prv(self.Trans_Reader.wel_gepland_prv,self.openedfile)
            self.mail.sendmail_wel_gepland(self.Trans_Reader.wel_gepland,self.openedfile)
            self.mail.sendmail_niet_gepland(self.Trans_Reader.niet_gepland,self.openedfile)
            self.mail.make_raport('Send Mail to ALL _rapport_',self.Trans_Reader.geen_mail)
        self.load_P4F_btn.setDisabled(True)
        self.load_file_btn.setDisabled(True)
        self.send_all.setDisabled(True)        

#    def send_prv_clk(self):
#        self.mail.sendmail_prv()
#        self.mail.make_raport('Send Mail (prive) _rapport_')
#        
#    def send_work_clk(self):  
#        self.mail.sendmail_wel_gepland()
#        self.mail.make_raport('Send Mail (gepland) _rapport_')
#        
#    def send_wolne_clk(self):  
#        self.mail.sendmail_niet_gepland()
#        self.mail.make_raport('Send Mail (vrij) _rapport_')



class Login(QtWidgets.QDialog):   
    def __init__(self):
        super().__init__() 
        self.login = ''
        self.password = ''
        self.init_login()

    def init_login(self):
        self.setWindowTitle('Login')
        self.setGeometry(530,350,300,0)
        self.loginedit = QtWidgets.QLineEdit() 
        self.loginedit.setPlaceholderText('email')
        self.passedit = QtWidgets.QLineEdit()        
        self.passedit.setEchoMode(self.passedit.EchoMode(2))
        self.passedit.setPlaceholderText('password')
        self.login_btn = QtWidgets.QPushButton('Log In')    
        self.login_status = QtWidgets.QLabel('')
        
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.loginedit)
        v_box.addWidget(self.passedit)
        v_box.addWidget(self.login_status) 
        v_box.addWidget(self.login_btn)        
        
        self.login_btn.clicked.connect(self.login_btn_clk)          
        
        self.setLayout(v_box)

        self.show()

    def login_btn_clk(self):
        self.login = self.loginedit.text()
        self.password = self.passedit.text()
        self.attempt = 0
        try:
            s = smtplib.SMTP('smtp.office365.com',587)
            s.ehlo()
            s.starttls()
            s.login(self.login, self.password)
            s.quit()
            self.accept()
        except Exception:
            self.attempt = self.attempt + 1
            self.login_status.setText('Foult, Attempts: '+str(self.attempt))
            s.quit()
            pass



class Table(QtWidgets.QWidget):   
    def __init__(self):
        super().__init__() 
        self.init_table()
        
    def init_table(self):      
        self.setGeometry(530,350,1300,800)
        
        self.data_list = DB.get_data()
        self.table = QtWidgets.QTableWidget(self)
        self.table.setRowCount(len(self.data_list))
        self.table.setColumnCount(len(self.data_list[0]))
        
        hor_headers = window.Trans_Reader.headers
        self.table.setHorizontalHeaderLabels(hor_headers)
        
        self.data_to_table()
        
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        
        grid_box = QtWidgets.QVBoxLayout()        
        grid_box.addWidget(self.table, 100)
        
        self.setLayout(grid_box)     
        
    def data_to_table(self):
        self.data_list
        r = -1
        for row in self.data_list:
            c = -1
            r += 1
            for item in row:
                c += 1
                self.table.setItem(r,c,QtWidgets.QTableWidgetItem(item))



if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    login_window = Login()

    if login_window.exec_() == QtWidgets.QDialog.Accepted:
        window = Window()
        window.show()
        sys.exit(app.exec_())

#app = QtWidgets.QApplication(sys.argv)
#window = Window()
#sys.exit(app.exec_())