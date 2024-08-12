import csv
import os

# Datei lesen und in eine Liste umwandeln
input_file = os.getcwd() + '/etl/wordlist.csv'
output_file = os.getcwd() + '/etl/sorted_wordlist.csv'

with open(input_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

# Konvertiere den zweiten Eintrag in jeder Zeile zu einem Float für die Sortierung
data.sort(key=lambda x: float(x[1]), reverse=True)

# Sortierte Daten in eine neue Datei schreiben
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Die Daten wurden erfolgreich in '{output_file}' sortiert und gespeichert.")
