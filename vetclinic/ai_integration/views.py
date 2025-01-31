from django.shortcuts import render
from django.http import JsonResponse
import requests

def ai_chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        # Call the OpenWeb UI API with the user input
        response = requests.post(
            'https://api.openwebui.com/ask',  # Replace with actual API endpoint
            json={'question': user_input}
        )
        ai_response = response.json().get('answer', 'Sorry, I could not process your request.')
        return JsonResponse({'answer': ai_response})
    return render(request, 'ai_integration/chat.html')