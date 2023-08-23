from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from datarepo.models import Category,SubCategory



# Create your views her


@api_view(['post'])
def add_category(request):
    name = request.POST.get('name', None)
    if name is None:
        context = {
            'message': 'name is missing'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_record = Category.objects.create(
                name=name
            )
            new_record.save()
            context = {
                'message': 'successfully added the category',
                'data': {
                    'category_id': new_record.id,
                    'name': new_record.name
                }
            }
            return Response(context, status=status.HTTP_200_OK)
        except ValueError:
            context = {
                'message': "invalled name"
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_category(request):
    all_categories = Category.objects.all()
    data = []
    for category in all_categories:
        temp = {
            'category_id': category.id,
            'category_name': category.name
        }
        data.append(temp)
    context = {
        'data': data
    }
    return Response(context, status=status.HTTP_200_OK)


@api_view(['PATCH'])
def update_category(request):
    category_id = request.POST.get('category_id', None)
    new_name = request.POST.get('name', None)
    if category_id is None:
        context = {
            'message': 'category_id is missing'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_category = Category.objects.get(id=category_id)
            get_category.name = new_name if new_name is not None else get_category.name
            get_category.save()
            context = {
                'category_id': get_category.id,
                'category_name': get_category.name
            }
            return Response(context, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            context = {
                'message': 'invalid category_id'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            context = {
                'message': "invalid category_id"
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_category(request):
    category_id = request.POST.get('category_id', None)
    if category_id is None:
        context = {
            'message': 'category_id is missing'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_category = Category.objects.get(id=category_id)
            get_category.delete()
            context = {
                'message': 'successfully deleted'
            }
            return Response(context, status=status.HTTP_200_OK)
        except ValueError:
            contact = {
                'message': 'ivalid....!!!'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def add_subcategory(request):
    name=request.POST.get('name',None)
    if name is None:
        context={
            'message':'name is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_record=SubCategory.objects.create(
                name=name
            )
            new_record.save()
            context = {
                'message': 'successfully added the sub_category',
                'data': {
                    'subcategory_id': new_record.id,
                    'name': new_record.name
                }
            }
            return Response (context,status=status.HTTP_200_OK)
        except ValueError:
            context={
                'message':'ivalid name....!!'
            }
            return Response (context,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_subcategory(request):
    all_subcategories=SubCategory.objects.all()
    data=[]
    for subcategory in all_subcategories:
        temp={
            'subcategory_id':subcategory.id,
            'subcategory_name':subcategory.name
        }
        data.append(temp)
        context={
            'data':data
        }
        return Response(context,status=status.HTTP_200_OK)


@api_view(['PATCH'])
def update_subcategory(request):
    subcatecory_id=request.POST.get('subcategory_id',None)
    if subcategory_id is None:
        context={
            'message':'subcategory_id is missing..'
        }
        return Response (context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_subcategory=SubCategory.objects.get(id=subcategory_id)
            get_subcategory.save()
            context={
                'subcategory_id':get_subcategory.id
            }
            return Response(context,status=status.HTTP_200_OK)
        except SubCategory.DoesNotExist:
            context={
                'message':'ivaliid subcategory_id'
            }
            return Response (context,status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            context={
                'message':'ivalid subcategory id!!!!'
            }
            return Response (context,status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def delete_subcategory(request):
    subcategory_id=request.POST.get('subcategory_id',None)
    if subcategory_id is None:
        context={
            'message':'subcategory_id missing..'
        }
        return Response (context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_subcategory=SubCategory.objects.get(id=subcategory_id)
            get_subcategory.delete()
            context={
                'message':'successfully deleted'
            }
            return Response(context,HTTP_200_OK)
        except ValueError:
            contact={
                'message':'invalid...!!!!'
            }
            return Response (contact,status=status.HTTP_400_BAD_REQUEST)