import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import datetime
import csv
from email.mime.application import MIMEApplication

class Plan_mail():
    def __init__(self,date,login,password):
        self.me = login
        self.date = date
        self.raport_list = []
        self.login = login
        self.password = password
        
    def sendmail_niet_gepland(self, l_niet_gepland, openedfile='None'):
        s = smtplib.SMTP('smtp.office365.com',587)
        s.ehlo()
        s.starttls()
        s.login(self.login , self.password)
        if openedfile != 'None':
            attachedfile = MIMEApplication(openedfile, _subtype = "pdf", _encoder = encoders.encode_base64)
        for line in l_niet_gepland:
            try:
                msg = MIMEMultipart()
                if line [11]  == 'Poolse':
                    msg['Subject'] = "Jutro masz wolne!"
                else:
                    msg['Subject'] = "Tomorrow, you have a day off!"
                msg['From'] = self.me
                msg['To'] = line[10]
                
                if line [11]  == 'Poolse':
                    text = \
                    'Witam '+line[2]+' '+line[1]+',\
                    \n \nJutro ('+self.date+') masz wolne\
                    \n \nPozdrawiam Planning!'
                    
                else:
                    text = \
                    'Hi '+line[2]+' '+line[1]+',\
                    \n \nTomorrow ('+self.date+') you have a day off!\
                    \n \nBest Regards\
                    \nPlanning!'  
                    
                part1 = MIMEText(text, 'plain')
                msg.attach(part1)
                
                if openedfile != 'None':
                    attachedfile.add_header('content-disposition', 'attachment', filename = 'Plan '+self.date+'.pdf')
                    msg.attach(attachedfile)
                               
                s.sendmail(self.me, line[10], msg.as_string())
                self.raport_list.append(['Succesfully sent to: ',line[2]+' '+line[1],'email: ',line[10]])

            except smtplib.SMTPException:
                self.raport_list.append(['Cannot send to: ',line[2]+' '+line[1],'email: ',line[10]])
        s.quit()        

    def sendmail_wel_gepland(self, l_wel_gepland, openedfile='None'):
        s = smtplib.SMTP('smtp.office365.com',587)
        s.ehlo()
        s.starttls()
        s.login(self.login , self.password)
        if openedfile != 'None':
            attachedfile = MIMEApplication(openedfile, _subtype = "pdf", _encoder = encoders.encode_base64)
        for line in l_wel_gepland:
            try:
                msg = MIMEMultipart('alternative')
                if line [11]  == 'Poolse':
                    msg['Subject'] = "Twój plan na "+self.date
                else:
                    msg['Subject'] = "Your plan for "+self.date
                msg['From'] = self.me
                msg['To'] = line[10]
    
                if line [11]  == 'Poolse':
                    text = \
                    'Witam '+line[2]+' '+line[1]+',\
                    \nJutro ('+self.date+') pracujesz w firmie '+line[7]+'\
                    \npracę rozpoczynasz o godzinie: '+line[9]+'\
                    \n \nTransport przyjedzie po Ciebie o godzinie: '+line[6]+'\
                    \n Kierowca: '+line[5]+'\
                    \n \nW załączniku znajdziesz również pełny plan na jutro.\
                    \n \nKażdą nieobecność zgłoś natychmiast pod numer tel. 0031 614750502 / 0031 618974055 \
                    \n \nSerdecznie pozdrawiamy! \nPlanning'
                    
                else:
                    text = \
                    "Hi "+line[2]+' '+line[1]+"!\
                    \nTomorrow ("+self.date+") you are working in "+line[7]+"\
                    \nYou start work at: "+line[9]+"\
                    \n \nTransport will come for you at: "+line[6]+"\
                    \nDriver's name: "+line[5]+"\
                    \n \nIn the attechment you will also find a full plan for tomorrow.\
                    \n \nEvery absent you have to report immediately at phone nr. 0031 614750502 / 0031 618974055 \
                    \n \nBest Regards\
                    \nPlanning!"
                    
                part1 = MIMEText(text, 'plain')
                msg.attach(part1)
                
                if openedfile != 'None':
                    attachedfile.add_header('content-disposition', 'attachment', filename = 'Plan '+self.date+'.pdf')
                    msg.attach(attachedfile)
    
                s.sendmail(self.me, line[10], msg.as_string())
                self.raport_list.append(['Succesfully sent to: ',line[2]+' '+line[1],'email: ',line[10]])
            except smtplib.SMTPException:
                self.raport_list.append(['Cannot send to: ',line[2]+' '+line[1],'email: ',line[10]])
        s.quit()
        
    def sendmail_prv(self,l_wel_gepland_prv, openedfile='None'):
        s = smtplib.SMTP('smtp.office365.com',587)
        s.ehlo()
        s.starttls()
        s.login(self.login , self.password)
        if openedfile != 'None':
            attachedfile = MIMEApplication(openedfile, _subtype = "pdf", _encoder = encoders.encode_base64)
        for line in l_wel_gepland_prv:
            try:
                msg = MIMEMultipart('alternative')
                if line [11]  == 'Poolse':
                    msg['Subject'] = "Twój plan na "+self.date
                else:
                    msg['Subject'] = "Your plan for "+self.date
                msg['From'] = self.me
                msg['To'] = line[10]
                
                if line [11]  == 'Poolse':
                    text = \
                    'Witam '+line[2]+' '+line[1]+',\
                    \nJutro ('+self.date+') pracujesz w firmie '+line[7]+'\
                    \npracę rozpoczynasz o godzinie: '+line[9]+'\
                    \n \nTransport do pracy prosimy zorganizować we własnym zakresie.\
                    \n \nW załączniku znajdziesz również pełny plan na jutro.\
                    \n \nKażdą nieobecność zgłoś natychmiast pod numer tel. 0031 614750502 / 0031 618974055 \
                    \n \nPozdrawiam Planning!'
                    
                else:
                    text = \
                    'Hi '+line[2]+' '+line[1]+'!\
                    \nTomorrow ('+self.date+') you are working in '+line[7]+'\
                    \nYou start work at: '+line[9]+"\
                    \n \nTransport to work should be organized on your own.\
                    \n \nIn the attechment you will also find a full plan for tomorrow.\
                    \n \nEvery absent you have to report immediately at phone nr. 0031 614750502 / 0031 618974055 \
                    \n \nBest Regards\
                    \nPlanning!"
                    
                part1 = MIMEText(text, 'plain')
                msg.attach(part1)
                
                if openedfile != 'None':
                    attachedfile.add_header('content-disposition', 'attachment', filename = 'Plan '+self.date+'.pdf')
                    msg.attach(attachedfile)
                
                s.sendmail(self.me, line[10], msg.as_string())
                self.raport_list.append(['Succesfully sent to: ',line[2]+' '+line[1],'email: ',line[10]])
            except smtplib.SMTPException:
                self.raport_list.append(['Cannot send to: ',line[2]+' '+line[1],'email: ',line[10]])
        s.quit()
                
    def make_raport(self, file_name, l_geen_mail=None):
        if l_geen_mail != None:
            for line in l_geen_mail:
                self.raport_list.append(['Cannot send to: ',line[2]+' '+line[1],' no email'])
        with open(file_name + ' '+str(datetime.datetime.now().strftime("%Y-%m-%d %H;%M;%S")) + '.csv', 'w', newline='') as raport_file:
                writer = csv.writer(raport_file, delimiter=';')
                for line in self.raport_list:
                    writer.writerow(line)
        self.raport_list.clear()

if __name__ == '__main__':        
    from trans_Reader import Trans_Reader               
    z = Trans_Reader() 
    z.planning_reader('transport.csv')
    z.p4f_reader('P4F.csv')
    z.data_split()
    
    zz = Plan_mail('20-20-666','login','password')
#    zz.sendmail_niet_gepland()
#    zz.sendmail_wel_gepland()
#    zz.sendmail_prv()