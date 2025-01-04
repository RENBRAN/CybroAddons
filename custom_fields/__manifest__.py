{
    'name': 'Custom sale and invoice fields',
    'version': '1.0',
    'summary': 'Module to manage deal eligibles',
    'description': 'Custom module for managing deals and their details in Sales Management.',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'category': 'Sales',
    'depends': ['base', 'sale', 'account','purchase',],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/account_move_views',
    ],
    'installable': True,
    'application': True,
}