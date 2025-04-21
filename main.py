import json

file_path = r"C:\Users\andre\dio-1c-agent\parser\parsed_data\answer.json"


with open(file_path, "r", encoding="utf-8") as file:
    data = json.loads(file.read())


print(len(data))

# print(data[1])

a = "12"
print(a[3:])

s = """
[ 1С:Предприятие 8 Система программ ](https://v8.1c.ru/)\n[ ](https://1c.ru)\nТюмень\nИнформация на сайте будет отображаться для региона\n**Тюмень** Да, все верно Выбрать другой\n  * Программы 1С\n  * Платформа и технологии\n  * Поддержка и обучение\n  * Приобретение и внедрение\n\n\n[1С:ERP Управление предприятием](https://v8.1c.ru/erp/)\n[Купить, внедрить, проконсультироваться](https://v8.1c.ru/partners/erp/tyumen/)\n  * [ О продукте ](https://v8.1c.ru/erp/)\n  * [ Преимущества ](https://v8.1c.ru/erp/preimushchestva/)\n[ Преимущества ](https://v8.1c.ru/erp/preimushchestva/) [ Истории успеха ](https://v8.1c.ru/erp/istorii-uspekha-1c-erp/) [ Экономический эффект ](https://v8.1c.ru/erp/ekonomicheskiy-effekt/) [ Сертифицированные партнеры ](https://v8.1c.ru/erp/sertifitsirovannye-partnery/) [ Отраслевые решения ](https://v8.1c.ru/erp/otraslevye-resheniya/) [ Технологии внедрения ](https://v8.1c.ru/erp/tekhnologii-vnedreniya/) [ Переход с «1С:УПП» ](https://v8.1c.ru/erp/perekhod-s-1s-upravlenie-proizvodstvennym-predpriyatiem/) [ Миграция с зарубежных систем ](https://v8.1c.ru/erp/migratsiya-s-drugih-sistem/)\n  * [ Функциональность ](https://v8.1c.ru/erp/funktsionalnost-1s-erp/)\n[ Функциональность ](https://v8.1c.ru/erp/funktsionalnost-1s-erp/) [ Мониторинг и анализ показателей деятельности ](https://v8.1c.ru/erp/monitoring/) [ Управление финансами и бюджетирование ](https://v8.1c.ru/erp/budget/) [ Казначейство ](https://v8.1c.ru/erp/treasury/) [ Международный финансовый учет ](https://v8.1c.ru/erp/finances/) [ Управление продажами ](https://v8.1c.ru/erp/sales/) [ Управление взаимоотношениями с клиентами ](https://v8.1c.ru/erp/clients/) [ Управление закупками ](https://v8.1c.ru/erp/purchasing/) [ Управление складом и запасами ](https://v8.1c.ru/erp/warehouse/) [ Регламентированный учет ](https://v8.1c.ru/erp/reglamentirovannyy-uchet/) [ Управление затратами и расчет себестоимости ](https://v8.1c.ru/erp/cost_management/)\n[ Управление персоналом и расчет заработной платы ](https://v8.1c.ru/erp/hrm_payroll/) [ Управление производством ](https://v8.1c.ru/erp/production/) [ Организация ремонтов ](https://v8.1c.ru/erp/repairs/) [ Планирование запасов ](https://v8.1c.ru/erp/tovarnoe-planirovanie/) [ Интеграция с системой «Честный знак» ](https://v8.1c.ru/erp/integratsiya-s-sistemoy-chestnyy-znak/) [ Интеграция с маркетплейсами ](https://v8.1c.ru/erp/integratsiya-s-marketpleysami-erp/) [ Функциональная модель «1С:ERP Управление предприятием» ](https://v8.1c.ru/erp/funktsionalnaya-model-1s-erp-upravlenie-predpriyatiem/) [ Совместное использование с «1С:Документооборот 8» ](https://v8.1c.ru/erp/doc8corp/) [ Политика конфиденциальности приложения 1С:ERP ](https://v8.1c.ru/erp/politika-konfidentsialnosti-prilozheniya-1s-erp/)\n  * [ 1С:ERP WE ](https://v8.1c.ru/erp/1s-erp-we/)\n  * [ Сервисы ИТС ](https://v8.1c.ru/erp/servisy-its/)\n  * [ Полезные материалы ](https://v8.1c.ru/erp/poleznye-materialy/)\n  * Цена\n  * [Купить, внедрить, проконсультироваться](https://v8.1c.ru/partners/erp/tyumen/)\n\n\n  * [Главная](https://v8.1c.ru/)\n
"""
print(len(s))