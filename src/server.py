from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from tempfile import NamedTemporaryFile
from ultralytics import YOLO
from PIL import Image, ImageDraw
import uvicorn

# Initialize FastAPI app
app = FastAPI()

# Load the YOLO model
model = YOLO("best.pt")

# Endpoint to perform object detection
@app.post("/predict/")
async def predict_objects(image: UploadFile = File(...)):
    try:
        # Save the uploaded image temporarily
        with NamedTemporaryFile(delete=False, suffix=".jpg") as temp_image:
            temp_image_path = temp_image.name
            temp_image.write(await image.read())

        # Run inference on the saved image
        results = model(temp_image_path)

        # Process detection results and annotate the image
        image = Image.open(temp_image_path)
        draw = ImageDraw.Draw(image)
        for i, r in enumerate(results):
            # Plot results image
            im_bgr = r.plot()  # BGR-order numpy array
            im_rgb = Image.fromarray(im_bgr[..., ::-1])  # RGB-order PIL image

            # Show results to screen (in supported environments)
            r.show()

            # Save results to disk
            r.save(filename="results.jpg")
        # Return the annotated image file as response
        return FileResponse("results.jpg", media_type="image/jpeg")

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Main section to run the FastAPI application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)