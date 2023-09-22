# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    @api.model
    def create(self, vals):
        if 'vat' in vals:
            vals['vat'] = vals['vat'].upper().replace('-', '')
        return super(ResPartner, self).create(vals)
        
    def write(self, vals):
        if 'vat' in vals:
            vals['vat'] = vals['vat'].upper().replace('-', '')
        return super(ResPartner, self).write(vals)