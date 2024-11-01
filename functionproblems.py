# Your challenge ....
# · Create a function to simplify writing to files.
# · Set the function to accept parameters
# - one for text
# - one for the name of a file
# · Add the code that will write the text out to the file.
def main():
    text=data()
    fileName(text)
    return
def data():
    text=input('')
    return text
def fileName(text):
    file=input('Enter the name of file with extension: ')
    accessmode=input('')
    with open(file,accessmode) as f:
        f.write(text)
        print(f)
        return

main()
    