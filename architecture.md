# Goals & Design Considerations

- Implement a FastAPI server for object detection using YOLO.
- Use Docker to containerize both the server and potentially the client.
- Ensure seamless communication between the client (client.py) and the server (server.py).

## Architecture

### Assumptions
- The FastAPI server (server.py) will receive image files via HTTP POST requests, perform object detection using YOLO, and return annotated images.
- The client (client.py) will send image files to the server and handle responses.

## Components
### FastAPI Server (server.py):

- Uses FastAPI for handling HTTP requests.
- Integrates YOLO for object detection on uploaded images.
- Responds with annotated images (results.jpg) or error messages.

### Client Script (client.py):

- Sends HTTP POST requests to the FastAPI server with image files.
- Handles server responses, saving annotated images locally or reporting errors.

## Technology

### Docker:

- Uses a Python 3.9 slim image as the base for both server and potentially client containers.
- Installs necessary dependencies (libgl1-mesa-glx, libopencv-dev).
- Copies application code (requirements.txt, source files).

### FastAPI:

- Provides a modern web framework for building APIs with Python.
- Handles asynchronous requests and file uploads (UploadFile).

### YOLO:

- Utilizes the ultralytics YOLO implementation for object detection.
- Processes images uploaded to the server, annotating detected objects.

## Operations

### Dockerfile:

- Defines build steps for setting up the server container (server.py).
- Installs dependencies, copies application files, and exposes port 8000 for communication.
- Uses uvicorn to run the FastAPI application (server.py).

### Client (client.py):

- Uses requests library to send HTTP POST requests to the server.
- Handles image file uploads (files={"image": file}) and server responses.
- Saves annotated images locally (annotated_image.jpg) upon successful detection.

## Example Use Case

### Build and Run Docker Containers:

- Build the server container: docker build -t my-server-image .
- Run the server container: docker run -d -p 8000:8000 my-server-image

### Execute Client Script (client.py):

- Ensure client.py points to the correct server URL (http://localhost:8000).
- Execute client.py: python client.py

## Result:

- client.py sends an image (test.jpeg) to the FastAPI server.
- Server (server.py) performs object detection using YOLO and returns an annotated image (results.jpg).
- Client script (client.py) saves results.jpg locally if successful, indicating a successful interaction.

## FastAPI: http://127.0.0.1:8000/docs (use: "try it out" feature to predict object detection on your image.)