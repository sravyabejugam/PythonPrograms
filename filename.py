filename=input()
extension=filename.split('.')
if extension[1]=='py':
    print("The extension of file is python")
elif extension[1]=='java':
    print("The extension of file is java")
elif extension[1]=='c':
    print("The extension of file is c")
else:
    print("enter a valid file")
    
