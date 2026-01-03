from odoo import models, fields

class TpObjetPerdu(models.Model):
    _name = "tp.objet.perdu"
    _description = "Objet perdu"

    name = fields.Char(string="Nom de l'objet", required=True)
    type_objet = fields.Selection([
        ("electronique", "Électronique"),
        ("vetement", "Vêtement"),
        ("document", "Document"),
        ("autre", "Autre"),
    ], string="Type d'objet", default="autre")

    date_perte = fields.Date(string="Date de perte")
    lieu_perte = fields.Char(string="Lieu de perte")
    statut = fields.Selection([
        ("declare", "Déclaré"),
        ("retrouve", "Retrouvé"),
        ("restitue", "Restitué"),
    ], string="Statut", default="declare")

    description = fields.Text(string="Description")
