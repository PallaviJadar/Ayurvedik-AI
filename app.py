import gradio as gr
import os
from PIL import Image

import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini AI
if not api_key:
    print("Warning: GEMINI_API_KEY not found in environment variables.")
else:
    print(f"GEMINI_API_KEY found: {api_key[:4]}...{api_key[-4:]}")

try:
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"Error configuring Gemini API: {e}")

generation_config = {
    "temperature": 0.9,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

model_genai = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

# Lazy-load ML model removed - using Gemini Vision

def predict_plant(image):
    """Identify medicinal plant from image using Gemini Vision"""
    if image is None:
        return "Please upload an image first!"
    
    try:
        # Use Gemini 1.5 Flash for vision capabilities
        prompt = "Identify this medicinal plant. Provide the name and a confidence score. If it's not a medicinal plant, say so."
        response = model_genai.generate_content([prompt, image])
        
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

def get_plant_info(plant_name):
    """Get detailed information about a medicinal plant"""
    if not plant_name:
        return "Please identify a plant first!"
    
    try:
        chat = model_genai.start_chat(history=[])
        prompt = f"Tell me everything about the medicinal plant '{plant_name}'. Include scientific name, medicinal properties, traditional uses, preparation methods, health benefits, and precautions. Format with emojis and clear sections."
        
        response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

def chat_with_ai(message, history):
    """Chat with Gemini AI about Ayurveda and medicinal plants"""
    try:
        # Initialize history if None
        if history is None:
            history = []
            
        chat = model_genai.start_chat(history=[])
        chat.send_message("You are AyurVedik AI, an expert in medicinal plants and Ayurveda. Answer questions helpfully with emojis.")
        
        response = chat.send_message(message)
        
        # Append new message and response to history in 'messages' format
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": response.text})
        
        return history, "" # Return updated history and empty string to clear input
    except Exception as e:
        if history is None:
            history = []
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": f"❌ Error: {str(e)}"})
        return history, ""

# Create Gradio Interface
with gr.Blocks(title="AyurVedik AI", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🌿 AyurVedik AI - Medicinal Plant Identifier")
    gr.Markdown("### Identify medicinal plants and learn about Ayurveda")
    
    with gr.Tab("🔍 Identify Plant"):
        with gr.Row():
            with gr.Column():
                image_input = gr.Image(type="pil", label="Upload Plant Image")
                identify_btn = gr.Button("🔍 Identify Plant", variant="primary")
            with gr.Column():
                prediction_output = gr.Markdown(label="Identification Result")
        
        # plant_name_state removed
        
        with gr.Row():
            plant_name_input = gr.Textbox(label="Plant Name (from identification above)", placeholder="Enter plant name or use identification result")
            get_info_btn = gr.Button("📚 Get Plant Info", variant="secondary")
        
        info_output = gr.Markdown(label="Plant Information")
        
        identify_btn.click(
            fn=predict_plant,
            inputs=image_input,
            outputs=prediction_output
        )
        
        get_info_btn.click(
            fn=get_plant_info,
            inputs=plant_name_input,
            outputs=info_output
        )
    
    with gr.Tab("💬 Chat with AI"):
        gr.Markdown("### Ask me anything about medicinal plants and Ayurveda!")
        chatbot = gr.Chatbot(height=400, type="messages")
        msg = gr.Textbox(label="Your Question", placeholder="Ask about medicinal plants, Ayurveda, health benefits...")
        
        msg.submit(chat_with_ai, [msg, chatbot], [chatbot, msg])

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
