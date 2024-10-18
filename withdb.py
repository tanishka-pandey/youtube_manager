import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor= conn.cursor()

cursor.execute(''' 
   CREATE TABLE if NOT Exists videos(
   id INTEGER PRIMARY KEY,
   name TEXT NOT NULL,
   time TEXT NOT NULL)  
''')

def show_videos():
    cursor.execute("SELECT * FROM  videos ")
    for row in cursor.fetchall():
        print(row)
        
def list_videos():
    cursor.execute("SELECT * FROM  videos ")
    for row in cursor.fetchall():
        print(row)
        
def add_videos(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    conn.commit()
    
def update_videos(video_id,name,time):
    cursor.execute("UPDATE videos SET name= ? , time= ? WHERE  ID = ? ",(name,time,video_id))
    conn.commit()
    
def delete_videos(video_id):
    cursor.execute("DELETE videos WHERE ID = ?",(video_id,))
    conn.commit()

def main():
    while True :
        print("\n Youtube Manager || Choose an option ")
        print("1. Show all video ")
        print("2. List all youtube videos ")
        print("3. Add a youtube video ")
        print("4. Update a youtube video details ")
        print("5. Delete  a youtube video ")
        print("6. Exit the app ")
        choice= input ("Enter your choice: ")
        
        if choice== '1':
            show_videos()
        
        elif choice== '2':
            list_videos() 
        
        elif choice== '3':
            name= input("Enter the video name:")
            time= input("Enter the video time:")
            add_videos(name,time)
            
        elif choice== '4':
            video_id =input("Enter the video id to be updated:")
            name= input("Enter the video name:")
            time= input("Enter the video time:")
            update_videos(video_id,name,time)
            
        elif choice== '5':
            video_id =input("Enter the video id to be deleted:")
            delete_videos(video_id)
            
        elif choice== '6':
            break
        
        else:
            print("Oops ! you have entered a wrong choice.")
     
    conn.close()
    

if __name__ == "__main__" :
    main()