from tkinter import *
from tkinter import ttk
from forex_python.converter import CurrencyRates

with open('use_letter_code.txt', 'r') as file:
    value = file.readline()
    if value == 'yes':
        use_letter_code = True
    elif value == 'no':
        use_letter_code = False
    else:
        use_letter_code = True
        with open('use_letter_code.txt', 'w') as f:
            f.write('yes\n')

currency = {
            'Долар США': 'USD',
            'Євро': 'EUR',
            'Японська єна': 'JPY',
            'Болгарський лев': 'BGN',
            'Чеська крона': 'CZK',
            'Данська крона': 'DKK',
            'Фунт стерлінгів': 'GBP',
            'Угорський форинт': 'HUF',
            'Злотий': 'PLN',
            'Румунський лей': 'RON',
            'Шведська крона': 'SEK',
            'Швейцарський франк': 'CHF',
            'Ісландська крона': 'ISK',
            'Норвезька крона': 'NOK',
            'Хорватська куна': 'HRK',
            'Турецька ліра': 'TRY',
            'Австралійський долар': 'AUD',
            'Бразильський реал': 'BRL',
            'Канадський долар': 'CAD',
            'Юань Женьміньбі': 'CNY',
            'Гонконзький долар': 'HKD',
            'Індонезійська рупія': 'IDR',
            'Індійська рупія': 'INR',
            'Південнокорейська вона': 'KRW',
            'Мексиканський песо': 'MXN',
            'Малайзійський рингіт': 'MYR',
            'Новозеландський долар': 'NZD',
            'Філіппінське песо': 'PHP',
            'Сінгапурський долар': 'SGD',
            'Тайський бат': 'THB',
            'Південноафриканський ранд': 'ZAR'
            }

c = CurrencyRates()

element_parameters = [200, 25, 5]

root = Tk()
root.resizable(width=False, height=False)
root.geometry(f'{element_parameters[0]*2 + element_parameters[2]*3}'
              f'x{element_parameters[1]*2 + element_parameters[2]*3}')
root.title('Currency Converter')

if use_letter_code:
    box_names = list(currency.values())
else:
    box_names = list(currency.keys())

value1 = ttk.Combobox(root, values=box_names)
value2 = ttk.Combobox(root, values=box_names)
entry = ttk.Entry(root)
result = ttk.Label(root, wraplength=element_parameters[2]*2 + element_parameters[0], font='Arial 10')

value1.place(x=element_parameters[2], y=element_parameters[2],
             width=element_parameters[0], height=element_parameters[1])
value2.place(x=element_parameters[2]*2 + element_parameters[0], y=element_parameters[2],
             width=element_parameters[0], height=element_parameters[1])
entry.place(x=element_parameters[2], y=element_parameters[2]*2 + element_parameters[1],
            width=element_parameters[0], height=element_parameters[1])
result.place(x=element_parameters[2]*2 + element_parameters[0], y=element_parameters[2]*2 + element_parameters[1],
             width=element_parameters[0], height=element_parameters[1])

while True:
    try:
        if type(float(entry.get())) is float:
            if use_letter_code:
                base_currency = value1.get()
                dest_currency = value2.get()
            else:
                base_currency = currency[value1.get()]
                dest_currency = currency[value2.get()]
            result.configure(text=str(c.convert(base_currency,
                                                dest_currency,
                                                float(entry.get()))),
                             foreground='blue', font='Arial 10')
    except Exception as exc:
        result.configure(text=f'{exc.__class__.__name__}: {exc}', foreground='red', font='Arial 7')
    root.update()
