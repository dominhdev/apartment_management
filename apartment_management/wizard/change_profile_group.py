# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ChangeProfileGroup(models.TransientModel):
    _name = 'change.profile.group'
    _description = 'Change Profile Group'

    group_profile_id = fields.Many2one('res.groups', string="Profile Group")

    def act_approve(self):
        self.ensure_one()
        if not self.group_profile_id:
            raise UserError(_("Please select Group"))
        change_action = self.env.context.get('change_action')
        if change_action:
            check_change_action = self.env['ir.config_parameter'].sudo().get_param('vip_check_change_action')
            if check_change_action == '1':
                raise UserError(_("Please recheck change action"))
            code_group = self.group_profile_id.name.replace(" ", "").replace("Staff", "").replace("Manager", "").lower()
            if code_group:
                if code_group == 'leasing':
                    user_ids = self.env['res.users'].search([('vip_user_type', '=', code_group)])
                    action_id = self.env.ref('vip_base.vip_open_leasing_board_my_dash_action')
                elif code_group == 'pm':
                    user_ids = self.env['res.users'].search([('vip_user_type', '=', code_group)])
                    action_id = self.env.ref('vip_base.vip_open_pm_board_my_dash_action')
                else:
                    user_ids = False
                    action_id = False
                if user_ids and action_id:
                    for user in user_ids:
                        user.action_id = action_id.id
        else:
            active_ids = self.env.context.get('active_ids')
            if active_ids:
                user_ids = self.env['res.users'].sudo().browse(active_ids)
                for us_id in user_ids:
                    us_id.group_profile_id = self.group_profile_id.id if self.group_profile_id else False
                    us_id.function = self.group_profile_id.name
        return
