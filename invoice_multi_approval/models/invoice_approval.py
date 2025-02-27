# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Cybrosys Techno Solutions (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import api, fields, models


class InvoiceApproval(models.Model):
    """This class creates a model 'invoice.approval' and adds
    required fields"""
    _name = 'invoice.approval'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Invoice Approval'

    name = fields.Char(default='Approval Configuration', string="Name",
                       help="Approval configuration.")
    approve_customer_invoice = fields.Boolean(string="Approval on"
                                                     " Customer Invoice",
                                              help='Enable this field '
                                                   'for adding the approvals '
                                                   'for the customer invoice.')
    invoice_approver_ids = fields.Many2many('res.users',
                                            'invoice_id',
                                            string='Invoice Approver',
                                            domain=lambda self: [
                                                ('groups_id', 'in',
                                                 self.env.ref('invoice_multi_'
                                                              'approval.group_approver').id)],
                                            help='In this field you can add '
                                                 'the approvers for the '
                                                 'customer invoice.')
    approve_vendor_bill = fields.Boolean(string="Approval on Vendor Bill",
                                         help='Enable this field for adding'
                                              ' the approvals for the'
                                              ' Vendor bill.')
    bill_approver_ids = fields.Many2many('res.users',
                                         'bill_id',
                                         string='Bill Approver',
                                         domain=lambda self: [
                                             ('groups_id', 'in',
                                              self.env.ref('invoice_multi_'
                                                           'approval.group_approver').id)],
                                         help='In this field you can add the '
                                              'approvers for the Vendor bill.')
    approve_customer_credit = fields.Boolean(string='Approval on Customer'
                                                    ' Refund',
                                             help='Enable this field for'
                                                  ' adding the approvals'
                                                  ' for the customer credit '
                                                  'note.')
    cust_credit_approver_ids = fields.Many2many('res.users',
                                                'cust_credit_id',
                                                string='Customer Credit Note'
                                                       ' Approver',
                                                domain=lambda self: [
                                                    ('groups_id', 'in',
                                                     self.env.ref(
                                                         'invoice_multi_'
                                                         'approval.group_'
                                                         'approver').id)],
                                                help='In this field you can add'
                                                     'the approvers for the'
                                                     ' Customer credit note.')
    approve_vendor_credit = fields.Boolean(string='Approval on Vendor Refund',
                                           help='Enable this field for adding '
                                                'the approvals for the'
                                                ' Vendor credit note.')
    vend_credit_approver_ids = fields.Many2many('res.users',
                                                'vend_credit_id',
                                                string='Vendor Credit Note'
                                                       ' Approver',
                                                domain=lambda self: [
                                                    ('groups_id', 'in',
                                                     self.env.ref(
                                                         'invoice_multi_'
                                                         'approval.group_'
                                                         'approver').id)],
                                                help='In this field you can'
                                                     ' add the approvers '
                                                     'for the Vendor credit'
                                                     ' note.')
    no_approve = fields.Boolean(string='No Approval',
                                help='Approval is not needed',
                                compute="_compute_no_approve")

    @api.depends('approve_vendor_credit', 'approve_customer_invoice',
                 'approve_vendor_bill', 'approve_customer_credit')
    def _compute_no_approve(self):
        """Method _compute_no_approve to compute the value to the field
        no_approve"""
        for rec in self:
            rec.no_approve = True if rec.approve_customer_invoice or rec.approve_customer_credit or rec.approve_vendor_credit or rec.approve_vendor_bill else False
