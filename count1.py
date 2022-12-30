file= open("intro.txt",'r')
read1=file.read()
word=read1.split(" ")
print(" list  of  words  in  a  text  file  :  ",word)
file = open("intro.txt", "rt")
data = file.read()
words = data.split()
print(' Number  of  words  in  a  text  file  : ', len(words))
import string
file=open('intro.txt')
text=file.read().split()
mydict={}
for word1 in text:
    if word1 not in mydict.keys():
        mydict[word1]=1
    else:
        count=mydict[word1]
        mydict[word1]=count+1
print( " Number of words repeated in a text file : " ,mydict)				
				
	