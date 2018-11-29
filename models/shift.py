# -*- coding: utf-8 -*-
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import models, fields, api

class Shift(models.Model):
	_name = 'ksshiftmaster.shift'
	_description = 'Duty Shift'

	name 			= fields.Char(required=True)
	description 	= fields.Char()
	workplace		= fields.Many2one('ksworkplace.workplace', string="Workplace")

	active			= fields.Boolean('Active?', default=True)
