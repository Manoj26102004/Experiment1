import matplotlib.pyplot as plt

y_val = []
x_values = list(range(1, 11)) 

with open("input.txt", "r") as file:
    data = file.readlines()
    j=1
for i in range(0,30,3):
    a = int(data[i].strip())
    b = int(data[i+1].strip())
    c = int(data[i+2].strip())
    x = 0

    y = a * x**2 + b * x + c

    if(y):
        print(f"The model's prediction if it 'Rains' tomorrow is {y}%")
        y_val.append(y)
    else:
        print("Some error has occurred, contact developer")
    j+=1
plt.plot(x_values, y_val, marker='*', label="Rain Prediction")
plt.title("Model Prediction Values")
plt.xlabel("Dataset Values (By 10s)")
plt.ylabel("Prediction Value (y)")
plt.legend()
plt.grid(True)
plt.show()