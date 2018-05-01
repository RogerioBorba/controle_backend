# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import base64

import jwt
from hyper_resource.models import FeatureModel, BusinessModel
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from controle_backend.settings import SECRET_KEY
from django.contrib.gis.db import models

class Pessoa(BusinessModel):
    data_de_nascimento = models.TextField(blank=True, null=True)
    nome = models.TextField(blank=True, null=True)
    senha = models.TextField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    oid = models.AutoField(primary_key=True)
    avatar = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Pessoa'

    @classmethod
    def jwt_algorithm(cls):
        return 'HS256'

    @classmethod
    def getOneOrNone(cls, a_user_name, password):
        return Pessoa.objects.filter(nome=a_user_name, senha=password).first()

    def getToken(self):
        encoded = jwt.encode({'oid': self.oid, 'nome': self.nome}, SECRET_KEY,  algorithm=Pessoa.jwt_algorithm())
        return encoded

    @classmethod
    def login(cls, user_name, password):
        user = Pessoa.getOneOrNone(user_name, password)
        if user is None:
            return None
        a_dict = {}
        a_dict['id'] = user.id
        a_dict['nome'] = user.nome
        a_dict['avatar'] = user.avatar
        a_dict['token'] = user_name.getToken()
        return a_dict

    @classmethod
    def token_is_ok(cls, a_token):
        try:
            payload = jwt.decode(a_token, SECRET_KEY, algorithm=Pessoa.jwt_algorithm())
            return True
        except jwt.InvalidTokenError:
            return False

    def encodeField(self, a_field):
        return base64.b64encode(a_field.encode())

    def decodeField(self, a_field):
        return base64.b64decode(a_field.encode())

class Endereco(BusinessModel):
    complemento = models.TextField(blank=True, null=True)
    cep = models.TextField(blank=True, null=True)
    bairro = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    cidade = models.TextField(blank=True, null=True)
    oid = models.AutoField(primary_key=True)
    logradouro = models.TextField(blank=True, null=True)
    numero = models.TextField(blank=True, null=True)
    pessoa = models.ForeignKey(Pessoa, db_column='pessoa_oid', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'Endereco'


class Enderecoeletronico(BusinessModel):
    oid = models.AutoField(primary_key=True)
    mail = models.TextField(blank=True, null=True)
    pessoa_nome = models.TextField(db_column='Pessoa_nome', blank=True, null=True)  # Field name made lowercase.
    pessoa = models.ForeignKey(Pessoa, db_column='pessoa_oid', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        managed = False
        db_table = 'EnderecoEletronico'

class TipoGasto(BusinessModel):
        descricao = models.TextField(blank=True, null=True)
        oid = models.AutoField(primary_key=True)
        tipo_generico = models.ForeignKey('self', db_column='oid_parent', blank=True, null=True, on_delete=models.SET_NULL)
        class Meta:
            managed = False
            db_table = 'TipoDeGasto'


# Unable to inspect table 'Gasto'
class Gasto(BusinessModel):
    data_do_gasto = models.DateTimeField(blank=True, null=True)
    tipo_de_gasto = models.ForeignKey(TipoGasto, db_column='tipo_de_gasto_oid', blank=True, null=True, on_delete=models.SET_NULL)
    pessoa = models.ForeignKey(Pessoa, db_column='pessoa_oid', blank=True, null=True, related_name='gastos', on_delete=models.SET_NULL)
    valor = models.FloatField()
    descricao = models.TextField(blank=True, null=True)
    oid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'gasto'

    def print_string(self):

        vl = str(self.valor) if self.valor else '0'
        if self.tipo_de_gasto is None:
            return ' Tipo de gasto não informado: ' + vl

        tp_gasto = self.tipo_de_gasto.descricao
        return tp_gasto + ' : ' + vl

    def dataDoGasto(self):
        if self.data_do_gasto is not None:
            return self.data_do_gasto.date()
    def horaDoGasto(self):
        if self.data_do_gasto is not None:
            return self.data_do_gasto.time()

    def __repr__(self):
        return self.print_string()

    def __str__(self):
        return self.print_string()


# The error was: list index out of range

# Unable to inspect table 'Telefone'
class Telefone(BusinessModel):

    pessoa = models.ForeignKey(Pessoa, db_column='pessoa_oid', blank=True, null=True, on_delete=models.SET_NULL)
    observacao = models.TextField(blank=True, null=True)
    codigo = models.TextField(blank=True, null=True)
    numero = models.TextField(blank=True, null=True)
    oid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'telefone'



# The error was: list index out of range



