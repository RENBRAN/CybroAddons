# -*- coding: utf-8 -*-
###############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Cybrosys Techno Solutions(<https://www.cybrosys.com>)
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
#
###############################################################################
from odoo import api, fields, models


class ProjectTask(models.Model):
    """ Inherits project.task """
    _inherit = 'project.task'

    unique_code = fields.Char(string='Unique Code', readonly=True,
                              help='Unique code for each task.')
    _sql_constraints = [
        ('unique_code', 'unique(unique_code, company_id)',
         'Code must be unique per company!'),
    ]

    @api.model_create_multi
    def create(self, vals_list):
        """ Extends the create method to generate the unique code """
        for vals in vals_list:
            project = self.env['project.project'].browse(vals.get('project_id'))
            if project.sequence_id:
                vals['unique_code'] = project.sequence_id.next_by_id()
        return super().create(vals_list)
