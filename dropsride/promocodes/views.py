from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django.http import JsonResponse

from dropsride.promocodes.models import Coupons

User = get_user_model()

# Create your views here.
@login_required
def filter_coupons(request):
    if not request.user.is_staff:
        return JsonResponse({"status":401, "message":"Unauthorized Access Denied: You are not a staff"})

    if request.method == 'POST':
        return JsonResponse({"status":405, "message":"Method Not Allowed"})

    coupons = Coupons.objects.all().values('code', 'discount', "valid_from", "valid_to", 'active')
    coupons_list = list(coupons)
    return JsonResponse(coupons_list, safe=False)






@login_required
def create_coupons(request):
    discount = request.POST.get("discount")
    valid_from = request.POST.get("valid_from")
    valid_to = request.POST.get("valid_to")

    if not request.user.is_staff:
        return JsonResponse({"status":401, "message":"Unauthorized Access Denied: You are not a staff"})

    if request.method == "POST":
        if (discount, valid_from, valid_to) != "" or (discount, valid_from, valid_to) != None:
            Coupons.objects.create(discount=discount, valid_from=valid_from, valid_to=valid_to)
            return JsonResponse({"status":201, "message":"Coupon Created Successfully"})
        else:
            return JsonResponse({"status":204, "message":"No Content to process"})
    return render(request, "coupons/create.html")






login_required
def update_coupons(request, pk):
    discount = request.POST.get("discount")
    valid_from = request.POST.get("valid_from")
    valid_to = request.POST.get("valid_to")

    object = get_object_or_404(Coupons, pk=pk)
    context = {"object":object}


    if not request.user.is_staff:
        return JsonResponse({"status":401, "message":"Unauthorized Access Denied: You are not a staff"})

    if request.method == 'POST':
        return JsonResponse({"status":405, "message":"Method Not Allowed"})

    if request.method == "PUT":
        if (discount, valid_from, valid_to) != "" or (discount, valid_from, valid_to) != None:
            Coupons.objects.filter(pk=pk).update(discount=discount, valid_from=valid_from, valid_to=valid_to)
            return JsonResponse({"status":200, "message":"Coupon Updated Successfully"})
        else:
            return JsonResponse({"status":204, "message":"No Content to process"})
    return render(request, "coupons/update.html", context)






login_required
def delete_coupons(request, pk):
    if not request.user.is_staff:
        return JsonResponse({"status":401, "message":"Unauthorized Access Denied: You are not a staff"})

    try:
        Coupons.objects.get(pk=pk).delete()
        return JsonResponse({"status":200, "message":"Coupon Deleted Successfully"})
    except Coupons.DoesNotExist:
        return JsonResponse({"status":404, "message":"Coupon Code Does Not Exist"})
