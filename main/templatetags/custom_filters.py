from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """ Позволяет получать значение из словаря по ключу в шаблоне """
    return dictionary.get(key, "")

@register.filter
def attr(obj, attr_name):
    """ Получает атрибут объекта по имени """
    return getattr(obj, attr_name, "")