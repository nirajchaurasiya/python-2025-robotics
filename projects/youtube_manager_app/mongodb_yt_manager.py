import os
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv

load_dotenv()

# Access environment variables
MONGODB_STRING = os.getenv("MONGODB_STRING")

client = MongoClient(MONGODB_STRING)

db = client["ytmanager"]

video_collection = db["videos"]


def list_videos():
    try:
        for video in video_collection.find():
            print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")
    except Exception as e:
        print(e)


def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})


def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {"_id": ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}}
    )


def delete_video(video_id):
    video_collection.find_one_and_delete({"_id": ObjectId(video_id)})


def main():
    while True:
        print("Youtube manager app")

        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                list_videos()
            case "2":
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
            case "3":
                video_id = input("Enter video ID to update: ")
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                update_video(video_id, name, time)
            case "4":
                video_id = input("Enter video ID to delete: ")
                delete_video(video_id)
            case "5":
                break
            case _:
                print("not matched")


if __name__ == "__main__":
    main()
