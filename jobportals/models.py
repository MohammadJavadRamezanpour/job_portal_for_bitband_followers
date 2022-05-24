from django.db import models
from django.conf import settings
from datetime import datetime
from django.db.models import Q
from django.contrib import admin


class State(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
 

class JobCategory(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title


class JobSeeker(models.Model):
    GENDER_FEMALE = 'F'
    GENDER_MALE = 'M'
    GENDER_CHOICES = [
        (GENDER_FEMALE, 'Female'),
        (GENDER_MALE, 'Male')
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)	
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    expected_salary	= models.IntegerField(null=True, blank=True)
    preferred_job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    linkedin_profile = models.CharField(max_length=255, null=True, blank=True, help_text='for example linkedin.com/in/username')


    def __str__(self):
        return f"{self.user.first_name}  {self.user.last_name}"
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name


class LanguageTitle(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title


class EducationalBackground(models.Model):
    LEVEL_DIPLOMA = 'DI'
    LEVEL_ASSOCIATE = 'AS'
    LEVEL_BACHELOR = 'BA'
    LEVEL_MASTER = 'MA'
    LEVEL_DOCTORAL = 'DO'
    
    DEGREE_LEVEL = [
        (LEVEL_DIPLOMA, 'Diploma'),
        (LEVEL_ASSOCIATE, 'Associate'),
        (LEVEL_BACHELOR, 'Bachelor'),
        (LEVEL_MASTER, 'Master'),
        (LEVEL_DOCTORAL, 'Doctoral')
    ]
    
    YEAR_CHOICES = [(y,y) for y in range(1900, datetime.now().year)]
    MONTH_CHOICES = [(m,m) for m in range(1,13)]
    
    jobseeker = models.ForeignKey(JobSeeker,on_delete=models.CASCADE, related_name='jobseeker_educationalbackground', null=True, blank=True)
    jobdetail = models.ForeignKey('JobDetail',on_delete=models.PROTECT, related_name='jobdetail_educationalbackground', null=True, blank=True)
    employer = models.ForeignKey('Employer', on_delete=models.PROTECT, related_name='employer_educationalbackground', null=True, blank=True)
    degree_level = models.CharField(max_length=2, choices=DEGREE_LEVEL)
    field_of_Study = models.ForeignKey('FieldOfStudy', on_delete=models.CASCADE)
    university = models.CharField(max_length=255)
    gpa = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    from_year = models.IntegerField(choices=YEAR_CHOICES, null=True, blank=True)
    from_month = models.IntegerField(choices=MONTH_CHOICES, null=True, blank=True)
    to_year = models.IntegerField(choices=YEAR_CHOICES, null=True, blank=True)
    to_month = models.IntegerField(choices=MONTH_CHOICES, null=True, blank=True)
    studying =  models.BooleanField()

    class Meta:
        ordering = ['degree_level', 'university', 'gpa']
        index_together = [
            ['from_year', 'to_year'],
            ['from_month', 'to_month']
            ]
        constraints = [
            models.CheckConstraint(
                check=Q(jobseeker__isnull=False) | Q(jobdetail__isnull=False),
                name='not_both_null4'
            )
        ]


class SoftwareSkillCategory(models.Model):
    category_title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.category_title


class SoftwareSkillTitle(models.Model):
    title = models.CharField(max_length=255)
    softwareskillcategory = models.ForeignKey(SoftwareSkillCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class WorkExperience(models.Model):

    YEAR_CHOICES = [(y,y) for y in range(1900, datetime.now().year)]
    MONTH_CHOICES = [(m,m) for m in range(1,13)]
    
    jobseeker = models.ForeignKey(JobSeeker,on_delete=models.CASCADE, related_name='jobseeker_workexperience')
    job_title = models.CharField(max_length=255)
    job_category = models.CharField(max_length=255)
    seniority_level = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    from_month = models.IntegerField(choices=MONTH_CHOICES, null=True, blank=True)
    from_year = models.IntegerField(choices=YEAR_CHOICES, null=True, blank=True)
    to_year = models.IntegerField(choices=YEAR_CHOICES, null=True, blank=True)
    to_month = models.IntegerField(choices=MONTH_CHOICES, null=True, blank=True)
    current_job = models.BooleanField()
    achievements_and_main_tasks = models.TextField(max_length=1000)
    
    class Meta:
        ordering = ['job_title', 'job_category', 'seniority_level','company_name', 'state', 'city', 'current_job']
        index_together = [
            ['from_year', 'to_year'],
            ['from_month', 'to_month']
            ]


class Employer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)	
    phone_number = models.CharField(max_length=11)
    direct_corporate_phone_number = models.CharField(max_length=11)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class BasicInformationOfOrganization(models.Model):
    employer = models.OneToOneField(Employer, on_delete=models.PROTECT)
    name_of_organization = models.CharField(max_length=255)
    website_url = models.CharField(max_length=255)
    organization_phone_number = models.CharField(max_length=20)
    industry = models.CharField(max_length=255)
    organization_size = models.PositiveIntegerField()
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    introduction_of_company = models.CharField(max_length=255)
    companys_field_of_work = models.CharField(max_length=255)

    def __str__(self):
        return self.name_of_organization


class FieldOfStudy(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title


class JobDetail(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.PROTECT)
    job_title = models.CharField(max_length=255)
    organizational_category = models.CharField(max_length=255)
    type_of_cooperation = models.CharField(max_length=255)
    possibility_of_telecommuting = models.BooleanField()
    field_of_individual_activity = models.CharField(max_length=255)
    working_hoursand_days = models.CharField(max_length=255, help_text='for example: 9 AM-5 PM all day of week')
        
    AGE_CHOICES = [(m,str(m)) for m in range(18,50)]
    minimum_age = models.IntegerField(choices=AGE_CHOICES)
    maximum_age = models.IntegerField(choices=AGE_CHOICES)
    
    GENDER_NONE = 'N'
    GENDER_FEMALE = 'F'
    GENDER_MALE = 'M'
    GENDER_CHOICES = [
        (GENDER_NONE, 'Does not matter'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_MALE, 'Male')
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='N')
    
    attract_an_intern = models.BooleanField()
    attracting_the_disabled = models.BooleanField()
    completion_of_military_service = models.BooleanField()
    WORK_EXPERIENCE_CHOICES = [(m,str(m)) for m in range(0,18)]
    the_amount_of_work_experience = models.IntegerField(choices=WORK_EXPERIENCE_CHOICES)
    field_of_Study = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE,null=True ,blank=True)
    
    LEVEL_DIPLOMA = 'DI'
    LEVEL_ASSOCIATE = 'AS'
    LEVEL_BACHELOR = 'BA'
    LEVEL_MASTER = 'MA'
    LEVEL_DOCTORAL = 'DO'
    
    DEGREE_LEVEL = [
        (LEVEL_DIPLOMA, 'Diploma'),
        (LEVEL_ASSOCIATE, 'Associate'),
        (LEVEL_BACHELOR, 'Bachelor'),
        (LEVEL_MASTER, 'Master'),
        (LEVEL_DOCTORAL, 'Doctoral')
    ]
    
    degree_level = models.CharField(max_length=2, choices=DEGREE_LEVEL)

    SALARY_1 = '6-8'
    SALARY_2 = '8-10'
    SALARY_3 = '10-12'
    SALARY_4 = '12-16'
    SALARY_5 = '16-20'
    SALARY_6 = '20-25'
    SALARY_7 = '25 - ?'

    SALARY_CHOICES = [
        (SALARY_1, '6 to 8 million tomans'),
        (SALARY_2, '8 to 10 million tomans'),
        (SALARY_3, '10 to 12 million tomans'),
        (SALARY_4, '12 to 16 million tomans'),
        (SALARY_5, '16 to 20 million tomans'),
        (SALARY_6, '20 to 25 million tomans'),
        (SALARY_7, '25 million tomans and above'),
    ]

    salary = models.CharField(max_length=6, choices=SALARY_CHOICES)
    facilities_and_benefits = models.CharField(max_length=255, null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.job_title
    
    class Meta:
        index_together = [
            ['minimum_age', 'maximum_age'],
            ]


class SoftwareSkill(models.Model):
    title = models.ForeignKey(SoftwareSkillTitle, on_delete=models.PROTECT)
    softwareskillcategory = models.ForeignKey(SoftwareSkillCategory, on_delete=models.PROTECT)
    jobseeker = models.ForeignKey(JobSeeker,on_delete=models.CASCADE, related_name='jobseeker_softwareskill', null=True, blank=True)
    jobdetail = models.ForeignKey(JobDetail,on_delete=models.PROTECT, related_name='jobdetail_softwareskill', null=True, blank=True)
    employer = models.ForeignKey(Employer, on_delete=models.PROTECT, related_name='employer_softwareskill', null=True, blank=True)
    
    LEVEL_ADVANCED = 'L'
    LEVEL_MEDIUM = 'M'
    LEVEL_INTRODUCTORY = 'I'
    
    SKILL_LEVEL = [
        (LEVEL_ADVANCED, 'Advanced'),
        (LEVEL_MEDIUM, 'Medium'),
        (LEVEL_INTRODUCTORY, 'Introductory')
    ]
    
    skill_level = models.CharField(max_length=1, choices=SKILL_LEVEL)
    
    class Meta:
        ordering = ['title', 'skill_level', 'softwareskillcategory']
        constraints = [
            models.CheckConstraint(
                check=Q(jobseeker__isnull=False) | Q(jobdetail__isnull=False),
                name='not_both_null2'
            )
        ]
        

class Language(models.Model):
    languagetitle = models.ForeignKey(LanguageTitle, on_delete=models.PROTECT)
    jobseeker = models.ForeignKey(JobSeeker,on_delete=models.CASCADE, related_name='jobseeker_language', null=True, blank=True)
    jobdetail = models.ForeignKey(JobDetail,on_delete=models.PROTECT, related_name='jobdetail_language', null=True, blank=True)
    employer = models.ForeignKey(Employer, on_delete=models.PROTECT, related_name='employer_language', null=True, blank=True)
    
    LEVEL_ADVANCED = 'A'
    LEVEL_MEDIUM = 'M'
    LEVEL_INTRODUCTORY = 'I'
    SKILL_LEVEL = [
        (LEVEL_ADVANCED, 'Advanced'),
        (LEVEL_MEDIUM, 'Medium'),
        (LEVEL_INTRODUCTORY, 'Introductory')
    ]
   
    skill_level = models.CharField(max_length=1, choices=SKILL_LEVEL)
    
    def __str__(self):
        return f"{self.languagetitle} | {self.skill_level}"

    class Meta:
        ordering = ['languagetitle', 'skill_level']
        constraints = [
            models.CheckConstraint(
                check=Q(jobseeker__isnull=False) | Q(jobdetail__isnull=False),
                name='not_both_null'
            )
        ]


class Applicant(models.Model):
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE, null=True, blank=True)
    cover_letter = models.TextField()
    jobdetail = models.ForeignKey(JobDetail, on_delete=models.PROTECT, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    STATUS_PENDING = 'P'
    STATUS_REJECTED = 'R'
    STATUS_INTERVIEW = 'I'
    STATUS_HIRE = 'H'
    
    APPLICANT_STATUS = (
    (STATUS_PENDING, 'Pending'),
    (STATUS_REJECTED, 'Rejected'),
    (STATUS_INTERVIEW, 'Interview'),
    (STATUS_HIRE, 'Hire'),
    )

    applicant_status = models.CharField(max_length=1, choices=APPLICANT_STATUS)
    
    def __str__(self):
        return str(f'{self.jobseeker.first_name} applied to {self.jobdetail.job_title}')

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=Q(jobseeker__isnull=False) | Q(jobdetail__isnull=False),
                name='not_both_null3'
            )
        ]        

