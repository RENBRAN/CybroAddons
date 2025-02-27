# -*- coding: utf-8 -*-
###############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Aysha Shalin (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC
#    LICENSE (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
from odoo import api, fields, models


class StockMove(models.Model):
    """Inherits Stock move for scanning multi barcode"""
    _inherit = 'stock.move'

    scan_barcode = fields.Char(string='Product Barcode',
                               compute='_compute_scan_barcode',
                               inverse='_inverse_scan_barcode',
                               store=True,
                               help="Here you can provide the barcode for the "
                                    "product")

    @api.depends('sale_line_id', 'purchase_line_id')
    def _compute_scan_barcode(self):
        """For updating the Product Barcode field in delivery while it's
                generating from a Purchase order or sale order"""
        for stock in self:
            if stock.sale_line_id:
                stock.scan_barcode = stock.sale_line_id.scan_barcode
            if stock.purchase_line_id:
                stock.scan_barcode = stock.purchase_line_id.scan_barcode

    def _inverse_scan_barcode(self):
        """Inverse function for scan_barcode"""
        for stock in self:
            stock.scan_barcode = stock.scan_barcode

    @api.onchange('scan_barcode')
    def _onchange_scan_barcode(self):
        """For getting the scanned barcode product"""
        if self.scan_barcode:
            product = self.env['product.multiple.barcodes'].search(
                [('product_multi_barcode', '=', self.scan_barcode)])
            self.product_id = product.product_id.id
