from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Custom fields for deal tracking
    booking_date = fields.Date(
        string='Booking Date',
        tracking=True,
    )

    developer_commission = fields.Float(
        string='Broker Commission',
        tracking=True,
        digits=(16, 2),
    )

    buyer_id = fields.Many2one(
        'res.partner',
        string='Buyer',
        tracking=True,
    )

    deal_id = fields.Integer(
        string='Deal ID',
        tracking=True,
        copy=False,  # Don't copy when duplicating record
    )

    project_id = fields.Many2one(
        'product.template',
        string='Project Name',
        tracking=True,
    )

    sale_value = fields.Monetary(
        string='Sale Value',
        tracking=True,
        currency_field='currency_id',
    )

    unit_id = fields.Many2one(
        'product.product',
        string='Unit',
        tracking=True,
        domain="[('product_tmpl_id', '=', project_id)]",  # Only show units related to selected project
    )

    @api.onchange('project_id')
    def _onchange_project_id(self):
        """Clear unit selection when project changes"""
        if self.project_id:
            self.unit_id = False