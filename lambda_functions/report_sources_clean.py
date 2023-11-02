import json
import pandas as pd
import boto3
import logging
import io  # Import the io module
import math

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def remove_null_values(event, context):
    try:
        # Get the S3 bucket and file information from the Lambda event
        s3_bucket = event['Records'][0]['s3']['bucket']['name']
        s3_key = event['Records'][0]['s3']['object']['key']
        logger.info(f'S3 Bucket: {s3_bucket}, S3 Key: {s3_key}')

        # Initialize the S3 client
        s3 = boto3.client('s3')
        
        # Download the CSV file from the source S3 bucket
        response = s3.get_object(Bucket=s3_bucket, Key=s3_key)
        csv_data = response['Body'].read().decode('utf-8')
        
        # Convert the CSV data to a Pandas DataFrame
        df = pd.read_csv(io.StringIO(csv_data))  # Use io.StringIO directly
        # print(df)
        
        # Uncomment and add your data cleaning and saving code here
        df7=df[['primary_id','caseid','rpsr_code','serialid']]
        df7=df7.dropna()
        df7=df7.drop_duplicates()
        df7['caseid'].astype(int)
        # Convert the resulting DataFrame to a CSV string
        cleaned_csv = df7.to_csv(index=False)
        
        # Upload the cleaned CSV to another S3 bucket
        cleaned_bucket = 'mock-project-cleaned-ap-south1'  # Replace with the destination S3 bucket name
        cleaned_key = 'cleaned_' + s3_key  # You can modify the key as needed
        s3.put_object(Bucket=cleaned_bucket, Key=cleaned_key, Body=cleaned_csv)

        return {
            'statusCode': 200,
            'body': 'Data cleaned and saved to S3'
        }
    except Exception as e:
        logger.error(f'Error: {str(e)}')
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
