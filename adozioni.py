import tkinter as tk
from tkinter import filedialog

class Adozione:
    def __init__(self, tipo_animale, razza, nome, descrizione, contatti, foto):
        self.tipo_animale = tipo_animale
        self.razza = razza
        self.nome = nome
        self.descrizione = descrizione
        self.contatti = contatti
        self.foto = foto

    def to_html(self):
        foto_html = ""
        for foto in self.foto:
            if foto.startswith("http"):
                foto_html += f'<img src="{foto}" alt="Foto di {self.nome}" style="max-width: 300px;"><br>'
            else:
                foto_html += f'<img src="file://{foto}" alt="Foto di {self.nome}" style="max-width: 300px;"><br>'
        
        return f'''
            <!DOCTYPE html>
            <html lang="it">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Dettagli Adozione</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 20px;
                        background-color: #f5f5f5;
                    }}
                    .container {{
                        max-width: 600px;
                        margin: 0 auto;
                        background-color: #fff;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }}
                    h1 {{
                        text-align: center;
                        color: #333;
                    }}
                    p {{
                        margin-bottom: 15px;
                    }}
                    img {{
                        display: block;
                        margin: 0 auto;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>🐾 Dettagli Adozione 🐾</h1>
                    <p><strong>🐶 Tipo Animale:</strong> {self.tipo_animale}</p>
                    <p><strong>🐶 Razza:</strong> {self.razza}</p>
                    <p><strong>🐾 Nome:</strong> {self.nome}</p>
                    <p><strong>💬 Descrizione:</strong> {self.descrizione}</p>
                    <p><strong>📞 Info e Contatti:</strong> {self.contatti}</p>
                    <p><strong>📸 Foto:</strong></p>
                    {foto_html}
                </div>
            </body>
            </html>
        '''

def seleziona_immagini():
    root = tk.Tk()
    root.withdraw()  # Nasconde la finestra principale di tkinter

    # Apre una finestra di dialogo per selezionare i file immagine
    file_path = filedialog.askopenfilenames(title="Seleziona le immagini", filetypes=[("Immagini", "*.jpg *.jpeg *.png *.gif")])
    
    # Trasforma il percorso dei file in una lista di stringhe
    file_list = list(file_path)

    return file_list


def main():
    print("Benvenuto nel modulo di adozione!")
    tipo_animale = input("Seleziona il tipo di animale (cane o gatto): ").lower()
    if tipo_animale not in ['cane', 'gatto']:
        print("Tipo di animale non valido. Si prega di inserire 'cane' o 'gatto'.")
        return

    razza = input(f"Inserisci la razza del {tipo_animale}: ")
    nome = input(f"Inserisci il nome del {tipo_animale}: ")
    descrizione = input("Inserisci una breve descrizione: ")
    contatti = input("Inserisci informazioni e contatti per l'adozione: ")

    print("Seleziona le immagini dell'animale:")
    foto_locali = seleziona_immagini()
    foto_online = input("Inserisci URL delle foto separate da virgola (se disponibili): ").split(',')

    foto = foto_online + foto_locali
    
    adozione = Adozione(tipo_animale, razza, nome, descrizione, contatti, foto)
    
    # Chiediamo all'utente di inserire il nome del file per il salvataggio
    nome_file = input("Inserisci il nome del file per il salvataggio (senza estensione): ")
    nome_file += ".html"  # Aggiungiamo l'estensione .html al nome del file
    
    # Creazione del file HTML con encoding UTF-8
    with open(nome_file, "w", encoding="utf-8") as file:
        file.write(adozione.to_html())
    print(f"🎉 Dettagli dell'adozione sono stati salvati in '{nome_file}' 🎉")

if __name__ == "__main__":
    main()
