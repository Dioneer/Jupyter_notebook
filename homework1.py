# Задача 2
storage = dict()

def member_fruits():
	flag=True
	while flag:
		choise = input("Если хотите записать фрукт и его количество нажмите 1, для выхода нажмите любую цифру: ")
		match(choise):
			case "1":
				name = input("Введите название фрукта: ")
				amount = input("Введите количесвто фруктов: ")
				storage[name] = int(amount)
			case "0":
				print("Goodbye!")
				flag=False
			case _:
				print("Goodbye!")
				flag=False

def counter_fruits():
    count = 0
    member_fruits()
    print(storage)
    for v in storage.values():
        count+= v
    print(count)
    return count
counter_fruits()

# Задача 3
arr = [100, 125, -90, 345, 655, -1, 0, 200]
result = sum(i for i in arr if i > -1)
print(result)

# Задача 4.1
date = ['2021-09-14', '2021-12-15', '2021-09-08', '2021-12-05', '2021-10-09', '2021-09-30', '2021-12-22', '2021-11-29', '2021-12-24', '2021-11-26', '2021-10-27', '2021-12-18', '2021-11-09', '2021-11-23', '2021-09-27', '2021-10-02', '2021-12-27', '2021-09-20', '2021-12-13', '2021-11-01', '2021-11-09', '2021-12-06', '2021-12-08', '2021-10-09', '2021-10-31', '2021-09-30', '2021-11-09', '2021-12-13', '2021-10-26', '2021-12-09']
cost = [1270, 8413, 9028, 3703, 5739, 4095, 295, 4944, 5723, 3701, 4471, 651, 7037, 4274, 6275, 4988, 6930, 2971, 6592, 2004, 2822, 519, 3406, 2732, 5015, 2008, 316, 6333, 5700, 2887]
print(f'Profit: {sum([cost[i] for i in range(len(date)-1) if "-11" in date[i]])}')

# Задача 4.2
def united_list(a: list, b: list)-> dict:
    united_dict = {}
    if(len(a)==len(b)):
        for i in range(len(a)):
            if(a[i].split('-')[1] in united_dict.keys()):
                united_dict[a[i].split('-')[1]] += b[i]
            else:
                united_dict[a[i].split('-')[1]] = b[i]
        print(united_dict)
    return united_dict
united_list(date, cost)