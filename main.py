from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
import logging
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def main():
    
    #Get the paths from environment variables and check if they are set
    raw_data_path = os.getenv("RAW_FILE_PATH")
    if not raw_data_path:
        raise ValueError("Environment variable RAW_FILE_PATH is not set.")
    
    processed_data_path = os.getenv("PROCESSED_FILE_PATH")
    if not processed_data_path:
        raise ValueError("Environment variable PROCESSED_FILE_PATH is not set.")
    
    #Extract the data from the raw csv file
    df = extract_data(raw_data_path)
    #Transform the data
    df_transformed = transform_data(df)
    #Load the data into a parquet file
    load_data(df_transformed, processed_data_path)
    
    logger.info("ETL process completed successfully.")

if __name__ == "__main__":
    main()