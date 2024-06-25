import requests

# URL of the FastAPI server
SERVER_URL = "http://localhost:8000"  # Replace with your server's URL if different

# Function to send a POST request with an image file to the server
def predict_objects(image_file):
    try:
        # Open the image file in binary mode
        with open(image_file, "rb") as file:
            files = {"image": file}
            response = requests.post(f"{SERVER_URL}/predict/", files=files)
            if response.status_code == 200:
                # Save the returned image response
                with open("annotated_image.jpg", "wb") as output_file:
                    output_file.write(response.content)
                print("Tests pass!")
                print("Prediction result saved as annotated_image.jpg")
            else:
                print("Tests failed!")
                print(f"Request failed with status code {response.status_code}")
                print(response.json())  # Print error message if available

    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    predict_objects("./test.jpeg")