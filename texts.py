dayoff_pl = \
    'Witam '+line[2]+' '+line[1]+',\
    \n \nJutro ('+self.date+') masz wolne\
    \n \nPozdrawiam Planning!'

dayoff_eng = \
    'Hi '+line[2]+' '+line[1]+',\
    \n \nTomorrow ('+self.date+') you have a day off!\
    \n \nBest Regards\
    \nPlanning!'  

prive_pl = \
    'Witam '+line[2]+' '+line[1]+',\
    \nJutro ('+self.date+') pracujesz w firmie '+line[7]+'\
    \npracę rozpoczynasz o godzinie: '+line[9]+'\
    \n \nTransport do pracy prosimy zorganizować we własnym zakresie.\
    \n \nW załączniku znajdziesz również pełny plan na jutro.\
    \n \nKażdą nieobecność zgłoś natychmiast pod numer tel. 0031 614750502 / 0031 618974055 \
    \n \nPozdrawiam Planning!'

prive_eng = \
    'Hi '+line[2]+' '+line[1]+'!\
    \nTomorrow ('+self.date+') you are working in '+line[7]+'\
    \nYou start work at: '+line[9]+"\
    \n \nTransport to work should be organized on your own.\
    \n \nIn the attechment you will also find a full plan for tomorrow.\
    \n \nEvery absent you have to report immediately at phone nr. 0031 614750502 / 0031 618974055 \
    \n \nBest Regards\
    \nPlanning!"

transport_pl = \
    'Witam '+line[2]+' '+line[1]+',\
    \nJutro ('+self.date+') pracujesz w firmie '+line[7]+'\
    \npracę rozpoczynasz o godzinie: '+line[9]+'\
    \n \nTransport przyjedzie po Ciebie o godzinie: '+line[6]+'\
    \n Kierowca: '+line[5]+'\
    \n \nW załączniku znajdziesz również pełny plan na jutro.\
    \n \nKażdą nieobecność zgłoś natychmiast pod numer tel. 0031 614750502 / 0031 618974055 \
    \n \nPozdrawiam Planning!'

transport_eng = \
    "Hi "+line[2]+' '+line[1]+"!\
    \nTomorrow ("+self.date+") you are working in "+line[7]+"\
    \nYou start work at: "+line[9]+"\
    \n \nTransport will come for you at: "+line[6]+"\
    \nDriver's name: "+line[5]+"\
    \n \nIn the attechment you will also find a full plan for tomorrow.\
    \n \nEvery absent you have to report immediately at phone nr. 0031 614750502 / 0031 618974055 \
    \n \nBest Regards\
    \nPlanning!"
