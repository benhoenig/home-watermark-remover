# Home Watermark Remover - LaMa Inpainting with TensorFlow.js

This web application uses the LaMa (Large Mask Inpainting) model converted to TensorFlow.js to remove watermarks and unwanted objects from images directly in your browser.

## 🚀 Features

- **In-browser Processing**: All processing happens in the browser - no image uploads to a server
- **Interactive Mask Drawing**: Draw masks over watermarks or objects you want to remove
- **Customizable Brush**: Adjust brush size for precise masking
- **Download Results**: Save inpainted images to your device
- **Mobile-friendly**: Works on desktop and mobile devices
- **Privacy-focused**: Your images never leave your device

## 🎮 How to Use

1. **Load an Image**: Click "Choose Image" to upload an image with a watermark
2. **Load the Model**: Click "Load Model" to initialize the AI model (only needed once)
3. **Draw a Mask**: Paint over the watermark or area you want to remove
4. **Run Inpainting**: Click "Run Inpainting" to process the image
5. **Download**: Save your clean, watermark-free image with the "Download Result" button

## 🔧 Technical Details

This app uses a simplified version of the LaMa (Large Mask Inpainting) model converted to TensorFlow.js. The original LaMa model is a PyTorch model that uses Fast Fourier Convolutions for high-quality inpainting.

- **Model Format**: TensorFlow.js LayersModel
- **Model Size**: ~4MB
- **Input**: RGB image and binary mask
- **Output**: Inpainted RGB image without the masked content

## 🏠 Local Development

1. Clone this repository
2. Navigate to the project directory
3. Run a local server:
   ```
   npx serve .
   ```
4. Open your browser to `http://localhost:3000`

## ☁️ Deploy to Vercel

1. Install the Vercel CLI:
   ```
   npm install -g vercel
   ```

2. Deploy:
   ```
   vercel
   ```

Or deploy directly from the Vercel dashboard:

1. Create a new project on [Vercel](https://vercel.com)
2. Import this repository
3. Deploy

## 👏 Credits

- Original [LaMa model](https://github.com/advimman/lama) by Roman Suvorov, et al.
- TensorFlow.js conversion and web interface implementation

## 📜 License

MIT 