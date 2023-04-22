import pprint

from django.contrib.auth import get_user_model
from thefuzz import fuzz

from config import celery_app
from config.mixins import ninVerify, phoneVerify
from dropsride.utils.logger import LOGGER

User = get_user_model()


@celery_app.task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()


@celery_app.task()
def verify_user_phone(dob, phone, short_name, email):
    if phone != "" and dob != "":
        user = User.objects.get(email=email)
        res = phoneVerify(phone)
        if res["statusCode"] == 200:
            for resp in res["data"]["phoneDetails"]:
                fn = resp["fullName"]
                res_dob = res["dateOfBirth"]
                point = fuzz.ratio(short_name, fn)
                LOGGER.info(f"Validate Phone: {point}")
                if point < 75 and res_dob == dob:
                    user.profile.phone_verifed = False
                    user.profile.save(update_fields=["phone_verifed"])
                else:
                    user.profile.phone_verifed = True
                    user.profile.save(update_fields=["phone_verifed"])


# @celery_app.task()
# def verify_nin_or_bvn(nin, bvn, user, first_name, last_name, date_of_birth, instance):
#     if nin != "":
#         if (
#             instance
#             and instance.nin != nin
#             and VerifiedDocuments.objects.filter(user=user.id, nin=nin).exists()
#         ):
#             raise serializers.ValidationError(
#                 {"nin": "This nin has already been used by another driver"}
#             )

#         res = ninVerify(nin, fn, ln, dob)
#         if res["statusCode"] == 200:
#             res_fn = res["data"]["validations"]["data"]["firstName"]["validated"]
#             phone = res["data"]["mobile"]
#             res_ln = res["data"]["validations"]["data"]["lastName"]["validated"]
#             if res_fn != True:
#                 raise serializers.ValidationError(
#                     {
#                         "nin": "Your first name doesn't match what you have on your NIN"
#                     }
#                 )
#             elif res_ln != True:
#                 raise serializers.ValidationError(
#                     {
#                         "nin": "Your last name doesn't match what you have on your NIN"
#                     }
#                 )
#             elif res_fn != True and res_ln != True:
#                 raise serializers.ValidationError(
#                     {
#                         "nin": "This NIN is incorrect. It fails to validate against your given name. Please ensure it is correct"
#                     }
#                 )

#             if phone and user.profile.phone != phone:
#                 raise serializers.ValidationError(
#                     {"phone": "This Phone Number is not associated with a NIN"}
#                 )

#     if data["bvn"] != "":
#         LOGGER.info(self.instance.bvn)
#         if (
#             self.instance
#             and self.instance.bvn != bvn
#             and VerifiedDocuments.objects.filter(user=user.id, bvn=bvn).exists()
#         ):
#             raise serializers.ValidationError(
#                 {"bvn": "This bvn has already been used by another driver"}
#             )

#         res = bvnVerify(bvn, fn, ln, dob)
#         if res["statusCode"] == 200:
#             res_fn = res["data"]["validations"]["data"]["firstName"]["validated"]
#             phone = res["data"]["mobile"]
#             res_ln = res["data"]["validations"]["data"]["lastName"]["validated"]
#             if res_fn != True:
#                 raise serializers.ValidationError(
#                     {
#                         "bvn": "Your first name doesn't match what you have on your BVN"
#                     }
#                 )
#             elif res_ln != True:
#                 raise serializers.ValidationError(
#                     {
#                         "bvn": "Your last name doesn't match what you have on your BVN"
#                     }
#                 )
#             elif res_fn != True and res_ln != True:
#                 raise serializers.ValidationError(
#                     {
#                         "bvn": "This BVN is incorrect. It fails to validate against your given name. Please ensure it is correct"
#                     }
#                 )

#             if phone and user.profile.phone != phone:
#                 raise serializers.ValidationError(
#                     {
#                         "phone": "This Phone Number on registered with your BVN does not validate with what we have on our system"
#                     }
#                 )
