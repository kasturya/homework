immutable_var = 1, 2, 'carrot', True
print(immutable_var)
print(type(immutable_var))

#immutable_var[0]=4
#print(immutable_var)
#Не получается, так как объекты не изменяются в кортеже

mutable_list = [1, 2, 'carrot', True]
mutable_list [0] = 2
print(mutable_list)
mutable_list [2] = 'notcarrot'
print(mutable_list)
