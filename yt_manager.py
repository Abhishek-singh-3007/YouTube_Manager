import json

def load_data():
    try:
        with open('Utube.txt', 'r') as file:
            test = json.load(file)
            print(type(test))
            return test

    except FileNotFoundError:
        return []

def save_video(videos):
    with open('Utube.txt', 'w') as file:
       json.dump(videos, file)

def all_videos(videos):
     print("\n")
     print("*" * 100)
     print("\n")
     for index, video in enumerate(videos, start=1):
        print(f"{index}.{video['name ']}, Duration: {video['time ']} ")
     print("\n")
     print("*" * 100)


def add_video(videos):
    v_name = input("Enter video name ")
    v_time = input("Enter lenght of the video ")
    videos.append({'name ': v_name, 'time ': v_time})
    save_video(videos)


def update_video(videos):
    all_videos(videos)
    index = int(input("Enter the video number want to update "))
    if 1 <= index <= len(videos):
        name = input("Enter the latest name of the video ")
        time = input("Enter the latest lenght of the video ")
        videos[index-1] = {'name ': name, 'time ': time}
        save_video(videos)
    else:
        print("Invalid index Selected ")


def delete_video_video(videos):
    all_videos(videos)
    index = int(input("Enter the index of the video want to be delete "))

    if 1 <= index <= len(videos):
        del videos[index-1]
        
        save_video(videos)
    else:
        print("Invalid index selected ")


def main():
    
    videos = load_data()
    while True:
        print("\n YouTube Manager  |   Please select your option ")
        print("1. List all Youtube videos available ")
        print("2. Add your favourite video in list ")
        print("3. Update your video list ")
        print("4. Delete video fro list ")
        print("5. Exist the App ")
        user_choice = input("Enter your choice ")
        # print(videos)


        match user_choice:
            case '1':
                all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()


