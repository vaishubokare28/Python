#Q.1)write a python program that writes a list of strings to a file each string on a new line by using functional programming

def list_of_string(file1,list1):
    pass
#to write the file
    
    f=open(file1,"w")
    for i in list1:
        f.write(i+"\n")
        
list_of_string(file1="fruits.txt",list1=['mango','banana','apple'])        

    

#Q.2)write a python program to append a string to an existing file
def appendfile(file2,string1):
    pass
    f=open(file2,"a")
    f.write("\n"+string1)

appendfile(file2="colors.txt",string1="purple")



#Q.3)write a python program to copy the contents of the file to another

def copy(sourcefile,destination):
    pass
    #read the data first in file1
    f=open("file1.txt",'r')
    data=f.read()
    #write this data in newfile1
    f=open("newfile1.txt",'w')
    f.write(data)
copy(sourcefile="file1.txt",destination="newfile.txt")



#Q.4)write a python program to read a text file and count the occurences
def count_word(color1,words):
    pass
    f=open("colors.txt",'r')
    content=f.read().lower()
    words_count=content.split().count(words_count.lower())

   # print(f"the word{count} appears {words_count}in the colors.txt file")
    print(words_count)
count_word(color1="colors.txt",words="purple")    


#Q.5)count the number of characters, count the numbers of words, number of lines
#no of digits