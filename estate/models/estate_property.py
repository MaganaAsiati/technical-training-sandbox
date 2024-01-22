
from odoo import fields, models
from datetime import datetime, timedelta

class estate_property(models.Model):
    _name = "estate.property"
    _description = "estate property"

    
    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(string='Availability Date', copy=False, default=lambda self: (datetime.now() + timedelta(days=90)).date())
    expected_price = fields.Float(required=True)
    selling_price  = fields.Float(string='Selling Price', readonly=True)
    bedrooms = fields.Integer(string='Number of Bedrooms', default=2)
    living_area=  fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    active  = fields.Boolean(default=False)
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='garden_orientation',
        selection=[
        ('north', 'North'),
        ('south', 'South'), 
        ('east', 'East'),
         ('west', 'West')],)
    state = fields.Selection(
            string='state',
            default='new', 
            required=True,
            copy=False,
            selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled')],)

    