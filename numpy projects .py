import numpy as np
temps_2024 = np.array([14, 18, 19, 16, 14, 16, 17, 14, 18, 29, 27, 28])
temps_2025 = np.array([12, 13, 15, 15, 16, 13, 19, 18, 26, 18, 18, 27])
mean_2024 = np.mean(temps_2024)
mean_2025 = np.mean(temps_2025)

hottest_month = np.argmax(temps_2025) + 1
coldest_month = np.argmin(temps_2025) + 1

print("average temperature 2024: ", mean_2024)
print("aveage temperature 2025: ", mean_2025)
print("hottest month (2025): ", hottest_month)
print("Difference (2025-2024):", temps_2025 - temps_2024)















