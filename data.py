import requests
import json

def get_all_emojis():
    url = "https://emojihub.yurace.pro/api/all"
    response = requests.get(url)
    
    if response.status_code == 200:  
        return response.json()  
    else:
        print("Failed to get emojis data:", response.status_code)
        return None

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    emojis_data = get_all_emojis()
    if emojis_data:
        save_to_json(emojis_data, 'emojis_data.json')
        print("Emojis data has been saved to emojis_data.json")
    else:
        print("Failed to get emojis data")

if __name__ == "__main__":
    main()