# Automated Image Augmentation with AWS

## Introduction
The cloud offers powerful serverless architectures for automation. This project demonstrates the use of AWS Cloud Infrastructure by integrating AWS Lambda and S3 to create an automated image augmentation workflow. Utilizing AWS S3 for scalable storage and AWS Lambda for serverless image processing, raw images are dynamically processed and stored for further use. This project highlights the efficiency and scalability of serverless computing for tasks like image manipulation.

## Tools Specification
- **AWS S3**: Scalable cloud storage for raw and augmented images.
- **AWS Lambda**: Executes serverless Python code for image augmentation.
- **IAM Roles**: Enforces secure interaction between services (S3 and Lambda).
- **Boto3**: AWS SDK for Python to enable seamless S3 operations.
- **Pillow (PIL)**: Python library for advanced image processing tasks.
- **Bash Scripting**: Facilitates efficient bulk uploads to the S3 bucket.

## Architecture Diagram
![image](https://github.com/user-attachments/assets/b0838b09-0dc6-480e-94f2-dee8596b2180)

## Techniques and Configuration

### Step 1: Configuring S3 Buckets
- **Buckets Created:**
  - `image-augment-automation`: Holds raw and processed images.
  - `numpy-pillow-for-lambda-layer`: Stores the Lambda layer zip file.

- **Folder Structure for `image-augment-automation`:**
  - `/raw-images/`: For input images.
  - `/augmented-images/`: For output images.

### Step 2: Workflow Design
- Workflow:
  1. Raw images uploaded to `/raw-images/`.
  2. S3 triggers the Lambda function.
  3. Lambda processes images and saves results in `/augmented-images/`.

### Step 3: Role Creation and Permission Management
- **IAM Role Created:**
  - `S3FullAccess`: For reading and writing image data.
  - `LambdaBasicExecutionRole`: For basic Lambda operations.

- Ensured secure execution and communication.

### Step 4: Lambda Function Development
- **Design Highlights:**
  - Dynamically processes uploaded images.
  - Uses Boto3(AWS SDK) for S3 interactions and Pillow for flipping images vertically.

- **Key Considerations:**
  - Efficient memory usage with `BytesIO`.
  - Seamless handling of `.jpg`, `.jpeg`, and `.png` formats.

### Step 5: Setting Up Lambda Trigger
- **S3 Event Notification:**
  - Configured to invoke the `AugmentOnDemand` Lambda function when an image is uploaded to `/raw-images/`.

- **Steps:**
  1. Set up event rules for the `/raw-images/` folder.
  2. Link the trigger to the Lambda function.

### Step 6: Lambda Layer for Dependencies
- **Problem:** Lambda's environment lacked essential Python libraries like Pillow.
- **Solution:**
  1. Created a virtual environment locally to install dependencies.
  2. Compressed libraries into a `layer_content.zip` file.
  3. Uploaded the zip to the `lambda-layer-na` bucket.
  4. Linked the layer to the Lambda function.
### Step 6: Lambda Layer Structure
  ```plaintext
layer_content.zip
└ python
    └ lib
        └ python3.11
            └ site-packages
                └ pillow
  ```

### Step 7: Automating Data Uploads with Bash
- **Bash Script Highlights:**
  - Automates uploads to the `/raw-images/` folder.
  - Displays error messages for failed uploads.
  - Implements a looping mechanism for bulk operations.

## Results and Discussion

### Output
- Images from `/raw-images/` successfully flipped and stored in `/augmented-images/`.
- Automated workflow eliminated manual intervention.

### Benefits
- Scalable solution for large image datasets.
- Cost-effective due to serverless architecture.
- Automation reduces errors and saves time.

---

## Repository Structure
```plaintext
.
├── raw-images/                # Folder for raw input images
├── augmented-images/          # Folder for processed output images
├── bash-scripts/              # Folder for Bash scripts
├── lambda/                    # Folder for Lambda function code
└── README.md                  # Project documentation (this file)
```

## How to Use
1. Clone this repository.
2. Configure your AWS environment with S3 buckets and Lambda function.
3. Deploy the Lambda layer with required dependencies.
4. Use the provided Bash script to upload images to `/raw-images/`.
5. Check `/augmented-images/` for processed outputs.

---

Feel free to contribute or raise issues for further enhancements!

