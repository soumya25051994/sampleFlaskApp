import re
import boto3
from api import db
from api.model import customers_object
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def get_boto3_session():
    """
    Function to create boto3 session object.
    """
    session = boto3.Session()
    return session

def get_s3_resource_object():
    """
    Function to create boto3 s3 resource object.
    """
    boto3_session = get_boto3_session()
    return boto3_session.resource('s3')


def replace_special_char(input_str):
    return re.sub('[^A-Za-z0-9]+', '_', input_str)
