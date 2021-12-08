# from django.test import TestCase
# import os, sys
# import datetime as dt

# from django.contrib.auth import get_user_model
# from django.db import DatabaseError

# proj = os.path.dirname(os.path.abspath('manage.py'))
# sys.path.append(proj)
# os.environ["DJANGO_SETTINGS_MODULE"] = "resume_service.settings"

# # import django
# # django.setup()

# # from scraping.parsers import *
# from scraping.models import Vacancy, Error, Url
# # Create your tests here.
# qs = Url.objects.all().values()
# url_dict = {(q['city_id'], q['language_id']): q['url_data'] for q in qs}
# urls = []
# print(url_dict)

# for pair in _settings:
#     if pair in url_dict:
#         tmp = {}
#         tmp['city'] = pair[0]
#         tmp['language'] = pair[1]
#         url_data = url_dict.get(pair)
#         if url_data:
#             tmp['url_data'] = url_dict.get(pair)
#             urls.append(tmp)
#             print(urls)