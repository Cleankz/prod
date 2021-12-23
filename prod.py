def ShopOLAP(N,items):
    result = []
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
                l = j.split(" ")
                num = num + int(l[1])
                items.pop(items.index(j))
        result.append(item + " " + str(num))
    result.sort()
    return result