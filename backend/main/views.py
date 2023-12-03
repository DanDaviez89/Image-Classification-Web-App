import joblib
from PIL import Image
import numpy as np
import io
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from tensorflow.keras.models import load_model

model = load_model('C:\\Users\Owner\\OneDrive\\Documents\\Programming\\Web Dev\\Machine Learning Apps\\Image Classification\\ML Models')

@api_view(['POST'])
def uploadedImage(request):
    if request.method == 'POST':
        # Get the file from request
        file = request.FILES['image']
        
        if not file:
            return JsonResponse({'message': 'No file uploaded.'}, status=400)

        # Read the image, resize it, and prepare for the model
        img = Image.open(file)
        img = img.resize((126, 126))  # Resize as per the model's input size
        img_array = np.array(img)
        img_array = img_array / 255.0  # Normalize
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        prediction = model.predict(img_array)
        probability = prediction[0][0]  # Assuming model outputs a single probability

        # Decide the class based on the probability
        threshold = 0.5 
        class_label = 1 if probability > threshold else 0

        # Return the response
        return JsonResponse({'prediction': class_label, 'probability': float(probability)})


    return JsonResponse({'message': 'Invalid request'}, status=400)