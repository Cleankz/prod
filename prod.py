def ShopOLAP(N,items):
    
    for i in range(len(items)):
        if len(items) == 0:
            break
        num = 0
        lst = items[0].split(" ")
        items.pop(0)
        item = lst[0]
        num = num + int(lst[1])
        for j in items:
            if item in j:
                const = j.split(" ") # l - const
                try:
                    num = num + int(const[1])
                except OverflowError:
                    print("Result is too big!")
                items.pop(items.index(j))
        result = []
        result.append(item + " " + str(num))
    result.sort()
    return result
