from unittest import TestCase

from src.dominio.aluno.email import Email
from src.exceptions import InvalidEmailException


class EmailTest(TestCase):

    def test_must_not_allow_create_email_with_invalid_addresses(self):
        self.assertRaises(InvalidEmailException, Email, None)
        self.assertRaises(InvalidEmailException, Email, "")
        self.assertRaises(InvalidEmailException, Email, "invalid email")
