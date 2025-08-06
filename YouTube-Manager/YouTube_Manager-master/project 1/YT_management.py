import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
               test= json.load(file)
               print(type(test))
               return test
    except FileNotFoundError:
        return []
        
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)   
             
def list_all_videos(videos):
    print("\n")
    print("*" * 100)
    for index,video in enumerate(videos,start=1):
        print(f"{index}.{video['name']},duration:{video['time']}")
        print("\n")
        print("*" * 100)
         
def  add_videos(videos):
    name=input("enter video name: ")
    time=input("enter video time: ")
    videos.append({"name":name,"time":time})
    save_data_helper(videos)
def update_videos(videos):
    list_all_videos(videos):
        index=int(input("enter the video no. to be update"))
        if 1<= index <= len(videos):
            name=input("enter new video name: ")
            time=input("enter the new video time: ")
            videos[index-1]={'name':name,'time':time}
            save_data_helper(videos)
        else:
            print("inavlid index selected")    
            
        
def delete_videos(videos):
    list_all_videos(videos)
    index=int(input("enter the video no.to be deleted"))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("invalid index is selected")    
    
def main():
    videos = load_data()
    while True:
        print("\n YOUTUBE MANAGER |choose an option ")
        print("1.List all you tube viodeos ")
        print("2.Add youtube video")
        print("3.Update a youtube videos details")
        print("4.Delete a youtube video")
        print("5.Exit an app")
        choice=int(input("Enter your chioce: "))
        print(videos)
    
    
        match choice:
             case 1:
                  list_all_videos(videos)
             case 2:
                  add_videos(videos)
             case 3:
                  update_videos(videos)
             case 4:
                 delete_videos(videos)
             case 5:
                 break
             case _:
                 print("Invalid choice")
            
if __name__ == "__main__":
    main()         
         
         
         
