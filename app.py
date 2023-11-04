# practice using packages. will not practice using "as" at this point of practice.

# 1st approach, import the module under python package by using only import. this will make the code longer.
import ecommerce.shipping

ecommerce.shipping.calc_total()
ecommerce.shipping.calc_total()

# 2nd approach, use from and call package and module then import function. a bit shorter
from ecommerce.shipping import calc_total

calc_total()
calc_total()

# 3rd approach, use from and call package, then import module
from ecommerce import shipping

shipping.calc_total()
shipping.calc_total()
