# Задание 2
A = int(input())
B = int(input())
if (A > 999 and A < 10000) and (B > 999 and B < 10000) and A < B:
  for i in range(A, B + 1):
    N_1 = i // 1000 
    N_2 = (i // 100) % 10
    N_3 = (((i // 10) % 100) % 10)
    N_4 = (((i % 1000) % 100) % 10)
    if (N_1 == N_4) and (N_2 == N_3):
      print(i)
else:
  print("Введённые данные некорректны.")
