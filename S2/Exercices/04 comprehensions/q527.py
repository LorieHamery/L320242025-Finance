even_sum_tuples = [(x, y) for x in range(1, 11) for y in range(1, 11) if (x + y) % 2 == 0]
print(even_sum_tuples)
#on parcourt toutes les valeur de 1 jusuq'a 10 afin de faire toutes les combinaisons, on fixe x à 1 puis on parcourt tous les y puis on fixe x à 2 ...etc jusuq'à 11. 
#%2 == 0 ca veut dire qu'on garde que l'addition de x et y sont paires 