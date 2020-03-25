#from django.db import models
import contentful
from reinertsen_web.settings import SPACE_ID, ACCESS_TOKEN, ENVIRONMENT
# Create your models here.

client = contentful.Client(
    space_id=SPACE_ID,
    access_token=ACCESS_TOKEN,
    environment=ENVIRONMENT
    )
