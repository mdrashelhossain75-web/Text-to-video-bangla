import requests

# Hugging Face API URL (Free Text-to-Video Model)
API_URL = "https://api-inference.huggingface.co/models/damo-vilab/text-to-video-ms-1.7b"

# Your Prompt
prompt = "A village boy walking near a green field in the morning, high quality, realistic"

def generate_video(prompt_text):
    headers = {"Authorization": "Bearer YOUR_HUGGINGFACE_TOKEN"}
    payload = {"inputs": prompt_text}
    
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        with open("output_video.mp4", "wb") as f:
            f.write(response.content)
        print("Video generated successfully: output_video.mp4")
    else:
        print("Error:", response.json())

if __name__ == "__main__":
    generate_video(prompt)
