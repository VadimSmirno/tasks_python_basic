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




number = int(input('Сколько сайтов? '))
name_product = input('Введите название продукта для нового сайта: ')
def fun_site (struct,name,count):
    if count == 0:
        return

    struct['html']['head']['title'] = f'Куплю/продам {name} недорого'
    struct['html']['body']['h2'] = f'У нас самая низкая цена на {name}'
    print (struct)

    name_product = input('Введите название продукта для нового сайта: ')
    fun_site(struct,name_product,count-1)


fun_site(site,name_product,number)