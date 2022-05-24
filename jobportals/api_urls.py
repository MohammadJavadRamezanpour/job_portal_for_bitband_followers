from rest_framework import routers
from .api_views import (StateViewSet, CityViewSet, JobCategoryViewSet, LanguageTitleViewSet,
                        FieldOfStudyViewSet, SoftwareSkillCategoryViewSet, SoftwareSkillTitleViewSet,
                        JobSeekerViewSet, EmployerViewSet, BasicInformationOfOrganizationViewSet,
                        JobDetailViewSet, EducationalBackgroundViewSet, LanguageViewSet,
                        WorkExperienceViewSet, SoftwareSkillViewSet, ApplicantViewSet) 


router = routers.DefaultRouter()
router.register('state', StateViewSet, basename='state')
router.register('city', CityViewSet, basename='city')
router.register('job_category', JobCategoryViewSet, basename='job_category')
router.register('language_title', LanguageTitleViewSet, basename='language_title')
router.register('field_study', FieldOfStudyViewSet, basename='field_study')
router.register('skill_category', SoftwareSkillCategoryViewSet, basename='skill_category')
router.register('s_title', SoftwareSkillTitleViewSet, basename='s_title')
router.register('jobseeker', JobSeekerViewSet, basename='jobseeker')
router.register('employer', EmployerViewSet, basename='employer')
router.register('basic_info', BasicInformationOfOrganizationViewSet, basename='basic_info')
router.register('job_detail', JobDetailViewSet, basename='job_detail')
router.register('edu_bg', EducationalBackgroundViewSet, basename='edu_bg')
router.register('lang', LanguageViewSet, basename='lang')
router.register('work_exp', WorkExperienceViewSet, basename='work_exp')
router.register('soft_skill', SoftwareSkillViewSet, basename='soft_skill')
router.register('applicant', ApplicantViewSet, basename='applicant')