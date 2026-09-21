meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "BY THE WAY": "comunque... inoltre...",
            "ah bho non lo so": "dubbio o incertezza",
            "CREEPY": "spaventoso, inquietante"
            }

parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")

if parola in meme_dict.keys():
    print(meme_dict[parola])
else:
    print("compà, non è stata trovata la parola")
