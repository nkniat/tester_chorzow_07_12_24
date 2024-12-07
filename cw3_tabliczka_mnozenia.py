# podwojna petla do tabliczki mnozenia
for i in range(15, 95):
    if i % 2 == 0:
        for j in range(5, 10):
            print(f"{i} x {j} = {i * j}")
    print()  #dla lepszej czytelnosci