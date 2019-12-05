from constraint import *

problem = Problem()

timeSlots = ["m-9", "m-10", "m-11", "tu-9", "tu-10", "tu-11", "w-9", "w-10", "w-11", "th-9", "th-10"]
subjects = ["n1", "n2", "s1", "s2", "m1", "m2", "e1", "e2", "l1", "l2", "pe"]
teachers = ["lucia", "andrea", "juan"]

problem.addVariables(subjects, timeSlots)

problem.addConstraint(AllDifferentConstraint(), subjects)

def consecutive (subjectTime1, subjectTime2):
	time1 = subjectTime1.split("-")
	time2 = subjectTime2.split("-")
	day1 = time1[0]
	day2 = time2[0]
	hour1 = int(time1[1])
	hour2 = int(time2[1])
	return day1==day2 and (hour1==hour2+1 or hour2==hour1+1)
	
problem.addConstraint(consecutive, ["s1", "s2"]) 

def notSameDay (mathTime1, mathTime2, naturalTime1, naturalTime2, englishTime1, englishTime2):
	dayMath1 = mathTime1.split("-")[0]
	dayMath2 = mathTime2.split("-")[0]
	dayNatural1 = naturalTime1.split("-")[0]
	dayNatural2 = naturalTime2.split("-")[0]
	dayEnglish1 = englishTime1.split("-")[0]
	dayEnglish2 = englishTime1.split("-")[0]
	set = {dayNatural1, dayNatural2, dayEnglish1, dayEnglish2}
	if dayMath1 not in set and dayMath2 not in set: return True
	return False
	
problem.addConstraint(notSameDay, ["m1","m2","n1","n2","e1","e2"])
            
def first (mathTime1, mathTime2):
	hour1 = int(mathTime1.split("-")[1])
	hour2 = int(mathTime2.split("-")[1])
	return hour1==9 and hour2==9
	
problem.addConstraint(first, ["m1", "m2"])

def last (naturalTime1, naturalTime2):
	day1 = naturalTime1.split("-")[0]
	day2 = naturalTime2.split("-")[0]
	hour1 = int(naturalTime1.split("-")[1])
	hour2 = int(naturalTime2.split("-")[1])
	last = True
	if day1=="th" and hour1 != 10: last = False
	elif day2=="th" and hour2 != 10: last = False
	elif hour1 != 11 or hour2 != 11: last = False
	return last
	

problem.addConstraint(last, ["n1", "n2"])

print(problem.getSolution())