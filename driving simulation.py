import matplotlib.pylot as plt

Max_Distance = int(input())
Initial_velocity =int(input())
Time_spent =int(input())
Acc =int(input())
Speed_limit=60


Distance_array=[]
Velocity_array=[]
Time_array[]


for i in range(0,Max_distance/10):
    Distance_array[i]=i*10

for i in range(0,len(Distance_array)):
    Velocity_array[i]= sqrt(2*Acc*i)

for i in range(0,len(Distance_array)):
    Time_Array[i]=sqrt(2*Distance_array[i]/Acc)

plt.plot(Time_Array,Distance_Array)


plt.xlabel('time')
plt.ylabel('distance')


for i in Distance_array:
    if(Distance_array[len(Distance_array)]>max_Distance):
        print("The person reached destination : ",  Distance_array[len(Distance_array)])
    else:
            print("The person did not reach destination:" , Distance_array[len(Distance_array)])

for i in Velocity_array:
    if(Velocity_array[len(Velocity_array)]>Speep_limit):
        print("The person went over speed limit max speed was : " + Velocity_array[len(Velocity_array)])
    else:
            print("The person did not go over speed limit max speed was :" + Velocity_array[len(Velocity_array)])

plt.show()
