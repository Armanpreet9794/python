import numpy as np

data=np.genfromtxt("sensor_data.csv", delimiter=",", skip_header=1, usecols=(1,2,3,4))
print(data)
print(data.dtype)
print(data.ndim)
print(data. shape)
temperature=data[:,0]
distance=data[:, 1] 
battery=data[:,2]
humidity=data[:,3]

# ques 1

# average
print("avg_t=",sum(temperature) /10000)
print("avg_d=",sum(distance)/10000) 
print("avg_b=",sum(battery)/10000) 
print("avg_h",sum (humidity)/10000)

# minimum
print("min_t",min (temperature))
print("min_d",min(distance)) 
print ("min_b",min (battery))
print("min_h",min (humidity))

# maximum
print("max_t",max(temperature))
print("max_d",max(distance)) 
print("max_b",max(battery))
print("max_h",max(humidity))

# ques 2
data_2=np.genfromtxt("sensor_data.csv",dtype=str,delimiter=",",skip_header=1,usecols=(0))
htindex=np.argmax(temperature)
print("highest temp at ",data_2[htindex])
data_3=np.genfromtxt("sensor_data.csv",delimiter=",",skip_header=1,usecols=(3))
below_30=data_3<30
count=np.sum(below_30)
print ("battery below 30:",count)
#3 
with open("new_data.csv",'w')as d:
    d.write(f"average of temp{sum(temperature)/10000}") 
    d.write(f"min temperature {min(temperature)}")