import logging
import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def load_data(dataframe: pd.DataFrame, output_path: str) -> None:
    try:
        dataframe.to_parquet(
            output_path,
            index=False,
            engine="pyarrow"
        )

        logger.info(
            "Data successfully loaded to %s",
            output_path
        )

    except Exception:
        logger.exception(
            "Error loading data to %s",
            output_path
        )
        raise