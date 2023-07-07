import decimal
from functools import cached_property

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from utils import get_anonymous_user

from . mixins import MarketModelMixin


UserModel = settings.AUTH_USER_MODEL


class Store(MarketModelMixin):
    STORE_CATEGORY = (
        ('farm', _("FARM PRODUCTS")),
        ('agric', _("AGRIC PRODUCTS")),
        ('service', _("SERVICES")),
    )

    store_type = models.CharField(
        _("Store type"), max_length=50, choices=STORE_CATEGORY, default=STORE_CATEGORY[0])
    owner = models.ForeignKey(
        UserModel, on_delete=models.SET_DEFAULT, default=get_anonymous_user,
        related_name='stores', verbose_name=_("Store owner"))

    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")

    @property
    def products(self):
        return self.store_products.all()

    def get_absolute_url(self):
        return reverse("store_detail", kwargs={"slug": self.slug})


class Product(MarketModelMixin):
    MARKET_TARGET = (
        ('all', _("ALL")),
        ('us', _("MARKET USERS")),
        ('fm', _("FARMERS ONLY")),
        ('agro', _("AGRO-SERVICES ONLY")),
        ('sup', _("SUPPORT ONLY")),
    )

    price = models.DecimalField(
        _("Price"), max_digits=7, decimal_places=2, default=0.00)
    discount = models.DecimalField(
        _("Discount"), max_digits=5, decimal_places=2, default=0.00)

    target = models.CharField(_("Market target"), max_length=120,
                              choices=MARKET_TARGET, default=MARKET_TARGET[1])
    qty = models.IntegerField(_("Quantity"), default=0)

    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, related_name='store_products', verbose_name=_("Store"))
    created_by = models.ForeignKey(
        UserModel, on_delete=models.SET_DEFAULT, default=get_anonymous_user,
        related_name='market_products', verbose_name=_("Created by"))
    date_created = models.DateTimeField(_("created on"), default=timezone.now)
    last_modified = models.DateTimeField(_("last modified"), auto_now=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    @property
    def short_description(self):
        return self.short_desc

    @property
    def long_description(self):
        return self.long_desc

    @property
    def qty_sold(self):
        return self.sales.count()

    @property
    def in_stock(self):
        return self.qty - self.qty_sold

    @cached_property
    def sales_price(self):
        return self.price - self.discount

    @property
    def credit_sales(self):
        _credit = decimal.Decimal()
        for sales in self.sales.all():
            _credit += sales.credit
        return _credit.quantize(decimal.Decimal('0.00'))

    @property
    def paid_sales(self):
        _paid = decimal.Decimal()
        for sales in self.sales.all():
            _paid += sales.paid
        return _paid.quantize(decimal.Decimal('0.00'))

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={
            "store": self.store.name, "pk": self.pk
        })


class Sale(models.Model):
    PAYMENT_STATUS = (
        ('pending', _("PENDING")),
        ('part_30', _("PAID (30%)")),
        ('part_50', _("PAID (50%)")),
        ('part_80', _("PAID (80%)")),
        ('full', _("FULL PAYMENT")),
    )
    DELIVERY_STATUS = (
        ('pending', _("PENDING")),
        ('delivered', _("DELIVERED")),
    )

    slug = models.SlugField(_("In-app url"), unique=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='sales',
        verbose_name=_("Product"),)
    payment = models.CharField(_("Payment"), max_length=120,
                               choices=PAYMENT_STATUS, default=PAYMENT_STATUS[0])
    delivery = models.CharField(_("Delivery"), max_length=120,
                                choices=DELIVERY_STATUS, default=DELIVERY_STATUS[0])

    date_created = models.DateTimeField(_("created on"), default=timezone.now)
    last_modified = models.DateTimeField(_("last modified"), auto_now=True)

    class Meta:
        verbose_name = _("Sales")
        verbose_name_plural = _("Sales")

    @property
    def paid(self):
        if self.payment == 'pending':
            return decimal.Decimal()
        elif self.payment == 'full':
            return self.product.sales_price
        _paid = int(self.payment[-2:])
        return (decimal.Decimal(str(_paid/100)) * self.product.sales_price)

    @property
    def credit(self):
        if self.payment == 'pending':
            return self.product.sales_price
        elif self.payment == 'full':
            return decimal.Decimal()
        _credit = int(self.payment[-2:]) - 100
        return (decimal.Decimal(str(_credit/100)) * self.product.sales_price)

    def __str__(self):
        return self.product.name

    def get_absolute_url(self):
        return reverse("sales_detail", kwargs={
            'prod': self.product.name, 'slug': self.slug
        })
