# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP


class AccessPartnerWizard(models.TransientModel):
    _name = 'nati.unaccess.partner.wiz'
    _description = 'Un Access Partner Rules'

    userunlink = fields.Boolean('User Unlink', default=False, help="If checked, the user owner will be Blank ")

    message_partner_ids = fields.Many2many(comodel_name='res.partner', string='Followers',
                                           domain="[('partner_share','=', False)]",)

    def unfollow(self):
        active_partner_ids = self.env['res.partner'].browse(self._context.get('active_ids', False))
        if not active_partner_ids:
            return

        if self.message_partner_ids:
            for partner in active_partner_ids:
                new_partners = self.message_partner_ids
                partner.message_unsubscribe(partner_ids=new_partners.ids)

        if self.userunlink:
            vals = {}
            vals.update({'userc_id': False})
            active_partner_ids.write(vals)
