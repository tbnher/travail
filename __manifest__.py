# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Futsal Management',
    'version': '1.0',
    'category': 'Sports',
    'author': 'Nathan Fontaine',
    'summary': 'Gestion Futsal',
    'sequence': -100,
    'description':"""Système de gestion de Futsal""",
    'depends': [],
    'data' : ["views/menu.xml",
              "views/menu_calendrier.xml",
              "views/menu_carriere.xml",
              "views/menu_club.xml",
              "views/menu_contrats.xml",
              "views/menu_effectif.xml",
              "views/menu_entrainement.xml",
              "views/menu_equipe.xml",
              "views/menu_extra.xml",
              "views/menu_finances.xml",
              "views/menu_forum.xml",
              "views/menu_jouer.xml",
              "views/menu_juniors.xml",
              "views/menu_saison.xml",
              "views/menu_stats.xml",
              "views/menu_structures.xml",
              "views/menu_transferts.xml",
              "views/menu_palmares.xml",
              ],
    'demo' : [],
    'application' : True,
    'auto_install' : False,
    'license' : 'LGPL-3',
}
