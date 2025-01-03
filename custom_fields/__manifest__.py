{
    'name': 'Deal Eligible Management',
    'version': '1.0',
    'summary': 'Module to manage deal eligibles',
    'description': 'Custom module for managing deals and their details in Sales Management.',
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'category': 'Sales',
    'depends': ['base', 'sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/deal_eligible_views.xml',
    ],
    'installable': True,
    'application': True,
}