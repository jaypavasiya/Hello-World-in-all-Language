n=int(input("enter no.of students:"))
marks=[]
max =int(input("enter maximum marks:"))

#taking marks
print("enter marks of students on seperate lines!")
print("Note: use -1 for absent students!")
for i in range(n):
	marks.append(int(input("Marks of students:")))
print(marks)

#initialize everthing to 0
top_score=0
avg_score=0
absent=0
h_score=0
l_score=max
temp_frequency=[]
for i in range(max+2):
	temp_frequency.append(0)

#calculating everything
for i in marks:
	if i<0:
		absent +=1
		countinue

	else:
		top_score+=i
		if i<l_score:
		      l_score=i
		if i>h_score:
		       h_score=i

	temp_frequency[i]+=1

avg_score=top_score/(n-absent)
print(temp_frequency)
#calulation maximum frequency
max_frequency=0
for i in temp_frequency:
	if i>max_frequency:
	       max_frequency=i

#show marks with maximum frequency
max_frequency_marks=[]
for i in range(max+2):
	if temp_frequency[i]==max_frequency:
		max_frequency_marks.append(i)

#print marks with max frequency
#print("marks with max freqency are {0}.format(max_frequency_marks))

print("The Average score of class is {0}".format(round(avg_score,2)))
print("The Highest score of class is {0}".format(h_score))
print("The Lowest score of class is {0}".format(l_score))
print("{0} Students were absent for the class".format(absent))
print("marks with max frequency are {0}".format(max_frequency_marks))

#print(max_freqency)
