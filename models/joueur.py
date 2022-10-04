from odoo import api, fields, models

class Joueur(models.Model):
    _name = "futsal.joueur"
    _description = "Joueur de Futsal"

    name = fields.Char(string='Name')
    familyname = fields.Char(string='FamilyName')
    age = fields.Integer(string='Age')
    level = fields.Selection([('junior','Junior'),('adulte','Adulte')],string='Niveau')
    gender = fields.Selection([('homme  ','m'),('femme','f')],string='Genre')
    attaque = fields.Integer(String='Attaque')
    defense = fields.Integer(String='Défense')
    physique = fields.Integer(String='Physique')
    technique = fields.Integer(String='Technique')
    endurance = fields.Integer(String='Endurance')
    forme = fields.Integer(String='Forme')

