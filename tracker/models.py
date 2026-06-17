from django.db import models

class Condition(models.Model):
    grade_name = models.CharField(max_length=10, verbose_name="Грейд")
    description = models.TextField(verbose_name="Описание")
    price_modifier = models.FloatField(verbose_name="Коэффициент цены")

    def __str__(self):
        return self.grade_name

class Device(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    brand = models.CharField(max_length=50, verbose_name="Бренд")
    base_market_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Базовая цена")
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, verbose_name="Состояние")

    def __str__(self):
        return f"{self.brand} {self.name}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [('BUY', 'Выкуп'), ('SELL', 'Продажа')]
    
    device = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name="Устройство")
    transaction_type = models.CharField(max_length=4, choices=TRANSACTION_TYPES, verbose_name="Тип сделки")
    actual_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена сделки")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f"{self.transaction_type} - {self.device.name}"