def build_auto_info(manufacturer, model, **auto_info):
    auto_info['manufacturer'] = manufacturer
    auto_info['model'] = model
    return auto_info

car = build_auto_info('subaru', 'outback', color='blue', tow_package=True)
print(car)
