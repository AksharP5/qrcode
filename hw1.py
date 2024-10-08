# Import necessary libraries
import matplotlib.pyplot as plt
import numpy
import qrcode

# Function to generate QR code
def generate_qr_code(data):
    # Create a QRCode object with specified parameters
    qr = qrcode.QRCode()
    # Add data to the QRCode object
    qr.add_data(data)
    qr.make()
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Return the generated image
    return qr_img

# Set the data to be encoded in the QR code
data_to_encode = "https://www.youtube.com"

# Generate QR code using the defined function
qr_code_img = generate_qr_code(data_to_encode)

# Display the QR code using Matplotlib
plt.imshow(qr_code_img)
plt.show()