# ==========================================
# 1. IMPORTAÇÃO DAS BIBLIOTECAS
# ==========================================
import platform     # Permite identificar informações sobre o sistema operacional (Windows, Linux, etc.)
import subprocess   # Permite executar comandos do sistema operacional (como o comando 'ping')
import socket       # Fornece acesso a ferramentas de rede para verificar IPs e hostnames
import psutil       # Biblioteca externa para monitorar recursos da máquina (CPU, memória, disco)

# ==========================================
# 2. FUNÇÃO DE DIAGNÓSTICO DE REDE (PING)
# ==========================================
def testar_conectividade(destino="8.8.8.8"):
    """
    Testa a conectividade com a internet ou com um IP específico usando o comando ping.
    Por padrão, testa o DNS público do Google (8.8.8.8).
    """
    print(f"\n[*] Testando conectividade com: {destino}...")
    
    # Identifica se o sistema é Windows ou Linux/Mac para ajustar o parâmetro de quantidade de pings
    parametro_contador = "-n" if platform.system().lower() == "windows" else "-c"
    
    # Monta a lista de argumentos para executar o comando ping no terminal do sistema
    comando = ["ping", parametro_contador, "2", destino]
    
    try:
        # Adicionado encoding='cp850' e errors='ignore' para evitar erros de acentuação do Windows
        resultado = subprocess.run(
            comando, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True, 
            encoding='cp850', 
            errors='ignore',
            timeout=5
        )
        
        # Se o código de retorno for 0, o ping teve sucesso
        if resultado.returncode == 0:
            print(f"[SUCESSO] Conexão com {destino} estabelecida com sucesso!")
            return True
        else:
            print(f"[ALERTA] Falha ao comunicar com {destino}. Sem resposta.")
            return False
    except subprocess.TimeoutExpired:
        print(f"[ERRO] O teste de ping para {destino} esgotou o tempo limite (Timeout).")
        return False
    except Exception as e:
        print(f"[ERRO] Ocorreu um erro ao executar o ping: {e}")
        return False
# ==========================================
# 3. FUNÇÃO DE COLETA DE DADOS DO SISTEMA E REDE LOCAL
# ==========================================
def obter_info_sistema():
    """
    Coleta informações básicas de hardware, IP local e sistema operacional.
    """
    print("\n" + "="*40)
    print("      DIAGNÓSTICO DE SISTEMA E REDE      ")
    print("="*40)
    
    # Obtém o nome do host (nome do computador na rede)
    hostname = socket.gethostname()
    print(f"-> Nome do Computador (Hostname): {hostname}")
    
    # Obtém o endereço IP local da máquina na rede interna
    try:
        ip_local = socket.gethostbyname(hostname)
        print(f"-> Endereço IP Local: {ip_local}")
    except Exception as e:
        print(f"-> Não foi possível obter o IP local: {e}")
    
    # Exibe informações sobre o Sistema Operacional
    print(f"-> Sistema Operacional: {platform.system()} {platform.release()}")
    
    # Utiliza a biblioteca psutil para checar o uso de recursos de hardware
    uso_cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory()
    
    print(f"-> Uso atual de CPU: {uso_cpu}%")
    print(f"-> Memória RAM Total: {round(memoria.total / (1024**3), 2)} GB")
    print(f"-> Memória RAM Usada: {memoria.percent}%")
    print("="*40)

# ==========================================
# 4. FUNÇÃO PRINCIPAL DE EXECUÇÃO
# ==========================================
def main():
    """
    Função principal que coordena a execução de todas as verificações.
    """
    print("Iniciando o Assistente de Diagnóstico de TI...")
    
    # 1. Executa a checagem de hardware e rede local
    obter_info_sistema()
    
    # 2. Testa o gateway local / DNS da rede
    testar_conectividade("8.8.8.8")
    
    # 3. Testa a resolução de nomes (DNS) acessando um site externo
    testar_conectividade("google.com")
    
    print("\n[+] Diagnóstico concluído com sucesso!\n")

# Garante que o script seja executado apenas se rodado diretamente
if __name__ == "__main__":
    main()