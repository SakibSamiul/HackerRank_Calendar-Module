import datetime

def dateTime(t):
    day = datetime.datetime.strptime(t, "%m %d %Y").date()

    day_name = day.strftime("%A")
    print(day_name.upper())

if __name__== '__main__':
    t = input("mm dd yyyy")
    result = dateTime(t)