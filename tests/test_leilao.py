from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao


class TestAvaliador(TestCase):

    def setUp(self):
        self.gui = Usuario('Gui', 500.0)
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao('Celular')

    def este_teste_deve_retornar_o_maior_e_o_menor_valores_de_um_lance_quando_adicionandos_em_ordem_crescente(self):
        yuri = Usuario('Yuri', 500.0)
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def teste_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(ValueError):
            yuri = Usuario('Yuri', 500.0)
            lance_do_yuri = Lance(yuri, 100.0)

            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_yuri)

            # menor_valor_esperado = 100.0
            # maior_valor_esperado = 150.0
            #
            # self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
            # self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def teste_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_lances_quando_o_leilao_tiver_apenas_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def este_teste_deve_retornar_o_maior_e_o_menor_valores_quando_o_leilao_tiver_tres_lances(self):
        yuri = Usuario('Yuri', 500.0)
        lance_do_yuri = Lance(yuri, 100.0)
        vini = Usuario('Vini', 500.0)

        lance_do_vini = Lance(vini, 200.0)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # se o leilão não tiver lances, deve permitir propor um lance
    def teste_deve_permitir_propor_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_gui)

        quantidade_de_lances_recebida = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebida)

    # se o ultimo usuario for diferente, deve permitir propor um lance
    def teste_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('Yuri', 500.0)
        lance_do_yuri = Lance(yuri, 200.0)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        quantidade_de_lances_recebida = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebida)

    # se o ultimo usuario for o mesmo, não deve permtir propor um lance
    def teste_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_gui200 = Lance(self.gui, 200.0)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui200)
        # try:
        #     self.leilao.propoe(self.lance_do_gui)
        #     self.leilao.propoe(lance_do_gui200)
        #     self.fail(msg='Não lançou exceção')
        # except ValueError:
        #     quantidade_de_lances_recebida = len(self.leilao.lances)
        #     self.assertEqual(1, quantidade_de_lances_recebida)