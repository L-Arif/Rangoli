def print_rangoli(size):
    import string
    
    huruf = string.ascii_lowercase
    baris = []
    
    for i in range(size):
        pola = "-".join(huruf[i:size])
        baris.append((pola[:0:-1] + pola).center(4 * size - 3, "-"))
        
    print("\n".join(baris[:0:-1] + baris))
    
    

n = int(input())
print_rangoli(n)
