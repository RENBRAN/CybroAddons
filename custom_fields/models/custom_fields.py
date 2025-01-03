from odoo import models, fields, api

class DealEligible(models.Model):
    _name = 'deal.eligible'
    _description = 'Deal Eligible'

    booking_date = fields.Date(string="Booking Date")
    developer_commission = fields.Float(string="Broker Commission", tracking=True)
    buyer = fields.Many2one('res.partner', string="Buyer Name", tracking=True)
    deal_id = fields.Integer(string="Deal ID", tracking=True)
    project = fields.Many2one('product.template', string="Project Name", tracking=True)
    sale_value = fields.Monetary(string="Sale Value", tracking=True, currency_field='currency_id')
    unit = fields.Many2one('product.product', string="Unit", tracking=True)
    currency_id = fields.Many2one('res.currency', string="Currency")