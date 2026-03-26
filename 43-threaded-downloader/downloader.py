import threading
import time
import requests

def download_file(url, filename):
    try:
        print(f"[{threading.current_thread().name}] Starting to download {filename}...")
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()
        
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    
        print(f"[{threading.current_thread().name}] Finished downloading {filename}")
    except Exception as e:
        print(f"[{threading.current_thread().name}] Error: {e}")

if __name__ == "__main__":
    urls = [
        ("https://jsonplaceholder.typicode.com/posts", "posts.json"),
        ("https://jsonplaceholder.typicode.com/comments", "comments.json"),
        ("https://jsonplaceholder.typicode.com/users", "users.json")
    ]
    
    threads = []
    start_time = time.time()
    
    for url, filename in urls:
        thread = threading.Thread(target=download_file, args=(url, filename))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()
        
    end_time = time.time()
    print(f"\nAll downloads completed in {end_time - start_time:.4f} seconds.")
