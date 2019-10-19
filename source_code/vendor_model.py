import csv
from datetime import time, datetime

lunch_time = [time(11), time(13)]
dinner_time = [time(18), time(20)]

class Vendor(object):
    def __init__(self, name, photopath, queuingK, openhourstr, menus = []):
        self.name = name
        self.photo = photopath
        self.queuingK = queuingK
        self.menus = menus
        self.openingTime = openhourstr
        self.opentime = []

    def menu(self, timeStamp):
        if not self.isOpening(timeStamp):
            return []
        day = timeStamp.weekday()
        t = timeStamp.time()
        m  = self.menus[day]
        menu_result = []
        menu_result.append([m.Dish1, m.Price1])
        menu_result.append([m.Dish2, m.Price2])
        if (lunch_time[0] <= t <= lunch_time[1]):
            menu_result.append([m.LunchDish, m.LunchPrice])
        if (dinner_time[0] <= t <= dinner_time[1]):
            menu_result.append([m.DinnerDish, m.DinnerPrice])

        return menu_result

    def isOpening(self,timeStamp):
        day = timeStamp.weekday()
        t = timeStamp.time()
        today_opening_time = self.opentime[day]
        if (today_opening_time[0] == today_opening_time[1]):
            return False

        return today_opening_time[0] <= t <= today_opening_time[1]

    def queueTime(self,queueLen):
        return queueLen * self.queuingK


def get_basic_info(vendorlist):
    with open("cz1003vendor.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for line in csv_reader:
            vendorlist.append(Vendor(line[0], line[1], float(line[2]), line[3]))


def get_openning_time(vendorlist):
    with open("cz1003operating.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        index = 0
        vendor = vendorlist[index]
        for line in csv_reader:
            if len(line[0]) == 0:
                vendor.opentime.append([time(), time()])
                index += 1
                if index >= len(vendorlist):
                    break
                vendor = vendorlist[index]
                continue
            opentime = datetime.strptime(line[0], "%H%M").time()
            closetime = datetime.strptime(line[1], "%H%M").time()
            vendor.opentime.append([opentime, closetime])

def get_menus(vendorlist):
    with open("cz1003menu.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        index = 0
        vendor = vendorlist[index]
        for l in csv_reader:
            if len(l[0]) == 0:
                vendor.opentime.append([time(), time()])
                index += 1
                if index >= len(vendorlist):
                    break
                vendor = vendorlist[index]
                continue
            vendor.menus.append(Menu(l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7]))

class Menu(object):
    def __init__(self, Dish1, Price1, Dish2, Price2, LunchDish, LunchPrice, DinnerDish, DinnerPrice):
        self.Dish1 = Dish1
        self.Price1 = Price1
        self.Dish2 = Dish2
        self.Price2 = Price2
        self.LunchDish = LunchDish
        self.LunchPrice = LunchPrice
        self.DinnerDish = DinnerDish
        self.DinnerPrice = DinnerPrice



def allVendor():
    vendorlist = []
    get_basic_info(vendorlist)
    get_openning_time(vendorlist)
    get_menus(vendorlist)

    return  vendorlist
