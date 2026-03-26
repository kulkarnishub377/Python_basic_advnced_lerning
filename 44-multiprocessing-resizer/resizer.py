import os
import multiprocessing
import time
from PIL import Image

def resize_image(task):
    """
    Worker function to process a single image.
    Receives a tuple containing (input_path, output_path, target_size)
    """
    input_path, output_path, size = task
    try:
        with Image.open(input_path) as img:
            # We use thumbnail instead of resize to preserve aspect ratio
            img.thumbnail(size)
            img.save(output_path)
        print(f"[{multiprocessing.current_process().name}] Resized {os.path.basename(input_path)}")
        return True
    except Exception as e:
        print(f"[{multiprocessing.current_process().name}] Failed to resize {os.path.basename(input_path)}: {e}")
        return False

def setup_directories(input_dir, output_dir):
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
        # Create dummy images if input is empty
        print(f"Created {input_dir}. Please place some images inside it.")
        
        # Create a sample red image for testing
        img = Image.new('RGB', (1920, 1080), color = 'red')
        img.save(os.path.join(input_dir, 'sample1.jpg'))
        img = Image.new('RGB', (2560, 1440), color = 'blue')
        img.save(os.path.join(input_dir, 'sample2.jpg'))
        img = Image.new('RGB', (3840, 2160), color = 'green')
        img.save(os.path.join(input_dir, 'sample3.jpg'))
        
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

if __name__ == "__main__":
    # Unlike threading, multiprocessing creates entirely new Python processes.
    # Therefore, Windows requires the __main__ safety guard block.
    
    INPUT_DIR = "images_input"
    OUTPUT_DIR = "images_output"
    TARGET_SIZE = (800, 800)
    
    setup_directories(INPUT_DIR, OUTPUT_DIR)
    
    # Get list of images
    valid_extensions = (".jpg", ".jpeg", ".png")
    image_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(valid_extensions)]
    
    if not image_files:
        print("No images found to process.")
        exit()
        
    # Prepare task data for workers
    tasks = []
    for filename in image_files:
        in_path = os.path.join(INPUT_DIR, filename)
        out_path = os.path.join(OUTPUT_DIR, filename)
        tasks.append((in_path, out_path, TARGET_SIZE))
        
    start_time = time.time()
    
    # We create a Pool of processes exactly matching our CPU cores
    cpu_cores = multiprocessing.cpu_count()
    print(f"Starting multiprocessing with {cpu_cores} CPU cores...")
    
    # Map the worker function to our tasks array
    with multiprocessing.Pool(processes=cpu_cores) as pool:
        results = pool.map(resize_image, tasks)
        
    end_time = time.time()
    
    success_count = sum(1 for r in results if r)
    print(f"\nSuccessfully resized {success_count}/{len(tasks)} images in {end_time - start_time:.4f} seconds.")
