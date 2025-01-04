import requests
import pandas as pd
import json
from google.cloud import storage
from datetime import datetime, timedelta
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Google Cloud Storage settings
BUCKET_NAME = "your-bucket-name"
GCP_CREDENTIALS_PATH = "/path/to/your-service-account-key.json"

# API Endpoint and parameters
API_URL = "https://api.example.com/data"
API_KEY = "your-api-key"

# Configure paths
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GCP_CREDENTIALS_PATH
LOCAL_FOLDER = "./data"
os.makedirs(LOCAL_FOLDER, exist_ok=True)

# Fetch data from API
def fetch_api_data():
    try:
        logging.info("Fetching data from API...")
        response = requests.get(API_URL, headers={"Authorization": f"Bearer {API_KEY}"})
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        logging.info("Data fetched successfully.")
        return data
    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        return None

# Transform data to structured format (e.g., DataFrame)
def transform_data(raw_data):
    try:
        logging.info("Transforming data...")
        # Example transformation logic (depends on API structure)
        records = [
            {
                "id": item["id"],
                "value": item["value"],
                "timestamp": item["timestamp"]
            }
            for item in raw_data["results"]
        ]
        df = pd.DataFrame(records)
        logging.info("Data transformed successfully.")
        return df
    except Exception as e:
        logging.error(f"Error transforming data: {e}")
        return None

# Save DataFrame to local CSV file
def save_to_csv(df, filename):
    try:
        filepath = os.path.join(LOCAL_FOLDER, filename)
        df.to_csv(filepath, index=False)
        logging.info(f"Data saved locally at {filepath}.")
        return filepath
    except Exception as e:
        logging.error(f"Error saving data to CSV: {e}")
        return None

# Upload file to Google Cloud Storage
def upload_to_gcs(local_file, bucket_name, gcs_path):
    try:
        logging.info(f"Uploading {local_file} to GCS bucket {bucket_name}...")
        client = storage.Client()
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(gcs_path)
        blob.upload_from_filename(local_file)
        logging.info(f"File uploaded successfully to GCS: {gcs_path}")
    except Exception as e:
        logging.error(f"Error uploading file to GCS: {e}")

# Main automation function
def main():
    logging.info("Starting data pipeline automation...")
    
    # Step 1: Fetch data from API
    raw_data = fetch_api_data()
    if not raw_data:
        logging.error("Failed to fetch data. Exiting pipeline.")
        return

    # Step 2: Transform data
    df = transform_data(raw_data)
    if df is None or df.empty:
        logging.error("Failed to transform data. Exiting pipeline.")
        return

    # Step 3: Save data locally
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    local_file = save_to_csv(df, f"transformed_data_{timestamp}.csv")
    if not local_file:
        logging.error("Failed to save data locally. Exiting pipeline.")
        return

    # Step 4: Upload data to GCS
    gcs_path = f"data/transformed_data_{timestamp}.csv"
    upload_to_gcs(local_file, BUCKET_NAME, gcs_path)

    logging.info("Data pipeline automation completed successfully.")

if __name__ == "__main__":
    main()
