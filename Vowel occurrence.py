vowels=['a','e','i','o','u']
count=[0,0,0,0,0]
sentence=input("Enter the sentence to search for vowels: ")
found=[]
for letter in sentence:
    if letter in vowels:
        count[vowels.index(letter)]+=1
        if letter not in found:
            found.append(letter)
print("Vowels in Sentence ",found)
print("Each Vowel repeated as ",count)
print("The number of different vowels present in",sentence,"is",len(found)) 
