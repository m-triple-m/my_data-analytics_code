def createFile(filename, data):
    with open(filename, 'w') as content:
        content.write(data)