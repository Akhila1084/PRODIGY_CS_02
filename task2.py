from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    # Open the image and convert it to an array
    img = Image.open(input_image_path)
    img_array = np.array(img)

    # Encrypt the image by manipulating pixel values
    encrypted_array = (img_array + key) % 256  # Add key to pixel values and wrap around at 256
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))

    # Save the encrypted image
    encrypted_image.save(output_image_path)
    print(f"Encrypted image saved as: {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    # Open the encrypted image and convert it to an array
    img = Image.open(input_image_path)
    img_array = np.array(img)

    # Decrypt the image by reversing the pixel manipulation
    decrypted_array = (img_array - key) % 256  # Subtract key from pixel values and wrap around at 256
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))

    # Save the decrypted image
    decrypted_image.save(output_image_path)
    print(f"Decrypted image saved as: {output_image_path}")

if __name__ == "__main__":
    # Example usage
    input_image = "input_image.png"  # Replace with your input image path
    encrypted_image = "encrypted_image.png"
    decrypted_image = "decrypted_image.png"
    key = 50  # You can choose any integer key

    # Encrypt the image
    encrypt_image(input_image, encrypted_image, key)

    # Decrypt the image
    decrypt_image(encrypted_image, decrypted_image, key)
