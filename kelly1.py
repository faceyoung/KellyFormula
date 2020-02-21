import numpy as np
import matplotlib.pyplot as plt

players = 100
times = 10000
up = 0.6
down = 0.4
winners = 0
balance = 0.0

kelly = 1
print("Kelly is", kelly)

for j in range(players):
    m = np.zeros(times)
    m[0] = 100.0
    for i in range(1, times):
        if np.random.randint(2):
            m[i] = m[i - 1] * (1 + up) * kelly + m[i - 1] * (1 - kelly)
        else:
            m[i] = m[i - 1] * (1 - down) * kelly + m[i - 1] * (1 - kelly)

    if m[-1] > m[0]:
        winners += 1
    if m[-1] > balance:
        balance = m[-1]
    plt.semilogy(m)

print('The number of winners is', winners)
print(balance)
plt.xlabel('Times')
plt.ylabel('Balance')
plt.show()