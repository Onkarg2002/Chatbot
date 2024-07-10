from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json

def index(request):
    return render(request, 'chat/chat.html')

@csrf_exempt
def send_query(request):
    if request.method == 'POST':
        query = json.loads(request.body).get('query')
        session_id = request.session.session_key
        if not session_id:
            request.session.create()
            session_id = request.session.session_key
        
        response = requests.post('https://gemini-api-url', json={'query': query}, headers={'Authorization': 'AIzaSyAYz_SRYGUxl8Pvb08FvFQjGsTlRkRTHp4'})
        response_data = response.json()

        conversation = request.session.get('conversation', [])
        conversation.append({'query': query, 'response': response_data['response']})
        request.session['conversation'] = conversation[-3:]

        return JsonResponse({'response': response_data['response'], 'conversation': conversation})
    return JsonResponse({'error': 'Invalid request'}, status=400)
