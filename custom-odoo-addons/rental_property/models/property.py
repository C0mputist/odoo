from odoo import api, fields, models

class RentalProperty(models.Model):
    _name = "rental.property"
    _description = "Rental Property"

    name = fields.Char(string='Name', required=True)
    full_address = fields.Char(string='Full Address', required=True)
    building_number = fields.Char(string='Building Number')
    street_name = fields.Char(string='Street Name')
    city = fields.Char(string='City')
    district = fields.Char(string='District')
    postal_code = fields.Char(string='Postal Code')
    bedrooms = fields.Integer(string='Bedrooms', required=True)
    bathrooms = fields.Integer(string='Bathrooms', required=True)
    rental_price = fields.Float(string='Rental Price', required=True)
    description = fields.Text(string='Description')
    availability = fields.Boolean(string='Availability', default=True)
    property_type = fields.Selection([('apartment', 'Apartment'), ('shop', 'Shop'), ('warehouse', 'Warehouse'),
                                      ('office', 'Office')], string='Property Type', required=True)
    # tenants = fields.Many2many('my_module.tenant', string='Tenants')
    # tenant_history = fields.Text(string='Tenant History')
    # property_owner = fields.Many2one('my_module.partner', string='Property Owner', domain="[('is_company','=',True)]")
    # tenant_history = fields.Text(string='Tenant History')
    # google_maps_url = fields.Char(string='Google Maps URL', compute='_compute_google_maps_url')