import random
import streamlit as st

st.set_page_config(page_title="Meu Super App", page_icon="🔢")

st.title("MEU SUPER APP")
st.write("Escolha uma ferramenta no menu.")

def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

opcao = st.sidebar.selectbox(
    "MENU",
    [
        "Início",
        "Jogo de Adivinhação",
        "Calculadora Robusta",
        "Primos de 1 a 100",
        "Primos até N"
    ]
)

if opcao == "Início":
    st.header("Bem-vindo!")
    st.write("Selecione uma opção no menu lateral.")

elif opcao == "Jogo de Adivinhação":
    st.header("JOGO DE ADIVINHAÇÃO")

    if "secreto" not in st.session_state:
        st.session_state.secreto = random.randint(1, 100)
        st.session_state.tentativas = 0
        st.session_state.acertou = False

    palpite = st.number_input(
        "Digite seu palpite:",
        min_value=1,
        max_value=100,
        step=1
    )

    if st.button("Enviar palpite"):
        if not st.session_state.acertou:
            st.session_state.tentativas += 1

            if palpite < st.session_state.secreto:
                st.warning("O número secreto é MAIOR!")

            elif palpite > st.session_state.secreto:
                st.warning("O número secreto é MENOR!")

            else:
                st.session_state.acertou = True
                st.success(
                    f"Parabéns! Você acertou em "
                    f"{st.session_state.tentativas} tentativas!"
                )

    if st.button("Novo jogo"):
        for chave in ["secreto", "tentativas", "acertou"]:
            st.session_state.pop(chave, None)
        st.rerun()

elif opcao == "Calculadora Robusta":
    st.header("CALCULADORA ROBUSTA")

    n1 = st.number_input("Primeiro número:")
    n2 = st.number_input("Segundo número:")

    operacao = st.selectbox(
        "Escolha a operação:",
        ["Somar", "Subtrair", "Multiplicar", "Dividir"]
    )

    if st.button("Calcular"):

        if operacao == "Somar":
            resultado = n1 + n2

        elif operacao == "Subtrair":
            resultado = n1 - n2

        elif operacao == "Multiplicar":
            resultado = n1 * n2

        else:
            if n2 == 0:
                st.error("Não é possível dividir por zero!")
                resultado = None
            else:
                resultado = n1 / n2

        if resultado is not None:
            st.success(f"Resultado: {resultado:g}")

elif opcao == "Primos de 1 a 100":
    st.header("NÚMEROS PRIMOS DE 1 A 100")

    numeros = [
        n for n in range(1, 101)
        if primo(n)
    ]

    st.success(" ".join(map(str, numeros)))
    st.write(f"Total de números primos: {len(numeros)}")

elif opcao == "Primos até N":
    st.header("VERIFICADOR DE NÚMEROS PRIMOS")

    n = st.number_input(
        "Digite o limite N:",
        min_value=0,
        max_value=100000,
        value=100
    )

    if st.button("Verificar"):

        n = int(n)

        if primo(n):
            st.success(f"O número {n} É PRIMO!")
        else:
            st.error(f"O número {n} NÃO é primo.")

        numeros = [
            x for x in range(2, n + 1)
            if primo(x)
        ]

        st.subheader(f"Primos de 1 até {n}:")

        if numeros:
            st.write(", ".join(map(str, numeros)))
        else:
            st.write("Nenhum número primo encontrado.")
