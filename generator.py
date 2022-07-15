import requests

def generate_lyrics(song_name, api_token):
    api_url = "https://api-inference.huggingface.co/models/steeldream/letov"
    headers = {"Authorization": f"Bearer {api_token}"}
    payload = {
        "inputs": f"<s>Название песни: {song_name}\nТекст песни:\n",
        "parameters": {
            "top_k": 5,
            "top_p": 1,
            "do_sample": True,
            "max_length": 20, #400
            "temperature": 0.8,
            "repetition_penalty": 1.0,
            "return_full_text": False,
        },
        "options": {
            "use_cache": False,
            "use_gpu": True,
            "wait_for_model": True,
        }
    }
    response = requests.post(api_url, headers=headers, json=payload)
    output = response.json()
    try:
        output_text = output[0]['generated_text']
    except:
        output_text = output
    try:
        res = str(output_text[:output_text.index("</s>") + 1])[:-1]
    except:
        res = output_text
    return res
