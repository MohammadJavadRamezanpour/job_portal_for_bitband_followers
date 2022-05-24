from django.contrib import admin
from .models import (State, City, JobSeeker, LanguageTitle, EducationalBackground, SoftwareSkillCategory, 
                    SoftwareSkillTitle, WorkExperience, Employer, BasicInformationOfOrganization,
                    FieldOfStudy, JobDetail, SoftwareSkill, Language, Applicant, JobCategory )
from django.db.models.aggregates import Count


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 10
    

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'state_name', 'jobseeker_count']
    list_per_page = 10
    list_select_related = ['state']
    list_display_links = ['state_name']

    def state_name(self, city):
        return city.state.name    
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(jobseeker_count=Count('jobseeker'))
    
    @admin.display(ordering='jobseeker_count')
    def jobseeker_count(self, city):
        return city.jobseeker_count


@admin.register(JobSeeker)
class JobSeekerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'phone_number', 'date_of_birth', 'expected_salary', 'preferred_job_category', 
                    'linkedin_profile']
    
    ordering = ['user__first_name', 'user__last_name', 'gender', 'date_of_birth', 
                'expected_salary', 'preferred_job_category',
                'state', 'city']
    list_select_related = ['user']
    search_fields = ['user__first_name', 'user__last_name']
    list_per_page = 10

    # def first_name(self, obj):
    #         return obj.user.first_name

    # def last_name(self, obj):
    #     return obj.user.last_name        

@admin.register(LanguageTitle)
class LanguageTitleAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_per_page = 10


@admin.register(EducationalBackground)
class EducationalBackgroundAdmin(admin.ModelAdmin):
    list_display = ['jobseeker', 'degree_level', 'university', 'gpa', 'from_year', 'to_year', 'from_month', 'to_month', 'studying']


@admin.register(SoftwareSkillCategory)
class SoftwareSkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title',]
    list_per_page = 10


@admin.register(SoftwareSkillTitle)
class SoftwareSkillsTitleAdmin(admin.ModelAdmin):
    list_display = ['softwareskillcategory', 'title']
    list_per_page = 10 


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'job_category', 'seniority_level',
                    'company_name', 'state', 'city', 'from_month',
                    'from_year', 'to_year', 'to_month', 'current_job',
                    'achievements_and_main_tasks']
    list_per_page = 10   


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'direct_corporate_phone_number']
    list_per_page = 10        
 

@admin.register(BasicInformationOfOrganization)
class BasicInformationOfOrganizationAdmin(admin.ModelAdmin):
    list_display = ['employer_id', 'name_of_organization',
                    'website_url', 'organization_phone_number', 'industry', 'organization_size', 
                    'state', 'city', 'introduction_of_company', 'companys_field_of_work']
    list_per_page = 10   


@admin.register(FieldOfStudy)
class FieldOfStudyAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_per_page = 10        


@admin.register(JobDetail)
class JobDetailAdmin(admin.ModelAdmin):
    list_display = ['employer_id', 'job_title', 'organizational_category', 'type_of_cooperation', 
                    'possibility_of_telecommuting', 'field_of_Study', 'degree_level', ]
    list_per_page = 10  


@admin.register(SoftwareSkill)
class SoftwareSkillsAdmin(admin.ModelAdmin):
    list_display = ['jobseeker','jobdetail', 'employer', 
                    'softwareskillcategory', 'title', 'skill_level']
    list_per_page = 10  


@admin.register(Language)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['jobseeker','jobdetail', 'employer', 'languagetitle', 'skill_level']
    list_per_page = 10


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ['jobseeker', 'created', 'applicant_status']
    list_per_page = 10   


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_per_page = 10   