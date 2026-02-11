# Elsparkcykel-uthyrningssystem 🛴

**Programmering nivå 2 - Docker, OOP & PostgreSQL**

---

## 📋 Om projektet

Detta är ett elsparkcykel-uthyrningssystem (likt Voi, Lime, Tier) där användare kan:
- Registrera sig och ladda saldo
- Hyra elsparkcyklar
- Starta och avsluta resor
- Se sin resehistorik

Systemet körs i **två Docker-containers:**
- **Container 1:** PostgreSQL-databas (sparar all data)
- **Container 2:** Python-applikation (ditt program)

---

## 🎯 Din uppgift

Du ska implementera följande filer:

### ⚠️ MÅSTE IMPLEMENTERAS (för E):

| Fil | Vad du ska göra |
|-----|-----------------|
| `app/database.sql` | Skapa 3 tabeller med SQL (users, scooters, trips) |
| `app/database.py` | Klass för databaskoppling |
| `app/user.py` | User-klass med inkapsling |
| `app/scooter.py` | Scooter-klass med inkapsling |
| `app/trip.py` | Trip-klass för resor |
| `app/main.py` | Huvudprogram med meny (9 val) |

### ✅ REDAN FÄRDIGT:

- `docker-compose.yml` - Startar båda containers
- `app/Dockerfile` - Bygger Python-containern
- `app/requirements.txt` - Python-paket som behövs

---

## 📁 Projektstruktur

### Grundstruktur (E-nivå)
```
scooter_rental/
├── docker-compose.yml
├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── database.sql
│   ├── database.py
│   ├── user.py
│   ├── scooter.py
│   ├── trip.py
│   └── main.py
└── README.md
```

### Förbättrad struktur (C/A-nivå) ⭐

För högre betyg, organisera koden i tydliga mappar:
```
scooter_rental/
├── docker-compose.yml
├── README.md
│
└── app/
    ├── Dockerfile
    ├── requirements.txt
    │
    ├── database/
    │   └── init.sql              # Databas-schema
    │
    ├── models/        # Klasser som representerar data
    │   ├── __init__.py
    │   ├── user.py
    │   ├── scooter.py
    │   └── trip.py
    │
    ├── services/                 # Affärslogik
    │   ├── __init__.py
    │   └── database.py
    │
    ├── ui/                       # Användargränssnitt
    │   ├── __init__.py
    │   └── menu.py               # Menyhantering
    │
    ├── tests/                    # Tester (extra för A)
    │   ├── __init__.py
    │   ├── test_user.py
    │   ├── test_scooter.py
    │   └── test_trip.py
    │
    └── main.py                   # Startpunkt
```

**Fördelar med strukturerad organisation:**
- ✅ Lättare att hitta kod
- ✅ Tydlig separation av ansvar
- ✅ Professionell struktur (används i verkliga projekt)
- ✅ Enklare att testa och underhålla
- ✅ Visar djupare förståelse för kodorganisation

---

## 🗄️ Databasstruktur

Systemet använder 3 tabeller:
![Databasdiagram](/images/ScooterRental_data_diagram.png)

**Relationer:**
- En användare kan ha många resor (one-to-many)
- En scooter kan användas i många resor (one-to-many)
- Varje resa tillhör en användare OCH en scooter (foreign keys)

**Exempeldata:**
![Exempeldata](/images/ScooterRental_data_example.png)

---

## 📚 Programflöde
```
1. Användare registrerar sig
   ↓
2. Användare laddar pengar (saldo)
   ↓
3. Användare väljer ledig elsparkcykel
   ↓
4. Resa startas (tid börjar räknas)
   ↓
5. Användare kör runt
   ↓
6. Resa avslutas (tid slutar räknas)
   ↓
7. Kostnad beräknas (minuter × pris)
   ↓
8. Pengar dras från saldo
   ↓
9. Elsparkcykel blir ledig igen
```

---

## 💻 Menyval som ska implementeras
```
[1] Registrera ny användare
[2] Visa alla användare
[3] Ladda saldo
[4] Lägg till elsparkcykel
[5] Visa lediga elsparkcyklar
[6] Starta resa
[7] Avsluta resa
[8] Visa mina resor
[9] Avsluta programmet
```

---

## 🚀 Snabbstart (efter implementering)

### 1. Starta systemet
```bash
docker-compose up -d
```

Vänta 10 sekunder så databasen hinner starta.

### 2. Kör programmet
```bash
docker-compose exec app python main.py
```

### 3. Stoppa systemet
```bash
docker-compose down
```

---

## 🧪 Testa ditt arbete

