# Deploying LaMa Inpainting to Vercel

Follow these steps to deploy the LaMa Inpainting web application to Vercel.

## Prerequisites

- A [Vercel](https://vercel.com) account
- Git installed on your computer
- Node.js installed (for local testing)

## Deployment Options

### Option 1: Deploy via Vercel CLI (Recommended)

1. Install the Vercel CLI globally:
   ```bash
   npm install -g vercel
   ```

2. Navigate to the project directory (the `lama_tfjs` folder):
   ```bash
   cd lama_tfjs
   ```

3. Login to your Vercel account:
   ```bash
   vercel login
   ```

4. Deploy to Vercel:
   ```bash
   vercel
   ```

5. Answer the prompts:
   - Set up and deploy? **y**
   - Which scope? **Select your account or team**
   - Link to existing project? **n**
   - Project name? **lama-inpainting** (or choose your own)
   - Directory? **.** (current directory)

6. Wait for deployment to complete and note the URL provided.

### Option 2: Deploy via Vercel Web Interface

1. Create a GitHub repository and push this project to it:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/lama-inpainting.git
   git push -u origin main
   ```

2. Log in to [Vercel Dashboard](https://vercel.com/dashboard)

3. Click "Add New" > "Project"

4. Import your Git repository

5. Configure the project:
   - Framework Preset: **Other**
   - Root Directory: **lama_tfjs** (if the repository contains more than just this project)
   - Build Command: Leave empty
   - Output Directory: **.**
   - Install Command: `npm install`

6. Click "Deploy"

## Verifying the Deployment

Once deployed, visit your Vercel URL to confirm the application is working:

1. Load the page
2. Upload an image
3. Load the model
4. Draw a mask
5. Run inpainting

If everything works correctly, you should see the inpainted result.

## Optimizing for Production

For a production application, consider these additional steps:

1. Setup a custom domain in Vercel dashboard

2. Configure Analytics to track usage

3. Add a Content Delivery Network (CDN) for better model file delivery

4. Consider implementing a more sophisticated UI with progress indicators

## Troubleshooting

If you encounter issues:

1. **Model fails to load**: Check browser console for errors. Ensure model paths are correct.

2. **Slow model loading**: The model is ~4MB. Consider adding a loading progress indicator.

3. **Memory issues**: For large images, consider adding image resizing before processing.

4. **CORS errors**: Verify headers in vercel.json are set correctly.

## Useful Vercel Commands

- **Preview deployment**: `vercel`
- **Production deployment**: `vercel --prod`
- **View deployment info**: `vercel ls`
- **View logs**: `vercel logs your-deployment-url.vercel.app` 