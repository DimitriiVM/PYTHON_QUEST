# ЗАДАНИЕ: Поиск дубликатов в массиве
# Напишите функцию, которая принимает список чисел и возвращает количество повторений каждого элемента.
import random
arr = [random.randint(0, 10) for i in range(20)]
print(arr)

#arr = [ i for i in  range(20)]
#print('Далее введите массив чисел')
#for i in range(0, 20):
#	arr[i] = input()
#print(arr)

def DuplicateSearch(List = []):
	Sort = []
	for i in range(len(List)):
		number = 0		
		if List[i] not in Sort:
			Sort.append(List[i])
			for q in  range(0, len(List)):
				if List[i] == List[q]:
					number += 1
			print(f'Число: {List[i]} в массиве повторяется {number} раз')

DuplicateSearch(arr)
