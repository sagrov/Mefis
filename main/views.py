from django.shortcuts import render


def index(request):
    products = [
        {
            'name': 'Зелений стілець',
            'cost': 100.25,
            'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
            'img': {
                'url': '../../static/main/img/1.jpg'
            }

        },
        {
            'name': 'Зелений стілець',
            'cost': 100.25,
            'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
            'img': {
                'url': '../../static/main/img/2.jpg'
            }

        },
        {
            'name': 'Зелений стілець',
            'cost': 100.25,
            'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
            'img': {
                'url': '../../static/main/img/1.jpg'
            }

        },
        {
            'name': 'Зелений стілець',
            'cost': 100.25,
            'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
            'img': {
                'url': '../../static/main/img/1.jpg'
            }

        },
        {
            'name': 'Зелений стілець',
            'cost': 100.25,
            'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
            'img': {
                'url': '../../static/main/img/1.jpg'
            }

        },
        {
            'name': 'Зелений стілець',
            'cost': 100.25,
            'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
            'img': {
                'url': '../../static/main/img/1.jpg'
            }

        },
        {
            'name': 'Зелений стілець',
            'cost': 100.25,
            'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
            'img': {
                'url': '../../static/main/img/1.jpg'
            }

        },
        {
            'name': 'Зелений стілець',
            'cost': 100.25,
            'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
            'img': {
                'url': '../../static/main/img/1.jpg'
            }

        },
        {
            'name': 'Зелений стілець',
            'cost': 100.25,
            'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
            'img': {
                'url': '../../static/main/img/1.jpg'
            }

        },
        {
            'name': 'Зелений стілець',
            'cost': 100.25,
            'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
            'img': {
                'url': '../../static/main/img/1.jpg'
            }

        },

    ],
    categories = [
        {
            'name': 'Лампа',
            'img': {
                'url': '../../static/main/img/1.jpg'
            }
        },
        {
            'name': 'Лампа',
            'img': {
                'url': '../../static/main/img/1.jpg'
            }
        },
        {
            'name': 'Лампа',
            'img': {
                'url': '../../static/main/img/1.jpg'
            }
        },
        {
            'name': 'Лампа',
            'img': {
                'url': '../../static/main/img/2.jpg'
            }
        },
        {
            'name': 'Лампа',
            'img': {
                'url': '../../static/main/img/1.jpg'
            }
        },
        {
            'name': 'Лампа',
            'img': {
                'url': '../../static/main/img/2.jpg'
            }
        },
    ],

    return render(request, 'main/index.html', context={"products": products, "categories": categories})
    # products = [
    #     {
    #         'name': 'Зелений стілець',
    #         'cost': 100.25,
    #         'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
    #         'img': {
    #             'url': '../../static/main/img/1.jpg'
    #         }
    #
    #     },
    #     {
    #         'name': 'Зелений стілець',
    #         'cost': 100.25,
    #         'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
    #         'img': {
    #             'url': '../../static/main/img/1.jpg'
    #         }
    #
    #     },
    #     {
    #         'name': 'Зелений стілець',
    #         'cost': 100.25,
    #         'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
    #         'img': {
    #             'url': '../../static/main/img/1.jpg'
    #         }
    #
    #     },
    #     {
    #         'name': 'Зелений стілець',
    #         'cost': 100.25,
    #         'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
    #         'img': {
    #             'url': '../../static/main/img/1.jpg'
    #         }
    #
    #     },
    #     {
    #         'name': 'Зелений стілець',
    #         'cost': 100.25,
    #         'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
    #         'img': {
    #             'url': '../../static/main/img/1.jpg'
    #         }
    #
    #     },
    #     {
    #         'name': 'Зелений стілець',
    #         'cost': 100.25,
    #         'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
    #         'img': {
    #             'url': '../../static/main/img/1.jpg'
    #         }
    #
    #     },
    #     {
    #         'name': 'Зелений стілець',
    #         'cost': 100.25,
    #         'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
    #         'img': {
    #             'url': '../../static/main/img/1.jpg'
    #         }
    #
    #     },
    #     {
    #         'name': 'Зелений стілець',
    #         'cost': 100.25,
    #         'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
    #         'img': {
    #             'url': '../../static/main/img/1.jpg'
    #         }
    #
    #     },
    #     {
    #         'name': 'Зелений стілець',
    #         'cost': 100.25,
    #         'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
    #         'img': {
    #             'url': '../../static/main/img/1.jpg'
    #         }
    #
    #     },
    #     {
    #         'name': 'Зелений стілець',
    #         'cost': 100.25,
    #         'descriptions': 'Этот текст содержит в себе информацию о данном товаре',
    #         'img': {
    #             'url': '../../static/main/img/1.jpg'
    #         }
    #
    #     },
    #
    # ]
    # return render(request, 'main/index.html', context={"products": products})


def catalog(request):
    category_menues = [
        {
            'name': 'Стільці'
        },
        {
            'name': 'Столи'
        },
        {
            'name': 'Лампи'
        },
        {
            'name': 'Ліжко'
        },
        {
            'name': 'Дивани'
        },
    ],
    sub_category_menues = [
        {
            'name': 'Всі товари'
        },
        {
            'name': 'Офісні'
        },
        {
            'name': 'Домашні'
        }
    ],
    return render(request, 'main/catalog.html', context={"category_menues": category_menues, "sub_category_menues": sub_category_menues})


def cart(request):
    return render(request, 'main/cart.html')

# def products_features():
#     products = [
#         {
#             'product': {
#                 'name': 'Зелений стілець',
#                 'cost': 100.25,
#                 'descriptions': 'Этот текст содержит в себе информацию о данном товаре'
#             }
#         }
#     ]
#     return 0
