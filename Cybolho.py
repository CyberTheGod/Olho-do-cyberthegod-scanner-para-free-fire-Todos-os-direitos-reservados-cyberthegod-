# -*- coding: utf-8 -*-
import hashlib
import os
import sys
import time
import psutil

# Banner ASCII Customizado Exato com Suporte a UTF-8
CUSTOM_ASCII_BANNER = r"""
██████╗ ██╗     ██╗  ██╗ ██████╗     ██████╗  ██████╗      ██████╗██╗   ██╗██████╗ ███████╗██████╗ ████████╗██╗  ██╗███████╗ ██████╗  ██████╗ ██████╗ 
██╔═══██╗██║     ██║  ██║██╔═══██╗    ██╔══██╗██╔═══██╗    ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔════╝ ██╔═══██╗██╔══██╗
██║   ██║██║     ███████║██║   ██║    ██║  ██║██║   ██║    ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝   ██║   ███████║█████╗  ██║  ███╗██║   ██║██║  ██║
██║   ██║██║     ██╔══██║██║   ██║    ██║  ██║██║   ██║    ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗   ██║   ██╔══██║██╔══╝  ██║   ██║██║   ██║██║  ██║
╚██████╔╝███████╗██║  ██║╚██████╔╝    ██████╔╝╚██████╔╝    ╚██████╗   ██║   ██████╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗╚██████╔╝╚██████╔╝██████╔╝
 ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝     ╚═════╝  ╚═════╝      ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ 
"""

AUTHOR_CREDIT = "Por: CyberTheGod"

# Base de Dados de Assinaturas Extremas (Xits, Bypasses, Proxies e Modificadores)
EXTREME_THREAT_SIGNATURES = [
    # Injetores, Debuggers & Cheats Clássicos
    "cheatengine",
    "cheat engine",
    "trainer",
    "injector",
    "speedhack",
    "wemod",
    "xmod",
    "lordpe",
    "x64dbg",
    "ollydbg",
    "processhacker",
    "modmenu",
    "aimbot",
    "wallhack",
    "radar",
    "packeteditor",
    "wireshark",
    "charles",
    "fiddler",
    "autoclicker",
    "artmoney",
    # Free Fire & Bypasses de Emulador
    "bypass",
    "ff_bypass",
    "smartgaga",
    "ldplayer",
    "nox",
    "bluestacks",
    "hd-player",
    "memu",
    "macro",
    "script",
    "regedit_ff",
    "regedit",
    "headshot",
    "sensitivity_tool",
    "antiban",
    "panel_ff",
    "freefire_mod",
    "apk_mod",
    "hacker",
    "aimlock",
    "silentaim",
    "magicbullet",
    # Proxies, Túneis e Softwares de Roteamento Suspeitos
    "proxifier",
    "charlesproxy",
    "fiddle",
    "shadowsocks",
    "v2ray",
    "openvpn",
    "wireguard",
    "psiphon",
    "httpinjector",
    "tlsunnel",
    "postman",
]

# Portas comumente utilizadas por Proxies locais e Túneis de Bypass
SUSPICIOUS_PORTS = [8080, 8888, 3128, 1080, 9050, 5353, 8443]


def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")


def print_banner():
  print("\033[96m" + CUSTOM_ASCII_BANNER + "\033[0m")
  print(
      "\033[91m=======================================================================================================================\033[0m"
  )
  print(
      f"\033[92m  [Olho do cyberthegod] - Sistema Definitivo Anti-Xit, Bypass & Proxy Inspection | Desenvolvido por: {AUTHOR_CREDIT}\033[0m"
  )
  print(
      "\033[91m=======================================================================================================================\033[0m"
  )


