# Importa a biblioteca customtkinter, usada para criar interfaces gráficas modernas em Python
import customtkinter as ctk

# Importa a biblioteca platform para identificar qual é o sistema operacional da máquina
import platform

# Importa a biblioteca subprocess para conseguir rodar comandos do sistema operacional (como o ping)
import subprocess

# Importa a biblioteca socket para conseguir pegar informações de rede, como o nome do PC e o IP
import socket

# Importa a biblioteca externa psutil para monitorar o uso de hardware (CPU e memória RAM)
import psutil

# Define o tema visual da janela para seguir automaticamente o padrão do Windows (Dark ou Light)
ctk.set_appearance_mode("System")

# Define a cor padrão dos botões e elementos interativos da interface como azul corporativo
ctk.set_default_color_theme("blue")

# Cria uma classe chamada DiagnosticApp que herda todas as funcionalidades de uma janela do CustomTkinter (ctk.CTk)
class DiagnosticApp(ctk.CTk):

    # Método construtor: é executado automaticamente assim que a classe é iniciada
    def __init__(self):

        # Inicializa a superclasse (a janela base do CustomTkinter)
        super().__init__()

        # Define o título que vai aparecer na barra superior da janela do aplicativo
        self.title("IT Diagnostic Assistant - Suporte N1")

        # Define o tamanho inicial da janela (largura x altura em pixels)
        self.geometry("520x580")

        # Impede que o usuário redimensione o tamanho da janela do aplicativo arrastando as bordas
        self.resizable(False, False)

        # Cria um rótulo de texto (CTkLabel) posicionado na janela principal para servir de título visual
        self.titulo_label = ctk.CTkLabel(
            self, 
            text="Assistente de Diagnóstico de TI", 
            font=("Arial", 20, "bold")
        )

        # Empacota e exibe o título na janela, aplicando um espaçamento vertical (pady) de 20 pixels
        self.titulo_label.pack(pady=20)

        # Cria um botão interativo (CTkButton) que o usuário vai clicar para rodar o diagnóstico
        self.btn_executar = ctk.CTkButton(
            self, 
            text="Executar Diagnóstico", 
            command=self.executar_diagnostico, # Vincula o clique do botão à função que faz os testes
            font=("Arial", 14, "bold"),
            height=40
        )

        # Empacota e exibe o botão na janela com um espaçamento vertical de 10 pixels
        self.btn_executar.pack(pady=10)

        # Cria uma caixa de texto multilinha (CTkTextbox) para exibir os resultados na tela
        self.texto_resultado = ctk.CTkTextbox(
            self, 
            width=460, 
            height=380, 
            font=("Consolas", 12)  # Usa fonte monoespaçada para alinhar os textos como um terminal de computador
        )

        # Empacota e exibe a caixa de texto na janela com um espaçamento vertical de 10 pixels
        self.texto_resultado.pack(pady=10)

    # Cria uma função auxiliar dedicada apenas a testar a conectividade de rede com ping
    def testar_conectividade(self, destino):

        # Verifica se o sistema operacional é Windows para definir qual argumento de contagem usar (-n ou -c)
        parametro_contador = "-n" if platform.system().lower() == "windows" else "-c"

        # Monta a lista com os comandos de rede que o subprocess vai executar no terminal
        comando = ["ping", parametro_contador, "2", destino]
        
        # Inicia um bloco de tratamento de erros (try/except) caso o comando falhe
        try:
            # Executa o comando de ping no sistema operacional e captura a resposta de saída
            resultado = subprocess.run(
                comando, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                text=True, 
                encoding='cp850', 
                errors='ignore',
                timeout=5
            )
            
            # Se o código de retorno do sistema for 0, significa que o ping obteve resposta com sucesso
            if resultado.returncode == 0:
                return f"[SUCESSO] Conexão com {destino} estabelecida."
            
            # Se o código for diferente de 0, o ping falhou
            else:
                return f"[ALERTA] Falha ao comunicar com {destino}."
                
        # Caso ocorra qualquer exceção ou timeout durante o comando, captura o erro e retorna a mensagem
        except Exception:
            return f"[ERRO] Ocorreu uma falha no teste para {destino}."

    # Cria a função principal que realiza o diagnóstico completo e joga os dados na tela do aplicativo
    def executar_diagnostico(self):

        # Limpa todo o texto que estava escrito anteriormente na caixa de resultados da interface
        self.texto_resultado.delete("0.0", "end")
        
        # Insere uma mensagem inicial informando que o processo começou
        self.texto_resultado.insert("end", "Iniciando triagem do sistema...\n\n")

        # Atualiza a janela visualmente na mesma hora para o usuário ver que começou
        self.update()

        # Usa a biblioteca socket para capturar o nome do host (nome da máquina) atual
        hostname = socket.gethostname()

        # Tenta descobrir o endereço IP local da máquina na rede interna
        try:
            ip_local = socket.gethostbyname(hostname)
            
        # Se falhar ao buscar o IP, define a variável com uma mensagem padrão de erro
        except:
            ip_local = "Não detectado"
        
        # Formata uma string contendo o nome e a versão do sistema operacional
        os_nome = f"{platform.system()} {platform.release()}"

        # Coleta o percentual de uso atual da CPU usando a biblioteca psutil (com intervalo de 1 segundo)
        uso_cpu = psutil.cpu_percent(interval=1)

        # Coleta as informações detalhadas da memória RAM instalada no computador
        memoria = psutil.virtual_memory()
        
        # Insere na caixa de texto do aplicativo o nome da máquina coletado
        self.texto_resultado.insert("end", f"-> Hostname: {hostname}\n")

        # Insere na caixa de texto o IP local da máquina
        self.texto_resultado.insert("end", f"-> Endereço IP Local: {ip_local}\n")

        # Insere na caixa de texto o sistema operacional identificado
        self.texto_resultado.insert("end", f"-> Sistema Operacional: {os_nome}\n")

        # Insere na caixa de texto a porcentagem de uso da CPU
        self.texto_resultado.insert("end", f"-> Uso de CPU: {uso_cpu}%\n")

        # Insere na caixa de texto a memória RAM total convertida de bytes para Gigabytes (GB)
        self.texto_resultado.insert("end", f"-> Memória RAM Total: {round(memoria.total / (1024**3), 2)} GB\n")

        # Insere na caixa de texto a porcentagem de memória RAM que está sendo usada no momento
        self.texto_resultado.insert("end", f"-> Memória RAM Usada: {memoria.percent}%\n")

        # Insere uma linha divisoria pontilhada para organizar visualmente o relatório
        self.texto_resultado.insert("end", "-" * 44 + "\n")

        # Atualiza a interface gráfica para exibir os dados coletados de hardware na tela
        self.update()

        # Escreve na tela que o teste de ping para o IP do Google está prestes a rodar
        self.texto_resultado.insert("end", "[*] Testando conectividade com 8.8.8.8...\n")

        # Atualiza a janela novamente
        self.update()

        # Chama a função de teste de ping passando o IP 8.8.8.8 e guarda o resultado na variável
        ping_dns = self.testar_conectividade("8.8.8.8")

        # Insere o resultado do ping do DNS na caixa de texto da tela
        self.texto_resultado.insert("end", f"   {ping_dns}\n\n")

        # Escreve na tela que o teste de resolução para o site do Google vai começar
        self.texto_resultado.insert("end", "[*] Testando resolução com google.com...\n")

        # Atualiza a interface
        self.update()

        # Chama a função de teste de ping passando o domínio google.com e guarda o resultado
        ping_web = self.testar_conectividade("google.com")

        # Insere o resultado do ping web na caixa de texto da tela
        self.texto_resultado.insert("end", f"   {ping_web}\n\n")

        # Insere a mensagem final indicando que todo o processo de diagnóstico terminou com sucesso
        self.texto_resultado.insert("end", "[+] Diagnóstico concluído com sucesso!\n")

# Condicional que verifica se o script está sendo executado diretamente pelo usuário no terminal
if __name__ == "__main__":

    # Instancia a classe principal da nossa aplicação, criando o aplicativo na memória
    app = DiagnosticApp()

    # Inicia o loop principal do CustomTkinter para manter a janela aberta, interativa e escutando cliques
    app.mainloop()