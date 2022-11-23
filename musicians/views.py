from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from musicians.models import Musician
from django.forms.models import model_to_dict


class MusicianView(APIView):
    def post(self, request):
        musician_data = request.data

        musician = Musician.objects.create(**musician_data)

        # musician = Musician.objects.create(
        #     first_name=musician_data["first_name"],
        #     last_name=musician_data["last_name"],
        #     instrument=musician_data["instruments"],
        # )

        return Response(model_to_dict(musician), 201)

    def get(self, request):
        musicians = Musician.objects.all()

        musicians_dict = musicians.values()

        # musicians = musicians.values()
        # musicians_dict = []

        # for musician in musicians:
        #     m = model_to_dict(musician)
        #     musicians_dict.append(m)

        return Response(musicians_dict)
