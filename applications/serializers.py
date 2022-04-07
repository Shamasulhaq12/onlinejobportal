from .models import QualifiedCv, UnQualifiedCv
from rest_framework import serializers


class QualifiedCvSerializers(serializers.ModelSerializer):
    class Meta:
        model = QualifiedCv
        fields = '__all__'


class PQualifiedCvSerializers(serializers.ModelSerializer):
    class Meta:
        model = QualifiedCv
        fields = [
            'id',
            'time_submitted',
            'paid',
            'accepted_by_hod',
            'job_confirm'
        ]


class UnQualifiedCvSerializers(serializers.ModelSerializer):
    class Meta:
        model = UnQualifiedCv
        fields = '__all__'


class PUnQualifiedCvSerializers(serializers.ModelSerializer):
    class Meta:
        model = UnQualifiedCv
        fields = [
            'id',
            'time_submitted',
            'paid',
            'accepted_by_hod',
            'job_confirm'
        ]
