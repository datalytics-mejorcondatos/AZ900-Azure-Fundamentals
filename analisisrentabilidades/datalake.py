from azure.storage.blob import BlobServiceClient

class InteractuarDataLake:

    def __init__(self,ACCOUNT_NAME,ACCOUNT_KEY):
        self.ACCOUNT_NAME = ACCOUNT_NAME
        self.ACCOUNT_KEY = ACCOUNT_KEY
        self.CREDENTIAL = {"account_name": self.ACCOUNT_NAME, "account_key": self.ACCOUNT_KEY}
        self.ACCOUNT_URL = f"https://{self.ACCOUNT_NAME}.blob.core.windows.net"

    def blob_client(self):

        blob_client = BlobServiceClient(
            account_url= self.ACCOUNT_URL,
            credential= self.CREDENTIAL)
        
        self.blob_client = blob_client

    def escritura_container(self,file_path,CONTAINER_NAME,BLOB_NAME, overwrite=True):

        blob_client = self.blob_client.get_blob_client(
            container=CONTAINER_NAME,
            blob=BLOB_NAME,
            )

        # Upload the created file
        with open(file=file_path, mode="rb") as data:
            blob_client.upload_blob(data,overwrite = overwrite)
        
        print("Se escribio correctamente")

    def lectura_container(self,download_file_path,CONTAINER_NAME,file_path):

        # download_file_path = 'Fondos_blob.csv'
        container_client = self.blob_client.get_container_client(container= CONTAINER_NAME)
        
        # List the blobs in the container
        blob_list = container_client.list_blobs()

        if file_path in [blob.name for blob in blob_list]:

            print("\n Descargando el blob en \n\t" + download_file_path)
            with open(file=download_file_path, mode="wb") as download_file:
                download_file.write(container_client.download_blob(file_path).readall())
            
            print("Descarga completa")

        else:
            print(f"El archivo {file_path} no existe en el contenedor {CONTAINER_NAME}")
        