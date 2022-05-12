
import uuid

from login_customer.functions import get_response, get_expire_time
from register_customer.models import Customer
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def loginC(request):
    if request.method == "POST":
        try:
            post_data = request.POST
            phone = post_data.get('phone')
            password = post_data.get('password')
            customer = Customer.objects.filter(national_code=phone).first()
            if customer:
                if check_password(password, customer.password):
                    token = uuid.uuid4().hex
                    customer.user_token = token
                    customer.expire_token = get_expire_time()
                customer.save()
                return get_response(60, '{{"token": "{}"}}'.format(token))
            else:
                return get_response(660)
        except Exception as d:
            return get_response(600)
    return get_response(601)
