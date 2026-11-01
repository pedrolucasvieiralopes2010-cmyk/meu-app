
import random
import streamlit as st

# ==========================================
# CONFIGURAÇÕES
# ==========================================

st.set_page_config(
    page_title="Meu Super App",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# ESTILO DARK PREMIUM
# ==========================================

st.markdown("""
<style>

.stApp {
    background: #090b13;
    color: #f1f1f7;
}

[data-testid="stSidebar"] {
    background: #101321;
    border-right: 1px solid #252941;
}

[data-testid="stSidebar"] h1 {
    color: #a78bfa;
}

h1, h2, h3 {
    color: #f5f3ff !important;
}

p, label, span {
    color: #c5c8d8;
}

.hero {
    background: linear-gradient(120deg, #19152f, #111a35);
    border: 1px solid #37305e;
    border-radius: 20px;
    padding: 35px;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 38px;
    margin-bottom: 10px;
    color: #ffffff;
}

.hero p {
    color: #b9b5d5;
    font-size: 16px;
}

.card {
    background: #141827;
    border: 1px solid #292f49;
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 15px;
}

.card h3 {
    color: #a78bfa !important;
    margin-top: 0;
}

.stButton > button {
    background: linear-gradient(90deg, #7c3aed, #4f46e5);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: bold;
    min-height: 43px;
    transition: 0.2s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #8b5cf6, #6366f1);
    border: 1px solid #a78bfa;
    color: white;
}

.stTextInput input,
.stNumberInput input {
    background: #171c2c;
    color: white;
    border: 1px solid #343b59;
    border-radius: 10px;
}

div[data-baseweb="select"] > div {
    background: #171c2c;
    border-color: #343b59;
}

[data-testid="stMetric"] {
    background: #141827;
    border: 1px solid #292f49;
    padding: 17px;
    border-radius: 14px;
}

[data-testid="stMetricValue"] {
    color: #a78bfa;
}

hr {
    border-color: #292f49;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# FUNÇÕES
# ==========================================

def eh_primo(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def listar_primos(limite):
    if limite < 2:
        return []

    numeros = [True] * (limite + 1)
    numeros[0] = False
    numeros[1] = False

    for i in range(2, int(limite ** 0.5) + 1):
        if numeros[i]:
            for j in range(i * i, limite + 1, i):
                numeros[j] = False

    return [
        i for i in range(2, limite + 1)
        if numeros[i]
    ]


# ==========================================
# ESTADOS DO SISTEMA
# ==========================================

if "secreto" not in st.session_state:
    st.session_state.secreto = random.randint(1, 100)

if "tentativas" not in st.session_state:
    st.session_state.tentativas = 0

if "acertou" not in st.session_state:
    st.session_state.acertou = False

if "historico" not in st.session_state:
    st.session_state.historico = []


# ==========================================
# MENU LATERAL
# ==========================================

with st.sidebar:

    st.markdown("# ⚡ SUPER APP")

    st.caption("DARK PREMIUM EDITION")

    st.divider()

    opcao = st.radio(
        "NAVEGAÇÃO",
        [
            "Início",
            "Jogo de Adivinhação",
            "Calculadora",
            "Primos de 1 a 100",
            "Primos até N",
            "Sobre"
        ]
    )

    st.divider()

    st.markdown("### SISTEMA")
    st.caption("Versão 2.0")
    st.caption("Desenvolvido em Python")

    st.markdown("---")
    st.caption("Meu Super App © 2026")


# ==========================================
# CABEÇALHO
# ==========================================

st.markdown("""
<div class="hero">
    <h1>⚡ MEU SUPER APP</h1>
    <p>Seu espaço de jogos, cálculos e ferramentas matemáticas.</p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# INÍCIO
# ==========================================

if opcao == "Início":

    st.subheader("Painel principal")

    st.write("Bem-vindo ao seu aplicativo!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>JOGOS</h3>
            <p>Teste sua sorte e raciocínio.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>CALCULADORA</h3>
            <p>Resolva operações matemáticas.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>MATEMÁTICA</h3>
            <p>Explore os números primos.</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.subheader("Ferramentas disponíveis")

    st.write("Selecione uma ferramenta no menu lateral para começar.")

    a, b = st.columns(2)

    with a:
        st.info("Jogo de Adivinhação: descubra o número secreto.")

    with b:
        st.info("Calculadora: some, subtraia, multiplique e divida.")


# ==========================================
# JOGO DE ADIVINHAÇÃO
# ==========================================

elif opcao == "Jogo de Adivinhação":

    st.subheader("Jogo de Adivinhação")

    st.write("Pense rápido e descubra o número secreto!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Tentativas", st.session_state.tentativas)

    with col2:
        status = "Concluído" if st.session_state.acertou else "Em andamento"
        st.metric("Status", status)

    st.divider()

    if not st.session_state.acertou:

        palpite = st.number_input(
            "Digite seu palpite:",
            min_value=1,
            max_value=100,
            value=50,
            step=1,
            key="palpite"
        )

        if st.button("ENVIAR PALPITE", use_container_width=True):

            st.session_state.tentativas += 1

            if palpite < st.session_state.secreto:
                st.warning("O número secreto é MAIOR!")

            elif palpite > st.session_state.secreto:
                st.warning("O número secreto é MENOR!")

            else:
                st.session_state.acertou = True
                st.session_state.historico.append(
                    st.session_state.tentativas
                )

                st.balloons()

                st.success(
                    f"PARABÉNS! Você acertou em "
                    f"{st.session_state.tentativas} tentativas!"
                )

    else:

        st.success(
            f"Você venceu! O número era "
            f"{st.session_state.secreto}."
        )

        if st.button("JOGAR NOVAMENTE", use_container_width=True):

            st.session_state.secreto = random.randint(1, 100)
            st.session_state.tentativas = 0
            st.session_state.acertou = False

            st.rerun()

    if st.session_state.historico:

        st.divider()
        st.subheader("Seu histórico")

        st.write(
            f"Vitórias registradas: {len(st.session_state.historico)}"
        )

        st.write(
            f"Melhor resultado: {min(st.session_state.historico)} tentativas"
        )


# ==========================================
# CALCULADORA
# ==========================================

elif opcao == "Calculadora":

    st.subheader("Calculadora Robusta")

    st.write("Realize suas operações matemáticas.")

    with st.form("calculadora"):

        n1 = st.number_input(
            "Primeiro número",
            value=0.0
        )

        operacao = st.selectbox(
            "Operação",
            [
                "Adição (+)",
                "Subtração (-)",
                "Multiplicação (×)",
                "Divisão (÷)",
                "Potenciação (xʸ)",
                "Resto da divisão (%)"
            ]
        )

        n2 = st.number_input(
            "Segundo número",
            value=0.0
        )

        calcular = st.form_submit_button(
            "CALCULAR",
            use_container_width=True
        )

    if calcular:

        if operacao == "Adição (+)":
            resultado = n1 + n2

        elif operacao == "Subtração (-)":
            resultado = n1 - n2

        elif operacao == "Multiplicação (×)":
            resultado = n1 * n2

        elif operacao == "Divisão (÷)":

            if n2 == 0:
                st.error("Não é possível dividir por zero!")
                resultado = None
            else:
                resultado = n1 / n2

        elif operacao == "Potenciação (xʸ)":

            if abs(n2) > 1000:
                st.error("Expoente muito grande.")
                resultado = None
            else:
                try:
                    resultado = n1 ** n2
                except (OverflowError, ValueError):
                    st.error("Não foi possível calcular essa potência.")
                    resultado = None

        else:

            if n2 == 0:
                st.error("Não é possível dividir por zero!")
                resultado = None
            else:
                resultado = n1 % n2

        if resultado is not None:

            if isinstance(resultado, complex):
                st.success(f"Resultado: {resultado}")
            elif abs(resultado) == float("inf") or resultado != resultado:
                st.error("Resultado fora do intervalo numérico permitido.")
            else:
                st.success(f"Resultado: {resultado:g}")


# ==========================================
# PRIMOS DE 1 A 100
# ==========================================

elif opcao == "Primos de 1 a 100":

    st.subheader("Números Primos de 1 a 100")

    primos = listar_primos(100)

    st.metric("Quantidade encontrada", len(primos))

    st.divider()

    st.write("Lista de números primos:")

    st.code("  |  ".join(map(str, primos)))

    st.success("Todos os números foram verificados!")


# ==========================================
# PRIMOS ATÉ N
# ==========================================

elif opcao == "Primos até N":

    st.subheader("Verificador de Números Primos")

    st.write("Descubra se um número é primo e liste os primos até ele.")

    with st.form("primos"):

        n = st.number_input(
            "Digite o limite N:",
            min_value=0,
            max_value=100000,
            value=100,
            step=1
        )

        verificar = st.form_submit_button(
            "VERIFICAR NÚMEROS",
            use_container_width=True
        )

    if verificar:

        n = int(n)

        if eh_primo(n):
            st.success(f"O número {n} É PRIMO!")
        else:
            st.error(f"O número {n} NÃO é primo.")

        primos = listar_primos(n)

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Limite pesquisado", n)

        with col2:
            st.metric("Quantidade de primos", len(primos))

        st.subheader(f"Números primos de 1 até {n}")

        if primos:
            st.code("  |  ".join(map(str, primos)))
        else:
            st.warning("Nenhum número primo encontrado.")


# ==========================================
# SOBRE
# ==========================================

elif opcao == "Sobre":

    st.subheader("Sobre o aplicativo")

    st.markdown("""
    <div class="card">
        <h3>MEU SUPER APP</h3>
        <p>
        Um projeto desenvolvido em Python com Streamlit,
        reunindo ferramentas matemáticas e jogos em um só lugar.
        </p>
        <p><b>Versão:</b> 2.0</p>
        <p><b>Linguagem:</b> Python</p>
        <p><b>Interface:</b> Streamlit</p>
        <p><b>Tema:</b> Dark Premium</p>
    </div>
    """, unsafe_allow_html=True)

    st.caption("Obrigado por utilizar o Meu Super App!")
            
