from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializer import Note, NoteSerializer

@api_view(['GET'])
def getNotes(request):
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def getNote(request, pk):
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def createNote(request):
# 
