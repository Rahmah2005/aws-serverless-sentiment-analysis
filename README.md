# Serverless Sentiment Analysis Pipeline with AWS Lambda & Amazon S3

An end-to-end automated serverless pipeline built on AWS to perform sentiment analysis on product reviews extracted from a Kaggle dataset. The architecture leverages Amazon S3 for cloud object storage and AWS Lambda for event-driven data processing and sentiment classification.

---

## Architecture Overview

1. Ingestion (Amazon S3): Input reviews are extracted and uploaded to an S3 bucket under the inputs/ prefix (sample_reviews.txt).
2. Compute & Analysis (AWS Lambda): A serverless Python function reads the input file directly from S3, analyzes the emotional polarity (Positive, Negative, Neutral) of each review, and scores the sentiment distribution.
3. Storage & Output (Amazon S3): The processed results and statistics are formatted and written back to S3 under the outputs/ prefix (analysis_summary.txt).
4. Monitoring (Amazon CloudWatch): Execution duration, memory allocation, and runtime performance are tracked via CloudWatch Logs.

---

## AWS Services & Technologies

- AWS Lambda: Serverless compute running Python 3.12.
- Amazon S3: Object storage for input datasets and generated analytical reports.
- Amazon CloudWatch: Logging, execution tracing, and resource monitoring.
- AWS IAM: Role-based access control using LabRole permissions.
- Python (Boto3): AWS SDK for Python to interact with S3 APIs.

---

## Project Structure

Project Root:
- lambda_function.py : Core AWS Lambda handler and sentiment logic
- sample_reviews.txt : Input dataset extracted from Kaggle reviews
- analysis_summary.txt : Processed sentiment report output
- screenshots/ : Execution proofs and AWS Console snapshots
  * S3_bucket.png
  * S3_bucket_object.png
  * Lambda_code_editor.png
  * Lambda_function.png
  * CloudWatch_Logs.png
  * output_file.png

---

## Implementation & Challenges Solved

- IAM Permission Constraints: Handled sandbox role restrictions (AccessDeniedException for Amazon Comprehend) by designing an embedded, lightweight keyword-based sentiment classification engine within Lambda, ensuring zero service failure while meeting pipeline requirements.
- Timeout & Memory Optimization: Configured execution timeout to 1 minute to ensure seamless processing of batch text files without cold-start interruptions.

---

## Sample Execution & Results

### 1. Cloud Storage Setup (Amazon S3)
Input data organized under inputs/ and final outputs routed to outputs/.

![S3 Bucket](screenshots/S3_bucket.png)
![S3 Objects](screenshots/S3_bucket_object.png)

### 2. Lambda Processing & Deployment
Serverless function triggered and tested successfully with HTTP 200 execution status.

![Lambda Editor](screenshots/Lambda_code_editor.png)
![Lambda Execution](screenshots/Lambda_function.png)

### 3. Monitoring & CloudWatch Tracing
Verified execution durations and memory utilization via CloudWatch log streams.

![CloudWatch Logs](screenshots/CloudWatch_Logs.png)

### 4. Output Sentiment Report
Processed reviews categorized into Positive, Negative, and Neutral scores.

![Analysis Summary](screenshots/output_file.png)
