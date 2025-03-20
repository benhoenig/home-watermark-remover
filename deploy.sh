#!/bin/bash

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "Vercel CLI not found. Installing..."
    npm install -g vercel
fi

# Check if the user is logged in
if ! vercel whoami &> /dev/null; then
    echo "Please log in to Vercel:"
    vercel login
fi

# Deploy to Vercel
echo "Deploying LaMa Inpainting to Vercel..."
vercel --prod

echo ""
echo "Deployment complete!"
echo "Your LaMa Inpainting app should now be available at the URL above."
echo ""
echo "Remember to test your deployment by:"
echo "1. Uploading an image"
echo "2. Loading the model"
echo "3. Drawing a mask"
echo "4. Running inpainting"
echo ""
echo "If you encounter any issues, refer to the DEPLOY.md file for troubleshooting." 