import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging


# ------------------------------------------------------------
# DYNAMIC PROJECT ROOT DIRECTORY
# ------------------------------------------------------------
# __file__ = src/components/data_ingestion.py
# Move up 2 levels => project root MLPRJECT
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join(ROOT_DIR, 'artifacts', 'train.csv')
    test_data_path: str = os.path.join(ROOT_DIR, 'artifacts', 'test.csv')
    raw_data_path: str = os.path.join(ROOT_DIR, 'artifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")

        try:
            # ------------------------------------------------------------
            # Correct absolute path to stud.csv
            # ------------------------------------------------------------
            csv_path = os.path.join(ROOT_DIR, "notebook", "data", "stud.csv")
            logging.info(f"Reading CSV file from: {csv_path}")

            df = pd.read_csv(csv_path)
            logging.info("Read dataset as DataFrame")

            # Create artifacts folder (force create)
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False)

            logging.info("Train-test split initiated")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("Ingestion of data completed successfully")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            logging.error("Exception occurred during Data Ingestion")
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
