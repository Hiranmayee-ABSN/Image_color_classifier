# Image_color_classifier
A simple and interactive web app built with **Python** and **Streamlit** that lets users upload an image and instantly detects the **most dominant color** in it using machine learning (KMeans clustering). Great for designers, artists, or curious minds who want to analyze colors quickly!

###  Features

*  Upload any image (`.jpg`, `.jpeg`, `.png`)
*  Detects the **most common color** using KMeans clustering
*  Maps RGB color to the nearest human-readable color name (e.g., "Navy", "Olive", etc.)
*  Displays a color swatch for visual reference
*  Runs locally in the browser with no external dataset needed



###  How it Works

1. The image is resized and pixels are extracted.
2. KMeans clustering groups similar colors.
3. The most frequent cluster is chosen as the dominant color.
4. The app finds the closest matching CSS3 color name.
5. It displays the color name and a swatch.



###  Requirements

Install all dependencies using pip:

```bash
pip install -r requirements.txt
```

**`requirements.txt`**

```txt
streamlit
numpy
Pillow
scikit-learn
webcolors
```

###  Run the App

To start the app locally:

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.


### Project Structure

```
Image_color_classifier/
├── app.py                # Main Streamlit app
├── requirements.txt      # Python package dependencies
└── README.md             # Project overview and guide
```


### Example Output
* **Uploaded Image**: A photo of a forest
* **Detected Color**: "DarkGreen"
* **RGB Value**: (0, 100, 0)
* **Color Swatch**: Displays a square filled with the detected color

### Why No Dataset?
This app doesn’t need any dataset! It uses **unsupervised learning (KMeans)** on the uploaded image itself to find the most common color.


### Future Improvements (Optional)
* Show **top 3 colors** with percentages
* Add **download color palette**
* Support for **image URLs**
* Dark/light **theme switcher**