### Kontrollera databasen
```bash
# Anslut till databasen
docker exec -it scooter_rental_db psql -U admin -d scooter_app

# Visa tabeller
\dt

# Visa innehåll i en tabell
SELECT * FROM users;

# Avsluta
\q
```

### Testscenario

När ditt program är klart, testa detta:

1. **Registrera användare:** "Anna Andersson", "anna@mail.com", "070-1234567"
2. **Ladda saldo:** 100 kr på Anna
3. **Lägg till scooter:** "VOI123", "Stureplan", 3 kr/min
4. **Visa lediga:** Ska visa VOI123
5. **Starta resa:** Anna hyr VOI123
6. **Vänta:** 1-2 minuter
7. **Avsluta resa:** Ska räkna kostnad och dra pengar
8. **Visa resor:** Ska visa Annas resa med kostnad

---

## 📤 Inlämning

### Steg 1: Bygg och tagga
```bash
cd app
docker build -t scooter-rental-app .
docker tag scooter-rental-app dittnamn/scooter-rental-app:v1.0
```

### Steg 2: Pusha till Docker Hub
```bash
docker login
docker push dittnamn/scooter-rental-app:v1.0
```

### Steg 3: Spela in demo med OBS Studio

**Krav för inspelningen (max 15 minuter):**

#### 📹 Tekniska krav:
- Använd **OBS Studio** (gratis från obsproject.com)
- Ditt **ansikte ska synas** (webbkamera)
- Din **röst ska höras** tydligt (mikrofon)
- **Skärmen ska synas** med din kod och terminal

#### 🎬 Innehåll i inspelningen:

**Del 1: Introduktion (1-2 min)**
- Säg ditt namn
- Kort förklara vad systemet gör
- Visa projektstrukturen i VSCode

**Del 2: Live-demo (8-10 min)**
- Starta Docker: `docker-compose up`
- Kör programmet: `docker-compose exec app python main.py`
- **Demonstrera ALLA 9 menyval live:**
  1. Registrera en användare
  2. Visa alla användare
  3. Ladda saldo
  4. Lägg till elsparkcykel
  5. Visa lediga elsparkcyklar
  6. Starta en resa
  7. Vänta 1-2 min, sedan avsluta resan
  8. Visa dina resor
  9. Avsluta programmet
- Visa att kostnad dras korrekt från saldo
- Visa att scooter blir ledig igen efter avslutad resa

**Del 3: Förklaring av design (3-5 min)**
- Förklara **varför** du valde din mappstruktur
- Förklara **hur** klasserna samarbetar (inte rad-för-rad, utan övergripande)
- Förklara en **utmaning** du stötte på och hur du löste den
- Visa en **databas-query** live i terminalen (`SELECT * FROM trips;`)

**Tips för inspelning:**
- Testa ljud och bild innan du börjar
- Prata tydligt och i lagom takt
- Visa ansiktet i ett hörn av skärmen (picture-in-picture)
- Pausa inspelningen om du behöver tänka
- Repetera inte - om något går fel, förklara hur du felsöker

**OBS Studio-inställningar:**
- Lägg till "Display Capture" (din skärm)
- Lägg till "Video Capture Device" (din webbkamera)
- Lägg till "Audio Input Capture" (din mikrofon)
- Exportera som MP4

### Steg 5: Lämna in på Campus

Ladda upp följande **3 filer** på Campus:

1. **Din ZIP-filen** (projektmappen som är komprimerad)
2. **Din OBS-inspelning** (MP4-video, max 15 min)
3. **Länk till Docker Hub** (skriv i kommentarsfältet på Campus)
```
   https://hub.docker.com/r/dittnamn/scooter-rental-app
```

---

## 🔍 Vanliga kommandon

| Kommando | Vad det gör |
|----------|-------------|
| `docker-compose up -d` | Startar båda containers i bakgrunden |
| `docker-compose down` | Stoppar och tar bort containers |
| `docker-compose logs app` | Visar loggar från Python-containern |
| `docker-compose exec app python main.py` | Kör huvudprogrammet |
| `docker ps` | Visa körande containers |
| `docker images` | Visa alla images |

---

## 🐛 Felsökning

### Problem: "Cannot connect to database"

**Lösning:** Vänta 10 sekunder efter `docker-compose up` innan du kör programmet.
```bash
docker-compose up -d
sleep 10
docker-compose exec app python main.py
```

### Problem: "Table does not exist"

**Lösning:** Din `database.sql` kördes inte. Kontrollera syntaxen och starta om:
```bash
docker-compose down
docker-compose up -d
```

### Problem: "ModuleNotFoundError" med mappstruktur

**Lösning:** Se till att alla mappar har `__init__.py` filer.
```bash
touch app/models/__init__.py
touch app/services/__init__.py
touch app/ui/__init__.py
```

