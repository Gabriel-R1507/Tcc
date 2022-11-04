from  passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def criptografar_senha(senha):
    return pwd_context.hash(senha)

def verificar_senha(senha, senhaC):
    return pwd_context.verify(senha, senhaC)