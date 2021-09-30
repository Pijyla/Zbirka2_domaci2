"""
Dat je četvorocifreni prirodan broj. Napisati kod koji štampa cifru stotina tog broja.
Napomena: npr. za broj 4647 poslednja cifra 7 se dobija kao ostatak pri dijeljenju datog broja sa 10.
"""

cetvorocifeni_broj = int(input('Unesite cetvorocifreni broj '))

cifra_stotina = (cetvorocifeni_broj // 100) % 10
print ('Cifra stotina je ', cifra_stotina)
