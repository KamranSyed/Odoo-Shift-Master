# -*- coding: utf-8 -*-
# See LICENSE and COPYRIGHT files for full copyright and licensing details.

from odoo import models, fields, api

class ShiftCalendarAssignment(models.Model):
	_name = 'ksshiftmaster.shift_calendar_assignment'
	_description = 'Shift Calendar Assignment'

	dt	 			= fields.Date(required=True)
	shift_id		= fields.Integer(required=True)
	resource_id		= fields.Integer(required=True)

