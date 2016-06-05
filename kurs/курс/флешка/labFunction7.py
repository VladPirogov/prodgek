def nun_n(S,m):
    Si=S//m
    Sr=S%m
    if Si>0:
        return (nun_n(Si,m)+str(Sr))
    else:
        return (str(Sr))


print(nun_n(10,2))
