# with open('example.py') as content:
#     print(content.read())

# with open('myfile.txt', 'w') as content:
#     # content.write("Here is some Text \n This should be in next line")
#     content.write('MMM')


with open('example.py', 'a') as content:
    content.write("\nprint('Using File Handling')")

