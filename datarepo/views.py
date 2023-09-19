from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from datarepo.models import Category, SubCategory, Products


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
    subcategory_id = request.POST.get('subcategory_id', None)
    name = request.POST.get('name', None)
    if subcategory_id is None:
        context = {
            'message': 'subcategory_id is misssing...'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_record = SubCategory.objects.create(
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
            return Response(context, status=status.HTTP_200_OK)
        except ValueError:
            context = {
                'message': 'ivalid name....!!'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        if name is None:
            context = {
                'message': 'name is missing'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                new_record = SubCategory.objects.create(
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
                return Response(context, status=status.HTTP_200_OK)
            except ValueError:
                context = {
                    'message': 'ivalid name....!!'
                }
                return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_subcategory(request):
    all_subcategories = SubCategory.objects.all()
    data = []
    for subcategory in all_subcategories:
        temp = {
            'subcategory_id': subcategory.id,
            'subcategory_name': subcategory.name
        }
        data.append(temp)
        context = {
            'data': data
        }
        return Response(context, status=status.HTTP_200_OK)


@api_view(['PATCH'])
def update_subcategory(request):
    category_id=request.POST.get('category_id',None)
    subcatecory_id = request.POST.get('subcategory_id', None)
    new_name = request.POST.get('new_name', None)
    if subcategory_id is None:
        context = {
            'message': 'subcategory_id is missing..'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_subcategory = SubCategory.objects.get(id=subcategory_id)
            get_subcategory.name = new_name if new_name is None else get_subcategory, name
            get_subcategory.save()
            context = {
                'subcategory_id': get_category.id,
                'subcategory_name': get_category.name
            }
            return Response(context, status=status.HTTP_200_OK)
        except SubCategory.DoesNotExist:
            context = {
                'message': 'ivaliid subcategory_id'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            context = {
                'message': 'ivalid subcategory id!!!!'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_subcategory(request):
    subcategory_id = request.POST.get('subcategory_id', None)
    if subcategory_id is None:
        context = {
            'message': 'subcategory_id missing..'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_subcategory = SubCategory.objects.get(id=subcategory_id)
            get_subcategory.delete()
            context = {
                'message': 'successfully deleted'
            }
            return Response(context, HTTP_200_OK)
        except ValueError:
            contact = {
                'message': 'invalid...!!!!'
            }
            return Response(contact, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_products(request):
    subcategory_id = request.POST.get('subcategory_id', None)
    name = request.POST.get('name', None)
    price = request.POST.get('price', None)
    description = request.POST.get('description', None)
    image=request.FILES.get('image',None)
    if subcategory_id is None or name is None or price is None or image is None or description is None:
        context = {
            'message': 'subcategory_id/name/price/image/description is missing'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_record = Products.objects.create(
                subcategory_id=subcategory_id,
                name=name,
                price=price,
                image=image,
                description=description,
            )
            new_record.save()
            context = {
                'message': 'Product added successfully',
                'data': {
                    'product_id': new_record.id,
                    'subcategory_id': new_record.subcategory_id,
                    'subcategory_name': new_record.subcategory.name,
                    'product_name': new_record.name,
                    'image':new_record.image.url if new_record.image else None,
                    'description': new_record.description,
                    'created_at': new_record.created_at,
                    'updated_at': new_record.updated_at
                }
            }
            return Response(context, status=status.HTTP_200_OK)
        except ValueError as e:
            context = {
                'message': str(e)
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        #except IntegrityError:
         #   context = {
          #      'message': 'invalid subcategory_id..'
           # }
           # return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_products(request):
    all_products = Products.objects.all()
    data = []
    for products in all_products:
        temp = {
            'product_id': products.id,
            'product_name': products.name,
            'product_price': products.price,
            'product_description': products.description,
        }
        data.append(temp)
        context = {
            'data': data
        }
        return Response(context, status=status.HTTP_200_OK)


@api_view(['PATCH'])
def update_products(request):
    product_id = request.POST.get('product_id', None)
    subcategory_id = request.POST.get('subcategory_id', None)
    new_name = request.POST.get('name', None)
    price = request.POST.get('price', None)
    description = request.POST.get('description', None)
    if product_id is None:
        context = {
            'message': 'product_id/subactegory_id/name/price/description is missing'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_products = Products.objects.get(id=product_id)
            get_products.name=new_name if new_name is not None else get_products.name
            products.save()

            context = {
                'message': 'Products updated successfully',
                'data': {
                    'product_id': products.id,
                    'subcategory_id': products.subcategory_id,
                    'name': products.name,
                    'price': products.price,
                    'description': products.description,
                    'created_at': products.created_at,
                    'updated_at': products.updated_at,
                }
            }
            return Response(context, status=status.HTTP_200_OK)
        except Products.DoesNotExist:
            context = {
                'message': 'product not found'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            context = {
                'message': 'invalid_id....'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_products(request):
    product_id = request.POST.get('product_id')
    if product_id is None:
        context = {
            'message': 'product is missing'
        }
        return Response(conttext, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            get_product = Products.objects.get(id=product_id)
            get_product.delete()
            context = {
                'message': 'successfully deleted Product'
            }
            return Response(context, status=status.HTTP_200_OK)
        except ValueError:
            context = {
                'message': 'invalid Product_id'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)
