#Reverse Words in String
st="I love coding"
# Output:"coding love I"

def revWords(st):
   words=st.split()
   
   li=list(words)
   
   li.reverse()
  
   
   return (" ".join(li))
    
    
    
print(revWords(st))
    




def revWords(st):
    words = st.split()
    words.reverse()
    return " ".join(words)

def revWords(st):
    return(" ".join(st.split()[::-1]))