### Problem: "docker-compose command not found"

**Lösning:** Se till att Docker Desktop är igång.

### Problem: Inspelning blir för stor för Campus

**Lösning:** 
- Komprimera videon i OBS (Settings → Output → Recording Quality: "High Quality, Medium File Size")
- Eller använd Handbrake (gratis) för att komprimera efter inspelning
- Max filstorlek på Campus är ofta ~250-500 MB

---

## 📊 Bedömningskriterier

### ✅ Godkänt (E)

- Image finns på Docker Hub och går att hämta
- `docker-compose up` fungerar utan fel
- Alla 3 tabeller skapade med rätt relationer
- Alla 3 klasser implementerade med privata attribut
- Minst 5 av 9 menyval fungerar i live-demon
- **Inspelning visar:**
  - Ditt ansikte och röst tydligt
  - Live-demo av systemet
  - Grundläggande förklaring av hur det fungerar
- **Struktur:** Grundstruktur (alla filer i `app/`)

### ✅ För C-nivå

Allt från E plus:
- Alla 9 menyval fungerar perfekt i demon
- Felhantering implementerad och demonstrerad
- Tydliga kommentarer och docstrings i koden
- Status-hantering fungerar (scooter ledig/uthyrd)
- **Inspelning visar:**
  - Professionell presentation
  - Tydlig förklaring av designval
  - Demonstration av felhantering
  - Visa databas-queries live
- **Struktur:** Förbättrad mappstruktur
  - `models/` för klasser
  - `services/` för databaskoppling
  - `ui/` för menyhantering (valfritt)
  - Alla `__init__.py` filer på plats

### ✅ För A-nivå

Allt från C plus:
- Extra funktioner (statistik, filter, ranking)
- Exceptionell kodkvalitet och konsekvent stil
- Kan förklara alternativa lösningar och trade-offs
- Djup förståelse för OOP-principer
- **Inspelning visar:**
  - Mycket professionell presentation
  - Djup teknisk förståelse
  - Diskussion om framtida förbättringar
  - Jämförelse med andra lösningar
  - Demonstration av extra funktioner
- **Struktur:** Professionell organisation
  - `tests/` mapp med enhetstester
  - Dokumentation i varje modul
  - Logisk och konsekvent namngivning
  - Separation of concerns (models, services, ui)

---

## 📁 Exempel: Imports med mappstruktur

### Med grundstruktur (E-nivå):
```python
# main.py
from database import Database
from user import User
from scooter import Scooter
from trip import Trip
```

### Med förbättrad struktur (C/A-nivå):
```python
# main.py
from services.database import Database
from models.user import User
from models.scooter import Scooter
from models.trip import Trip
from ui.menu import show_menu, handle_menu_choice  # Om du har UI-mapp
```

### Exempel: `models/__init__.py`
```python
"""Models package - contains all data classes"""
from .user import User
from .scooter import Scooter
from .trip import Trip

__all__ = ['User', 'Scooter', 'Trip']
```

---

## 💡 Tips för högre betyg

### För C-nivå:
- Separera klasser i `models/` mapp
- Lägg databaskoppling i `services/` mapp
- Använd `__init__.py` i alla mappar
- Skriv tydliga docstrings i alla klasser och metoder
- Implementera try/except för alla databasoperationer
- Öva din presentation innan inspelning

### För A-nivå:
- Skapa en `ui/menu.py` som hanterar all menylogik
- Lägg till en `tests/` mapp med enhetstester
- Skriv en `utils/` mapp för hjälpfunktioner
- Dokumentera varje modul med docstrings
- Implementera loggning
- Lägg till extra funktioner:
  - Statistik (mest använda scooter, total intäkt)
  - Filter (visa bara scooters på viss plats)
  - Sökfunktion (hitta användare via namn)
- Presentera som en professionell utvecklare i inspelningen

---

## 💡 Allmänna tips

- Börja med `database.sql` och testa att tabellerna skapas
- Implementera klasserna en i taget och testa löpande
- Använd `print()` för att debugga
- Läs felmeddelanden noggrant - de säger ofta vad som är fel
- För högre betyg: Planera mappstrukturen innan du börjar koda
- Testa din demo flera gånger innan inspelning
- Fråga läraren om du fastnar!

---

## 📞 Support

**Problem med Docker?** Fråga läraren  
**Frågor om uppgiften?** Se detaljerade instruktioner på Campus  
**Frågor om mappstruktur?** Be läraren om exempel  
**Problem med OBS Studio?** Testa inspelningen innan deadline  
**Tekniska problem?** Kontrollera att Docker Desktop är igång

---

**Lycka till!**