import streamlit as st
import torch
import torchvision.transforms as transforms
from torchvision.models import resnet18, ResNet18_Weights
from PIL import Image
import urllib.request

st.set_page_config(page_title="AI Image Classifier", page_icon="🖼️", layout="centered")

# --- Model Loading ---
@st.cache_resource
def load_model():
    """
    Load the pre-trained ResNet18 model.
    Cached so it only loads once per session.
    """
    weights = ResNet18_Weights.DEFAULT
    model = resnet18(weights=weights)
    model.eval() # Set to evaluation mode
    
    # Get the inference transforms specific to this model
    preprocess = weights.transforms()
    
    # Download ImageNet class labels
    url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
    try:
        response = urllib.request.urlopen(url)
        categories = [s.strip().decode("utf-8") for s in response.readlines()]
    except Exception:
        # Fallback if download fails
        categories = [f"Class {i}" for i in range(1000)]
        
    return model, preprocess, categories


# --- UI Setup ---
st.title("🤖 AI Image Classifier")
st.write("Upload an image and the Deep Learning model (ResNet-18) will tell you what it sees!")

with st.spinner("Loading AI model into memory..."):
    model, preprocess, categories = load_model()

# --- File Upload ---
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Create an analysis button
    if st.button("Analyze Image", type="primary", use_container_width=True):
        with st.spinner("Running neural network..."):
            # 1. Preprocess the image
            input_tensor = preprocess(image)
            # Create a mini-batch as expected by the model
            input_batch = input_tensor.unsqueeze(0)
            
            # 2. Run inference
            with torch.no_grad():
                output = model(input_batch)
            
            # 3. Process the output (Softmax to get probabilities)
            probabilities = torch.nn.functional.softmax(output[0], dim=0)
            
            # 4. Get the top 3 predictions
            top3_prob, top3_catid = torch.topk(probabilities, 3)
            
            # --- Display Results ---
            st.success("Analysis Complete!")
            st.subheader("Top Predictions:")
            
            for i in range(top3_prob.size(0)):
                prob = top3_prob[i].item() * 100
                category = categories[top3_catid[i]]
                
                # Create a visual progress bar for the confidence
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.write(f"**{category.title()}**")
                with col2:
                    st.progress(prob / 100)
                    st.caption(f"Confidence: {prob:.2f}%")
