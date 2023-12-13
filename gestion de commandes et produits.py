import copy

class gestion_produit():
    _nbrp = 0
    def __init__(self , id , des , pa , pv , nbr ):
        self.__id = id
        self.__des = des
        self.__pa = pa
        self.__pv = pv
        self.__nbr = nbr
        gestion_produit._nbrp += 1

    #GETTERS
    def getid(self):
        return self.__id
    
    def getdes(self):
        return self.__des
    
    def getpa(self):
        return self.__pa
    
    def getpv(self):
        return self.__pv
     
    def getnbr(self):
        return self.__nbr
    
    def getnbrp():
        return gestion_produit._nbrp
    
    #SETTERS
    def setid(self,id):
        self.__id = id
    
    def setdes(self,des):
        self.__des = des
    
    def setpa(self,pa):
        self.__pa = pa
    
    def setpv(self,pv):
        self.__pv = pv
     
    def setnbr(self,nbr):
        self._nbr = nbr
    


    #method
    def __str__(self):
        return(f" nombre en stock :{self.__nbr} \n  designation :{self.__des}\n prix achat :{self.__pa} \n prix de vente :{self.__pv}")

    def __eq__(self,other):
        return self.__id == other.__id

    

class gestion_commande():
    def __init__(self , date , ep , qu):
        
        self.__date = date
        self.__ep = copy.copy(ep)
        self.__qu =qu

    #GETTERS
    def getdate(self):
        return self.__date
    
    def getep(self):
        return self.__ep
    
    def getqu(self):
        return self.__qu
    
    #SETTERS
    def setid(self,date):
        self.__date = date
    
    def setdes(self,ep):
        self.__ep = ep
    
    def setpa(self,qu):
        self.__qu = qu

    #method
    def __str__(self):
        return(f" Date :{self.__date} \n Produit :{str(self.__ep)} \n quantité :{self.__qu}")

    def __eq__(self,other):
         return self.__date == other.__date and self.__ep == other.__ep and self.__qu == other.__qu
         

    




p1  = gestion_produit(1233 , "azeerty" , 456 , 3456 , "stock"  )   
p2  = gestion_produit(123 , "azeerty" , 456 , 3456 , "stock" )   
print(p1)
print(p2)
print(f"nombre de produit :{gestion_produit.getnbrp()}")

if p1 == p2:
        print("equal.")

else :
        print("not equal")

c1 = gestion_commande("12/10/2023", p2 , 123)
c2 = gestion_commande("12/10/2023", p2 , 123)

print(c1)
if c1 == c2:
        print("equal.")

else :
        print("not equal")


