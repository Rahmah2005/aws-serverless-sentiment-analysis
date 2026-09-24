import boto3
import json

s3_client = boto3.client('s3')

# قاموس بسيط للكلمات الدلالية لتقييم المشاعر داخلياً بدون خدمات مقفولة
POSITIVE_WORDS = {'good', 'great', 'excellent', 'amazing', 'love', 'best', 'delicious', 'nice', 'wonderful', 'perfect'}
NEGATIVE_WORDS = {'bad', 'terrible', 'horrible', 'worst', 'damaged', 'slow', 'poor', 'disappointed', 'awful', 'waste'}

def analyze_sentiment(text):
    words = set(text.lower().split())
    pos_matches = len(words.intersection(POSITIVE_WORDS))
    neg_matches = len(words.intersection(NEGATIVE_WORDS))
    
    if pos_matches > neg_matches:
        return "POSITIVE", 0.90, 0.05, 0.05
    elif neg_matches > pos_matches:
        return "NEGATIVE", 0.05, 0.90, 0.05
    else:
        return "NEUTRAL", 0.10, 0.10, 0.80

def lambda_handler(event, context):
    bucket_name = 'sample-test-10'
    input_key = 'inputs/sample_reviews.txt'
    output_key = 'outputs/analysis_summary.txt'
    
    # 1. قراءة الملف من S3
    response = s3_client.get_object(Bucket=bucket_name, Key=input_key)
    reviews_text = response['Body'].read().decode('utf-8')
    reviews_list = [r.strip() for r in reviews_text.split('\n') if r.strip()]
    
    analysis_results = []
    
    # 2. تحليل المشاعر لكل سطر
    for i, review in enumerate(reviews_list, 1):
        sentiment, pos_score, neg_score, neu_score = analyze_sentiment(review)
        
        analysis_results.append(
            f"Review {i}: {review}\n"
            f"Sentiment: {sentiment} "
            f"(Positive: {pos_score:.2f}, Negative: {neg_score:.2f}, Neutral: {neu_score:.2f})\n"
            f"{'-'*40}\n"
        )
    
    # 3. حفظ النتيجة في مجلد outputs في S3
    final_report = "".join(analysis_results)
    s3_client.put_object(
        Bucket=bucket_name,
        Key=output_key,
        Body=final_report.encode('utf-8')
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Analysis completed and saved to outputs folder!')
    }