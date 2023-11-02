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
        
        # data cleaning
        df1=df[['primaryid','caseid','event_dt','mfr_dt','init_fda_dt','fda_dt','rept_cod','mfr_num','age','age_cod','age_grp','sex','e_sub','wt','wt_cod','rept_dt','to_mfr','occp_cod','reporter_country','occr_country','serialid']]
        df1 = df1.dropna()
        df1= df1.drop_duplicates()
        
        lbs_rows = df1.loc[df1['wt_cod'] == 'LBS']
        lbs_rows.loc[:,'wt'] = lbs_rows['wt'] * 0.453592
        lbs_rows.loc[:,'wt_cod'] = 'KG'
        df1.update(lbs_rows)
        
        df1['wt'] = df1['wt'].apply(lambda x: math.ceil(x))
        
        
        #Converting Decade to Years
        dec_row = df1.loc[df1['age_cod']=='DEC']
        dec_row.loc[:,'age']=dec_row['age']*10
        dec_row.loc[:,'age_cod'] = 'YR'

        df1.update(dec_row)
        
        #Converting Months to Year
        mons_row = df1.loc[df1['age_cod']=='MON']
        mons_row.loc[:,'age']=mons_row['age']/12
        mons_row.loc[:,'age_cod'] = 'YR'
        
        df1.update(mons_row)
        
        #Converting weeks to years
        wk_row = df1.loc[df1['age_cod']=='WK']
        wk_row.loc[:,'age']=wk_row['age']/52
        wk_row.loc[:,'age_cod'] = 'YR'
        
        df1.update(wk_row)
        
        #Converting days to years
        dy_row = df1.loc[df1['age_cod']=='DY']
        dy_row.loc[:,'age']=dy_row['age']/365
        dy_row.loc[:,'age_cod'] = 'YR'
        
        df1.update(dy_row)
        
        df1['caseid'].astype(int)
        # Convert the resulting DataFrame to a CSV string
        cleaned_csv = df1.to_csv(index=False)
        
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
