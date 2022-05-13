def purge_quote(data):
    for i in range(len(data)):
        data[i] = str(data[i]).replace("\'"," ")
    return data