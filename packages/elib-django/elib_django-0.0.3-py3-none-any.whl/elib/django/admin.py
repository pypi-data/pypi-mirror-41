#
# copyright (c) 2019 east301
#
# This software is released under the Apache License, Version 2.0.
# https://opensource.org/licenses/Apache-2.0
#

from django.contrib import admin


def reregister_model_admin(model):
    def apply(model_admin):
        admin.site.unregister(model)
        admin.site.register(model, model_admin)
        return model_admin

    return apply


def short_description(description):
    def apply(func):
        func.short_description = description
        return func

    return apply


def order_field(field):
    def apply(func):
        func.admin_order_field = field
        return func

    return apply
