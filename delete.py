# import os
# import django
#
# # Указываем Django, где искать настройки
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diplommain.settings')  # Замените "myproject" на название вашего проекта
# django.setup()
#
# from django.db import connection
# from main.models import FirstVariantBd
# with connection.cursor() as cursor:
#     cursor.execute("DELETE FROM main_firstvariantbd")
#     cursor.execute("VACUUM")

#
# # Получаем все значения из столбца scientific_speciality
# scientific_specialities = FirstVariantBd.objects.values_list('scientific_speciality', flat=True)
#
# # Выводим данные
# for speciality in scientific_specialities:
#     if 'Юриспруденция' in speciality:
#         print(speciality)
# from main.views import user_data
#
# print(user_data)

s = {'Преподаватель': 'Иванов И.И.', 'Наименование предмета': 'Web-технологии', 'Направление': '38.03.01 - Экономика', 'competencies': [], 'topics': [{'topic': '54353', 'description':
'advafvd'}], 'curriculum': [{'profiles': 'Бизнес и финансы социальной сферы, Государственное и корпоративное казначейство, Государственные и муниципальные финансы, Государственный финансовый контроль, Управление финансовыми рисками и страхование, Финансы и банковское дело, Финансы и управление финансовыми активами', 'topics': [{'topic': '54353', 'total': '12', 'classroom': '3', 'lectures': '1', 'seminars': '1', 'independent': '3'}, {'topic': '', 'total': '108', 'classroom': '34', 'lectures': '16', 'seminars': '18', 'independent': '74'
}]}, {'profiles': 'Финансы и инвестиции', 'topics': [{'topic': '54353', 'total': '34', 'classroom': '12', 'lectures': '4', 'seminars': '3', 'independent': '42'}, {'topic': '', 'total': '108', 'classroom': '24', 'lectures': '8', 'seminars': '16', 'independent': '84'}]}]}

for i in s:
    print(i)