"""Author: Harshada Tupe"""

# Third party library imports
from google.cloud import storage
import os
import threading
import requests
import ffmpeg
from datetime import datetime, timedelta


GCS_BUCKET_NAME = "python-security-camera-project"
MOTION_DETECTED_API_ENDPOINT = "http://127.0.0.1:5001/motion_detected"
GCS_CLIENT = storage.Client.from_service_account_json('credentials.json')
bucket = GCS_CLIENT.get_bucket(GCS_BUCKET_NAME)

def upload_to_gcs_bucket(blob_name, path_to_file):
    blob = bucket.blob(blob_name)
    blob.content_type = 'video/mp4'
    blob.upload_from_filename(path_to_file)

    blob.patch()
    blob.make_public()

    os.remove(path_to_file)

    print(f"A new file by the name of {blob_name} was created in your bucket {GCS_BUCKET_NAME}")
    return blob.public_url


def handle_detection(path_to_file):
    def action_thread(path_to_file):
        output_path = path_to_file.split(".mp4")[0] + "-out.mp4"
        ffmpeg.input(path_to_file).output(output_path, vf='scale=-1:720').run()
        os.remove(path_to_file)
        url = upload_to_gcs_bucket(path_to_file, output_path)
        data = {
            "url": url,
        }
        requests.post(MOTION_DETECTED_API_ENDPOINT, json=data)
    
    thread = threading.Thread(target=action_thread, args=(path_to_file,))
    thread.start()


def get_videos(extension=".mp4"):
    matching_videos = []

    # Iterate over the blobs (objects) in the bucket
    for blob in bucket.list_blobs():
        # Check if the blob name ends with the desired file extension
        matching_videos.append({"url": blob.public_url, "date": blob.time_created})
    
    return matching_videos
