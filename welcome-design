height, width = map(int, input().split()) #MANDATORY:(1)"height" must be an odd number;(2)"width" must be three times of height

decoration = ".|."
pattern = int((height-1)/2)
max_decoration = (2*pattern)-1


#top pattern
for i in range(pattern):
    c = (2*i)+1
    print((c*decoration).center(width,"-"))
    
#text
print("WELCOME".center(width,"-"))

#bottom pattern
for i in range(pattern):
    c = max_decoration - (2*i)
    print((c*decoration).center(width,"-"))    
