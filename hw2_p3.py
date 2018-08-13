data_name=input("Input your name:")
data=input("Input your birthday (yyyy/mm/dd):")
data_year=data[0:4]#to get the year,we have to cut down the string of data
data_month=data[5:7]#to get the month,we have to cut down the string of data
data_day=data[8:]#to get the day,we have to cut down the string of data
true_false=1


#to make the year become integer
i=0
while i<4 and int(data_year[:1])==0:
	data_year=data_year[1:]
	i=i+1



if int(data_month[:1])==0:
	data_month=data_month[1:]
#to make the month become integer
if int(data_day[:1])==0:
	data_day=data_day[1:]
#to make the day become integer


#if int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)):
	#data_year_leap=int(data_year)
	#print(data_year_leap)

#the program below is to detect whether day and month are valid	
if not 1<=int(data_month)<=12:
	print("Month Invalid.")
	true_false=0
elif (int(data_month)==1 or  int(data_month)==3 or  int(data_month)==5 or int(data_month)==7 or  int(data_month)==8 or  int(data_month)==10 or int(data_month)==12) and (not 1<=int(data_day)<=31):
	print("Day Invalid.")
	true_false=0
elif (int(data_month)==4 or int(data_month)==6 or int(data_month)==9 or int(data_month)==11) and (not 1<=int(data_day)<=30):
	print("Day Invalid.")
	true_false=0
elif(int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0))) and int(data_month)==2 and (not 1<=int(data_day)<=29):
	print("Day Invalid.")
	true_false=0
elif (not(int(data_year)%4==0 and ((not int(data_year)%100==0) or (int(data_year)%400==0)))) and int(data_month)==2 and (not 1<=int(data_day)<=28):
	print("Day Invalid.")
	true_false=0
elif not 1<=int(data_day)<=31:
	print("Day Invalid.")
	true_false=0
else:
	true_false=1

if not 1<=int(data_month)<=12:
	if not 1<=int(data_day)<=31:
		print("Day Invalid.")
		true_false=0

#to sum up the digits of year
i1=0
sum_year=0
length1=len(data_year)
while i1<length1 and true_false:
	data_year1=int(data_year[i1:i1+1])
	sum_year=sum_year+data_year1
	i1=i1+1
if  sum_year>=10:
	sum_year=sum_year//10+sum_year%10
if  sum_year>=10:
	sum_year=sum_year//10+sum_year%10





#to sum up the digits of month
i2=0
sum_month=0
length2=len(data_month)
while i2<length2 and true_false:
	data_month1=int(data_month[i2:i2+1])
	sum_month=sum_month+data_month1
	i2=i2+1
#print(sum_month)



#to sum up the digits of day
i3=0
sum_day=0
length3=len(data_day)
while i3<length3 and true_false:
	data_day1=int(data_day[i3:i3+1])
	sum_day=sum_day+data_day1
	i3=i3+1
#print(sum_day)



#to sum up the digits of sum_total
sum_total=str(sum_day+sum_month+sum_year)

i4=0
life_path_number=0
length4=len(sum_total)
while i4<length4 and true_false:
	n1=sum_total[i4:i4+1]
	n2=int(n1)
	life_path_number=life_path_number+n2
	i4=i4+1
#print(life_path_number)

if  life_path_number>=10:
	life_path_number=life_path_number//10+life_path_number%10



if true_false:
	print(data_name+", your \"Life Path Number\"is",life_path_number,".")





