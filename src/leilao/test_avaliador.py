from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.dominio import Avaliador


class TestAvaliador(TestCase):

    def setUp(self):
        self.gui = Usuario('Gui')
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao('Celular')

    def este_teste_deve_retornar_o_maior_e_o_menor_valores_de_um_lance_quando_adicionandos_em_ordem_crescente(self):
        yuri = Usuario('Yuri')
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.lances.append(lance_do_yuri)
        self.leilao.lances.append(self.lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def este_teste_deve_retornar_o_maior_e_o_menor_valores_de_um_lance_quando_adicionandos_em_ordem_decrescente(self):
        yuri = Usuario('Yuri')
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.lances.append(self.lance_do_gui)
        self.leilao.lances.append(lance_do_yuri)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def teste_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_lances_quando_o_leilao_tiver_apenas_um_lance(self):
        self.leilao.lances.append(self.lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(150.0, avaliador.menor_lance)
        self.assertEqual(150.0, avaliador.maior_lance)

    def este_teste_deve_retornar_o_maior_e_o_menor_valores_quando_o_leilao_tiver_tres_lances(self):
        yuri = Usuario('Yuri')
        lance_do_yuri = Lance(yuri, 100.0)
        vini = Usuario('Vini')

        lance_do_vini = Lance(vini, 200.0)

        leilao = Leilao('Celular')

        leilao.lances.append(self.lance_do_gui)
        leilao.lances.append(lance_do_yuri)
        leilao.lances.append(lance_do_vini)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
