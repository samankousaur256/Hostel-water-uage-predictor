import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
water = [5000, 5100, 4900, 5200, 5300, 5250, 5400]

average = sum(water) / len(water)

print("average water usage =", average)
print("predicted next day water usage =", average)

plt.plot(days, water, marker='o')
plt.xlabel("days")
plt.ylabel("water usage (liters)")
plt.title("hostel water usage predictor")
plt.grid(True)
plt.show()