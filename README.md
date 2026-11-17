# 🛠️ IT Diagnostic Assistant (GUI Edition)

Uma aplicação desktop moderna desenvolvida em Python para auxiliar analistas de suporte técnico e help desk na verificação instantânea de status de rede, conectividade e saúde de hardware.

## 📸 Demonstração

<img width="1920" height="1080" alt="diagnostic" src="https://github.com/user-attachments/assets/6b5d3dba-5678-45e1-8cdf-3a493542ca8a" />


> *Nota: Para adicionar a imagem no GitHub, tire um print da tela do aplicativo rodando (`Win + Shift + S`), selecione esta linha no editor do README e aperte `Ctrl + V`.*

---

## ✨ Funcionalidades

* **Interface Moderna:** Desenvolvido em modo escuro utilizando `customtkinter` para uma experiência visual limpa e profissional.
* **Diagnóstico de Sistema:** Identifica automaticamente o hostname da máquina, IP local e sistema operacional.
* **Monitoramento de Recursos:** Coleta em tempo real o percentual de uso da CPU e o consumo total/percentual da memória RAM.
* **Teste de Conectividade:** Executa testes automatizados de *ping* para validar a comunicação com servidores DNS (`8.8.8.8`) e resolução de nomes (`google.com`).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Bibliotecas Nativas:** `platform`, `subprocess`, `socket`
* **Bibliotecas Externas:** `customtkinter` (interface gráfica), `psutil` (monitoramento de hardware)

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3** instalado na sua máquina.
2. Clone este repositório:
   ```bash
   git clone https://github.com/caiobraza/IT-Diagnostic-Assistant.git
