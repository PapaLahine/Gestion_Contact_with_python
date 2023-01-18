import sqlite3

with sqlite3.connect("contacts.db") as connection:
    cursor = connection.cursor()
    
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS contacte  (id INTEGER PRIMARY KEY AUTOINCREMENT,nomComplet TEXT, email TEXT, telephone TEXT)" )
    connection.commit()


class GestionContact():
    def __init__(self):
        print("BIENVENUE DANS VOTRE APPLICATION DE CONTACT ")
        


     
            


    def ajouter_contacte(self):
         nomcomplet=input("Entrer votre nom\n")
         cursor.execute(
            "INSERT INTO contacte (nomComplet, email, telephone) VALUES(?, false,false)" ,(nomcomplet,))
         connection.commit()
         email=input("Votre email\n")
         cursor.execute(
            "INSERT INTO contacte (nomComplet, email, telephone) VALUES(false, ?,false)" ,(email,))
         connection.commit()
         tel=input("votre tel\n")
         cursor.execute(
            "INSERT INTO contacte (nomComplet, email, telephone) VALUES(false, false,?)" ,(tel,))
         connection.commit()
         
         print("Vos informations ont bien été enregistrees")
         
         
         
            
    def afficher_les_contactes(self):
        
            rows = cursor.execute("SELECT * FROM contacte").fetchall()
            connection.commit()
            print( rows)


    def afficher_un_contacte(self):
            row = cursor.execute(
                "SELECT * FROM contacte WHERE telephone=?").fetchone()
            connection.commit()
            print(row)


    def supprimer_contacte(self):
            telephone = input("Veuillez le numero de Telephone que vous voulez supprimer")
            cursor.execute(
                "DELETE FROM contacte WHERE telephone = ?",
                (telephone,)
            )
            connection.commit()
            print("Vos informations ont bien été enregistrees")
         


    def modifier_contacte(self):
            ancien_numero = input("Veuillez entrer votre ancien numero\n")
            nouveau_numero = input("Veuillez entrer votre nouveau numero\n")
            cursor.execute(
                "UPDATE contacte SET telephone = ? WHERE telephone = ?",
                (ancien_numero,nouveau_numero )
            )
            connection.commit()
            print("Vos informations ont bien été enregistrees")
         
            
            
    def menu(self):
        
        print("_________VOUS ETES DANS VOTRE APPLICATION DE GESTION DE CONTACT________") 
        choix=""
        print("___ 1- Enregistrer un contact __") 
        #print("___ 2- Afficher un contact __")
        print("___ 2- Afficher des contact __") 
        print("___ 3- Modifier un contact __") 
        print("___ 4- Supprimer un contact __")
        print("___ 5- Quitter l'appli  __")
        choix=input("Faites votre choix\n")
        
        if choix=="1":
            self.ajouter_contacte()
            self.menu()
        
        elif choix=="2":
            self.afficher_les_contactes()
            self.menu()
        elif choix=="3":
            self.modifier_contacte()
            self.menu()
        elif choix=="4":
            self.supprimer_contacte()
            self.menu()
        elif choix=="5":
            exit()
            
        else:
            print('faite un bon choix!!!!!!')                    
                  
            
app=GestionContact()
app.menu()            