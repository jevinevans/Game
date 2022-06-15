import json

from loguru import logger


def load_data(filename: str):
    data = {}
    try:
        assert filename.endswith(".json")
        assert "/data/" in filename
        with open(filename, encoding="utf-8") as load_file:
            data = json.load(load_file)

    except Exception as e:
        logger.warning(e)
        print(f"{e}\n - No data could be loaded for {filename}")

    return data
