def main():
    lista = [47, 49, 51, 49, 60, 46, 50, 58, 46, 55, 45, 47, 42, 42, 68, 53, 56, 56, 35, 43, 54, 76, 55, 50, 68, 49, 46, 56, 37, 38, 69, 62, 60, 50, 70, 72, 62, 66, 49, 46, 62, 52, 43, 61, 53, 51, 49, 30, 52, 57, 69, 50, 55, 52, 54, 48, 60, 65, 37, 53, 48, 80, 63, 51, 69, 68, 63, 18, 59, 38, 43, 66, 52, 39, 75, 58, 45, 66, 49, 47, 46, 55, 45, 60, 46, 49]
    counter = [[],[],[],[],[],[],[],[],[]]
    for element in lista:
        if element >= 10 and element < 20:
            counter[0].append(1)
        elif element >= 20 and element <30:
            counter[1].append(1)
        elif element >=30 and element < 40:
            counter[2].append(1)
        elif element >=40 and element < 50:
            counter[3].append(1)
        elif element >= 50 and element < 60:
            counter[4].append(1)
        elif element >= 60 and element < 70:
            counter[5].append(1)
        elif element >= 70 and element < 80:
            counter[6].append(1)
        elif element >=80 and element < 90:
            counter[7].append(1)
        else: print(element)
            
    print("rango 1", len(counter[0]))
    print("rango 2", len(counter[1]))
    print("rango 3", len(counter[2]))
    print("rango 4", len(counter[3]))
    print("rango 5", len(counter[4]))
    print("rango 6", len(counter[5]))
    print("rango 7", len(counter[6]))
    print("rango 8", len(counter[7]))
    
    
    
    print(counter)
main()
