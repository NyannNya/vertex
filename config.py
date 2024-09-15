import os

class Config:
    BIGQUERY_PROJECT_ID = os.getenv('BIGQUERY_PROJECT', 'bishare-1606')
    GOOGLE_APPLICATION_CREDENTIALS  = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', 'etc/secrets/google_adc.json')