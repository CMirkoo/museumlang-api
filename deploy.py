import subprocess

# Funzione per avviare i container usando Docker Compose
def deploy_with_docker_compose():
    """
    PER AVVIARE LO SCRIPT DEPLOY.py È NECESSARIO DOCKER APERTO SUL COMPUTER
    """
    try:
        print("Starting Docker Compose...")
        subprocess.run(['docker-compose', 'up', '--build'], check=True)
        print("Docker Compose started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Avvio del deploy tramite Docker Compose
if __name__ == "__main__":
    deploy_with_docker_compose()
