from minio import Minio
import os

client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

BUCKET = "analytics-lake"

if not client.bucket_exists(BUCKET):
    client.make_bucket(BUCKET)

base_path = os.path.abspath("../data/parquet")

for root, _, files in os.walk(base_path):
    for file in files:
        local_path = os.path.join(root, file)

        # Create clean S3 object path
        object_path = os.path.relpath(local_path, base_path)
        object_path = object_path.replace("\\", "/")  # Windows fix

        client.fput_object(
            BUCKET,
            object_path,
            local_path
        )

        print(f"Uploaded: {object_path}")

print("All parquet files uploaded to MinIO successfully")
