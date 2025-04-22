import pymysql
class DigitalAssetManager:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            passwd='Indhu',
            db='asset_db',
        )
        print("Connected to the digital Asset Database")

    def Add_Asset(self,asset_id,name,asset_type,file_size,last_modified):
        q="""INSERT INTO assets (asset_id, name, asset_type, file_size, last_modified) VALUES (%s, %s, %s, %s, %s)"""
        cursor = self.connection.cursor()
        c=cursor.execute(q, (asset_id, name, asset_type, file_size, last_modified))
        if c!=0:
            print("Asset added sucessfully")
        else:
            print("error ~ ",c)
        pass
        cursor.close()
    
    def View_Asset(self):
        q = """SELECT * FROM assets"""
        cursor = self.connection.cursor()
        c=cursor.execute(q)
        if c!=0:
            print("asset_id | name | asset_type | file_size | last_modified")
            results=cursor.fetchall()
            for i in results:
                for j in i:
                    print(j,end=" ")
                print()
        else:
            print("error ~ ",c)
        self.connection.commit()        
        cursor.close()

    def Update_Asset(self,asset_id,new_name,new_type):
        q="""UPDATE assets SET name = %s, asset_type = %s WHERE asset_id = %s"""
        cursor=self.connection.cursor()
        c=cursor.execute(q,(new_name,new_type,asset_id))
        if c!=0:
            print("Asset updated sucessfully")
        else:
            print("error ~ ",c)
        self.connection.commit()
        cursor.close()

    def Search_Asset(self,key,name,type):
            q="""SELECT * FROM assets WHERE asset_id = %s OR name = %s OR asset_type = %s"""
            cursor = self.connection.cursor()
            c=cursor.execute(q,(key,"%"+name+"%","%"+type+"%"))
            row_count=cursor.fetchall()
            if c==0:
                print("No records found")
            else:
                print("asset_id | name | asset_type | file_size | last_modified")
                for row in row_count:
                   print(row)
            cursor.close()
    
    def Delete_Asset(self,asset_id):
        q="""DELETE FROM assets WHERE asset_id = %s"""
        cursor=self.connection.cursor()
        c=cursor.execute(q,(asset_id))
        if c!=0:
            print("Asset deleted sucessfully")
        else:
            print("error ~ ",c)
        self.connection.commit()
        cursor.close()
    
    def close(self):
        self.connection.close()
        print("App closed!")