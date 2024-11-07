somma = 0

# Ciclo che continua finché l'utente non inserisce 0
while True:
    # Chiedi all'utente di inserire un numero
    numero = int(input("Inserisci un numero intero (0 per terminare): "))
    
    # Se il numero inserito è 0, esci dal ciclo
    if numero == 0:
        break
    
    # Aggiungi il numero alla somma
    somma += numero

