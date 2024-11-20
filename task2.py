def find_duplicates(data):
    duplicates = []
    for i in range(len(data)):
        for j in range(i, len(data)):  
            if data[i] == data[j] and data[i] not in duplicates:
                duplicates.append(data[i])
    return duplicates
