# Alan De Lara, Strings Motes Python

#string is a data type that hold any info surrounded by qoutation marks "" ''

#note= "Alan's class" #yes string

#name = input("What is your first name?"\n).strip().capitalize()

#print(f"Hello {name} well come to my program\n")

#print("this it you name"+ name)

sentence = "the quick brown fox jumps over the lazy dog."

#print(len(sentace))
#print(sentence[4])
start = sentence.find("brown")
length = len("brown fox") 
print(sentence[start:start+length])