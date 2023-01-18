import pandas as pd

df = pd.read_excel("../../pdfs/VESTUNB_23.xlsx")

Nome = "Agronomia (Bacharelado)" #nome que deseja pesquisar
Vazia = "Unnamed: 0" #nome da coluna vazia

#filtra apenas os diurnos
linha_diurno = df.loc[(df[0] == Nome) & (df[Vazia] <= 71)]
if linha_diurno.shape[0] != 0:
    indice_linha_curso_diurno = linha_diurno.index[0]
    
    vagas_cotas_negros_diurno = df.at[indice_linha_curso_diurno, 1]
    inscritos_cotas_negros_diurno = df.at[indice_linha_curso_diurno, 2]
    
    vagas_cotas_escolaPublica_negros_def_rendaInf_diurno = df.at[indice_linha_curso_diurno, 4]
    inscritos_cotas_escolaPublica_negros_def_rendaInf_diurno = df.at[indice_linha_curso_diurno, 5]

    vagas_cotas_escolaPublica_negros_rendaInf_diurno = df.at[indice_linha_curso_diurno, 7]
    inscritos_cotas_escolaPublica_negros_rendaInf_diurno = df.at[indice_linha_curso_diurno, 8]

    vagas_cotas_escolaPublica_negros_def_rendaSup_diurno = df.at[indice_linha_curso_diurno, 10]
    inscritos_cotas_escolaPublica_negros_def_rendaSup_diurno = df.at[indice_linha_curso_diurno, 11]
    
    vagas_cotas_escolaPublica_negros_rendaSup_diurno = df.at[indice_linha_curso_diurno, 13]
    inscritos_cotas_escolaPublica_negros_rendaSup_diurno = df.at[indice_linha_curso_diurno, 14]

    vagas_cotas_escolaPublica_def_rendaInf_diurno = df.at[indice_linha_curso_diurno, 16]
    inscritos_cotas_escolaPublica_def_rendaInf_diurno = df.at[indice_linha_curso_diurno, 17]
    
    vagas_cotas_escolaPublica_rendaInf_diurno = df.at[indice_linha_curso_diurno, 19]
    inscritos_cotas_escolaPublica_rendaInf_diurno = df.at[indice_linha_curso_diurno, 20]

    vagas_cotas_escolaPublica_def_rendaSup_diurno = df.at[indice_linha_curso_diurno, 22]
    inscritos_cotas_escolaPublica_def_rendaSup_diurno = df.at[indice_linha_curso_diurno, 23]
    
    vagas_cotas_escolaPublica_rendaSup_diurno = df.at[indice_linha_curso_diurno, 25]
    inscritos_cotas_escolaPublica_rendaSup_diurno = df.at[indice_linha_curso_diurno, 26]

    vagas_universais_diurno = df.at[indice_linha_curso_diurno, 28]
    inscritos_universais_diurno = df.at[indice_linha_curso_diurno, 29]

    



#filtra apenas os noturnos
linha_noturno = df.loc[(df[0] == Nome) & (df[Vazia] > 71)]
if linha_noturno.shape[0] != 0:
    indice_linha_curso_noturno = linha_noturno.index[0]
    vagas_cotas_negros_noturno = df.at[indice_linha_curso_noturno, 1]
    inscritos_cotas_negros_noturno = df.at[indice_linha_curso_noturno, 2]

    


print(vagas_cotas_negros_diurno)
print(inscritos_cotas_negros_diurno)