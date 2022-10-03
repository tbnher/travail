from odoo import api, fields, models

class Joueur(models.Model):
    _name = "joueur"
    _description = "Joueur de Futsal"

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    level = fields.Selection([('junior','Junior'),('adult','Adult')],string='Niveau')
    gender = fields.Selection([('homme','Homme'),('femme','Femme')],string='Genre')