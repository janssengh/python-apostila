def ano_bissexto(ano):
    if ano % 400 == 0:
        return True
    if ano % 100 == 0:
        return False
    if ano % 4 == 0:
        return True
    else:
        return False

print(ano_bissexto(1900))
print(ano_bissexto(2004))
print(ano_bissexto(2024))
        
        
