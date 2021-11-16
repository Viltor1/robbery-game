import math
village=[]
day=[]
def robbery (resourses,armyCapacity):
    result=[]
    sumResourses = sum(resourses) # общее количество ресурсов в деревне
    if sumResourses > armyCapacity:# В случае, если грузоподъемность меньше количества ресурсов в деревне

        proportion = armyCapacity/sumResourses #Определение рациональной пропорции
        floatResult = [i*proportion for i in resourses] #Определение сколько каждого ресурса можно унести с учётом пропорции
        day = [math.trunc(floatResult[i]) for i in range(len(floatResult))] #Целые числа сворованных товаров
        remain = armyCapacity-sum(day) #Cколько ещё пространства осталось

        remainders = [i%1 for i in floatResult]
        # remain = round(sum(remainders)) #ost
        for j in range(remain): #Для каждого из незадейственных мест
            for i in range(len(remainders)): #Каждый из ресурсов будет добавляться лишь единожды
                if remainders[i] == max(remainders): # Определяем найболее важный для сохранения пропорции ресурс
                    remainders[i] = -1 # Более не используем этот ресурс
                    floatResult[i] = math.ceil(floatResult[i]) #Фактически добавляем этот ресурс к тем, что украли
                    break
        for i in range(len(floatResult)): # Для оставшихся не добавляем ресурс в украденное
            result.append(math.trunc(floatResult[i]))
        return result
    else: #В случае, если ресурсов в общем меньше, чем доступного места
        result = resourses
        return result



print('Количество наименовании и количество каждого ресурса')
vsego = int(input())# Ввод количества наименований ресурсов
for i in range(vsego):
    village.append(int(input()))
print('Введите грузоподъемность армии')
armyCapacity = int(input())
# village= [100 , 300, 25,23,545,1]
# armyCapacity = 300
print(robbery(village,armyCapacity))