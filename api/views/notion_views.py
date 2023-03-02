import os

from django.shortcuts import render
from notion_client import Client

from api.models import NotionDatabase


def notion_database_view(request):
    token = os.getenv('NOTION_TOKEN')
    database_id = os.getenv('NOTION_DATABASE_ID')
    
    notion = Client(auth=token)
    results = notion.databases.query(database_id).get('results')
    
    for result in results:
        title = result['properties']['title']['title'][0]['plain_text']
        description = result['properties']['description']['rich_text'][0]['plain_text']
        created_time = result['created_time']
        
        NotionDatabase.objects.update_or_create(
            title=title,
            defaults={
                'description': description,
                'created_time': created_time,
            }
        )
    
    return render(request, 'index.html')
