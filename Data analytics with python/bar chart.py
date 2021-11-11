import pandas
import matplotlib.pyplot as plt
data8 = pandas.read_excel("PROBLEM 1.xlsx")
data = pandas.read_excel("Book1 spend hours.xlsx")
data46 = pandas.read_excel("Spend Time.xlsx")
# print(data)
print('....................................')

tasks = data8.groupby(['TRAINEE'])['SUBJECT'].count()
# print(tasks)  
plt.pie(data['Spend Hours'], labels=data['Courses'])
plt.bar(tasks.index, tasks)
# data46['Day'] = data46['Start Date']
# print(data46)
# tasks1 = data46.groupby(['Day'])['Spend Time'].count()
# print(tasks1)
plt.plot(data46['Start Date'],data46['Spend Time'])
print(plt.show())