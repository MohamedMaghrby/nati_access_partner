# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP


class AccessPartnerWizard(models.TransientModel):
    _name = 'nati.access.partner.wiz'
    _description = 'Access Partner Rules'

    userc_id = fields.Many2one('res.users', string='Owner')
    message_partner_ids = fields.Many2many(comodel_name='res.partner', string='Followers',
                                           domain="[('partner_share','=', False)]",)

    def add_followers(self):
        active_partner_ids = self.env['res.partner'].browse(self._context.get('active_ids', False))
        if not active_partner_ids:
            return

        if self.message_partner_ids:
            for partner in active_partner_ids:
                new_partners = self.message_partner_ids - partner.sudo().message_partner_ids
                partner.message_subscribe(partner_ids=new_partners.ids)


        vals = {}
        if self.userc_id:
            vals.update({'userc_id': self.userc_id})

        active_partner_ids.write(vals)

    def unfollow(self):
        active_partner_ids = self.env['res.partner'].browse(self._context.get('active_ids', False))
        if not active_partner_ids:
            return

        if self.message_partner_ids:
            for partner in active_partner_ids:
                new_partners = self.message_partner_ids
                partner.message_unsubscribe(partner_ids=new_partners.ids)

        vals = {}
        vals.update({'userc_id': False})
        active_partner_ids.write(vals)
