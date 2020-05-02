 
class Book(object):


    def __init__(self,b_id,b_name,b_author,b_publication):
        
        self.b_id = b_id
        self.b_name = b_name
        self.b_author = b_author
        self.b_publication = b_publication
       
    def __del__(self):
        pass

    @property
    def b_id(self):
        return self.__b_id

    @b_id.setter
    def b_id(self, b_id):
        while True:
            try:

                if type(b_id)==str and b_id!=None and len(b_id)>=4: # VALIDTION OF INPUT
                    self.__b_id= b_id
                    break

                else:
                    raise Exception("")

            except Exception as e:
                b_id=input("\nError: Enter Valid Book ID : ")
                continue
       


    @property
    def b_name(self):
        return self.__b_name

    @b_name.setter
    def b_name(self, b_name):
        while True:
            try:
                if type(b_name)==str and b_name!=None and len(b_name)>=4: # VALIDTION OF INPUT
                    self.__b_name= b_name
                    break
                else:
                    raise Exception("")
                

            except Exception as e:
                b_name=input("\nError: Enter Valid Book Name : ")
                continue

    

    @property
    def b_author(self):
        return self.__b_author

    @b_author.setter
    def b_author(self,b_author):
        while True:
            try:
                if type(b_author)==str and b_author!=None and len(b_author)>=4: # VALIDTION OF INPUT
                    self.__b_author= b_author
                    break
                else:
                    raise Exception("")


            except Exception as e:
                b_author= input("\nError: Enter Valid Book Name : ")
                continue

    @property
    def b_publication(self):
        return self.__b_publication

    @b_publication.setter
    def b_publication(self, b_publication):
        while True:
            try:
                if type(b_publication)==str and b_publication!=None and len(b_publication)>=4: # VALIDTION OF INPUT
                    self.__b_publication = b_publication
                    break
                else:
                    raise Exception("")

            except Exception as e:
                b_publication=input("\nError: Enter Valid Book publication : ")
                continue

    def __str__(self):
        return self.b_id+"  " +\
        self.b_name+"  " +\
        self.b_author+"  " +\
        self.b_publication




    
   