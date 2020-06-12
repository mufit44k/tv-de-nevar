import requests
from datetime import datetime
from bs4 import BeautifulSoup
class Dmax():
    def __init__(self):
        self.programs = []      #diğer class larda bunlar yazılmayacak çünkü Dmax class ını miras alma tekniği ile miras alacağız
        self.ekstra()
    def ekstra(self):
        date = datetime.now().date()
        url = "https://www.dmax.com.tr/yayin-akisi?date="
        response = requests.get(url+str(date))
        html = response.content
        soup = BeautifulSoup(html,"html.parser")
        data = soup.find_all("div",{"class":"image-list-item"})
        names = []
        hours = []
        for i in data:
            for i in i.find_all("li"):
                for i in i.find_all("h4",{"class":"hidden-sm hidden-md hidden-lg"}):
                    hours.append(i.text)
        for i in data:
            for i in i.find_all("li"):
                for i in i.find_all("h3"):
                    names.append(i.text)
        for i in zip(names,hours):
            self.programs.append(str(i[1]+" ------> "+i[0]))
    def progams(self):
        a = ""
        for i in self.programs:
            a += str(i)+str("\n")
        return a
class Fox():
    pass
class Kanald(Dmax):
    # def __init__(self):
    #     self.ekstra(self)
    def ekstra(self):
        url = "https://www.kanald.com.tr/yayin-akisi"
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html,"html.parser")
        a = soup.find_all("div",{"class":"schedule-list"})
        hours = []
        names = []
        for i in a:
            for i in i.find_all("div",{"class":"schedule-item"}):
                for i in i.find_all("span",{"class":"time"}):
                    hours.append(i.text)

        for i in a:
            for i in i.find_all("figure"):
                for i in i.find_all("h3"):
                    names.append(i.text)
        for i in zip(names,hours):
            self.programs.append(str(i[1]+" ------> "+i[0]))
class show(Dmax):
    def ekstra(self):
        url = "https://www.showtv.com.tr/yayin-akisi/"
        days = {0:"pazartesi",1:"sali",2:"carsamba",3:"persembe",4:"cuma",5:"cumartesi",6:"pazar"}
        today1 = datetime.today().weekday()
        today = days[today1]
        response = requests.get(url+today)
        html = response.content
        soup = BeautifulSoup(html,"html.parser")
        a = soup.find_all("div",{"class":"swiper-wrapper"})
        names = []
        hours = []
        single = []
        double = []
        for i in a:
            for i in i.find_all("figure"):
                for i in i.find_all("figcaption"):
                    for i in i.find_all("span",{"class":"title"}):
                        names.append(i.text)
        for i in a:
            for i in i.find_all("figure"):
                for i in i.find_all("figcaption"):
                    for i in i.find_all("span",{"class":"time"}):
                        for i in i.find_all("span"):
                            hours.append(i.text)
        for i in hours:
            if hours.index(i) % 2 == 0:
                double.append(i)
            elif hours.index(i) == 0:
                double.append(i)
            else:
                single.append(i)
        hour = list(zip(double,single))
        hour1 = []
        for i in hour:
            hour1.append(i[0]+i[1])
        for i in zip(names,hour1):
            self.programs.append(str(i[1]+" ------> "+i[0]))

class star(Dmax):
    def ekstra (self):
        url = "https://www.startv.com.tr/yayin-akisi"
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html,"html.parser")
        a = soup.find_all("section",{"class":"section series-list"})
        names = []
        hours = []
        for i in a:
            for i in i.find_all("li"):
                for i in i.find_all("div",{"class":"data"}):
                    for i in i.find_all("a"):
                        names.append(i.text)
        for i in a:
            for i in i.find_all("li"):
                for i in i.find_all("div",{"class":"date"}):
                    for i in i.find_all("span",{"class":"time"}):
                        hours.append(i.text)
        for i in zip(names,hours):
            self.programs.append(str(i[1]+" ------> "+i[0]))
class trt1(Dmax):
    def ekstra(self):
        days = {0:"Pazartesi",1:"Salı",2:"Çarşamba",3:"Perşembe",4:"Cuma",5:"Cumartesi",6:"Pazar"}
        today1 = datetime.today().weekday()
        today = days[today1]
        url = "https://www.trt1.com.tr/yayin-akisi"
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html,"html.parser")
        a = soup.find_all("div",{"id":today})
        hours = []
        names = []
        for i in a:
            for i in i.find_all("ul",{"class":"event-list"}):
                for i in i.find_all("time"):
                    for i in i.find_all("span",{"class":"day"}):
                        for i in i.find_all("a"):
                            hours.append(i.text)
        for i in a:
            for i in i.find_all("ul",{"class":"event-list"}):
                for i in i.find_all("li"):
                    for i in i.find_all("div",{"class":"info"}):
                        for i in i.find_all("h2",{"class":"title"}):
                            for i in i.find_all("a"):
                                names.append(i.text)
        for i in zip(names,hours):
            self.programs.append(str(i[1]+" ------> "+i[0]))