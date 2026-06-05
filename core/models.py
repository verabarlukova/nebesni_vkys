from django.db import models

class Client(models.Model):
    """Модель клиента"""
    name = models.CharField(max_length=100, verbose_name="Имя клиента")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email", null=True, blank=True) # Добавьте это
    address = models.TextField(verbose_name="Адрес доставки")
    preferences = models.TextField(blank=True, verbose_name="Предпочтения")

    def __str__(self):
        return self.name

class Product(models.Model):
    """Модель продукта"""
    CATEGORY_CHOICES = [
        ('Бургеры', 'Бургеры'),
        ('Пицца', 'Пицца'),
        ('Напитки', 'Напитки'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Категория")
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='products/', verbose_name="Картинка", null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    """Модель заказа"""
    address = models.TextField(verbose_name="Адрес доставки")
    status = models.CharField(max_length=50, verbose_name="Статус")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма заказа")
    order_type = models.CharField(max_length=50, verbose_name="Тип заказа")
    
    # Связи: Заказ принадлежит одному клиенту, но содержит много блюд
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    items = models.ManyToManyField(Product, verbose_name="Состав заказа")

    def __str__(self):
        return f"Заказ №{self.id} от {self.client.name}"

class Ingredient(models.Model):
    """Модель ингредиентов"""
    name = models.CharField(max_length=100, verbose_name="Название")
    quantity = models.FloatField(verbose_name="Количество")
    products = models.ManyToManyField(Product, verbose_name="В составе блюд")

    def __str__(self):
        return self.name

class Promotion(models.Model):
    """Модель акций"""
    name = models.CharField(max_length=100, verbose_name="Название акции")
    start_date = models.DateTimeField(verbose_name="Дата начала")
    end_date = models.DateTimeField(verbose_name="Дата окончания")
    conditions = models.TextField(verbose_name="Условия")
    products = models.ManyToManyField(Product, verbose_name="Товары по акции")

    def __str__(self):
        return self.name