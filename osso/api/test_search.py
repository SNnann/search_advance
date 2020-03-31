from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from info.models import Level, Document
from .serializers import LevelSerializer, DocumentSerializer
from rest_framework import generics, permissions, authentication
from datetime import datetime
from datetime import timedelta

class LevelSearchAdvance(APIView):
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.AllowAny]

	def get(self, request, text, a0, a1, a2, a3, time,format=None):

		if time == 1:
			three_month = datetime.now() - timedelta(90)
			month = three_month.month
			print(month)

		if time == 2:
			six_month = datetime.now() - timedelta(180)
			month = six_month.month
			print(month)

		if time == 3:
			six_month_over = datetime.now() - timedelta(180)
			month = six_month_over.month
			print(month)

		if a0 != "":
			if a1 != "":
				if a2 != "":
					if a3 != "":
						print(text)
						#print(a0)
						#print(a1)
						#print(a2)
						#print(a3)
						data = Level.objects.filter(level_name__contains=text)
						data_level0 = Level.objects.filter(level_state__contains=0).objects.filter(level_name__contains=a0)
						data_level1 = Level.objects.filter(level_state__contains=1).objects.filter(level_name__contains=a1)
						data_level2 = Level.objects.filter(level_state__contains=2).objects.filter(level_name__contains=a2)
						data_level3 = Level.objects.filter(level_state__contains=3).objects.filter(level_name__contains=a4)

						dataall = data_level0.intersection(data_level1).intersection(data_level2).intersection(data_level3)

						if len(dataall) != 0:
							print(2)

							returndata = []
							for x in dataall:
								returndata.append({
									'id': x.level_id,
									'name': x.level_name,
									'ref': x.level_ref,
									'link':'/level1/' + data_level3 + '/drill/' +str(x.level_id),
									'state': x.level_state
									})

								linkdata = []
								for x in Document.objects.filter(document_name_contains=dataall):
									linkdata.append({
										'id': x.document_id,
										'name': x.document_name,
										'file': 'http://datacenter.thai-fda.com//' + x.document_file.url,
										'group': x.group,
										'isfile': True,
									})

								file = {
									'data': returndata,
									'file': linkdata,
									'count': len(returndata)+len(linkdata),
								}

								return Response(file)
							else:
								data = []
								print(7)
								return Response(data)

					else:
						#print(text)
						data = Level.objects.filter(Level_name__contains=text)
						data_level0 = Level.objects.filter(level_state__contains=0).objects.filter(level_name__contains=a0)
						data_level1 = Level.objects.filter(level_state__contains=1).objects.filter(level_name__contains=a1)
						data_level2 = Level.objects.filter(level_state__contains=2).objects.filter(level_name__contains=a3)

						dataall = data_level0.intersection(data_level1).intersection(data_level2)

						if len(dataall) != 0:
							print(2)
							returndata = []
							for x in dataall:
								returndata.append({
									'id': x.level_id,
									'name': x.level_name,
									'ref': x.level_ref,
									'link': '/level1/' + data_level2 + '/drill/' + str(x.level_id),
									'state': x.level_state
								})
							
							linkdata = []
							for x in Document.objects.filter(document_name__contains=dataall):
								linkdata.append({
									'id': x.document_id,
									'name': x.document_name,
									'file': 'http://datacenter.thai-fda.com//' + x.docuemnt_file.url,
									'group': x.group,
									'isfile': True,
								})

							file = {
								'data': returndata,
								'file': linkdata,
								'count': len(returndata)+len(linkdata),
							}

							return Response(file)
						else:
							data = []
							print(7)
							return Response(data)
						#print(a0)
						#print(a1)
						#print(a2)
				else:
					#print(text)
					data = Level.objects.filter(level_name__contains=text)
					data_level0 = Level.objects.filter(level_state__contains=0).objects.filter(level_name__contains=a0)
					data_level1 = Level.objects.filter(level_state__contains=1).objects.filter(level_name__contains=a1)
					dataall = data_level0.intersection(data_level1)
					if len(dataall) != 0:
						print(2)
						returndata = []
						for x in data:
							returndata.append({
								'id': x.level_id,
								'name': x.level_name,
								'ref': x.level_ref,
								'link': '/level1/' + data_level1 + '/drill/' + str(x.level_id),
								'state': x.level_state
							})
						linkdata = []
						for x in Document.objects.filter(document_name__contains=dataall):
							linkdata.append({
								'id': x.document_id,
								'name': x.document_name,
								'file': 'http://datacenter.thai-fda.com//' + x.document_file.url,
								'group': x.group,
								'isfile': True,
							})
						
						file = {
							'data': returndata,
							'file': linkdata,
							'count': len(returndata) + len(linkdata),
						}

						return Response(file)
					else:
						data = []
						print(7)
						return Response(data)

					#print(a0)
					#print(a1)
			else:
				#print(text)
				data = Level.objects.filter(level_name__contains=text)
				data2 = Level.objects.filter(group__contains=a0)
				data_level0 = Level.objects.filter(level_state__contains=0).objects.filter(level_name__contains=a0)
				dataall = data_level0

				if len(dataall) != 0:
					print(2)
					returndata =[]
					for x in dataall:
						returndata.append({
							'id': x.level_id,
							'name': x.level_name,
							'ref': x.level_ref,
							'link': '/level1/' + data_level0 + '/drill/' + str(x.level_id),
							'state': x.level_state
						})
					
					linkdata = []
					for x in Document.objects.filter(document_name__contains=dataall):
						linkdata.append({
							'id': x.document_id,
							'name': x.document_name,
							'file': 'http://datacenter.thai-fda.com//' + x.document_file.url,
							'group': x.group,
							'isfile': True,
						})
					
					file = {
						'data': returndata,
						'file': linkdata,
						'count': len(returndata)+len(linkdata),
					}

					return Response(file)
				else:
					data = []
					print(7)
					return Response(data)

				#print(a0)
		