import logging

def setup_logger():
    logger = logging.getLogger(__name__)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

def handle_error(e):
    logger = setup_logger()
    logger.error(f"An error occurred: {str(e)}")
    return {"error": str(e)}, 500
