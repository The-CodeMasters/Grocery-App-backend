from django.contrib import admin
from .models import usertb
from .models import delivery_user
from .models import delivery_histroy
from .models import admin_user
from .models import product
from .models import cart
from .models import favourite
from .models import order
from .models import order_item
from .models import promo_code
from .models import promo_used
from .models import primary_cat
from .models import secondary_cat
# Register your models here.

admin.site.register(usertb.UserTable)
admin.site.register(admin_user.AdminUser)
admin.site.register(delivery_histroy.DeliveryHistory)
admin.site.register(delivery_user.DeliveryUser)
admin.site.register(product.Product)
admin.site.register(cart.Cart)
admin.site.register(favourite.FavouriteProduct)
admin.site.register(order.Order)
admin.site.register(promo_code.PromoCode)
admin.site.register(promo_used.PromoUsed)
admin.site.register(primary_cat.PrimaryCategory)
admin.site.register(secondary_cat.SecondaryCategory)
