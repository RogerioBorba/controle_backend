from collections import OrderedDict
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from hyper_resource.views import *
from controle.models import *
from controle.serializers import *
from controle.contexts import *

def get_root_response(request):
    format = None
    root_links = {

      'endereco-list': reverse('controle:Endereco_list' , request=request, format=format),
      'enderecoeletronico-list': reverse('controle:Enderecoeletronico_list' , request=request, format=format),
      'gasto-list': reverse('controle:Gasto_list' , request=request, format=format),
      'pessoa-list': reverse('controle:Pessoa_list' , request=request, format=format),
      'telefone-list': reverse('controle:Telefone_list' , request=request, format=format),
      'tipo-gasto-list': reverse('controle:TipoGasto_list' , request=request, format=format),
    }

    ordered_dict_of_link = OrderedDict(sorted(root_links.items(), key=lambda t: t[0]))
    return ordered_dict_of_link

class APIRoot(APIView):

    def __init__(self):
        super(APIRoot, self).__init__()
        self.base_context = BaseContext('api-root')

    def options(self, request, *args, **kwargs):
        context = self.base_context.getContextData(request)
        root_links = get_root_response(request)
        context.update(root_links)
        response = Response(context, status=status.HTTP_200_OK, content_type="application/ld+json")
        response = self.base_context.addContext(request, response)
        return response

    def get(self, request, *args, **kwargs):
        root_links = get_root_response(request)
        response = Response(root_links)
        return self.base_context.addContext(request, response)

class EnderecoList(CollectionResource):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    contextclassname = 'endereco-list'
    def initialize_context(self):
        self.context_resource = EnderecoListContext()
        self.context_resource.resource = self

class EnderecoDetail(NonSpatialResource):
    serializer_class = EnderecoSerializer
    contextclassname = 'endereco-list'
    def initialize_context(self):
        self.context_resource = EnderecoDetailContext()
        self.context_resource.resource = self

class EnderecoeletronicoList(CollectionResource):
    queryset = Enderecoeletronico.objects.all()
    serializer_class = EnderecoeletronicoSerializer
    contextclassname = 'enderecoeletronico-list'
    def initialize_context(self):
        self.context_resource = EnderecoeletronicoListContext()
        self.context_resource.resource = self

class EnderecoeletronicoDetail(NonSpatialResource):
    serializer_class = EnderecoeletronicoSerializer
    contextclassname = 'enderecoeletronico-list'
    def initialize_context(self):
        self.context_resource = EnderecoeletronicoDetailContext()
        self.context_resource.resource = self

class GastoList(CollectionResource):
    queryset = Gasto.objects.all()
    serializer_class = GastoSerializer
    contextclassname = 'gasto-list'
    def initialize_context(self):
        self.context_resource = GastoListContext()
        self.context_resource.resource = self

class GastoDetail(NonSpatialResource):
    serializer_class = GastoSerializer
    contextclassname = 'gasto-list'
    def initialize_context(self):
        self.context_resource = GastoDetailContext()
        self.context_resource.resource = self

class PessoaList(CollectionResource):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    contextclassname = 'pessoa-list'
    def initialize_context(self):
        self.context_resource = PessoaListContext()
        self.context_resource.resource = self

class PessoaRegister(CollectionResource):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    contextclassname = 'pessoa-list'
    def initialize_context(self):
        self.context_resource = PessoaListContext()
        self.context_resource.resource = self

    def post(self, request, *args, **kwargs):
        #print(request)
        resp = super(PessoaRegister, self).post(request, *args, **kwargs)
        resp['x-access-token'] = self.object_model.getToken()
        resp['content-location'] = request.build_absolute_uri()[:-9] + str(self.object_model.oid) + '/'
        return resp

class PessoaLogin(CollectionResource):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    contextclassname = 'pessoa-list'
    def initialize_context(self):
        self.context_resource = PessoaListContext()
        self.context_resource.resource = self

    def post(self, request, *args, **kwargs):

        res = Pessoa.getOneOrNone(request.data['nome'], request.data['senha'])

        if res is None:
            res = Response(status=status.HTTP_401_UNAUTHORIZED, content_type='application/json')
            res['WWW-Authenticate'] = 'Bearer'
            return res

        response = Response(status=status.HTTP_201_CREATED, content_type='application/json')
        self.add_base_headers(request, response)
        response['Content-Location'] = request.build_absolute_uri()[:-6] + str(res.oid) + '/'
        response['x-access-token'] = res.getToken()
        return response

class PessoaDetail(NonSpatialResource):
    serializer_class = PessoaSerializer
    contextclassname = 'pessoa-list'
    def initialize_context(self):
        self.context_resource = PessoaDetailContext()
        self.context_resource.resource = self

class TelefoneList(CollectionResource):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerializer
    contextclassname = 'telefone-list'
    def initialize_context(self):
        self.context_resource = TelefoneListContext()
        self.context_resource.resource = self

class TelefoneDetail(NonSpatialResource):
    serializer_class = TelefoneSerializer
    contextclassname = 'telefone-list'
    def initialize_context(self):
        self.context_resource = TelefoneDetailContext()
        self.context_resource.resource = self

class TipoGastoList(CollectionResource):
    queryset = TipoGasto.objects.all()
    serializer_class = TipoGastoSerializer
    contextclassname = 'tipo-gasto-list'
    def initialize_context(self):
        self.context_resource = TipoGastoListContext()
        self.context_resource.resource = self

class TipoGastoDetail(NonSpatialResource):
    serializer_class = TipoGastoSerializer
    contextclassname = 'tipo-gasto-list'
    def initialize_context(self):
        self.context_resource = TipoGastoDetailContext()
        self.context_resource.resource = self

