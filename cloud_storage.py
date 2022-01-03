import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)  

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token ="sl.A_Lw91ZgPBdMmU7FWaJS1lPgjCtn8pJ5KGw9wFi9y12XW8KR90g_BH2_QY5flAOZBQu47p3cAwC3pkghIS6IRNXg-VA_VEQwdSgbSqSWtsXNZaXFbt3TDvy57W4WF9S5PRMJ72g"
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer:- ")
    file_to = input("enter the full path to upload to dropbox:-")

    transferData.upload_file(file_from,file_to)
    print("file has been moved !!!")    
    
    
main()