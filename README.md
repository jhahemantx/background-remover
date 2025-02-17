# Background Removal with OpenCV

## Preview
![Screenshot 2025-02-17 212726](https://github.com/user-attachments/assets/373b23be-9728-4537-bc7a-efee5feb32dd)<br>

![Screenshot 2025-02-17 212611](https://github.com/user-attachments/assets/e6ac7b6e-9e01-4cb3-a861-c1309c2dc550)



## Features
- Captures video frames from a webcam.
- Removes the background using OpenCV and `cvzone`'s `SelfiSegmentationModule`.
- Allows switching between different background images.
- Streams the processed video with background removal in real-time.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Flask
- OpenCV
- NumPy
- cvzone

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/jhahemantx/background-remover.git
   cd background-remover
   ```

2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask server:**
   ```sh
   python app.py
   ```

2. Open a browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure
```
background-remover/
│-- app.py              # Flask backend
│-- requirements.txt    # Required Python packages
│-- templates/
│   ├── index.html      
│-- static/
│   ├── style.css       
│-- Images/           # Folder containing background images
│   ├── 1.jpg         # Sample background image
│   ├── 2.jpg         # Sample background image
```

## API Endpoints
- `/` : Renders the frontend UI.
- `/video_feed` : Provides the video stream with background removal.
- `/change_background/<direction>` : Changes the background image. Accepts `prev` or `next` as `<direction>`.

## Future Enhancements
- Deploy on a cloud service.
- Improve background segmentation using Deep Learning models.
- Implement a WebSocket-based streaming solution for smoother video feeds.
- Allow users to upload custom background images.



