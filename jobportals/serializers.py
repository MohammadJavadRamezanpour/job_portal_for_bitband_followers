from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import (State, City, JobCategory, LanguageTitle, FieldOfStudy, SoftwareSkillCategory,
                    SoftwareSkillTitle, JobSeeker, Employer, BasicInformationOfOrganization,
                    JobDetail, EducationalBackground, Language, WorkExperience, SoftwareSkill,
                    Applicant)
from accounts.serializers import UserSerializer


class StateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = State
        fields = ['name']
        
        
class CitySerializer(serializers.ModelSerializer):
    state = StateSerializer()

    class Meta:
        model = City
        fields = ['name', 'state']   
        
        
class JobCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = JobCategory
        fields = ['title']


class LanguageTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = LanguageTitle
        fields = ['title']  


class FieldOfStudySerializer(serializers.ModelSerializer):

    class Meta:
        model = FieldOfStudy
        fields = ['title']


class SoftwareSkillCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SoftwareSkillCategory
        fields = ['category_title']        


class SoftwareSkillTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = SoftwareSkillTitle
        fields = ['title', 'softwareskillcategory'] 


class EmployerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employer
        fields = ['user', 'phone_number', 'direct_corporate_phone_number']


class BasicInformationOfOrganizationSerializer(serializers.ModelSerializer):
    state = StateSerializer()
    city = CitySerializer()
    
    class Meta:
        model = BasicInformationOfOrganization
        fields = ['employer', 'name_of_organization',
                  'website_url', 'industry', 'organization_size', 'state', 
                  'city', 'introduction_of_company', 'companys_field_of_work']

    def validate(self, data):
        dependent_cities = City.objects.filter(state=data['state'])
        if data['city'] not in dependent_cities:
            raise serializers.ValidationError('this city does not dependent to selected state')
        return data


class EducationalBackgroundSerializer(serializers.ModelSerializer):
    field_of_Study = FieldOfStudySerializer()

    class Meta:
        model = EducationalBackground
        fields = ['jobseeker', 'jobdetail', 'employer','degree_level', 'field_of_Study', 
                    'university', 'gpa', 'from_year', 'from_month', 'to_year', 'to_month', 'studying']

    def validate(self, data):
        if data['from_year'] > data['to_year']:
            raise serializers.ValidationError({"to_year": "finish must occur after start"})
        elif data['from_year'] == data['to_year']:
            if data['from_month'] >= data['to_month']:
                raise serializers.ValidationError({"to_month": "finish must occur after start"})
        return data


class WorkExperienceSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)
    city = CitySerializer(read_only=True)

    class Meta:
        model = WorkExperience
        fields = ['job_title', 'job_category', 'seniority_level', 
                  'company_name', 'state', 'city', 'from_month', 'from_year', 'to_year', 'to_month', 
                  'current_job', 'achievements_and_main_tasks']

    def save(self, **kwargs):
        job_title = self.validated_data['job_title']
        job_category = self.validated_data['job_category']
        seniority_level = self.validated_data['seniority_level']
        company_name = self.validated_data['company_name']
        city = self.validated_data['city']
        current_job = self.validated_data['current_job']
        achievements_and_main_tasks = self.validated_data['achievements_and_main_tasks']
        jobseeker = self.context['request'].user

        obj = WorkExperience.objects.create(job_title=job_title, job_category=job_category,
        seniority_level=seniority_level, company_name=company_name, city=city, 
        current_job=current_job, achievements_and_main_tasks=achievements_and_main_tasks,
        jobseeker=jobseeker)

        return obj


    def validate(self, data):
        dependent_cities = City.objects.filter(state=data['state'])
        if data['city'] not in dependent_cities:
            raise serializers.ValidationError('this city does not dependent to selected state')
        if data['from_year'] > data['to_year']:
            raise serializers.ValidationError({"to_year": "finish must occur after start"})
        elif data['from_year'] == data['to_year']:
            if data['from_month'] >= data['to_month']:
                raise serializers.ValidationError({"to_month": "finish must occur after start"})
        return data
    

class SoftwareSkillSerializer(serializers.ModelSerializer):
    title = SoftwareSkillTitleSerializer(read_only=True)
    softwareskillcategory = SoftwareSkillCategorySerializer(read_only=True)
    
    class Meta:
        model = SoftwareSkill
        fields = ['title', 'softwareskillcategory', 'jobseeker', 'jobdetail', 
                'employer', 'skill_level']


class LanguageSerializer(serializers.ModelSerializer):
    languagetitle = LanguageTitleSerializer(read_only=True)

    class Meta:
        model = Language
        fields = ['languagetitle', 'jobseeker', 'employer','jobdetail', 'skill_level' ]


class JobSeekerSerializer(serializers.ModelSerializer):
    preferred_job_category = JobCategorySerializer(read_only=True)
    jobseeker_educationalbackground = EducationalBackgroundSerializer(many=True, read_only=True)
    jobseeker_workexperience = WorkExperienceSerializer(many=True, read_only=True)
    jobseeker_softwareskill = SoftwareSkillSerializer(many=True, read_only=True)
    jobseeker_language = LanguageSerializer(many=True, read_only=True)
    state = StateSerializer()
    city = CitySerializer()

    class Meta:
        model = JobSeeker
        fields = ['user' ,'first_name','last_name', 'gender',
                  'phone_number', 'date_of_birth', 'expected_salary','preferred_job_category', 
                  'linkedin_profile', 'state', 'city', 'zip_code', 'jobseeker_educationalbackground',
                  'jobseeker_workexperience', 'jobseeker_softwareskill', 'jobseeker_language'] 


class JobDetailSerializer(serializers.ModelSerializer):
    jobdetail_softwareskill = SoftwareSkillSerializer(many=True, read_only=True)
    employer = EmployerSerializer()
    field_of_Study = FieldOfStudySerializer()
    jobdetail_educationalbackground = EducationalBackgroundSerializer(many=True, read_only=True)
    jobdetail_language = LanguageSerializer(many=True, read_only=True)

    class Meta:
        model = JobDetail
        fields = ['employer', 'job_title', 'organizational_category', 'type_of_cooperation', 
                  'possibility_of_telecommuting', 'field_of_individual_activity',
                  'working_hoursand_days' , 'minimum_age', 
                  'maximum_age', 'gender', 'attract_an_intern', 'attracting_the_disabled', 
                  'completion_of_military_service', 'the_amount_of_work_experience',
                  'field_of_Study', 'degree_level', 'salary', 'facilities_and_benefits',
                  'job_description', 'jobdetail_softwareskill', 'jobdetail_educationalbackground',
                  'jobdetail_language']

    def create(self, validated_data):
        softwareskills = validated_data.pop('jobdetail_softwareskill')
        job_detail = JobDetail.objects.create(**validated_data)
        for softwareskill in softwareskills:
            SoftwareSkill.objects.create(jobdetail=job_detail, **softwareskill)
        return job_detail

    def validate(self, data):
        if data['maximum_age'] < data['minimum_age']:
            raise serializers.ValidationError('maximum age must be greather than minimum age')
        return data


class ApplicantSerializer(serializers.ModelSerializer):
    jobseeker = JobSeekerSerializer()
    jobdetail = JobDetailSerializer()

    class Meta:
        model = Applicant
        fields = ['cover_letter', 'jobseeker', 'jobdetail' ,'created' , 'applicant_status']

