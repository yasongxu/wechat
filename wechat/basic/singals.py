from django.dispatch import Signal

handler_add = Signal(providing_args=["user"])
view_init = Signal(providing_args=["user"])