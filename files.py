fileName='demo.txt'#we have to define including extension to create file
accessMode='w'#accessmode defines how we want to open the file like read,write,append,
data=input()
myFile=open(fileName,mode=accessMode)
myFile.write(data)
myFile.close
print('file created successfully')