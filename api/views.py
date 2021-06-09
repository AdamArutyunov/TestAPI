import json
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from api.models import *


class GetAll(View):
    def get(self, request):
        institutions = Institution.objects.all()

        institutions_response = list(map(lambda x: x.to_dict(), institutions))

        return JsonResponse(institutions_response, safe=False)


class GetById(View):
    def get(self, request, institution_id):
        try:
            institution = Institution.objects.get(id=institution_id)
        except Institution.DoesNotExist:
            return HttpResponseNotFound("Instutituion with specifed ID is not found.")

        return JsonResponse(institution.to_dict(), safe=False)


class Search(View):
    http_method_names = ['post']

    def post(self, request):
        search_fields = ['id', 'type', 'full_name', 'short_name', 'director', 'address', 'phone_number', 'site_url']

        try:
            request_json = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON.")

        query_kwargs = {}

        for key, value in request_json.items():
            if key in search_fields:
                query_kwargs[f'{key}__icontains'] = rf"{str(value)}"

        print(query_kwargs)
        institutions = Institution.objects.filter(**query_kwargs)
        print(institutions.query)

        institutions_response = list(map(lambda x: x.to_dict(), institutions))

        return JsonResponse(institutions_response, safe=False)


class Create(View):
    http_method_names = ['post']

    def post(self, request):
        create_fields = ['type', 'full_name', 'short_name', 'director', 'address', 'phone_number', 'site_url']

        try:
            request_json = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON.")
        data = {}

        for key, value in request_json.items():
            if key not in create_fields:
                return HttpResponseBadRequest(f"Unknown field '{key}'.")

            value = value.strip()

            if key == 'phone_number':
                value = ''.join(list(filter(lambda x: x.isdigit() or x in ',;', list(value))))

            data[key] = value

        try:
            institution = Institution.objects.create(**data)
            return JsonResponse(institution.to_dict())
        except Exception as e:
            return HttpResponseBadRequest(e)


class Delete(View):
    http_method_names = ['delete']

    def delete(self, request, institution_id):
        try:
            institution = Institution.objects.get(id=institution_id)
        except Institution.DoesNotExist:
            return HttpResponseNotFound("Instutituion with specifed ID is not found.")

        institution.delete()

        return JsonResponse({'status': 'OK'})


class Update(View):
    http_method_names = ['put']

    def put(self, request, institution_id):
        update_fields = ['type', 'full_name', 'short_name', 'director', 'address', 'phone_number', 'site_url']

        try:
            request_json = json.loads(request.body)
        except json.decoder.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON.")

        try:
            institution = Institution.objects.get(id=institution_id)
        except Institution.DoesNotExist:
            return HttpResponseNotFound("Instutituion with specifed ID is not found.")

        for key, value in request_json.items():
            if key in update_fields:
                setattr(institution, key, value)

        try:
            institution.save()
            return JsonResponse(institution.to_dict())
        except Exception as e:
            return HttpResponseBadRequest(e)


