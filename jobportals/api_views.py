from .serializers import (StateSerializer, CitySerializer, JobCategorySerializer, LanguageTitleSerializer,
                         FieldOfStudySerializer, SoftwareSkillCategorySerializer, SoftwareSkillTitleSerializer,
                         JobSeekerSerializer, EmployerSerializer, BasicInformationOfOrganizationSerializer,
                         JobDetailSerializer, EducationalBackgroundSerializer, LanguageSerializer,
                         WorkExperienceSerializer, SoftwareSkillSerializer, ApplicantSerializer)
from .models import (State, City, JobCategory, LanguageTitle, FieldOfStudy, SoftwareSkillCategory,
                    SoftwareSkillTitle, JobSeeker, Employer, BasicInformationOfOrganization,
                    JobDetail, EducationalBackground, Language, WorkExperience, SoftwareSkill,
                    Applicant )
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class StateViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = State.objects.all()
        serialize_data = StateSerializer(queryset, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = State.objects.all()
        state = get_object_or_404(queryset, pk=pk)
        serialize_data = StateSerializer(state)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        state = StateSerializer(data=data)
        if state.is_valid(): 
            state.save()
            return Response({'message': 'sucess'}, status=status.HTTP_201_CREATED)
        else:    
            return Response(state.errors, status=status.HTTP_400_BAD_REQUEST)   


class CityViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = City.objects.all()
        serialize_data = CitySerializer(queryset, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = City.objects.all()
        city = get_object_or_404(queryset, pk=pk)
        serialize_data = CitySerializer(city)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        city = CitySerializer(data=data)
        if city.is_valid(): 
            city.save()
            return Response({'message': 'sucess'}, status=status.HTTP_201_CREATED)
        else:    
            return Response(city.errors, status=status.HTTP_400_BAD_REQUEST)   


class JobCategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = JobCategory.objects.all()
        serialize_data = JobCategorySerializer(queryset, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = JobCategory.objects.all()
        job_category = get_object_or_404(queryset, pk=pk)
        serialize_data = JobCategorySerializer(job_category)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        job_category = JobCategorySerializer(data=data)
        if job_category.is_valid(): 
            job_category.save()
            return Response({'message': 'sucess'}, status=status.HTTP_201_CREATED)
        else:    
            return Response(job_category.errors, status=status.HTTP_400_BAD_REQUEST)  


class LanguageTitleViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = LanguageTitle.objects.all()
        serialize_data = LanguageTitleSerializer(queryset, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = LanguageTitle.objects.all()
        language_title = get_object_or_404(queryset, pk=pk)
        serialize_data = LanguageTitleSerializer(language_title)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        language_title = LanguageTitleSerializer(data=data)
        if language_title.is_valid(): 
            language_title.save()
            return Response({'message': 'sucess'}, status=status.HTTP_201_CREATED)
        else:    
            return Response(language_title.errors, status=status.HTTP_400_BAD_REQUEST)  


class FieldOfStudyViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = FieldOfStudy.objects.all()
        serialize_data = FieldOfStudySerializer(queryset, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = FieldOfStudy.objects.all()
        field_study = get_object_or_404(queryset, pk=pk)
        serialize_data = FieldOfStudySerializer(field_study)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        field_study = FieldOfStudySerializer(data=data)
        if field_study.is_valid(): 
            field_study.save()
            return Response({'message': 'sucess'}, status=status.HTTP_201_CREATED)
        else:    
            return Response(field_study.errors, status=status.HTTP_400_BAD_REQUEST)


class SoftwareSkillCategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = SoftwareSkillCategory.objects.all()
        serialize_data = SoftwareSkillCategorySerializer(queryset, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = SoftwareSkillCategory.objects.all()
        skill_category = get_object_or_404(queryset, pk=pk)
        serialize_data = SoftwareSkillCategorySerializer(skill_category)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        skill_category = SoftwareSkillCategorySerializer(data=data)
        if skill_category.is_valid(): 
            skill_category.save()
            return Response({'message': 'sucess'}, status=status.HTTP_201_CREATED)
        else:    
            return Response(skill_category.errors, status=status.HTTP_400_BAD_REQUEST)  


class SoftwareSkillTitleViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = SoftwareSkillTitle.objects.all()
        serialize_data = SoftwareSkillTitleSerializer(queryset, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = SoftwareSkillTitle.objects.all()
        skill_title = get_object_or_404(queryset, pk=pk)
        serialize_data = SoftwareSkillTitleSerializer(skill_title)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        skill_title = SoftwareSkillTitleSerializer(data=data)
        if skill_title.is_valid(): 
            skill_title.save()
            return Response({'message': 'sucess'}, status=status.HTTP_201_CREATED)
        else:    
            return Response(skill_title.errors, status=status.HTTP_400_BAD_REQUEST)                                  


class JobSeekerViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = JobSeeker.objects.all()
        serialize_data = JobSeekerSerializer(queryset, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = JobSeeker.objects.all()
        jobseeker = get_object_or_404(queryset, pk=pk)
        serialize_data = JobSeekerSerializer(jobseeker)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        jobseeker = JobSeekerSerializer(data=data)
        if jobseeker.is_valid(): 
            jobseeker.save()
            return Response({'message': 'sucess'}, status=status.HTTP_201_CREATED)
        else:    
            return Response(jobseeker.errors, status=status.HTTP_400_BAD_REQUEST)  


class EmployerViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Employer.objects.all()
        serialize_data = EmployerSerializer(queryset, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Employer.objects.all()
        employer = get_object_or_404(queryset, pk=pk)
        serialize_data = EmployerSerializer(employer)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        employer = EmployerSerializer(data=data)
        if employer.is_valid(): 
            employer.save()
            return Response({'message': 'sucess'}, status=status.HTTP_201_CREATED)
        else:    
            return Response(employer.errors, status=status.HTTP_400_BAD_REQUEST)


class BasicInformationOfOrganizationViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = BasicInformationOfOrganization.objects.all()
        serialize_data = BasicInformationOfOrganizationSerializer(queryset, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = BasicInformationOfOrganization.objects.all()
        basic_info = get_object_or_404(queryset, pk=pk)
        serialize_data = BasicInformationOfOrganizationSerializer(basic_info)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        basic_info = BasicInformationOfOrganizationSerializer(data=data)
        if basic_info.is_valid(): 
            basic_info.save()
            return Response({'message': 'sucess'}, status=status.HTTP_201_CREATED)
        else:    
            return Response(basic_info.errors, status=status.HTTP_400_BAD_REQUEST)  


class JobDetailViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = JobDetail.objects.all()
        serialize_data = JobDetailSerializer(queryset, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = JobDetail.objects.all()
        job_detail = get_object_or_404(queryset, pk=pk)
        serialize_data = JobDetailSerializer(job_detail)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        job_detail = JobDetailSerializer(data=data)
        if job_detail.is_valid(): 
            job_detail.save()
            return Response({'message': 'sucess'}, status=status.HTTP_201_CREATED)
        else:    
            return Response(job_detail.errors, status=status.HTTP_400_BAD_REQUEST)   


class EducationalBackgroundViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = EducationalBackground.objects.all()
        serialize_data = EducationalBackgroundSerializer(queryset, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = EducationalBackground.objects.all()
        educational_background = get_object_or_404(queryset, pk=pk)
        serialize_data = EducationalBackgroundSerializer(educational_background)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        educational_background = EducationalBackgroundSerializer(data=data)
        if educational_background.is_valid(): 
            educational_background.save()
            return Response({'message': 'sucess'}, status=status.HTTP_201_CREATED)
        else:    
            return Response(educational_background.errors, status=status.HTTP_400_BAD_REQUEST)  


class LanguageViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Language.objects.all()
        serialize_data = LanguageSerializer(queryset, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Language.objects.all()
        lang = get_object_or_404(queryset, pk=pk)
        serialize_data = LanguageSerializer(lang)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        lang = LanguageSerializer(data=data)
        if lang.is_valid(): 
            lang.save()
            return Response({'message': 'sucess'}, status=status.HTTP_201_CREATED)
        else:    
            return Response(lang.errors, status=status.HTTP_400_BAD_REQUEST) 


class WorkExperienceViewSet(viewsets.ViewSet):

    def get_serializer_context(self):
        return {'request': self.request}

    def list(self, request):
        queryset = WorkExperience.objects.all()
        serialize_data = WorkExperienceSerializer(queryset, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = WorkExperience.objects.all()
        work_exp = get_object_or_404(queryset, pk=pk)
        serialize_data = WorkExperienceSerializer(work_exp)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        work_exp = WorkExperienceSerializer(data=data)
        if work_exp.is_valid(): 
            work_exp.save()
            return Response({'message': 'sucess'}, status=status.HTTP_201_CREATED)
        else:    
            return Response(work_exp.errors, status=status.HTTP_400_BAD_REQUEST)  


class SoftwareSkillViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = SoftwareSkill.objects.all()
        serialize_data = SoftwareSkillSerializer(queryset, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = SoftwareSkill.objects.all()
        skill = get_object_or_404(queryset, pk=pk)
        serialize_data = SoftwareSkillSerializer(skill)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        skill = SoftwareSkillSerializer(data=data)
        if skill.is_valid(): 
            skill.save()
            return Response({'message': 'sucess'}, status=status.HTTP_201_CREATED)
        else:    
            return Response(skill.errors, status=status.HTTP_400_BAD_REQUEST)  


class ApplicantViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Applicant.objects.all()
        serialize_data = ApplicantSerializer(queryset, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Applicant.objects.all()
        app = get_object_or_404(queryset, pk=pk)
        serialize_data = ApplicantSerializer(app)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def create(self, request):
        data = request.data
        app = ApplicantSerializer(data=data)
        if app.is_valid(): 
            app.save()
            return Response({'message': 'sucess'}, status=status.HTTP_201_CREATED)
        else:    
            return Response(app.errors, status=status.HTTP_400_BAD_REQUEST)                                                                                            