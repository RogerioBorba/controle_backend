import datetime

from controle.models import *
from hyper_resource.serializers import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from django.utils.dateparse import parse_datetime
from rest_framework.serializers import HyperlinkedRelatedField

class EnderecoSerializer(BusinessSerializer):
    pessoa = HyperlinkedRelatedField(view_name='controle:Pessoa_detail', many=False, read_only=True)
    class Meta:
        model = Endereco
        fields = ['complemento','cep','bairro','estado','cidade','oid','logradouro','numero','pessoa']
        identifier = 'oid'
        identifiers = ['pk', 'oid']

    def field_relationship_to_validate_dict(self):
        a_dict = {}
        a_dict['pessoa_id'] = 'pessoa'
        return a_dict

class EnderecoeletronicoSerializer(BusinessSerializer):
    pessoa = HyperlinkedRelatedField(view_name='controle:Pessoa_detail', many=False, read_only=True)
    class Meta:
        model = Enderecoeletronico
        fields = ['oid','mail','pessoa_nome','pessoa']
        identifier = 'oid'
        identifiers = ['pk', 'oid']

    def field_relationship_to_validate_dict(self):
        a_dict = {}
        a_dict['pessoa_id'] = 'pessoa'
        return a_dict

class GastoSerializer(BusinessSerializer):
    tipo_de_gasto = HyperlinkedRelatedField(view_name='controle:TipoGasto_detail', many=False, read_only=True)
    pessoa = HyperlinkedRelatedField(view_name='controle:Pessoa_detail', many=False, read_only=True)
    class Meta:
        model = Gasto
        fields = ['dataDoGasto','horaDoGasto' ,'tipo_de_gasto','pessoa','descricao','oid', 'valor', 'print_string']
        identifier = 'oid'
        identifiers = ['pk', 'oid']

    def field_relationship_to_validate_dict(self):
        a_dict = {}
        a_dict['tipo_de_gasto_id'] = 'tipo_de_gasto'
        a_dict['pessoa_id'] = 'pessoa'
        return a_dict

    def save_gasto_repetido(self, a_validated_data, qtd_repeticao):

        dt = parse_datetime(a_validated_data['data_do_gasto'])
        tp_de_gasto = a_validated_data['tipo_de_gasto_id']
        pessoa_id = a_validated_data['pessoa_id']
        desc = a_validated_data['descricao']
        vl = a_validated_data['valor']
        for i in range(1, qtd_repeticao):
            gasto = Gasto(data_do_gasto=dt +  datetime.timedelta(i*30), tipo_de_gasto_id=tp_de_gasto, pessoa_id=pessoa_id,descricao=desc, valor=vl)
            gasto.save()

    def create_or_update(self, instance, validated_data):

        dt_gasto = self.initial_data['dataDoGasto']
        if 'horaDoGasto' in  self.initial_data:
            tm_gasto = self.initial_data['horaDoGasto']
        else:
            tm_gasto ='00:00:00'
        data_do_gasto = dt_gasto +' ' + tm_gasto
        validated_data['data_do_gasto'] = data_do_gasto
        an_instance = super(GastoSerializer, self).create_or_update(instance, validated_data)

        if 'qtd_repeticao' in self.initial_data and int(self.initial_data['qtd_repeticao']) > 0:
            qtd = int(self.initial_data['qtd_repeticao']) + 1
            self.save_gasto_repetido(validated_data, qtd)

        return an_instance


class PessoaSerializer(BusinessSerializer):
    gastos = HyperlinkedRelatedField(view_name='controle:Gasto_detail', many=True, read_only=True)
    class Meta:
        model = Pessoa
        fields = ['gastos','data_de_nascimento','nome','tipo','oid', 'avatar']
        identifier = 'oid'
        identifiers = ['pk', 'oid']

class TelefoneSerializer(BusinessSerializer):
    tipo_de_gasto = HyperlinkedRelatedField(view_name='controle:TipoGasto_detail', many=False, read_only=True)
    pessoa = HyperlinkedRelatedField(view_name='controle:Pessoa_detail', many=False, read_only=True)
    class Meta:
        model = Telefone
        fields = ['nome','tipo_de_gasto','pessoa','observacao','codigo','numero','oid']
        identifier = 'oid'
        identifiers = ['pk', 'oid']

    def field_relationship_to_validate_dict(self):
        a_dict = {}
        a_dict['tipo_de_gasto_id'] = 'tipo_de_gasto'
        a_dict['pessoa_id'] = 'pessoa'
        return a_dict

class TipoGastoSerializer(BusinessSerializer):
    tipo_generico = HyperlinkedRelatedField(view_name='controle:TipoGasto_detail', many=False, read_only=True)
    class Meta:
        model = TipoGasto
        fields = ['descricao','oid','tipo_generico']
        identifier = 'oid'
        identifiers = ['pk', 'oid']

    def field_relationship_to_validate_dict(self):
        a_dict = {}
        a_dict['tipo_generico_id'] = 'tipo_generico'
        return a_dict



serializers_dict = {}