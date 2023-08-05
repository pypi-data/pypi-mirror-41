
import os
import json
import unicodedata
import re

from glob import iglob
from decimal import Decimal
from collections import OrderedDict
from cnab240 import errors


class CampoBase(object):
    def __init__(self):
        self._valor = None

    def _normalize_str(self, string):
        """
        Remove special characters and strip spaces
        """
        if string:
            if not isinstance(string, str):
                string = str(string, 'utf-8', 'replace')

            return unicodedata.normalize('NFKD', string).encode(
                'ASCII', 'ignore').decode('ASCII')
        return ''

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):

        if self.formato == 'alfa':
            if not isinstance(valor, str):
                print("{0} - {1}".format(self.nome, valor))
                raise errors.TipoError(self, valor)

            valor = self._normalize_str(valor)

            if len(valor) > self.digitos:
                print("truncating - {0}".format(self.nome))
                # reduz o len(valor)
                cortar = len(valor) - self.digitos
                valor = valor[:-(cortar)]

        elif self.decimais:
            if not isinstance(valor, Decimal):
                print("{0} - {1}".format(self.nome, valor))
                raise errors.TipoError(self, valor)

            num_decimais = valor.as_tuple().exponent * -1
            if num_decimais != self.decimais:
                print("{0} - {1}".format(self.nome, valor))
                raise errors.NumDecimaisError(self, valor)

            if len(str(valor).replace('.', '')) > self.digitos:
                print("{0} - {1}".format(self.nome, valor))
                raise errors.NumDigitosExcedidoError(self, valor)

        else:
            if not isinstance(valor, int):
                print("{0} - {1}".format(self.nome, valor))
                raise errors.TipoError(self, valor)
            if len(str(valor)) > self.digitos:
                print("{0} - {1}".format(self.nome, valor))
                raise errors.NumDigitosExcedidoError(self, valor)

        self._valor = valor

    def __str__(self):

        if self.valor is None:
            if self.default is not None:
                if self.decimais:
                    self.valor = Decimal(
                        '{0:0.{1}f}'.format(self.default,
                                            self.decimais)
                    )
                else:
                    self.valor = self.default
            elif (self.default is None) & (self.valor is None):
                if self.decimais or self.formato == 'num':
                    self.valor = 0
                else:
                    self.valor = ''
            else:
                raise errors.CampoObrigatorioError(self.nome)

        if self.formato == 'alfa' or self.decimais:
            if self.decimais:
                valor = str(self.valor).replace('.', '')
                chars_faltantes = self.digitos - len(valor)
                return ('0' * chars_faltantes) + valor
            else:
                valor = self.valor
                chars_faltantes = self.digitos - len(valor)
                return valor + (' ' * chars_faltantes)

        return '{0:0{1}d}'.format(self.valor, self.digitos)

    def __repr__(self):
        return str(self)

    def __set__(self, instance, value):
        self.valor = value

    def __get__(self, instance, owner):
        return self.valor


def criar_classe_campo(spec):

    nome = spec.get('nome')
    inicio = spec.get('posicao_inicio') - 1
    fim = spec.get('posicao_fim')

    attrs = {
        'nome': nome,
        'inicio': inicio,
        'fim': fim,
        'digitos': fim - inicio,
        'formato': spec.get('formato', 'alfa'),
        'decimais': spec.get('decimais', 0),
        'default': spec.get('default'),
        'ignore': spec.get('ignore', False),
    }

    return type(nome, (CampoBase,), attrs)


class RegistroBase(object):

    def __new__(cls, **kwargs):
        campos = OrderedDict()
        attrs = {'_campos': campos}

        for Campo in list(cls._campos_cls.values()):
            campo = Campo()
            campos.update({campo.nome: campo})
            attrs.update({campo.nome: campo})

        new_cls = type(cls.__name__, (cls, ), attrs)
        return super(RegistroBase, cls).__new__(new_cls)

    def __init__(self, **kwargs):
        self.fromdict(kwargs)

    def necessario(self):
        for campo in list(self._campos.values()):
            eh_controle = campo.nome.startswith('controle_') or campo.nome.startswith('servico_')
            if not eh_controle and campo.valor is not None:
                return True

        return False

    def todict(self):
        data_dict = dict()
        for campo in list(self._campos.values()):
            if campo.valor is not None:
                data_dict[campo.nome] = campo.valor
        return data_dict

    def fromdict(self, data_dict):
        ignore_fields = lambda key: any((
            key.startswith('vazio'),
            key.startswith('servico_'),
            key.startswith('controle_'),
        ))

        for key, value in list(data_dict.items()):
            if hasattr(self, key) and not ignore_fields(key):
                setattr(self, key, value)

    def carregar(self, registro_str):
        for campo in list(self._campos.values()):
            valor = registro_str[campo.inicio:campo.fim].strip()
            if campo.decimais:
                exponente = campo.decimais * -1
                dec = valor[:exponente] + '.' + valor[exponente:]
                campo.valor = Decimal(dec)

            elif campo.formato == 'num':
                try:
                    campo.valor = int(valor)
                except ValueError:
                    if campo.ignore:
                        campo.valor = 0
                        continue
                    raise errors.TipoError(campo, valor)
            else:
                campo.valor = valor

    def __str__(self):
        return ''.join([str(campo) for campo in list(self._campos.values())])


class Registros(object):
    def __init__(self, specs_dirpath):
        # TODO: Validar spec: nome (deve ser unico para cada registro),
        #   posicao_inicio, posicao_fim, formato (alpha), decimais (0),
        #   default (zeros se numerico ou brancos se alfa)
        registro_filepath_list = iglob(os.path.join(specs_dirpath, '*.json'))

        for registro_filepath in registro_filepath_list:
            registro_file = open(registro_filepath)
            spec = json.load(registro_file)
            registro_file.close()

            setattr(self, spec.get('nome'), self.criar_classe_registro(spec))

    def criar_classe_registro(self, spec):
        campos = OrderedDict()
        attrs = {'_campos_cls': campos}
        cls_name = spec.get('nome')

        campo_specs = spec.get('campos', {})
        for key in sorted(campo_specs.keys()):
            Campo = criar_classe_campo(campo_specs[key])
            entrada = {Campo.nome: Campo}

            campos.update(entrada)

        return type(cls_name, (RegistroBase, ), attrs)