def elite_deep_system_scan():
  clear_screen()
  print_banner()
  print(
      "\n\033[93m[+] Iniciando varredura profunda de nível de kernel (Memória,"
      + " Processos, Bypasses e Proxies)...\033[0m"
  )
  time.sleep(1.5)

  detected = []
  total_scanned = 0

  print(
      f"\n{'PID':<8} | {'NOME DO PROCESSO':<25} | {'DIAGNÓSTICO DE AMEAÇA':<35}"
  )
  print("-" * 75)

  for proc in psutil.process_iter(["pid", "name", "exe"]):
    try:
      total_scanned += 1
      info = proc.info
      p_name = info["name"] or ""
      p_exe = info["exe"] or "Desconhecido"

      matched = None
      for sig in EXTREME_THREAT_SIGNATURES:
        if sig in p_name.lower() or sig in p_exe.lower():
          matched = sig
          break

      if matched:
        detected.append(
            {"pid": info["pid"], "name": p_name, "sig": matched, "exe": p_exe}
        )
        print(
            f"\033[91m{info['pid']:<8} | {p_name[:25]:<25} | 🚨 ALERTA CRÍTICO"
            + f" ({matched.upper()})\033[0m"
        )
    except (psutil.NoSuchProcess, psutil.AccessDenied):
      continue

  print("-" * 75)
  print(
      f"\n[INFO] Varredura concluída. Total de processos inspecionados:"
      + f" {total_scanned}"
  )

  if detected:
    print(
        f"\033[91m[!] ATENÇÃO: {len(detected)} processos maliciosos ou de"
        + " bypass detectados no sistema!\033[0m"
    )
  else:
    print(
        "\033[92m[✓] Status Limpo! Nenhuma assinatura de xit, bypass ou proxy"
        + " ativo encontrada.\033[0m"
    )

  input("\nPressione ENTER para voltar ao painel principal...")


def advanced_network_proxy_audit():
  clear_screen()
  print_banner()
  print(
      "\n\033[93m[+] Analisando Sockets, Endpoints e Portas de Proxy"
      + " Suspeitas...\033[0m\n"
  )
  print(
      f"{'PID':<8} | {'PROCESSO':<18} | {'ENDEREÇO LOCAL':<22} |"
      + f" {'ENDEREÇO REMOTO':<22} | {'ESTADO':<12}"
  )
  print("-" * 90)

  suspicious_connections = 0
  try:
    for conn in psutil.net_connections(kind="inet"):
      if conn.pid:
        try:
          p = psutil.Process(conn.pid)
          p_name = p.name()
        except Exception:
          p_name = "Desconhecido"

        lport = conn.laddr.port if conn.laddr else 0
        rport = conn.raddr.port if conn.raddr else 0

        # Verifica se usa portas associadas a proxies/tunelamento
        is_proxy_port = lport in SUSPICIOUS_PORTS or rport in SUSPICIOUS_PORTS

        laddr = f"{conn.laddr.ip}:{lport}" if conn.laddr else "N/A"
        raddr = f"{conn.raddr.ip}:{rport}" if conn.raddr else "N/A"

        if is_proxy_port:
          suspicious_connections += 1
          print(
              f"\033[91m{conn.pid:<8} | {p_name[:18]:<18} | {laddr:<22} |"
              + f" {raddr:<22} | PROXY/TÚNEL [!]\033[0m"
          )
        else:
          print(
              f"{conn.pid:<8} | {p_name[:18]:<18} | {laddr:<22} |"
              + f" {raddr:<22} | {conn.status:<12}"
          )
  except Exception as e:
    print(f"\033[91m[X] Erro ao inspecionar conexões: {e}\033[0m")

  print("-" * 90)
  print(
      f"\n[INFO] Auditoria de rede finalizada. Portas proxy suspeitas"
      + f" encontradas: {suspicious_connections}"
  )
  input("\nPressione ENTER para voltar ao painel principal...")


