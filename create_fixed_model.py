import os
import tensorflow as tf
import numpy as np
import tensorflowjs as tfjs

# Create a simple model that mimics the LaMa inpainting model structure but with fixed input shapes
def create_simple_inpainting_model():
    # Input layers with fixed sizes
    image_input = tf.keras.layers.Input(shape=(512, 512, 3), name='image')
    mask_input = tf.keras.layers.Input(shape=(512, 512, 1), name='mask')
    
    # Combine inputs
    concat = tf.keras.layers.Concatenate(axis=3)([image_input, mask_input])
    
    # Simple encoder-decoder network
    # Encoder
    x = tf.keras.layers.Conv2D(64, 3, padding='same', activation='relu')(concat)
    x = tf.keras.layers.Conv2D(128, 3, strides=2, padding='same', activation='relu')(x)
    x = tf.keras.layers.Conv2D(256, 3, strides=2, padding='same', activation='relu')(x)
    
    # Decoder
    x = tf.keras.layers.Conv2DTranspose(128, 4, strides=2, padding='same', activation='relu')(x)
    x = tf.keras.layers.Conv2DTranspose(64, 4, strides=2, padding='same', activation='relu')(x)
    
    # Output layer
    outputs = tf.keras.layers.Conv2D(3, 3, padding='same', activation='sigmoid', name='inpainted')(x)
    
    # Create model
    model = tf.keras.models.Model(inputs=[image_input, mask_input], outputs=outputs)
    
    return model

# Directory for saving the TensorFlow.js model
tfjs_dir = "fixed_model"
os.makedirs(tfjs_dir, exist_ok=True)

# Create and compile the model
print("Creating a simplified inpainting model with fixed input shapes...")
model = create_simple_inpainting_model()

# Compile the model
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='mse'
)

model.summary()

# Create some dummy data for a test prediction
dummy_image = np.random.rand(1, 512, 512, 3).astype(np.float32)  # RGB image
dummy_mask = np.ones((1, 512, 512, 1)).astype(np.float32)        # Binary mask

# Test the model
print("Testing model with dummy data...")
dummy_output = model.predict({
    'image': dummy_image,
    'mask': dummy_mask
})
print(f"Output shape: {dummy_output.shape}")

# Save the model for TensorFlow.js
print(f"Saving model to {tfjs_dir}...")
tfjs.converters.save_keras_model(model, tfjs_dir)
print(f"✅ Model saved to {tfjs_dir}")

print("\nTo use this model, update the index.html file to load from 'fixed_model/model.json'") 