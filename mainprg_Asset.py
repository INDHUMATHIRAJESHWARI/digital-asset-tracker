import DB_Asset
from datetime import datetime

def main():
    db=DB_Asset.DigitalAssetManager()

    while True:
        print("1. Add Asset\n2. View Asset\n3. Update Asset\n4. Search Asset\n5. Delete Asset\n0. Exit")

        ch=int(input("Enter your choice: "))

        if ch>5:
            print("Invalid choice!")

        elif ch==1:
            asset_id=int(input("Enter Asset ID: "))
            name=input("Enter Asset Name: ")
            asset_type=input("Enter Asset Type: ")
            file_size=input("Enter File Size: ")
            last_modified=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            db.Add_Asset(asset_id,name,asset_type,file_size,last_modified)

        elif ch==2:
            db.View_Asset()

        elif ch==3:
            asset_id=int(input("Enter Asset ID to update: "))
            new_name=input("Enter new Asset Name: ")
            new_type=input("Enter new Asset Type: ")
            db.Update_Asset(asset_id,new_name,new_type)

        elif ch==4:
            k=input("Enter Asset ID: ")
            name=input("Enter Asset Name to search: ")
            type=input("Enter Asset Type to search: ")
            db.Search_Asset(k,name,type)

        elif ch==5:
            id=int(input("Enter Asset ID to delete: "))
            db.Delete_Asset(id)

        elif ch==0:
            db.close()
            break
main()


"""
python mainprg_Asset.py
Connected to the digital Asset Database
1. Add Asset
2. View Asset
3. Update Asset
4. Search Asset
5. Delete Asset
0. Exit
Enter your choice: 1
Enter Asset ID: 1002
Enter Asset Name: song.mp3
Enter Asset Type: audio
Enter File Size: 23.56
Asset added sucessfully
1. Add Asset
2. View Asset
3. Update Asset
4. Search Asset
5. Delete Asset
0. Exit
Enter your choice: 2
asset_id | name | asset_type | file_size | last_modified
1001 kit.png photo 2.50 2025-04-20 16:43:53
1002 song.mp3 audio 23.56 2025-04-20 17:47:51
1003 pop.pm3 audio 4.50 2025-04-20 17:39:44
1. Add Asset
2. View Asset
3. Update Asset
4. Search Asset
5. Delete Asset
0. Exit
Enter your choice: 3
Enter Asset ID to update: 1001
Enter new Asset Name: kiwi.png
Enter new Asset Type: photo
Asset updated sucessfully
1. Add Asset
2. View Asset
3. Update Asset
4. Search Asset
5. Delete Asset
0. Exit
Enter your choice: 4
Enter Asset ID: 1002
Enter Asset Name to search:
Enter Asset Type to search:
asset_id | name | asset_type | file_size | last_modified
(1002, 'song.mp3', 'audio', Decimal('23.56'), datetime.datetime(2025, 4, 20, 17, 47, 51))
1. Add Asset
2. View Asset
3. Update Asset
4. Search Asset
5. Delete Asset
0. Exit
Enter your choice: 5
Enter Asset ID to delete: 1003
Asset deleted sucessfully
1. Add Asset
2. View Asset
3. Update Asset
4. Search Asset
5. Delete Asset
0. Exit
Enter your choice: 0
App closed!
"""