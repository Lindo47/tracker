import os
import pandas as pd
import matplotlib

# Устанавливаем бэкенд 'Agg' до импорта pyplot, чтобы графики рисовались в фоне без GUI
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .models import Device
from .forms import DeviceForm


def device_list(request):
    # Обработка добавления нового устройства
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = DeviceForm()

    devices = Device.objects.all()
    analyzed_devices = []
    
    brands_data = []
    prices_data = []

    # Расчет оценочной стоимости для каждого устройства
    for device in devices:
        estimated_price = float(device.base_market_price) * device.condition.price_modifier
        device.estimated_price = round(estimated_price, 2)
        analyzed_devices.append(device)
        
        brands_data.append(device.brand)
        prices_data.append(device.estimated_price)

    chart_exists = False

    # Генерация графика, если есть данные
    if brands_data:
        df = pd.DataFrame({
            'Бренд': brands_data,
            'Стоимость выкупа': prices_data
        })
        
        brand_stats = df.groupby('Бренд')['Стоимость выкупа'].sum()

        plt.figure(figsize=(6, 4))
        brand_stats.plot(kind='bar', color='#198754', edgecolor='black')
        plt.title('Общая стоимость выкупа по брендам', fontsize=12, fontweight='bold')
        plt.xlabel('Бренд', fontsize=10)
        plt.ylabel('Сумма (руб.)', fontsize=10)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Создание директории для статики, если её нет
        static_dir = os.path.join(settings.BASE_DIR, 'tracker', 'static', 'tracker')
        os.makedirs(static_dir, exist_ok=True)
        
        # Сохранение графика
        chart_path = os.path.join(static_dir, 'chart.png')
        plt.savefig(chart_path)
        plt.close()
        chart_exists = True

    return render(request, 'tracker/device_list.html', {
        'devices': analyzed_devices, 
        'form': form,
        'chart_exists': chart_exists
    })


def delete_device(request, device_id):
    # Обработка удаления устройства
    if request.method == "POST":
        device = get_object_or_404(Device, id=device_id)
        device.delete() 
    return redirect("device_list")