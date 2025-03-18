strings = ["apple", "banana", "cherry"]
vowel_replaced = [''.join(['*' if char.lower() in 'aeiouy' else char for char in word]) for word in strings]
print(strings)
print(vowel_replaced)
#on veut remplacer toutes les voyelles par des * 
#char.lower pour changer toutes les lettres en minuscule 
#''.join coller les caractères des mots composant la chaîne de caractère. 
#print(vowel_replaced) pour imprimer le résultat 
#char=charactere 
#l.apppend => ajouter 
