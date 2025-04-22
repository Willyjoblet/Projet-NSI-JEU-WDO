# -*- coding: utf-8 -*-
import mysql.connector

mydb = mysql.connector.connect(
    host = '0504-srv-sig',
    database = 'nsi_eleve8',
    user = 'nsi_eleve8',
    password = 'eleve8'
)

print(mydb)

class Batiment:

    def __int__(self,nom,point_de_vie):
        """constructeur"""
        self.nom=nom
        self.point_de_vie=point_de_vie

    def set_points_vie(self,nouvelle_valeur):
        """mutateur ou setter qui permet de modifier la valeur de l'attribut points_vie"""
        self.__points_vie=int(nouvelle_valeur)

    def get_points_vie(self):
        """accesseur ou getter qui permet de recuperer la valeur de l'attribut points_vie"""
        return self.__points_vie

    def __str__(self):
        return( self.__nom + " PV:" + str(self.__points_vie))

class Carte:

    def __int__(self,nom,type,degats,protection):
        """constructeur"""
        self.nom=nom
        self.type=type
        self.degats=degats
        self.protection=protection
