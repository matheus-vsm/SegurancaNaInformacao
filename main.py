# Atividade 2 - Função Hash
# Bruno Umeoka Higuti - R.A: 22.121.082-6 
# Gabriel de Almeida Gava - R.A: 22.121.079-2 
# Guilherme Bizon Jeronymo - R.A: 22.121.128-7 
# Matheus Venâncio Scomparim - R.A: 22.121.063-6 
# Gustavo Leite Bueno de Oliveira - R.A: 22.121.057-8

import hashlib

frases = [
    {
        "texto": "A primeira das instituições criadas pelo Pe. Roberto Sabóia de Medeiros foi a antiga Escola Superior de Administração de Negócios de São Paulo - ESAN/SP.",
        "sha256": "d24de3ec3835115c576a55188a31761b73af93ed2c45a171c810bb66b24b08f9",
        "md5": "c850e1a34a6ed572e0758ccd9c615bda"
    },
    {
        "texto": "A FEI é uma instituição vinculada estatutariamente à Companhia de Jesus",
        "sha256": "6979a3d7a19e5921ae00ca7db9b814e1b83831dcedfca33dbb72e761ca084337",
        "md5": "b710771da8d7521524f45233ea9dd9e1"
    },
    {
        "texto": "Em 20 de janeiro de 1951 foi realizada a sessão solene da congregação para a Colação de Grau da primeira turma da Faculdade de Engenharia Industrial.",
        "sha256": "6c582a993ba3ea454f11221a374878e534cfe666060c87ba03127de07f1ca4e6",
        "md5": "55748c2cb669a9d9508677cb914cb025"
    },
    {
        "texto": "A Capela Santo Inácio de Loyola foi construída no ano de 1978, em concreto aparente.",
        "sha256": "254e695d0f8835651bc231f9cf1b2a7a097b849648f05f79f1855a55f85b089e",
        "md5": "f4a8a299fd4da2a5d70b374be2e48147"
    },
    {
        "texto": "Tendo como função principal a promoção do aprimoramento profissional no campo administrativo e tecnológico, o IECAT (Instituto de Especialização em Ciências Administrativas e Tecnológicas) foi criado em 1982",
        "sha256": "d2150d688c337fc57e235adafd57f86d7aba0b8682c249b1006ba592706f88a0",
        "md5": "1c4ecc238571333ae507f82ff6a5e9e4"
    },
    {
        "texto": "Dentro de uma proposta de integração e de agregação de competências, visando a excelência de seus cursos, as instituições FEI, FCI e ESAN foram transformadas no Centro Universitário da FEI no ano de 2002.",
        "sha256": "faefb927a21dd282ee00effe42bc0688f649450677a61edce15863a15461b721",
        "md5": "98420532cbf1be32a98be579f592cd72"
    },
    {
        "texto": "O Centro Universitário da FEI passou a fazer parte do seleto grupo que produz ciência no Brasil, quando a CAPES aprovou o primeiro curso de Mestrado em Engenharia Elétrica em 2005.",
        "sha256": "da9f214449005850f4fd552238658820434c15ca06389d018b1814bb376abaa6",
        "md5": "2e20bfbece6fdc62de4c4bb80a77ba1f"
    },
    {
        "texto": "Em 2016 foi realizada a primeira edição do congresso de inovação - Megatendências 2050.",
        "sha256": "56f4ba0ea34d91fe386f09dc687f1c35c757009b0230a828fa43e48ac08f8d0c",
        "md5": "5cbf7c58bf9acd451c3bf1b48392a9e6"
    },
    {
        "texto": "Em 2012 o Centro Universitário FEI celebrou 70 anos de história e de excelência na inovação e na formação de mais de 50 mil profissionais altamente qualificados para o setor empresarial, entre Administradores, Engenheiros e Cientistas da Computação.",
        "sha256": "2707325bd4929bbbadb422851a2248615bf7998bf3607b6ad934168be6a45859",
        "md5": "a0a80cbc42bcd7b4b6ab317d0d2efa33"
    },
    {
        "texto": "Em 1999 iniciam-se as atividades da FCI (Faculdade de Informática), como o curso de Ciência da Computação.",
        "sha256": "b2ff0457c8c20ccd84e20cd72f06c08140b8ea472d6a6848a5c291319bf9e4a8",
        "md5": "0288b32001adf2f237ba8410f8415e50"
    },
    {
        "texto": "SHA256 e MD5 corretos",
        "sha256": "c034489664dd98c3a2b0d7c1afc0717378827d9fa778288c8bb1c567c8bc2ec1",
        "md5": "19406b49ace5073c806a79061f58dbd3"
    },
    {
        "texto": "Somente SHA256 correto",
        "sha256": "5b22f6bf621c2116f0d4589c3b5405ed3b5d768b9ba1dfafbae9292331ce9827",
        "md5": "cfe69ac7a0b07810b391c27b1ea838cd"
    },
    {
        "texto": "Somente MD5 correto",
        "sha256": "58d909cc5c6ac58bb509d4651528c66a8b9bd8a197ec260dd7d6754b98b6b63e",
        "md5": "c4e28d48ac81f88aaade5ed31f2e2c26"
    },
    {
        "texto": "Nenhum dos dois corretos",
        "sha256": "d55825a0c3ee133ac29986b3fcefb30432968e99967787191bb48be89e485cf8",
        "md5": "8bdf3218ccd26f327220ad0daf3d3ce0"
    }
]

print("""Atividade 2 - Função Hash
Bruno Umeoka Higuti - R.A: 22.121.082-6 
Gabriel de Almeida Gava - R.A: 22.121.079-2 
Guilherme Bizon Jeronymo - R.A: 22.121.128-7 
Matheus Venâncio Scomparim - R.A: 22.121.063-6 
Gustavo Leite Bueno de Oliveira - R.A: 22.121.057-8\n""")

for idx, info_frase in enumerate(frases, start=1):
    texto = info_frase["texto"]
    sha256_prof = info_frase["sha256"]
    md5_prof = info_frase["md5"]

    sha256_nosso = hashlib.sha256(texto.encode('utf-8')).hexdigest()
    md5_nosso = hashlib.md5(texto.encode('utf-8')).hexdigest()

    sha256_corresponde = sha256_nosso == sha256_prof
    md5_corresponde = md5_nosso == md5_prof

    print(f'Frase {idx}:')
    print(f'Texto: "{texto}"')
    print(f'Hash SHA256 fornecido: {sha256_prof}')
    print(f'Hash SHA256 calculado: {sha256_nosso}')
    print(f'SHA256 correspondem: {sha256_corresponde}')
    print(f'Hash MD5 fornecido: {md5_prof}')
    print(f'Hash MD5 calculado: {md5_nosso}')
    print(f'MD5 correspondem: {md5_corresponde}')
    print("\n" + '-' * 80 + "\n")
