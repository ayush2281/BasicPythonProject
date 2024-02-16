names = []
phone_numbers = []
num = 3

for i in range(num):
    name=input("Name: ")
    phone_number = input("Phone Number: ")

    names.append(name)
    phone_numbers.append(phone_number)

print("\nName\t\tPhone Number\n")

for i in range(num):
    print("{}\t\t\t{}".format(names[i],phone_numbers[i]))

search_terms = input("\nEnter the search terms: ")
if search_terms in names:
    index=names.index(search_terms)
    phone_numbers = phone_numbers[index]
    print("Names {}\t, Phone Number\t: {}".format(search_terms,phone_numbers))
else:
    print("Name Not Found")
