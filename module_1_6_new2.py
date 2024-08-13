#работа со словарями
my_dict = {"Ivan":1978,"Tanya":1970, "Petr":1990,"Semen":1968}
print(my_dict)
print(my_dict["Tanya"])#вывод существующего ключа
print(my_dict.get("Nikita"))#вывод несуществующего ключа (без ошибки)
my_dict.update({"Alex":1983,#добавление двух значений
                "Olya":1984})
print(my_dict)
my_dict.pop("Semen")#удаление пары и вывод ее значения
print(my_dict)

#работа с множествами
my_set={1,1,1,'Яблоко','Яблоко','42,314','42,314'}
print(my_set)
print(my_set.update((13,(5,6,1.6))))
print(my_set.discard(1))
print(my_set)
