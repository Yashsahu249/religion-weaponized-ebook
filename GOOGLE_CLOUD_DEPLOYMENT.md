# Google Cloud Deployment Instructions for Book Cover Generator

## Prerequisites
1. **Google Cloud Account**: Ensure you have a Google Cloud account.
2. **Google Cloud SDK**: Install the Google Cloud SDK on your local machine.
3. **Billing Account**: Set up a billing account if you haven't done so already.

## Step 1: Create a New Project
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Click on the project drop-down and select **New Project**.
3. Enter a project name and click **Create**.

## Step 2: Enable Required APIs
1. Navigate to the **API & Services** > **Library**.
2. Enable the following APIs:
   - Cloud Functions API
   - Cloud Build API
   - Cloud Storage API

## Step 3: Set Up Cloud Storage
1. In the Cloud Console, go to **Storage** > **Browser**.
2. Click on **Create Bucket**.
3. Choose a globally unique name, select a location type, and click **Create**.

## Step 4: Deploying Your Code
1. Use the following command to deploy your function:
   ```bash
   gcloud functions deploy cover-generator \
       --runtime python39 \
       --trigger-http \
       --allow-unauthenticated \
       --entry-point = main_function \
       --source . \
       --project YOUR_PROJECT_ID
   ```
2. Replace `YOUR_PROJECT_ID` with your actual project ID.

## Step 5: Testing the Deployment
1. After deployment, you will receive a URL to access your function.
2. Use a browser or a tool like Postman to send requests to the generated URL.

## Troubleshooting
- Ensure your Google Cloud SDK is configured correctly with:
  ```bash
  gcloud init
  ```
- Check function logs for errors using:
  ```bash
  gcloud functions logs read cover-generator
  ```
 
## Additional Resources
- [Google Cloud Functions Documentation](https://cloud.google.com/functions/docs)
- [Cloud Storage Documentation](https://cloud.google.com/storage/docs)

## Conclusion
Following these steps should have your Book Cover Generator up and running on Google Cloud!