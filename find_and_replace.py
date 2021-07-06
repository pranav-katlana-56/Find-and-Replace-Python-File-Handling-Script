def new_file(sentence):
    newfile =open("result.txt" , "w")
    tobewritten = sentence.split(".",)
    for data in tobewritten:
    
        newfile.write(data + "\n")




def change(filee= "", word = "", changed_word =""):
    b= 0
    sentence = " "  
   
    File = open(filee)
    data = File.readlines()
    newlines = []
    for d in data:
    
        x = list(d.split())
        for c in x:
            if c == word:
                newlines.append(changed_word)
                    
            else:
                newlines.append(c)
        for q in x:
                sentence.join(q)    

        b += 1 
    for r in newlines:
        sentence = str(sentence) + " " + str(r)
    new_file(sentence)



        


def main():
  
    B = input("Enter File Name with Extention")
    C = input("Enter word to change")
    D = input("Enter changed word")
    change(B,C,D)
    
main()
