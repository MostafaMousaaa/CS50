import sys
import os
from PIL import Image, ImageDraw
import face_recognition
from cs50 import get_string

def load_known_faces(directory):
    """Load known faces from a directory"""
    known_face_encodings = []
    known_face_names = []
    
    if not os.path.exists(directory):
        print(f"Directory {directory} not found")
        return known_face_encodings, known_face_names
    
    # Load each image file in the directory
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Load image
            image_path = os.path.join(directory, filename)
            image = face_recognition.load_image_file(image_path)
            
            # Get face encoding
            face_encodings = face_recognition.face_encodings(image)
            
            if face_encodings:
                # Use the first face found in the image
                known_face_encodings.append(face_encodings[0])
                # Use filename (without extension) as name
                name = os.path.splitext(filename)[0]
                known_face_names.append(name)
                print(f"Loaded {name} from {filename}")
            else:
                print(f"No face found in {filename}")
    
    return known_face_encodings, known_face_names

def recognize_faces_in_image(image_path, known_face_encodings, known_face_names):
    """Recognize faces in a given image"""
    # Load the image
    try:
        image = face_recognition.load_image_file(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return
    
    # Find face locations and encodings
    print("Looking for faces...")
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    
    print(f"Found {len(face_locations)} face(s) in the image")
    
    # Convert image to PIL format for drawing
    pil_image = Image.fromarray(image)
    draw = ImageDraw.Draw(pil_image)
    
    # Recognize each face
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"
        
        # Calculate face distances
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        
        if matches:
            # Find the best match
            best_match_index = face_distances.argmin()
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                confidence = 1 - face_distances[best_match_index]
                print(f"Recognized: {name} (confidence: {confidence:.2f})")
        
        # Draw rectangle around face
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 255, 0), width=3)
        
        # Draw name below face
        text_width = draw.textlength(name)
        draw.rectangle(((left, bottom - 35), (right, bottom)), fill=(0, 255, 0), outline=(0, 255, 0))
        draw.text((left + 6, bottom - 32), name, fill=(255, 255, 255))
    
    # Save the result
    output_path = "recognized_" + os.path.basename(image_path)
    pil_image.save(output_path)
    print(f"Result saved as {output_path}")
    
    return len(face_locations)

def compare_two_faces(image1_path, image2_path):
    """Compare two faces to see if they're the same person"""
    try:
        # Load images
        image1 = face_recognition.load_image_file(image1_path)
        image2 = face_recognition.load_image_file(image2_path)
        
        # Get face encodings
        encoding1 = face_recognition.face_encodings(image1)
        encoding2 = face_recognition.face_encodings(image2)
        
        if not encoding1:
            print(f"No face found in {image1_path}")
            return
        
        if not encoding2:
            print(f"No face found in {image2_path}")
            return
        
        # Compare faces
        results = face_recognition.compare_faces([encoding1[0]], encoding2[0])
        distance = face_recognition.face_distance([encoding1[0]], encoding2[0])
        
        if results[0]:
            print(f"Same person! Distance: {distance[0]:.3f}")
        else:
            print(f"Different people. Distance: {distance[0]:.3f}")
        
        return results[0], distance[0]
        
    except Exception as e:
        print(f"Error comparing faces: {e}")
        return None, None

def batch_face_recognition(input_directory, known_faces_directory):
    """Process multiple images for face recognition"""
    # Load known faces
    known_face_encodings, known_face_names = load_known_faces(known_faces_directory)
    
    if not known_face_encodings:
        print("No known faces loaded. Please add reference images.")
        return
    
    # Process all images in input directory
    if not os.path.exists(input_directory):
        print(f"Input directory {input_directory} not found")
        return
    
    results = []
    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_directory, filename)
            print(f"\nProcessing {filename}...")
            
            faces_found = recognize_faces_in_image(image_path, known_face_encodings, known_face_names)
            results.append((filename, faces_found))
    
    # Summary
    print(f"\n=== Batch Processing Summary ===")
    total_images = len(results)
    total_faces = sum(count for _, count in results)
    
    print(f"Processed {total_images} images")
    print(f"Found {total_faces} total faces")
    
    for filename, count in results:
        print(f"{filename}: {count} face(s)")

def create_face_database():
    """Interactive function to create a face database"""
    print("=== Create Face Database ===")
    
    database_dir = "known_faces"
    if not os.path.exists(database_dir):
        os.makedirs(database_dir)
        print(f"Created directory: {database_dir}")
    
    print(f"Add reference images to the '{database_dir}' directory")
    print("Name each file with the person's name (e.g., 'john.jpg', 'mary.png')")
    print("Press Enter when you've added the images...")
    input()
    
    # Load and verify the database
    known_face_encodings, known_face_names = load_known_faces(database_dir)
    
    print(f"Loaded {len(known_face_names)} known faces:")
    for name in known_face_names:
        print(f"  - {name}")
    
    return database_dir

def main():
    """Main face recognition program"""
    print("=== Face Recognition System ===")
    print("This program demonstrates face recognition using Python")
    print("Note: Requires face_recognition and PIL libraries")
    print("Install with: pip install face-recognition pillow")
    
    try:
        import face_recognition
        from PIL import Image
    except ImportError as e:
        print(f"Required library not installed: {e}")
        print("Please install required libraries and try again")
        return
    
    while True:
        print("\nOptions:")
        print("1. Recognize faces in an image")
        print("2. Compare two faces")
        print("3. Batch process images")
        print("4. Create face database")
        print("5. Exit")
        
        choice = get_string("Choose an option: ")
        
        if choice == "1":
            image_path = get_string("Enter image path: ")
            database_dir = get_string("Enter known faces directory (or press Enter for 'known_faces'): ")
            if not database_dir:
                database_dir = "known_faces"
            
            known_encodings, known_names = load_known_faces(database_dir)
            if known_encodings:
                recognize_faces_in_image(image_path, known_encodings, known_names)
            else:
                print("No known faces found. Create a database first.")
        
        elif choice == "2":
            image1 = get_string("Enter first image path: ")
            image2 = get_string("Enter second image path: ")
            compare_two_faces(image1, image2)
        
        elif choice == "3":
            input_dir = get_string("Enter input directory: ")
            database_dir = get_string("Enter known faces directory: ")
            batch_face_recognition(input_dir, database_dir)
        
        elif choice == "4":
            create_face_database()
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice")

# Demonstration of face recognition concepts
def demonstrate_concepts():
    """Demonstrate key face recognition concepts"""
    print("=== Face Recognition Concepts ===")
    
    print("\n1. Face Detection:")
    print("   - Locate faces in images")
    print("   - Return bounding box coordinates")
    print("   - Uses machine learning models")
    
    print("\n2. Face Encoding:")
    print("   - Convert face to numerical representation")
    print("   - 128-dimensional vector")
    print("   - Captures unique facial features")
    
    print("\n3. Face Recognition:")
    print("   - Compare face encodings")
    print("   - Calculate similarity/distance")
    print("   - Determine if faces match")
    
    print("\n4. Applications:")
    print("   - Security systems")
    print("   - Photo organization")
    print("   - Social media tagging")
    print("   - Attendance systems")
    
    print("\n5. Challenges:")
    print("   - Lighting conditions")
    print("   - Pose variations")
    print("   - Age changes")
    print("   - Privacy concerns")

if __name__ == "__main__":
    # Uncomment to see concept demonstration
    # demonstrate_concepts()
    
    main()
