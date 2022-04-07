from .models import QualifiedCv, UnQualifiedCv
from job.models import AnnouncedJobs
from rest_framework.views import APIView
from .serializers import QualifiedCvSerializers, UnQualifiedCvSerializers
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

# Create your views here.
# class ApplicationsCreateApiView(CreateAPIView):
# 	serializer_class = QualifiedCvSerializers
# 	def perform_create(self, serializer):
# 		try:
# 			print(serializer.validated_data['paid'],"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa                              a", self)
# 			return super(ApplicationsCreateApiView, self).perform_create(serializer=serializer)
# 		except Exception as e:
# 			print(e)
# 			return Response({"error": "error while submitting form "})



class ApplicationsCreateApiView(CreateAPIView):
	def post(self, request, format=None):
		try:
			data = self.request.data
			user = self.request.user
			# print(data)
			if not data['degree_1']:
				return Response({'error': 'Kindly! Choose your Degree'})

			job = AnnouncedJobs.objects.get(id=data['job_id'])

			if int(data['degree_1']) >= job.Degree:
				experience = int(data['experience_period_1']) + int(data['experience_period_2']) + int(data['experience_period_3'])

				if experience >= job.experience:
					print("aaaaaaaaaaaaaaaa")
					QualifiedCv.objects.create(
						user=user,
						candidate_name=data['candidate_name'],
						guardian_name=data['guardian_name'],
						nationality=data['nationality'],
						gender=data['gender'],
						date_of_birth=str(data['date_of_birth']),
						domicile=data['domicile'],
						permanent_address=data['permanent_address'],
						present_address=data['present_address'],
						land_line_no=data['land_line_no'],
						office_no=data['office_no'],
						cell_no=data['cell_no'],
						email=data['email'],
						cnic=data['cnic'],

						degree_1=data['degree_1'],
						degree_date_1=data['degree_date_1'],
						degree_institue_1=data['degree_institue_1'],
						degree_specialization_1=data['degree_specialization_1'],
						degree_grade_1=data['degree_grade_1'],
						degree_2=data['degree_2'],
						degree_date_2=data['degree_date_2'],
						degree_institue_2=data['degree_institue_2'],
						degree_specialization_2=data['degree_specialization_2'],
						degree_grade_2=data['degree_grade_2'],
						degree_3=data['degree_3'],
						degree_date_3=data['degree_date_3'],
						degree_institue_3=data['degree_institue_3'],
						degree_specialization_3=data['degree_specialization_3'],

						training_institution_1=data['training_institution_1'],
						training_course_1=data['training_course_1'],
						training_diploma_1=data['training_diploma_1'],
						training_field_1=data['training_field_1'],
						training_remarks_1=data['training_remarks_1'],
						training_institution_2=data['training_institution_2'],
						training_course_2=data['training_course_2'],
						training_diploma_2=data['training_diploma_2'],
						training_field_2=data['training_field_2'],
						training_remarks_2=data['training_remarks_2'],
						training_institution_3=data['training_institution_3'],
						training_course_3=data['training_course_3'],
						training_diploma_3=data['training_diploma_3'],
						training_field_3=data['training_field_3'],
						training_remarks_3=data['training_remarks_3'],

						experience_institution_1=data['experience_institution_1'],
						experience_designation_1=data['experience_designation_1'],
						experience_payscale_1=data['experience_payscale_1'],
						experience_job_1=data['experience_job_1'],
						experience_period_1=data['experience_period_1'],
						experience_institution_2=data['experience_institution_2'],
						experience_designation_2=data['experience_designation_2'],
						experience_payscale_2=data['experience_payscale_2'],
						experience_job_2=data['experience_job_2'],
						experience_period_2=data['experience_period_2'],
						experience_institution_3=data['experience_institution_3'],
						experience_designation_3=data['experience_designation_3'],
						experience_payscale_3=data['experience_payscale_3'],
						experience_job_3=data['experience_job_3'],
						experience_period_3=data['experience_period_3'],

						extra_activities=data['extra_activities'],
						reference_phone_1=data['reference_phone_1'],
						reference_phone_2=data['reference_phone_2'],
						reference_position_1=data['reference_position_1'],
						reference_position_2=data['reference_position_2'],
						reference_residence_1=data['reference_residence_1'],
						reference_residence_2=data['reference_residence_2'],
						file=data['file']
					)
				else:
					print("aaaaaaaaaaaaaaaa")
					UnQualifiedCv.objects.create(
						user=user,
						candidate_name=data['candidate_name'],
						guardian_name=data['guardian_name'],
						nationality=data['nationality'],
						gender=data['gender'],
						date_of_birth=data['date_of_birth'],
						domicile=data['domicile'],
						permanent_address=data['permanent_address'],
						present_address=data['present_address'],
						land_line_no=data['land_line_no'],
						office_no=data['office_no'],
						cell_no=data['cell_no'],
						email=data['email'],
						cnic=data['cnic'],

						degree_1=data['degree_1'],
						degree_date_1=data['degree_date_1'],
						degree_institue_1=data['degree_institue_1'],
						degree_specialization_1=data['degree_specialization_1'],
						degree_grade_1=data['degree_grade_1'],
						degree_2=data['degree_2'],
						degree_date_2=data['degree_date_2'],
						degree_institue_2=data['degree_institue_2'],
						degree_specialization_2=data['degree_specialization_2'],
						degree_grade_2=data['degree_grade_2'],
						degree_3=data['degree_3'],
						degree_date_3=data['degree_date_3'],
						degree_institue_3=data['degree_institue_3'],
						degree_specialization_3=data['degree_specialization_3'],

						training_institution_1=data['training_institution_1'],
						training_course_1=data['training_course_1'],
						training_diploma_1=data['training_diploma_1'],
						training_field_1=data['training_field_1'],
						training_remarks_1=data['training_remarks_1'],
						training_institution_2=data['training_institution_2'],
						training_course_2=data['training_course_2'],
						training_diploma_2=data['training_diploma_2'],
						training_field_2=data['training_field_2'],
						training_remarks_2=data['training_remarks_2'],
						training_institution_3=data['training_institution_3'],
						training_course_3=data['training_course_3'],
						training_diploma_3=data['training_diploma_3'],
						training_field_3=data['training_field_3'],
						training_remarks_3=data['training_remarks_3'],

						experience_institution_1=data['experience_institution_1'],
						experience_designation_1=data['experience_designation_1'],
						experience_payscale_1=data['experience_payscale_1'],
						experience_job_1=data['experience_job_1'],
						experience_period_1=data['experience_period_1'],
						experience_institution_2=data['experience_institution_2'],
						experience_designation_2=data['experience_designation_2'],
						experience_payscale_2=data['experience_payscale_2'],
						experience_job_2=data['experience_job_2'],
						experience_period_2=data['experience_period_2'],
						experience_institution_3=data['experience_institution_3'],
						experience_designation_3=data['experience_designation_3'],
						experience_payscale_3=data['experience_payscale_3'],
						experience_job_3=data['experience_job_3'],
						experience_period_3=data['experience_period_3'],

						extra_activities=data['extra_activities'],
						reference_phone_1=data['reference_phone_1'],
						reference_phone_2=data['reference_phone_2'],
						reference_position_1=data['reference_position_1'],
						reference_position_2=data['reference_position_2'],
						reference_residence_1=data['reference_residence_1'],
						reference_residence_2=data['reference_residence_2'],
						file=data['file']
					)
					print("created")
			else:
				UnQualifiedCv.objects.create(
					user=user,
					candidate_name=data['candidate_name'],
					guardian_name=data['guardian_name'],
					nationality=data['nationality'],
					gender=data['gender'],
					date_of_birth=data['date_of_birth'],
					domicile=data['domicile'],
					permanent_address=data['permanent_address'],
					present_address=data['present_address'],
					land_line_no=data['land_line_no'],
					office_no=data['office_no'],
					cell_no=data['cell_no'],
					email=data['email'],
					cnic=data['cnic'],

					degree_1=data['degree_1'],
					degree_date_1=data['degree_date_1'],
					degree_institue_1=data['degree_institue_1'],
					degree_specialization_1=data['degree_specialization_1'],
					degree_grade_1=data['degree_grade_1'],
					degree_2=data['degree_2'],
					degree_date_2=data['degree_date_2'],
					degree_institue_2=data['degree_institue_2'],
					degree_specialization_2=data['degree_specialization_2'],
					degree_grade_2=data['degree_grade_2'],
					degree_3=data['degree_3'],
					degree_date_3=data['degree_date_3'],
					degree_institue_3=data['degree_institue_3'],
					degree_specialization_3=data['degree_specialization_3'],

					training_institution_1=data['training_institution_1'],
					training_course_1=data['training_course_1'],
					training_diploma_1=data['training_diploma_1'],
					training_field_1=data['training_field_1'],
					training_remarks_1=data['training_remarks_1'],
					training_institution_2=data['training_institution_2'],
					training_course_2=data['training_course_2'],
					training_diploma_2=data['training_diploma_2'],
					training_field_2=data['training_field_2'],
					training_remarks_2=data['training_remarks_2'],
					training_institution_3=data['training_institution_3'],
					training_course_3=data['training_course_3'],
					training_diploma_3=data['training_diploma_3'],
					training_field_3=data['training_field_3'],
					training_remarks_3=data['training_remarks_3'],

					experience_institution_1=data['experience_institution_1'],
					experience_designation_1=data['experience_designation_1'],
					experience_payscale_1=data['experience_payscale_1'],
					experience_job_1=data['experience_job_1'],
					experience_period_1=data['experience_period_1'],
					experience_institution_2=data['experience_institution_2'],
					experience_designation_2=data['experience_designation_2'],
					experience_payscale_2=data['experience_payscale_2'],
					experience_job_2=data['experience_job_2'],
					experience_period_2=data['experience_period_2'],
					experience_institution_3=data['experience_institution_3'],
					experience_designation_3=data['experience_designation_3'],
					experience_payscale_3=data['experience_payscale_3'],
					experience_job_3=data['experience_job_3'],
					experience_period_3=data['experience_period_3'],

					extra_activities=data['extra_activities'],
					reference_phone_1=data['reference_phone_1'],
					reference_phone_2=data['reference_phone_2'],
					reference_position_1=data['reference_position_1'],
					reference_position_2=data['reference_position_2'],
					reference_residence_1=data['reference_residence_1'],
					reference_residence_2=data['reference_residence_2'],
					file=data['file']
				)
			return Response({'success': 'order has been placed'})
		except Exception as e:
			print(e)
			return Response({'error': 'error while creating order'})



class PaymentApiVIEW(APIView):
	def post(self, request, format=None):
		try:
			data = self.request.data
			obj = QualifiedCv.objects.get(id = data['app_id'])
			obj.paid = True
			obj.save()
			
			return Response({'success': 'Payment done successfully'})
		except Exception as e: 
			return Response({'error': 'error Occur kindly contact us'})