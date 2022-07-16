from django.apps import AppConfig


class RegisterCustomerConfig(AppConfig):
    name = 'register_customer'

    def ready(self):
        import register_customer.signals
