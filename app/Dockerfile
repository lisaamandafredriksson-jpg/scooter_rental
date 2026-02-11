# ============================================
# DOCKERFILE FÖR ELSPARKCYKEL-APPLIKATION
# ============================================

# Basimage: Python 3.12 (slim = mindre storlek)
FROM python:3.12-slim

# Metadata
LABEL maintainer="ditt-namn"
LABEL description="Elsparkcykel-uthyrningssystem för Programmering 2"

# Sätt arbetsmapp (alla kommandon körs härifrån)
WORKDIR /app

# Kopiera requirements.txt först
# (Om requirements.txt inte ändras, kan Docker cache:a detta steg)
COPY requirements.txt .

# Installera Python-paket
# --no-cache-dir = spara inte cache (minskar image-storlek)
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera ALL kod till containern
COPY . .

# Håll containern igång så vi kan köra kommandon
# (tail -f /dev/null = läs en tom fil i oändlighet)
CMD ["tail", "-f", "/dev/null"]

# ANVÄNDING:
# Bygg: docker build -t scooter-app .
# Kör program: docker-compose exec app python main.py