def file_hash_integrity_checker():
  clear_screen()
  print_banner()
  print(
      "\n\033[93m[+] Verificador Avançado de Integridade por Hash (SHA256)...\033[0m"
  )
  target_path = (
      input(
          "\nDigite o caminho completo do executável ou arquivo do jogo para"
          + " verificar: "
      )
      .strip()
      .strip('"')
  )

  if os.path.exists(target_path):
    print("\nCalculando Hash de segurança...")
    sha256_hash = hashlib.sha256()
    try:
      with open(target_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
          sha256_hash.update(byte_block)
      print(f"\033[92m[✓] Arquivo: {target_path}\033[0m")
      print(f"\033[96m[HASH SHA256]: {sha256_hash.hexdigest()}\033[0m")
      print(
          "\033[93m(Compare este hash com a versão limpa oficial para garantir"
          + " que não há modificações)\033[0m"
      )
    except Exception as e:
      print(f"\033[91m[X] Erro ao ler o arquivo: {e}\033[0m")
  else:
    print("\033[91m[X] O caminho especificado não foi encontrado.\033[0m")

  input("\nPressione ENTER para voltar ao painel principal...")


def terminate_target_process():
  clear_screen()
  print_banner()
  print(
      "\n\033[91m[!] EXPURGO DE TAREFA SUSPEITA (MATAR PROCESSO PELO PID)\033[0m\n"
  )
  pid_input = input("Digite o PID exato do processo que deseja eliminar: ")

  if pid_input.isdigit():
    pid = int(pid_input)
    try:
      p = psutil.Process(pid)
      name = p.name()
      p.terminate()
      print(
          f"\033[92m[✓] Sucesso! Processo '{name}' (PID: {pid}) foi"
          + " aniquilado.\033[0m"
      )
    except Exception as e:
      print(
          f"\033[91m[X] Falha ao encerrar o processo (Acesso negado ou ID"
          + f" inválido): {e}\033[0m"
      )
  else:
    print("\033[91m[X] Entrada inválida. Digite apenas números para o PID.\033[0m")

  input("\nPressione ENTER para voltar ao painel principal...")


def export_official_audit_report():
  clear_screen()
  print_banner()
  print(
      "\n\033[93m[+] Compilando relatório oficial de auditoria forense...\033[0m"
  )

  filename = f"auditoria_suprema_{int(time.time())}.txt"
  try:
    with open(filename, "w", encoding="utf-8") as f:
      f.write(
          "===================================================================\n"
      )
      f.write("      RELATÓRIO OFICIAL DE AUDITORIA - OLHO Do CYBERTHEGOD\n")
      f.write(
          "===================================================================\n"
      )
      f.write(f"Autoria: {AUTHOR_CREDIT}\n")
      f.write(f"Data e Hora: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
      f.write("Relação completa de processos ativos auditados:\n")
      f.write("-" * 70 + "\n")

      for proc in psutil.process_iter(["pid", "name", "exe"]):
        try:
          info = proc.info
          f.write(
              f"PID: {info['pid']} | Nome: {info['name']} | Caminho:"
              + f" {info['exe']}\n"
          )
        except Exception:
          continue

    print(
        f"\033[92m[✓] Relatório forense gerado e salvo com sucesso em:"
        + f" {filename}\033[0m"
    )
  except Exception as e:
    print(f"\033[91m[X] Erro ao gravar arquivo de relatório: {e}\033[0m")

  input("\nPressione ENTER para voltar ao painel principal...")


def main_control_menu():
  while True:
    clear_screen()
    print_banner()
    print(f"\n\033[1m[ PAINEL DE CONTROLE CENTRAL - {AUTHOR_CREDIT} ]\033[0m")
    print(
        " 1. ⚡ Executar Varredura Completa (Xits, Bypasses, Macros e"
        + " Emuladores)"
    )
    print(" 2. 🌐 Inspecionar Sockets, Conexões e Portas de Proxy")
    print(" 3. 🔍 Verificar Integridade de Arquivo por Hash (SHA256)")
    print(" 4. ❌ Encerrar Processo Suspeito por PID (Kill Engine)")
    print(" 5. 💾 Exportar Relatório Oficial de Auditoria (.txt)")
    print(" 6. 🚪 Desconectar do Sistema")

    choice = input(
        "\n\033[93mSelecione o comando desejado [1-6]: \033[0m"
    ).strip()

    if choice == "1":
      elite_deep_system_scan()
    elif choice == "2":
      advanced_network_proxy_audit()
    elif choice == "3":
      file_hash_integrity_checker()
    elif choice == "4":
      terminate_target_process()
    elif choice == "5":
      export_official_audit_report()
    elif choice == "6":
      print(
          f"\n\033[96mDesconectando o Olho de Deus Supreme. {AUTHOR_CREDIT} —"
          + " Jogo limpo sempre!\033[0m"
      )
      sys.exit()
    else:
      input(
          "\n\033[91mComando inválido! Pressione ENTER para tentar"
          + " novamente...\033[0m"
      )


if __name__ == "__main__":
  try:
    main_control_menu()
  except KeyboardInterrupt:
    print(
        "\n\033[91m[!] Sessão interrompida de forma abrupta pelo operador."
        + " Encerrando...\033[0m"
    )
