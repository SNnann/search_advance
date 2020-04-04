from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from info.models import Level, Document
from .serializers import LevelSerializer, DocumentSerializer
from rest_framework import generics, permissions, authentication
from django.utils import timezone
from datetime import datetime, timedelta

class LevelViewSet(ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class LevelSearch(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request,text, format=None):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        print(text)
        data = Level.objects.filter(level_name__contains=text)
        data2 = Level.objects.filter(group__contains=text)
        if len(data) > len(data2):
            dataall = data.union(data2)
        else:
            dataall = data2.union(data)
        if len(dataall) != 0:
            print(2)
            returndata = []
            for x in data:
                returndata.append({
                    'id': x.level_id,
                    'name': x.level_name,
                    'ref': x.level_ref,
                    'link': '/level1/' + text + '/drill/' + str(x.level_id),
                    'state': x.level_state
                })
            linkdata = []
            for x in Document.objects.filter(document_name__contains=text):
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
            '''data = Level.objects.filter(level_name__contains=text, level_state=2)
            if len(data) != 0:
                print(3)
                returndata = []
                for x in data:
                    returndata.append({
                        'id': x.level_id,
                        'name': x.level_name,
                        'ref': x.level_ref,
                        'state': x.level_state
                    })
                redata = {
                    'data': returndata,
                    'count': len(returndata)
                }
                return Response(redata)
            else:
                data = Level.objects.filter(level_name__contains=text, level_state=3)
                if len(data) != 0:
                    print(4)
                    returndata = []
                    for x in data:
                        returndata.append({
                            'id': x.level_id,
                            'name': x.level_name,
                            'ref': x.level_ref,
                            'state': x.level_state
                        })
                    redata = {
                        'data': returndata,
                        'count': len(returndata)
                    }
                    return Response(redata)
                else:
                    data = Level.objects.filter(level_name__contains=text, level_state=4)
                    if len(data) != 0:
                        print(5)
                        returndata = []
                        for x in data:
                            returndata.append({
                                'id': x.level_id,
                                'name': x.level_name,
                                'state': x.level_state,
                                'ref': x.level_ref,
                                'group': x.group
                            })
                        redata = {
                            'data':returndata,
                            'count':len(returndata)
                        }
                        return Response(redata)
                    else:
                        data = Level.objects.filter(level_name__contains=text, level_state=5)
                        if len(data) != 0:
                            print(6)
                            returndata = []
                            for x in data:
                                returndata.append({
                                    'id': x.level_id,
                                    'name': x.level_name,
                                    'state': x.level_state,
                                    'ref': x.level_ref,
                                    'group': x.group
                                })
                            redata = {
                                'data': returndata,
                                'count': len(returndata)
                            }
                            return Response(redata)
                        else:
                            data = []
                            print(7)
                            return Response(data)'''
            data = []
            print(7)
            return Response(data)


class LevelDrill(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request,id, format=None):
        data = Level.objects.get(level_id=id)
        if data != None:

            if data.level_link.all().count() > 0:
                linkdata = []
                data.rank += 1
                data.save()
                for x in data.level_link.all():
                    linkdata.append({
                        'id': x.level_id,
                        'name': x.level_name,
                        'state': x.level_state,
                        'ref':x.level_ref,
                        'group': x.group,
                        'isfile': False,
                    })
                redata = {
                    'data': linkdata,
                    'name': data.level_name,
                    'route': data.level_route,
                    'role': data.level_role,
                    'isfile': False
                }
                return Response(redata)
            else:
                print(3)
                if Document.objects.filter(document_link__level_id=id).exists():
                    linkdata = []
                    data.rank += 1
                    data.save()
                    for x in Document.objects.filter(document_link__level_id=id):
                        linkdata.append({
                            'id': x.document_id,
                            'name': x.document_name,
                            'file': 'http://datacenter.thai-fda.com//'+x.document_file.url,
                            'group': x.group,
                            'isfile': True,
                        })
                    redata = {
                        'data': linkdata,
                        'name': data.level_name,
                        'route': data.level_route,
                        'role': data.level_role,
                        'isfile': True
                    }
                    return Response(redata)
                else:
                    linkdata = []
                    return Response(linkdata)
        else:
            data = []
            return Response(data)

class LevelSearchAdvance(APIView):
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.AllowAny]

	def post(self, request):
		now = datetime.now()
		#a0="อาหาร"
		#a1="สถานที่"    
		#a2="ขออนุญาตสถานที่ กรณีเข้าข่ายโรงงาน (เครื่องจักรมากกว่า 50 เครื่อง)"
		#a3="ขอใบอนุญาตใหม่"
		#time=1
		list_data = []
		list2 = []
		list3 = []
		print(request.data)
		if 'a0' in request.data:
			a0 = request.data['a0']
		else:
			a0 = ''

		if 'a1' in request.data:
			a1 = request.data['a1']
		else:
			a1 = ''
		
		if 'a2' in request.data:
			a2 = request.data['a2']
		else:
			a2 = ''
		
		if 'a3' in request.data:
			a3 = request.data['a3']
		else:
			a3 = ''
		if 'time' in request.POST:
			time = request.POST.get('time')
		else:
			time = 0

		print(time)
		
		def three_month_ago(value):
			delta = timedelta(days=90)
			return value - delta
		def six_month_ago(value):
			delta = timedelta(days=180)
			return value - delta
		
		t_time = 0
		check = ""
		if time == 1:
			t_time = three_month_ago(now)
			check = "time=1"
		elif time == 2:
			t_time = six_month_ago(now)
			check = "time=2"
		elif time == 0:
			t_time = datetime(20,1,1)
			check = "time=3"

		print(check)
		print(now)
		print(t_time)

		if a0 != "":
			if a1 != "":
				if a2 != "":
					if a3 != "":
						print("level3")
						#print(a0)
						list_data.append(a0)
						#print(a1)
						list_data.append(a1)
						#print(a2)
						list_data.append(a2)
						#print(a3)
						list_data.append(a3)

						data_level0 = Level.objects.filter(group=a0, level_name=a0)
						data_level1 = Level.objects.filter(group=a0, level_name__contains=a1, Date__gte=t_time)
						print(data_level0)

						for x in data_level0:
							if a0 == x.level_name:
								list3.append(x)

						for x in data_level1:
							for y in x.level_link.all():
								if a2 in y.level_name:
									list2.append(y)
									list3.append(x)
						for x in list2:
							for y in x.level_link.all():
								if a3 in y.level_name:
									list3.append(x)
									list3.append(y)

						if len(list3) != 0:
							
							returndata = []
							for x in list3:
								returndata.append({
									'id': x.level_id,
									'name': x.level_name,
									'ref': x.level_ref,
									'link': '/level1/' + x.level_name + '/drill/' +str(x.level_id),
									'state': x.level_state,
									'date': x.Date,
									'rank': x.rank
								})
							linkdata = []
							for x in Document.objects.filter(document_name__contains=list3):
								linkdata.append({
									'id':x.document_id,
									'name': x.document_name,
									'file': 'http://datacenter.thai-fda.com//' + x.document_file.url,
									'group': x.group,
									'isFile': True,
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

					else:
						print("level2")
						#print(a0)
						list_data.append(a0)
						#print(a1)
						list_data.append(a1)
						#print(a2)
						list_data.append(a2)

						data_level0 = Level.objects.filter(group=a0, level_name__contains=a0)
						data_level1 = Level.objects.filter(group=a0, level_name__contains=a1, Date__gte=t_time)

						for x in data_level0:
							if a0 == x.level_name:
								list3.append(x)

						for x in data_level1:
							for y in x.level_link.all():
								if a2 in y.level_name:
									list3.append(x)
									list3.append(y)
						
						if len(list3) != 0:
							print(2)
							returndata = []
							for x in list3:
								returndata = []
								for x in list3:
									returndata.append({
										'id': x.level_id,
										'name': x.level_name,
										'ref': x.level_ref,
										'link': '/level1/' + x.level_name + '/drill/' + str(x.level_id),
										'state': x.level_state,
										'date': x.Date,
										'rank': x.rank,
									})
								
								linkdata = []
								for x in Document.objects.filter(document_name__contains=list3):
									linkdata.append({
										'id': x.document_id,
										'name': x.document_name,
										'file': 'http://datacenter.thai-fda.com//' + x.document_file.url,
										'group': x.group,
										'isFile': True,
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
				else:
					print("level1")
					#print(a0)
					list_data.append(a0)
					#print(a1)
					list_data.append(a1)

					data_level0 = Level.objects.filter(group=a0, level_name=a0, Date__gte=t_time)
					for x in data_level0:
						for y in x.level_link.all():
							if a1 in y.level_name:
								list3.append(x)
								list3.append(y)
					
					if len(list3) != 0:
						print(2)
						returndata = []
						for x in list3:
							returndata.append({
								'id': x.level_id,
								'name': x.level_name,
								'ref': x.level_ref,
								'link': '/level1/' + x.level_name + '/drill/' + str(x.level_id),
								'state': x.level_state,
								'date': x.Date,
								'rank': x.rank,
							})
						linkdata = []
						for x in Document.objects.filter(document_name__contains=list3):
							linkdata.append({
								'id': x.document_id,
								'name': x.document_name,
								'file': 'http://datacenter.thai-fda.com//' + x.document_file.url,
								'group': x.group,
								'isFile': True,
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

			else:
				#print(a0)
				data_level0 = Level.objects.filter(group=a0, level_name__contains=a0, Date__gte=t_time)
				print(t_time)
				print(data_level0)
				for x in data_level0:
					if a0 == x.level_name:
						list3.append(x)
				
				if len(list3) != 0:
					print(2)
					returndata = []
					for x in list3:
						returndata.append({
							'id': x.level_id,
							'name': x.level_name,
							'ref': x.level_ref,
							'link': '/level1/' + a0 + '/drill/' + str(x.level_id),
							'state': x.level_state,
							'date': x.Date,
							'rank': x.rank,
						})
					
					linkdata = []
					for x in Document.objects.filter(document_name__contains=list3):
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
		else:
			print("user error")
			data = []
			print(7)
			return Response(data)
