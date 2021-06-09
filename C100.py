import dropbox
import cv2
from datetime import datetime


class Atm(object):

    def __init__(self,name,bankbalance,pin,wallet):
        
        self.name = name
        self.bankbalance = bankbalance
        self.pin = pin
        self.wallet = wallet

    def startAtm(self):
        print("Hello", self.name,".")


    def withDraw(self,withamount):
        withdrawamount = withamount
        if(self.bankbalance>=withdrawamount):
            self.bankbalance-=withdrawamount
            self.wallet+=withdrawamount
            print(withamount,"withdrawed! You have",self.wallet,"with you, and bank balance is",self.bankbalance)
            print("Thanks for using the ATM")
        else:
            print("Withdraw amount can't be more than bank balance")
    
    def deposit(self,depamount):
        depositamount = depamount
        if(depositamount<self.wallet):
            self.bankbalance+=depositamount
            self.wallet-=depositamount
            print(depositamount,"deposited! You have",self.wallet," with you, and new bank balance is", self.bankbalance)
            print("Thanks for using the ATM")
        else:
            print("You cannot deposit an amount of money more than what you have in your wallet!")
   
        
    
def startAtm():
    myname = input("Enter username")
    mypin = 1569
    print("Hi, ",myname)
    pininput = int(input("Enter your pin: "))
    myatm = Atm(myname,50000,pininput,100000)
    mychances = 3
    while(mychances>0):
        if(pininput==mypin):

           

            choice = input("Press w to withdraw, d to deposit and q to quit: ")
    
            if(choice=="w"):
                myamount = int(input("Enter amount to withdraw"))
                myatm.withDraw(myamount)
                video = cv2.VideoCapture(0)
                i = True
                while(i):
                    ret,frame = video.read()
                    now = datetime.now()
                    nowfile= "transaction"+str(now)+".png"
                    cv2.imwrite(nowfile,frame)
                    i = False
        
                video.release()
                cv2.destroyAllWindows()
                
                access_token = 'sl.AxM71HFG2hgkp__J3yFF2FmEkc8xfH2GNEnP7uc1gfY2_qR_h3D72O245Hl77JX27kGhs7tu59TLVcbBmYgi3-s6F_nFz7psz2CXwutMouLYvGfnb4NpV0Mu6g5EK-l2jqCd7JLhugE'


                file_from = nowfile
                file_to = '/transactions/transaction'+str(datetime.now())+".png" # The full path to upload the file to, including the file name

                # API v2  dbx = dropbox.Dropbox(self.access_token)
                dbx = dropbox.Dropbox(access_token)

                with open(file_from, 'rb') as f:
                    dbx.files_upload(f.read(), file_to)

                print("file uploaded!")


                
            elif choice=="d":
                depamount=  int(input("Enter amount to deposit"))
                
                myatm.deposit(depamount)
                video = cv2.VideoCapture(0)
                i = True
                while(i):
                    ret,frame = video.read()
                    now = datetime.now()
                    nowfile= "transaction"+str(now)+".png"
                    cv2.imwrite(nowfile,frame)
                    i = False
        
                video.release()
                cv2.destroyAllWindows()
                
                access_token = 'sl.AxM71HFG2hgkp__J3yFF2FmEkc8xfH2GNEnP7uc1gfY2_qR_h3D72O245Hl77JX27kGhs7tu59TLVcbBmYgi3-s6F_nFz7psz2CXwutMouLYvGfnb4NpV0Mu6g5EK-l2jqCd7JLhugE'


                file_from = nowfile
                file_to = '/transactions/transaction'+str(datetime.now())+".png" # The full path to upload the file to, including the file name

                # API v2  dbx = dropbox.Dropbox(self.access_token)
                dbx = dropbox.Dropbox(access_token)

                with open(file_from, 'rb') as f:
                    dbx.files_upload(f.read(), file_to)

                print("file uploaded!")

            else:
                print("bye!")
                break
        else:
            print("Wrong! Please try again later")
            break




startAtm()

        

