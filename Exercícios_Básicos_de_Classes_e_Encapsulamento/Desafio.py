# Crie uma classe VerificaCPF que possui um método da classe que verifica
# e valida um cpf retornando True caso seja um CPF válido e False para um CPF inválido

class VerificaCPF:
    def verificar(*args):
        cpf = []
        for i in args:
            cpf.append(i)
        z = 0
        count = 2
        for c in cpf:
            z += c * count
            count += 1
        cpf.append(11 - (z % 11)) if z % 11 >= 2 else cpf.append(0)
        x = 0
        countdown = 2
        for f in cpf:
            x += f * countdown
            countdown += 1
        cpf.append(11 - (x % 11)) if x % 11 >= 2 else cpf.append(0)
        print(cpf)


cpf = VerificaCPF()
cpf.verificar(1, 1, 1, 4, 4, 4, 7, 7, 7)
