# we can use database to store the images of authorised persons 
        # thre will be two section in database 
                #  1.Permanent : having permanent data which can't be deleted ( for history purpose & historical records )
                #  2. Changable : In which new client data will be stored and client info will be deleted as client leaves the 
                #                 orgamization & algo will be run on this data .
                # 
import os

class register:
    def __init__(self , client_name , client_id ):
        self.client_name = client_name  # dir where the person images get stored 
        self.client_id = client_id
        self.mainpath = "Data"

    def create_dir(self):
        try:
            self.path = os.path.join(self.mainpath , str(self.client_id) + "__"+ str(self.client_name))
            os.makedirs(self.path , exist_ok=True)
        except Exception as e:
            print('Exception Occured : classname : register , method : create_dir')
            raise e 




        
        