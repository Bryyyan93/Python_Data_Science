genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", \
                "R&B", "progressive rock", "disco") 
print(len(genres_tuple))
print(genres_tuple[7])

pattern = genres_tuple[7]

print(pattern.find("s"))

shopping_list = []
print(shopping_list)
items = ["Watch", "Laptop", "Shoes", "Pen", "Clothes"]
shopping_list.extend(items)
print(shopping_list)
items = "Football"
shopping_list.append(items)
print(shopping_list)
print(shopping_list[1:3])

shopping_list[3] = "Notebook"
print(shopping_list)

del(shopping_list[-1])

A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])

print("the sum of A is: ", sum(A))
print("the sum of B is: ", sum(B))

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3 = album_set1.union(album_set2)

print("the union is: ", album_set3)


soundtrack_dic = {"The Bodyguard":"1992", "Saturday Night Fever":"1977"}
print(soundtrack_dic)
print(soundtrack_dic.values())

album_sales_dict = {"Back in Black":50, "The Bodyguard":50, "Thriller":65}
print(album_sales_dict)

print(album_sales_dict["Thriller"])

inventory = {}

ProductNo1 = "Mobile Phone"
ProductNo1_quantity = 5
ProductNo1_price = 20000
ProductNo1_releaseYear= 2020

ProductNo2 = "Laptop"
ProductNo2_quantity = 10
ProductNo2_price = 50000
ProductNo2_releaseYear= 2023

inventory["ProductNo1"]= ProductNo1
inventory["ProductNo1_quantity"]= ProductNo1_quantity
inventory["ProductNo1_price"]= ProductNo1_price
inventory["ProductNo1_releaseYear"]=ProductNo1_releaseYear

inventory["ProductNo2"]= ProductNo2
inventory["ProductNo2_quantity"]= ProductNo2_quantity
inventory["ProductNo2_price"]= ProductNo2_price
inventory["ProductNo2_releaseYear"]=ProductNo2_releaseYear
print(inventory)

print("ProductNo1_releaseYear" in inventory)
print("ProductNo2_releaseYear" in inventory)

del(inventory["ProductNo1_releaseYear"])
del(inventory["ProductNo2_releaseYear"])


lista = [10, 20, 30]
tupla = (10, 20, 30)

lista[0] = 99
print(lista)  # ¿Funciona?

#tupla[0] = 99
print(tupla)  # ¿Funciona?

A = [1, 2, 2, 3, 3, 3]
B = set(A)

print(A)  # Lista
print(B)  # Set

print(len(A))  # ¿Cuántos elementos tiene?
print(len(B))  # ¿Cuántos tiene ahora?