import asyncio
import os

from django.core import paginator
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.utils.translation import gettext_lazy, gettext

from django.conf import settings
from .models import *
from .modules.tg_bot import SingletonBot
from .modules.tg_bot import MESSAGE as notificationMessage
from .modules.sort_types import *




mainMenu = [
    (gettext_lazy("MainmenuMainPage"), 'index'),
    (gettext_lazy("MainmenuProductionPage"), 'category'),
    (gettext_lazy("MainmenuAboutPage"), 'about'),
    (gettext_lazy("MainmenuContactsPage"), 'contacts'),
]


def addMessage(request, text, type='info'):
    _ = {
        'error': messages.error,
        'success': messages.success,
        'info': messages.info,
        'warning': messages.warning,
        'debug': messages.debug,
    }

    func = _[type]
    if not func: raise Exception(f'Message type {type} is not defined')

    func(request, text)


def renderPage(request, templateName, *args, **kwargs):
    builtinArgs = {
        'get': request.GET,
        'mainMenu': mainMenu,
        'media_url': settings.MEDIA_URL,
    }

    for k, v in kwargs.items():
        builtinArgs[k] = v

    return render(request, templateName, builtinArgs)


def change_language(request, lang_code):
    return redirect('index')

def index_view(request):
    return renderPage(
        request, 'main/index.html',
        title=gettext_lazy('TitleMainPage'),
        menuSelect='main-page'
    )


def category_view(request, category=None):
    categories = Category.objects.all().order_by('order')

    # search query
    searchQuery = request.GET.get('query')

    if not (searchQuery or category):
        return renderPage(
            request, 'main/category.html',
            title=gettext_lazy('TitleProductsPage'),
            menuSelect='products',
            categories=categories,
        )


    # list or grid
    orientation = request.GET.get('view') if request.GET.get('view') in ['list', 'grid'] else 'grid'

    # sorting configs
    currentSortingType = productSortTypes.get(
        request.GET.get('sort'), list(productSortTypes.values())[0]
    )

    # paginator configs
    paginatorValues = [25, 50, 100]
    try:
        currentPaginatorValue = int(request.GET.get('pag', paginatorValues[0]))
        assert currentPaginatorValue in paginatorValues
    except: currentPaginatorValue = paginatorValues[0]


    if searchQuery:
        products = Product.objects.filter(
            Q(name__iexact=searchQuery) | Q(description__icontains=searchQuery) | Q(name__icontains=searchQuery.lower()) | Q(name__icontains=searchQuery.upper())
        )
    else:
        category = get_object_or_404(Category, tag=category)
        products = Product.objects.filter(category=category)

    title = gettext_lazy('ProductspageSearchResult') + searchQuery if searchQuery else category.name
    productsPaginator = Paginator(
        products.order_by( currentSortingType.sort() ),
        currentPaginatorValue,
    )

    try:
        currentPage = max(
            1, min(int(request.GET.get('page', 1)), productsPaginator.num_pages)
        )
    except: currentPage = 1

    return renderPage(
        request, 'main/products.html',
        title=title,
        menuSelect='products',
        products=productsPaginator.page(currentPage),
        orientation=orientation,
        paginator_values=paginatorValues, currentPaginatorValue=currentPaginatorValue,
        currentPageString=gettext('Сторінка %(cpage)d з %(pages)d') % {'cpage': currentPage, 'pages': productsPaginator.num_pages},
        availableSortTypes=productSortTypes.values(),
    )


def product_view(request, tag):
    product = get_object_or_404(Product, tag=tag)

    return renderPage(
        request, 'main/product.html',
        title=product.name,
        menuSelect='products',
        product=product,
    )


def about_view(request):
    certificatesDir = settings.MEDIA_ROOT /  'certificates'
    certificatesUrl = settings.MEDIA_URL +  'certificates'
    certificates = [
        certificatesUrl + '/' + name for name in next(os.walk(certificatesDir))[2]
    ]

    aboutUsMediaDir = settings.MEDIA_ROOT /  'about_us_media'
    aboutUsMediaUrl = settings.MEDIA_URL +  'about_us_media'
    aboutUsMedia = [
        aboutUsMediaUrl + '/' + name for name in next(os.walk(aboutUsMediaDir))[2]
    ]


    return renderPage(
        request, 'main/about.html',
        title=gettext_lazy('TitleAboutPage'),
        menuSelect='about',
        certificates=certificates,
        aboutUsMedia=aboutUsMedia
    )

def contacts_view(request):
    if request.POST:
        fullname = request.POST.get('fullname')
        contact = request.POST.get('contact')
        message = request.POST.get('message')

        if fullname and contact and message:
            botTokenInfo = Info.objects.get(tag='notifications_bot')
            if not botTokenInfo: return redirect('contacts')

            token = botTokenInfo.data.get('token')
            recipients = botTokenInfo.data.get('recipients')

            if not all([token, recipients]):
                return redirect('contacts')

            message = notificationMessage.format(
                fullname, contact, message
            )

            for recipient in recipients:
                asyncio.run(
                    SingletonBot(token).sendMessage(
                        recipient, message
                    )
                )

            addMessage(request, gettext_lazy('MessageRequestAccepted'))

    return renderPage(
        request, 'main/contacts.html',
        title=gettext_lazy('TitleContactsPage'),
        menuSelect='contacts'
    )
