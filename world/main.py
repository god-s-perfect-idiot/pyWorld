import names
import random
import datetime

#People Details:
#0.Name
#1.BirthDay
#2.DeathProbabilityPercentage
#3.Age
#4.Status
#5.DeathDay
#6.Gender
#7.Parents

people_dict={}
people=[]
date=[]
sex=[]

date.append(1)
date.append(1)
date.append(1950)

def check_leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def inc_date():
    if(date[1] in [1,3,5,7,8,10,12]):
        if(date[0]<31):
            date[0]+=1
        else:
            date[0]=1
            if(date[1]<12):
                date[1]+=1
            else:
                date[1]=1
                date[2]+=1
    elif(date[1] in [4,6,9,11]):
        if(date[0]<30):
            date[0]+=1
        else:
            date[0]=1
            if(date[1]<12):
                date[1]+=1
            else:
                date[1]=1
                date[2]+=1
    elif((date[1] == 2) and check_leap(date[2])):
        if(date[0]<29):
            date[0]+=1
        else:
            date[0]=1
            if(date[1]<12):
                date[1]+=1
            else:
                date[1]=1
                date[2]+=1
    elif((date[1] == 2) and not check_leap(date[2])):
        if(date[0]<28):
            date[0]+=1
        else:
            date[0]=1
            if(date[1]<12):
                date[1]+=1
            else:
                date[1]=1
                date[2]+=1

def get_random_date(year):
    return datetime.datetime.strptime('{} {}'.format(random.randint(1, 366), year), '%j %Y')

def name(_gender):
    temp=[]
    temp.append(names.get_full_name(gender=_gender))
    return temp

def deathrefresh():

    for person in people:
        randomdeath=random.randint(1,100)
        randomsuddendeath=random.randint(1,1000)
        if(randomdeath==77 and randomsuddendeath==77):
            person[2]=100
        if((person[2]>87 and randomdeath==77) or person[2]>100):
            suredeath=random.randint(1,100)
            if(suredeath==1):
                person[4]="Dead"
                person[5]=str(date[0])+"-"+str(date[1])+"-"+str(date[2])

def dates():
    for person in people:
        millenial_prob=random.randint(1,10)
        if(millenial_prob>2):
            borny=random.randint(1970,1990)
        else:
            borny=random.randint(1970,2019)
        born=get_random_date(borny)
        early_death_prob=random.randint(1,10)
        if(early_death_prob>2):
            if(borny+30<=2019):
                deathy=random.randint(borny+30,2019)
            else:
                deathy=2019
        else:
            deathy=random.randint(borny,2019)
        death=get_random_date(deathy)
        person.append(str(born))
        person.append(str(death))
        age=deathy-borny
        person.append(str(age))

def birth():
    gender=random.randint(1,2)
    if(gender==1):
        vessel=name('male')
    else:
        vessel=name('female')
    vessel.append(str(date[0])+"-"+str(date[1])+"-"+str(date[2]))
    vessel.append(0)
    vessel.append(0)
    vessel.append("Alive")
    vessel.append("N/A")
    if(gender==1):
        vessel.append("Male")
    else:
        vessel.append("Female")
    people.append(vessel)
    people_dict[vessel[0]]=vessel

def had_sex():
    for couple in sex:
        if(people_dict[couple[0]][3]>16 and people_dict[couple[1]][3]>16):
            preg_chance=random.randint(1,100)
            if(preg_chance==77):
                birth()

def start():
    vessel=name('male')
    vessel.append(str(date[0])+"-"+str(date[1])+"-"+str(date[2]))
    vessel.append(0)
    vessel.append(0)
    vessel.append("Alive")
    vessel.append("N/A")
    vessel.append("Male")
    people.append(vessel)
    people_dict[vessel[0]]=vessel
    vessel=name('female')
    vessel.append(str(date[0])+"-"+str(date[1])+"-"+str(date[2]))
    vessel.append(0)
    vessel.append(0)
    vessel.append("Alive")
    vessel.append("N/A")
    vessel.append("Female")
    people.append(vessel)
    people_dict[vessel[0]]=vessel

    sextemp=[]
    sextemp.append(people[0][0])
    sextemp.append(people[1][0])
    sex.append(sextemp)

def refresh_ages():
    for person in people:
        if(str(date[0])+"-"+str(date[1]) == person[1][:-5] and person[4] != "Dead"):
            person[3]+=1
            person[2]+=1

def show_data():
    print("\n\n"+str(date[0])+"-"+str(date[1])+"-"+str(date[2]))
    print("\n-----------------------------------RECORDS--------------------------------------")
    for person in people:
        print("\n\nName:\t"+person[0]+"\nBirth:\t"+person[1]+"\nDeath Chance:\t"+str(person[2])+"\nAge:\t"+str(person[3])+
        "\nStatus:\t"+str(person[4])+"\nDeath Day:\t"+str(person[5])+"\nGender:\t"+str(person[6]))

def new_day():
    inc_date()
    refresh_ages()
    deathrefresh()
    had_sex()

start()

while(1):
    t=int(input())
    for i in range(t):
        new_day()

    show_data()
