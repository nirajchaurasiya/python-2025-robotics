# file = open("youtube.txt", "w")
import json

# >>> list = [{"name":"chai", "time":"2min"},{"name":"code","time":"2 hours"}]
# >>> list = [{"name":"chai", "time":"2min"},{"name":"code","time":"2 hours"}]
# >>> help
# Type help() for interactive help, or help(object) for help about object.
# >>> list = [{"name":"chai", "time":"2min"},{"name":"code","time":"2 hours"}]
# >>> list
# [{'name': 'chai', 'time': '2min'}, {'name': 'code', 'time': '2 hours'}]
# >>> enumerate(list,start=1)
# <enumerate object at 0x702fb65a8810>
# >>> list
# [{'name': 'chai', 'time': '2min'}, {'name': 'code', 'time': '2 hours'}]
# >>> list(enumerate(list,start=1))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'list' object is not callable
# >>> for i in enumerate(list,start=1):
# ...     print(i)
# ...
# (1, {'name': 'chai', 'time': '2min'})
# (2, {'name': 'code', 'time': '2 hours'})
# >>> for i, video in enumerate(list,start=1):
# ...     print(f"{i} {video['name']} {video['time']}  ")
# ...
# 1 chai 2min
# 2 code 2 hours


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            test = json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name: {video['name']}, Duration: {video['time']} ")
    print("*" * 70)
    print("\n")
    # for video in videos:
    #     print(f"{video}")


def add_a_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_a_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")


def delete_a_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("Invalid index selected")


def main():
    videos = load_data()
    while True:

        print("\nYoutube Manager | Choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_a_video(videos)
            case "3":
                update_a_video(videos)
            case "4":
                delete_a_video(videos)
            case "5":
                exit()


if __name__ == "__main__":
    main()
