from rest_framework import serializers
from info.models import Level, Document

class LevelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Level
		fields = [
			'level_id',
			'level_state',
			'level_name',
			'level_link',
			'group'
		]

class DocumentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Document
		fields = [
			'document_id',
			'document_name',
			'document_file',
			'document_link',
			'group'
		]