from pathlib import Path

# Define valid file extensions
EXTENSIONS = {
    'videos': {'.mp4', '.mov', '.avi', '.mkv'},
    'images': {'.jpg', '.jpeg', '.png', '.gif', '.bmp'},
}

def check_folder_contents(config):
    path = Path(config['path_dir'])
    print(f"Checking folder: {path}")
    print('-' * 40)

    # Check if path exists
    if not path.is_dir():
        print("❌ Path does not exist.")
        return None
    else:
        print("✅ Path exists.")

    # Collect files in directory (non-recursive)
    files = list(path.iterdir())

    # Filter files by type
    video_files = [f for f in files if f.suffix.lower() in EXTENSIONS['videos']]
    image_files = [f for f in files if f.suffix.lower() in EXTENSIONS['images']]

    # Count files
    video_count = len(video_files)
    image_count = len(image_files)

    # Check existence
    print(f"{'✅' if video_count > 0 else '❌'} Videos exist.")
    print(f"{'✅' if image_count > 0 else '❌'} Images exist.")

    print('-' * 40)
    print(f"Videos: expected {config['videos']}, found {video_count}  {'✅' if video_count == config['videos'] else '❌'}")
    print(f"Images: expected {config['images']}, found {image_count}  {'✅' if image_count == config['images'] else '❌'}")
    print('-' * 40)

    # Optional: List files (uncomment below if you want to print file names)
    # print("Video files:")
    # for f in video_files:
    #     print(f"  - {f.name}")
    # print("Image files:")
    # for f in image_files:
    #     print(f"  - {f.name}")

    return {
        'videos_found': video_count,
        'images_found': image_count,
        'videos_match': video_count == config['videos'],
        'images_match': image_count == config['images'],
    }

if __name__ == '__main__':
    config = {
        'path_dir': r'C:\Users\Mats\OneDrive\Desktop\DSA\data_check',  # Change this path if needed
        'videos': 1,
        'images': 1
    }

    check_folder_contents(config)
