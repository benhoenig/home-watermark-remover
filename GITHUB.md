# GitHub to Vercel Deployment Guide

This guide will help you set up automatic deployments from GitHub to Vercel for your Home Watermark Remover app.

## Connecting GitHub to Vercel

1. **Create a Vercel Account**
   - Go to [vercel.com](https://vercel.com) and sign up using your GitHub account

2. **Import Your GitHub Repository**
   - From the Vercel dashboard, click "Add New..." → "Project"
   - Select your `home-watermark-remover` repository from the list
   - Vercel will automatically detect that it's a static site

3. **Configure Project Settings**
   - Project Name: `home-watermark-remover` (or choose your own)
   - Framework Preset: Select "Other"
   - Root Directory: `./` (default)
   - Build Command: Leave empty
   - Output Directory: `.`
   - Install Command: `npm install`

4. **Environment Variables**
   - No environment variables are needed for this project

5. **Deploy**
   - Click "Deploy"
   - Vercel will build and deploy your project

## Automatic Deployments

Once connected, Vercel will automatically deploy:
- When you push to the `main` branch
- When pull requests are created (creates preview deployments)

## Custom Domain Setup

1. **Add a Custom Domain**
   - In your Vercel project dashboard, go to "Settings" → "Domains"
   - Add your domain name and follow the verification process

2. **DNS Configuration**
   - Configure your domain's DNS settings as instructed by Vercel
   - Typically this involves adding CNAME or A records

## Troubleshooting

If your deployment fails:
1. Check the Vercel build logs for errors
2. Ensure your repository structure matches the expected format
3. Verify that the model files are correctly included in the repository

## Useful Links

- [Vercel Documentation](https://vercel.com/docs)
- [GitHub Integration Guide](https://vercel.com/docs/concepts/git/vercel-for-github)
- [Custom Domain Setup](https://vercel.com/docs/concepts/projects/domains) 