import random

print("=" * 50)
print("SISTEMA INTELIGENTE DE MONITORAMENTO ESPACIAL")
print("=" * 50)

# Dados simulados da missão
temperatura = random.randint(20, 100)
energia = random.randint(0, 100)
comunicacao = random.choice(["ONLINE", "OFFLINE"])
modulo = random.choice(["NORMAL", "ATENCAO", "CRITICO"])

print(f"\nTemperatura: {temperatura}°C")
print(f"Energia: {energia}%")
print(f"Comunicação: {comunicacao}")
print(f"Status do Módulo: {modulo}")

print("\n--- ALERTAS GERADOS ---")

alerta = False

if temperatura > 80:
    print("⚠ ALERTA: Temperatura crítica detectada.")
    alerta = True

if energia < 20:
    print("⚠ ALERTA: Nível de energia crítico.")
    alerta = True

if comunicacao == "OFFLINE":
    print("⚠ ALERTA: Falha na comunicação.")
    alerta = True

if modulo == "CRITICO":
    print("⚠ ALERTA: Módulo em estado crítico.")
    alerta = True

if not alerta:
    print("Nenhum alerta encontrado.")

print("\n--- TOMADA DE DECISÃO AUTOMÁTICA ---")

if energia < 20:
    print("➡ Modo de economia de energia ativado.")

if temperatura > 80:
    print("➡ Sistema de resfriamento ativado.")

if comunicacao == "OFFLINE":
    print("➡ Tentando restabelecer comunicação.")

if modulo == "CRITICO":
    print("➡ Isolando módulo para proteção da missão.")

if (
    energia >= 20 and
    temperatura <= 80 and
    comunicacao == "ONLINE" and
    modulo != "CRITICO"
):
    print("➡ Operação funcionando normalmente.")

print("\nMonitoramento concluído.")