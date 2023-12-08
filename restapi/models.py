from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', help_text = 'Введите ваше имя')
    email = models.EmailField(verbose_name='Email', help_text = 'Введите ваш действующий электронный адрес')
    subject = models.CharField(max_length=100, verbose_name='Тема', help_text = 'Введите тему вашего сообщения')
    message = models.TextField(verbose_name='Сообщение', help_text = 'Оставьте ваше сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_read = models.BooleanField(verbose_name= "Прочитано", help_text = "Отметьте, если ваше сообщения было прочитано", default=False)
    
    def __str__(self):
        return f'{self.subject} - {self.name} - {self.email}'
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class Pricing(models.Model):
    service = models.CharField(max_length=100, verbose_name='Услуга', help_text = 'Введите название услуги')
    description = models.TextField(verbose_name='Описание услуги', help_text = 'Введите описание услуги')
    
    rate_per_hour = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость за час ($)', help_text = 'Укажите ставку в долларах за час работы')
    estimated_hours = models.IntegerField(verbose_name='Оценочное количество часов', help_text = 'Укажите, сколько часов требуется для выполнения услуги')
    
    def total_cost(self):
        """
        Метод total_cost вычиcляет общую стоимость на основе почасовой ставки и расчетных часов
        """
        return self.rate_per_hour * self.estimated_hours
    
    def __str__(self):
        return f"{self.service}-$ {self.total_cost()}"
    
    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Расценки'
        


        
        
class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Программирование'),
        ('design', 'Дизайн'),
        ('languages', 'Языки программирования'),
        ('database', 'Базы данных'),
        ('frameworks', 'Фреймворки'),
        ('tools', 'Инструменты разработки'),
        ('soft_skills', 'Soft Skills'),
        ('web', 'Веб-разработка'),
        ('mobile', 'Мобильная разработка'),
        ('cloud', 'Облачные технологии'),
        ('testing', 'Тестирование и QA'),
        ('analytics', 'Аналитика данных'),
        ('machine_learning', 'Машинное обучение и искусственный интеллект'),
        ('security', 'Информационная безопасность'),
        ('networking', 'Сетевые технологии'),
        ('graphics', 'Графический дизайн'),
        ('audio_video', 'Аудио и видео производство'),
        ('project_management', 'Управление проектами'),
        ('communication', 'Коммуникационные навыки'),
        ('leadership', 'Лидерство'),
        ('entrepreneurship', 'Предпринимательство'),
        ('data_science', 'Наука о данных'),
        ('automation', 'Автоматизация процессов'),
        ('devops', 'DevOps'),
        ('blockchain', 'Блокчейн технологии'),
        ('robotics', 'Робототехника'),
        ('language', 'язык'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name = 'Категория', help_text = 'Выберите категорию для навыка')
    name = models.CharField(max_length=50, verbose_name = 'Название', help_text = 'Введите название вашего навыка')
    percentage = models.PositiveSmallIntegerField(validators = (MinValueValidator(0), MaxValueValidator(100)), verbose_name = 'Проценты', help_text = 'Введите ваш уровень в процентах')
    
    def __str__(self):
        return f"{self.name} ({self.percentage} %)"
    
    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class Me(models.Model):
    first_name = models.CharField(max_length=50, verbose_name = 'Имя', help_text = 'Введите ваше имя')
    last_name = models.CharField(max_length=50, verbose_name = 'Фамилия', help_text = 'Введите вашу фамилию')
    email = models.EmailField( verbose_name = 'Email', help_text = 'Введите ваш действующий адрес электронной почты')
    phone = models.CharField(max_length=50, verbose_name = 'Телефон', help_text='Введите ваш номер телефона')
    instagram = models.URLField(max_length=50, verbose_name = 'Instagram',blank=True, null=True, help_text = 'Введите ваш логин в Instagram')
    github = models.URLField(max_length=50, verbose_name = 'Github',blank=True, null=True, help_text = 'Введите ваш профильв Github, если есть')
    linkedin = models.URLField(max_length=50, verbose_name = 'Linkedin',blank=True, null=True, help_text = 'Введите ваш профиль в Linkedin, если есть')
    telegram = models.URLField(max_length=50, verbose_name = 'Telegram',blank=True, null=True, help_text = 'Введите ваш профиль в Telegram, если есть')
    education = models.TextField(verbose_name = 'Образование', help_text = 'Введите ваше образование')
    work_history = models.TextField(verbose_name = 'История работы', help_text = 'Укажите ваш опыт работы')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'Информация о себе'
        verbose_name_plural = 'Информация о себе'
        

class Project(models.Model):
    file = models.FileField(upload_to='project_file/', blank=True, null=True, help_text = 'Выберите файл')
    image = models.ImageField(upload_to='project_image/', blank=True, null=True, help_text = 'Загрузите изображение проекта, если есть')
    title = models.CharField(max_length=50, verbose_name = 'Название проекта', help_text = 'Введите название вашего проекта')
    description = models.TextField(verbose_name = 'Описание проекта', help_text = 'Опишите подробнее ваш проект')
    start_date = models.DateField(verbose_name = 'Дата начала', help_text = 'Введите дату начала вашего проекта')
    end_date = models.DateField(verbose_name = 'Дата окончания',blank=True, null=True, help_text = 'Введите дату окончания вашего проекта')
    url = models.URLField(max_length=50, verbose_name = 'Ссылкана проект',blank=True, null=True, help_text = 'Введите ссылку на ваш проект')
    repository = models.URLField(max_length=50, verbose_name = 'Github репозиторий', blank=True, null=True, help_text = 'Введите ссылку на ваш репозиторий')
    
    techonolies_used = models.CharField(max_length=100, verbose_name='Используемые технологии', blank=True, null=True, help_text = 'Укажите технологии, используемые проекты')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name = 'Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name = 'Дата последнего обновления')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-updated_at']
    
        
        
    
