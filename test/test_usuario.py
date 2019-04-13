import unittest

from backend.usuario.usuario import Usuario


class UsuarioTest(unittest.TestCase):
    def test_generar_apodo(self):
        # Arrange
        usuario = Usuario('Alan Cristopher', 'Suarez Suarez', 'alanss2907@gmail.com', 'GG:v')
        # Act
        actual = usuario.obtener_apodo()
        # Assert
        expectativa = 'AlanSuarez'
        self.assertEqual(expectativa, actual)


if __name__ == '__main__':
    unittest.main()
