curso_a = {("Ana", 101),("Carlos", 102),('João', 103)}
curso_b = {("João",103),("Marina",104),("Carlos", 102)}
Aluno_A = curso_a - curso_b
Aluno_B = curso_b - curso_a
cursoAB = curso_a & curso_b

def exclusivo_A():
    print('Exclusivo do Curso A:')
    for aluno, matricula in Aluno_A:
        print(f'{aluno} ({matricula})')
    
def exclusivo_B():
    print('Exclusivo do Curso B:')
    for aluno, matricula in Aluno_B:
        print(f'{aluno} ({matricula})')

def cursosAB():
    print('Matriculados nos dois cursos:')
    for aluno, matricula in cursoAB:
        print(f'{aluno} ({matricula})')

def Programa():

    exclusivo_A()
    exclusivo_B()
    cursosAB()

Programa()