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
<img src="https://github.com/Vipinnnn/medication_errors_effects_data_analysis/assets/71926172/ed382f19-f0e0-45a7-8f04-e280fa20fa1b"></img>

1. **Data Staging**: The CSV data was staged in an AWS S3 bucket for easy accessibility and data preparation.
<img src="https://github.com/Vipinnnn/medication_errors_effects_data_analysis/assets/71926172/ad00df51-d37c-4eca-9055-56c3f8c5d4f4"></img>

2. **Data Cleaning and Transformation**: Lambda functions were implemented to clean and transform the data. Transformations included making age and weight formats consistent, dropping null and duplicate values. The cleaned data was stored in another S3 bucket for further processing.
<img src="https://github.com/Vipinnnn/medication_errors_effects_data_analysis/assets/71926172/537178ba-b0db-41a3-945e-89e8488b10d3"></img>
<img src="https://github.com/Vipinnnn/medication_errors_effects_data_analysis/assets/71926172/8498c8d4-b6c1-41b4-a44a-b05972a61354"></img>

3. **Data Loading**: The cleaned data was copied into a Redshift data warehouse for structured storage and efficient querying.
<img src="https://github.com/Vipinnnn/medication_errors_effects_data_analysis/assets/71926172/b132d683-2457-4a49-a811-b23598b662cd"></img>

4. **Data Visualization**: For Visualization purpose Tableau is used. Data from Amazon Redshift can be directly imported to Tableau Desktop(Enterprise version). Since this feature is not availabe on Tableau Public, the cleaned csv files are directly imported into Tableau and Dashboard is created. These dashboards effectively conveyed insights obtained from the data.

<a href="https://public.tableau.com/views/mock_proj_dashboard/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link">Tableau Public Dashboard<a>

<img src="https://github.com/Vipinnnn/medication_errors_effects_data_analysis/assets/71926172/4b8d52c9-5b28-40f9-8e70-39945bdb177c"></img>


## Conclusion

The Medication Errors and Effects project offers valuable insights into the analysis of medication error reports. It showcases the practical application of data engineering and visualization skills, as well as the utilization of cloud services for data processing. The project's results can be utilized to make informed decisions regarding drug safety and regulatory measures.

