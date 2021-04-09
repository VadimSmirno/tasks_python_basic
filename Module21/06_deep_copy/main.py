
site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}




def fun_site(struct, key, new_value):
    if key[0] in struct:
        struct[key[0]] = f'Куплю/продам {new_value} недорого'
    if key[1] in struct:
        struct[key[1]] = f'У нас самая низкая цена на {new_value}'
        return struct
    else:
        for i_val_struct in struct.values():
            if isinstance(i_val_struct, dict):
                fun_site(i_val_struct,key, new_value)

    return struct


def pretty(dct, indent=0):
   for key, value in dct.items():
      print('\t' * indent,key,':')
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print(' ' * (indent+1) ,value)



number = int(input('Сколько сайтов? '))
key = 'title','h2'
for _ in range (number):
    name_product = input('Введите название продукта для нового сайта: ')
    print (f'Сайт для {name_product}')
    result_fun_site = fun_site(site,key, name_product)
    print ('site')
    pretty(result_fun_site)


