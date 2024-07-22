from google.cloud import storage
import os
import threading
import requests
import ffmpeg
from datetime import datetime

# BUCKET_NAME = "video-security-bucket123"
# API_ENDPOINT = "http://127.0.0.1:5001/motion_detected"

# STORAGE_CLIENT = storage.Client.from_service_account_json('credentials.json')
# bucket = STORAGE_CLIENT.get_bucket(BUCKET_NAME)

# def upload_to_bucket(blob_name, path_to_file):
#     blob = bucket.blob(blob_name)
#     blob.content_type = 'video/mp4'

#     blob.upload_from_filename(path_to_file)

#     blob.patch()
#     blob.make_public()

#     os.remove(path_to_file)

#     print(f"A new file by the name of {blob_name} was created in your bucket {BUCKET_NAME}")
#     return blob.public_url

def handle_detection(path_to_file):
    def action_thread(path_to_file):
        output_path = path_to_file.split(".mp4")[0] + "-out.mp4"
        print ("----- start ---- ")
        print("encoding from: " + path_to_file + ", to: " + output_path)
        ffmpeg.input(path_to_file).output(output_path, vf='scale=-1:720').run()
        print("Removing: " + path_to_file)
        print ("----- end ---- ")
        os.remove(path_to_file)
        # url = upload_to_bucket(path_to_file, output_path)
        # data = {
        #     "url": url,
        # }
        # requests.post(API_ENDPOINT, json=data)
    
    thread = threading.Thread(target=action_thread, args=(path_to_file,))
    thread.start()


def list_videos_in_date_range(start_date, end_date, extension=".mp4"):
    # Convert the string dates to datetime objects
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d')

    matching_files = []
    # videos = os.listdir("/Users/harshadatupe/Desktop/videos")
    videos = os.listdir(os.getcwd())

    # base_path = "file:///Users/harshadatupe/Desktop/videos/" 
    base_path = os.getcwd()
    print("base_path: " + base_path)
    for video in videos:
        if video.endswith(".mp4"):
            matching_files.append({"url": str(video), "date": base_path + video})
            # matching_files.append({"url": base_path + str(video), "date": str(video)})

    # # Iterate over the blobs (objects) in the bucket
    # for blob in bucket.list_blobs():
    #     # Check if the blob name ends with the desired file extension
    #     blob_created_naive = blob.time_created.replace(tzinfo=None)
    #     if blob.name.endswith(extension):
    #         # Check if blob creation date is within the desired range
    #         if start_datetime <= blob_created_naive <= end_datetime:
    #             matching_files.append({"url": blob.public_url, "date": blob.time_created})



    return matching_files

