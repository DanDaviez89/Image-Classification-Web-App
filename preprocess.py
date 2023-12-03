from PIL import Image
import os

def delete_corrupt_images(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.jpg'):  # You can add other file types if needed
            try:
                with Image.open(os.path.join(directory, filename)) as img:
                    img.verify()  # Verify that it is, in fact, an image
            except (IOError, SyntaxError):
                print(f'Deleting corrupt file: {filename}')
                os.remove(os.path.join(directory, filename))

def resize_images(input_directory, output_directory, max_images=5000, size=(126, 126)):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    images_processed = 0
    for filename in os.listdir(input_directory):
        if images_processed >= max_images:
            break
        
        if filename.endswith('.jpg'):  # Add other file types if necessary
            input_filepath = os.path.join(input_directory, filename)
            output_filepath = os.path.join(output_directory, filename)

            with Image.open(input_filepath) as img:
                img = img.convert('RGB')  # Convert the image to RGB mode
                img = img.resize(size, Image.Resampling.LANCZOS)
                img.save(output_filepath)

            images_processed += 1


                
# Example usage
#delete_corrupt_images('C:\\Users\\Owner\\Downloads\\randomImages\\natural_images\\person')

resize_images('C:\\Users\\Owner\\Downloads\\DogCats\\PetImages\\Dog', 'C:\\Users\\Owner\\OneDrive\\Documents\\Programming\\Web Dev\\Machine Learning Apps\\Image Classification\\Images\\dogs', max_images=5000)
resize_images('C:\\Users\\Owner\\Downloads\\randomImages\\natural_images\\person', 'C:\\Users\\Owner\\OneDrive\\Documents\\Programming\\Web Dev\\Machine Learning Apps\\Image Classification\\Images\\non-dogs', max_images=800)
resize_images('C:\\Users\\Owner\\Downloads\\randomImages\\natural_images\\cat', 'C:\\Users\\Owner\\OneDrive\\Documents\\Programming\\Web Dev\\Machine Learning Apps\\Image Classification\\Images\\non-dogs', max_images=800)
resize_images('C:\\Users\\Owner\\Downloads\\randomImages\\natural_images\\motorbike', 'C:\\Users\\Owner\\OneDrive\\Documents\\Programming\\Web Dev\\Machine Learning Apps\\Image Classification\\Images\\non-dogs', max_images=800)
resize_images('C:\\Users\\Owner\\Downloads\\randomImages\\natural_images\\fruit', 'C:\\Users\\Owner\\OneDrive\\Documents\\Programming\\Web Dev\\Machine Learning Apps\\Image Classification\\Images\\non-dogs', max_images=800)
resize_images('C:\\Users\\Owner\\Downloads\\randomImages\\natural_images\\car', 'C:\\Users\\Owner\\OneDrive\\Documents\\Programming\\Web Dev\\Machine Learning Apps\\Image Classification\\Images\\non-dogs', max_images=800)
resize_images('C:\\Users\\Owner\\Downloads\\randomImages\\natural_images\\airplane', 'C:\\Users\\Owner\\OneDrive\\Documents\\Programming\\Web Dev\\Machine Learning Apps\\Image Classification\\Images\\non-dogs', max_images=800)
