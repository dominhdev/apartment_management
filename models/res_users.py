# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    group_profile_id = fields.Many2one('res.groups', string="Profile Group")
    vip_user_type = fields.Char()

    def write(self, vals):

        res = super(ResUsers, self).write(vals)
        group_equipment_manager = self.env.ref('maintenance.group_equipment_manager')
        group_maintenance_manager = self.env.ref('property_maintenance.groups_property_maintenance_manager')
        group_maintenance_worker = self.env.ref('property_maintenance.groups_property_maintenance_worker')
        group_sale_only_doc = self.env.ref('sales_team.group_sale_salesman')
        group_sale_all_doc = self.env.ref('sales_team.group_sale_salesman_all_leads')
        other_group = group_equipment_manager + group_maintenance_manager + group_maintenance_worker + group_sale_only_doc + group_sale_all_doc
        if 'group_profile_id' in vals:
            val_group_profile_id = vals.get('group_profile_id')
            profile_group_ids = self.env['res.groups'].search([('is_profile_group', '=', True)])
            if val_group_profile_id:
                for gr_id in profile_group_ids:
                    if gr_id.id == val_group_profile_id:
                        gr_id.write({'users': [(4, self.id)]})
                        self.vip_user_type = gr_id.name.replace(" ", "").replace("Staff", "").replace("Manager", "").lower()
                        if gr_id.implied_ids:
                            for other_g in other_group:
                                if other_g not in gr_id.implied_ids and other_g.is_profile_group == False:
                                    other_g.write({'users': [(3, self.id)]})
                    else:
                        group_profile_id = self.env['res.groups'].browse(val_group_profile_id)
                        if gr_id in group_profile_id.implied_ids:
                            gr_id.write({'users': [(4, self.id)]})
                            self.vip_user_type = gr_id.name.replace(" ", "").replace("Staff", "").replace("Manager", "").lower()
                        else:
                            gr_id.write({'users': [(3, self.id)]})
            else:
                for gr_id in profile_group_ids:
                    gr_id.write({'users': [(3, self.id)]})
            exit_history_id = self.env['profile.group.history'].search([('user_id', '=', self.id)])
            if exit_history_id:
                exit_history_id.history_ids.create({
                    'group_id': val_group_profile_id if val_group_profile_id else False,
                    'history_id': exit_history_id.id
                })
            else:
                self.env['profile.group.history'].create({
                    'function_admin_user_id': self.env.user.id,
                    'user_id': self.id,
                    'history_ids': [(0, 0, {
                        'group_id': val_group_profile_id if val_group_profile_id else False})]
                })
        return res

    # def write(self, vals):
    #     if 'group_profile_id' in vals:
    #         if vals.get('group_profile_id'):
    #             vals['groups_id'] = [(6, 0, [vals['group_profile_id']])]
    #         else:
    #             vals['groups_id'] = [(6, 0, [self.env.ref('base.group_user').id])]
    #     return super(ResUsers, self).write(vals)
