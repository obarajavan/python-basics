#open(filename,made)
#modes-r-read,w-write,a-append,x-create
x=open("demo.txt","w")
x.write("This is python file handling")
x.close()
#append
y=open("demo.txt",'a')
y.write('\nThis is some appended text')
y.close()
#read
z=open("demo.txt",'r')
(z.read())
z.close()
#x
file=open("example.txt",'x')
file.write("hello python")
file.write("This is python")
file.close()