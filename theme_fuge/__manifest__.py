# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
{
    'name': 'Theme Fuge',
    'version': '18.0.1.0.0',
    'category': 'Theme/eCommerce',
    'summary': 'Design Web Pages with theme fuge',
    'description': 'Theme Fuge is an attractive and modern eCommerce Website'
                   ' theme',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['website', 'website_sale_wishlist', 'website_blog'],
    'data': [
        'views/views.xml',
        'views/shop_view.xml',
        'views/shop_sidebar_view.xml',
        'views/product_view.xml',
        'views/blog.xml',
        'views/popular_posts.xml',
        'views/blog_details.xml',
        'views/about.xml',
        'views/contact.xml',
        'views/footer.xml',
        'views/snippets/banner.xml',
        'views/snippets/shop_with_us.xml',
        'views/snippets/offer_men.xml',
        'views/snippets/offer_women.xml',
        'views/snippets/product_section.xml',
        'views/snippets/latest_blogs.xml',
        'views/snippets/customer_review.xml',
        'views/snippets/subscribe.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'theme_fuge/static/src/css/style.css',
            'theme_fuge/static/src/css/owl.carousel.min.css',
            'theme_fuge/static/src/css/owl.theme.default.min.css',
            'theme_fuge/static/src/js/product.js',
        ],
    },
    "images": [
        "static/description/banner.jpg",
        "static/description/theme_screenshot.jpg",
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
