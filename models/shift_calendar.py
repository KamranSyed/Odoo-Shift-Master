# -*- coding: utf-8 -*-
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import models, fields, api

class ShiftCalendar(models.Model):
	_name = 'ksshiftmaster.shiftcalendar'
	_description = 'Shift Calendar'

	dt	 			= fields.Date(required=True)
	workplace		= fields.Many2one('ksworkplace.workplace', string="Workplace", required=True)
	shifts			= fields.Many2many('ksshiftmaster.shift', string='Shifts', required=True)
