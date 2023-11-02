# Medication Errors and Effects

## Project Overview

This project centers around the analysis of medication error reports submitted to the FDA to support post-marketing safety surveillance for drugs and therapeutic biologic products. The dataset structure adheres to international safety reporting standards, and adverse events and medication errors are coded using the Medical Dictionary for Regulatory Activities (MedDRA) terminology.

## Data Description

### Data Files
<a href="https://drive.google.com/file/d/1GMoIvbFhrRAr45y3cLlBFtNMpiweQBb7/view?usp=sharing"> Dataset<a>

The dataset comprises several CSV files, each serving a specific purpose:

- **Demographics_data_2015.csv**: Contains demographic and case information.
- **Drug Information.csv**: Provides details about drugs involved in reported cases.
- **Drug Therapy Duration.csv**: Offers insights into the duration of drug therapy.
- **Event Terms.csv**: Lists preferred medical terminology describing the event.
- **Patient Outcomes.csv**: Describes patient outcomes.
- **Preferred Term Indicators.csv**: Highlights preferred medical terminology describing the indication for drug use.
- **Report Sources.csv**: Contains information about the initial sources of the reports.






## Technologies Used

- AWS services: S3, Lambda, Redshift
- Data Cleaning: Python & Pandas
- Data visualization: Tableau

## Project Execution

The following steps were followed to complete this project:

## Architecture
<img></img>

1. **Data Staging**: The CSV data was staged in an AWS S3 bucket for easy accessibility and data preparation.
<img></img>

2. **Data Cleaning and Transformation**: Lambda functions were implemented to clean and transform the data. Transformations included making age and weight formats consistent, dropping null and duplicate values. The cleaned data was stored in another S3 bucket for further processing.
<img></img>

3. **Data Warehousing**: The cleaned data was copied into a Redshift data warehouse for structured storage and efficient querying.
<img></img>

4. **Data Visualization**: For Visualization purpose I have used Tableau. Data from Amazon Redshift can be directly imported to Tableau Desktop(Enterprise version). Since I had Tableau public I couldn't use this feature so I have directly imported the cleaned csv files into Tableau and build Dashboard. These dashboards effectively conveyed insights obtained from the data.
<img></img>


## Conclusion

The Medication Errors and Effects project offers valuable insights into the analysis of medication error reports. It showcases the practical application of data engineering and visualization skills, as well as the utilization of cloud services for data processing. The project's results can be utilized to make informed decisions regarding drug safety and regulatory measures.

