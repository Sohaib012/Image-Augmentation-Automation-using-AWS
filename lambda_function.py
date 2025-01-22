import boto3
from PIL import Image, ImageOps
import io

def lambda_handler(event, context):
    # Get the bucket name and object key from the event
    # bucket_name = event['Records'][0]['s3']['bucket']['name']
    bucket_name = 'image-augment-automation'
    key = event['Records'][0]['s3']['object']['key']
    #key = 'raw-images/thumb-1920-1063600.jpg'

    # Create S3 client
    s3 = boto3.client('s3')

    # Download the image from S3
    response = s3.get_object(Bucket=bucket_name, Key=key)
    image_data = response['Body'].read()

    # Open the image using Pillow
    img_bytes = io.BytesIO(image_data)
    img = Image.open(img_bytes)

    # Apply augmentation (e.g., flip image vertically)
    img_augmented = ImageOps.flip(img)
 
    # Save the processed image back to a BytesIO object
    buffer = io.BytesIO()
    if(key.endswith('.png')):
        img_augmented.save(buffer, format='PNG')
    elif(key.endswith('.jpg') or key.endswith('.jpeg')):
        img_augmented.save(buffer, format='JPEG')

    buffer.seek(0)

    # Save the augmented image back to S3
    augmented_key = key.replace('raw-images/', 'augmented-images/')
    s3.put_object(Bucket=bucket_name, Key=augmented_key, Body=buffer)

    return {"statusCode": 200, "body": "Image processed successfully"}
