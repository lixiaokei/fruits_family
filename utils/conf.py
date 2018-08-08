
"""指定工具中的特定参数"""

"""都能访问，但实现登陆与未登录的不同处理的接口"""
USER_PATH_PASS = [
    '/fruits_shop/index/',
    '/fruits_shop/detail/',
    '/fruits_shop/add_cart/',
    '/fruits_shop/get_cart_count/',
    '/fruits_shop/cart/',
    '/fruits_shop/subtotal/',
    '/fruits_shop/total_price/',
    '/fruits_shop/change_num/',
    '/fruits_shop/cart_delete/',
    '/fruits_shop/change_status/',
    '/user/user_center_info/',
    '/user/show_address/',
    '/user/add_address/',
    '/user/edit_address',
    '/fruits_shop/make_order/',
    '/fruits_shop/order_pay/',
    '/user/user_order_info/',
]

"""必须要登陆后才可访问的接口"""
USER_MUST_LOGIN_PATH = [
    '/user/user_center_info/',
    '/user/show_address/',
    '/user/add_address/',
    '/user/edit_address/',
    '/fruits_shop/make_order/',
    '/fruits_shop/order_pay/',
    '/user/user_order_info/',
]