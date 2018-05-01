from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from controle import views 


app_name="controle"

urlpatterns = format_suffix_patterns((
    url(r'^$', views.APIRoot.as_view(), name='api_root'),

    url(r'^endereco-list/(?P<pk>[0-9]+)/$', views.EnderecoDetail.as_view(), name='Endereco_detail'),
    url(r'^endereco-list/(?P<pk>[0-9]+)/(?P<attributes_functions>.*)/$', views.EnderecoDetail.as_view(), name='Endereco_detail_af'),
    url(r'^endereco-list/$', views.EnderecoList.as_view(), name='Endereco_list'),
    url(r'^endereco-list/(?P<attributes_functions>.*)/?$', views.EnderecoList.as_view(), name='Endereco_list_af'),

    url(r'^enderecoeletronico-list/(?P<pk>[0-9]+)/$', views.EnderecoeletronicoDetail.as_view(), name='Enderecoeletronico_detail'),
    url(r'^enderecoeletronico-list/(?P<pk>[0-9]+)/(?P<attributes_functions>.*)/$', views.EnderecoeletronicoDetail.as_view(), name='Enderecoeletronico_detail_af'),
    url(r'^enderecoeletronico-list/$', views.EnderecoeletronicoList.as_view(), name='Enderecoeletronico_list'),
    url(r'^enderecoeletronico-list/(?P<attributes_functions>.*)/?$', views.EnderecoeletronicoList.as_view(), name='Enderecoeletronico_list_af'),

    url(r'^gasto-list/(?P<pk>[0-9]+)/$', views.GastoDetail.as_view(), name='Gasto_detail'),
    url(r'^gasto-list/(?P<pk>[0-9]+)/(?P<attributes_functions>.*)/$', views.GastoDetail.as_view(), name='Gasto_detail_af'),
    url(r'^gasto-list/$', views.GastoList.as_view(), name='Gasto_list'),
    url(r'^gasto-list/(?P<attributes_functions>.*)/?$', views.GastoList.as_view(), name='Gasto_list_af'),

    url(r'^pessoa-list/(?P<pk>[0-9]+)/$', views.PessoaDetail.as_view(), name='Pessoa_detail'),
    url(r'^pessoa-list/(?P<pk>[0-9]+)/(?P<attributes_functions>.*)/$', views.PessoaDetail.as_view(), name='Pessoa_detail_af'),
    url(r'^pessoa-list/register/$', views.PessoaRegister.as_view(), name='Pessoa_register'),
    url(r'^pessoa-list/login/$', views.PessoaLogin.as_view(), name='Pessoa_login'),
    url(r'^pessoa-list/$', views.PessoaList.as_view(), name='Pessoa_list'),
    #url(r'^pessoa-list/(?P<attributes_functions>.*)/?$', views.PessoaList.as_view(), name='Pessoa_list_af'),

    url(r'^telefone-list/(?P<pk>[0-9]+)/$', views.TelefoneDetail.as_view(), name='Telefone_detail'),
    url(r'^telefone-list/(?P<pk>[0-9]+)/(?P<attributes_functions>.*)/$', views.TelefoneDetail.as_view(), name='Telefone_detail_af'),
    url(r'^telefone-list/$', views.TelefoneList.as_view(), name='Telefone_list'),
    url(r'^telefone-list/(?P<attributes_functions>.*)/?$', views.TelefoneList.as_view(), name='Telefone_list_af'),

    url(r'^tipo-gasto-list/(?P<pk>[0-9]+)/$', views.TipoGastoDetail.as_view(), name='TipoGasto_detail'),
    url(r'^tipo-gasto-list/(?P<pk>[0-9]+)/(?P<attributes_functions>.*)/$', views.TipoGastoDetail.as_view(), name='TipoGasto_detail_af'),
    url(r'^tipo-gasto-list/$', views.TipoGastoList.as_view(), name='TipoGasto_list'),
    url(r'^tipo-gasto-list/(?P<attributes_functions>.*)/?$', views.TipoGastoList.as_view(), name='TipoGasto_list_af'),


))
