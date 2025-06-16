import streamlit as st
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import webcolors


st.set_page_config(page_title="🎨 Image Color Classifier", layout="centered")
st.title("🌈 Image Color Classifier")
st.write("Upload an image and I’ll tell you the **most common color** in it!")


def get_nearest_color_name(rgb_color):
    closest_colors = {}
    for name, hex_value in webcolors.CSS3_NAMES_TO_HEX.items():
        r, g, b = webcolors.hex_to_rgb(hex_value)
        # Distance between colors
        distance = (r - rgb_color[0]) ** 2 + (g - rgb_color[1]) ** 2 + (b - rgb_color[2]) ** 2
        closest_colors[distance] = name
    return closest_colors[min(closest_colors.keys())]


def find_main_color(image, clusters=3):
    small_image = image.resize((100, 100))  # Make image smaller for faster processing
    pixels = np.array(small_image).reshape(-1, 3)  # Get all pixels

    model = KMeans(n_clusters=clusters, random_state=0)
    model.fit(pixels)

    # Find the most frequent color cluster
    unique_labels, label_counts = np.unique(model.labels_, return_counts=True)
    main_color = model.cluster_centers_[np.argmax(label_counts)]

    return tuple(map(int, main_color))


uploaded_image = st.file_uploader("📤 Upload your image here", type=["jpg", "jpeg", "png"])

if uploaded_image:
    img = Image.open(uploaded_image)
    st.image(img, caption="🖼️ Uploaded Image", use_container_width=True)

    with st.spinner("Finding the most common color..."):
        rgb_color = find_main_color(img)

        # Try to get exact color name, else find closest one
        try:
            color_name = webcolors.rgb_to_name(rgb_color)
        except ValueError:
            color_name = get_nearest_color_name(rgb_color)


    st.markdown(f"### 🎯 Most Common Color: **{color_name.title()}**")
    st.markdown(
        f"<div style='width:100px;height:100px;background-color:rgb{rgb_color};"
        f"border-radius:10px;border:2px solid #000;'></div>",
        unsafe_allow_html=True
    )
