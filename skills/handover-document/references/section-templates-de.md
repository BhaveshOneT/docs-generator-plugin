# Abschnitt-Vorlagen — Deutsch

Diese Vorlagen leiten die Inhaltsgenerierung für jeden Abschnitt des Übergabedokuments. Sie definieren die erwartete Struktur, erforderliche Elemente und Schreibmuster.

---

## 1. Projektübersicht und Hintergrund

**Vorlage:**

3-4 Absätze:

**Absatz 1 — Kunde & Herausforderung:**
"Die {Firmenname}, ein {Branchenbeschreibung}, steht aktuell vor der Herausforderung, {spezifisches Problem mit Größenordnung}. Dieser Prozess ist {Auswirkung: zeitintensiv, fehleranfällig, ressourcenbindend} und {geschäftliche Konsequenz}."

**Absatz 2 — Lösung:**
"Vor diesem Hintergrund wurde ein Projekt durchgeführt, mit dem Ziel, {Ziel: automatisieren/extrahieren/klassifizieren/optimieren}. In enger Zusammenarbeit und durch iterative Entwicklung konnte ein funktionsfähiges {Ergebnistyp: MVP, API, Plattform} realisiert werden, das {spezifische Fähigkeit}."

**Absatz 3 — Kernfähigkeiten:**
"Konkret werden Felder wie {Feld 1}, {Feld 2} und {Feld 3} zuverlässig {erkannt/extrahiert/verarbeitet}. Dadurch werden {Fehler minimiert, Aufwand reduziert, Zeitressourcen freigesetzt}."

**Absatz 4 (optional) — Qualitätssystem:**
"Die Lösung umfasst ein {Qualitätsmechanismus: Ampelsystem, Konfidenz-Bewertung}, das {Funktionsweise}. Ergänzend wird {optionaler Output: Report, Dashboard} generiert."

**Erforderliche Elemente:** Firmenname, Branche, Problemgröße, Lösungstyp, spezifische Fähigkeiten, Geschäftsnutzen
**Verboten:** Generische KI-Partnerschaft-Sprache, Marketing-Aussagen ohne Belege

---

## 2. Projektzeitplan

**Vorlage:**

```
## Sprint 1 (KW {Start} & {Ende})
**{Sprint-Ziel — ein Satz}**
- {Lieferergebnis 1}
- {Lieferergebnis 2}

## Sprint 2 (KW {Start} - {Ende})
**{Sprint-Ziel — ein Satz}**
- {Lieferergebnis 1}
- {Lieferergebnis 2}

## Test- und Übergabe-Phase (KW {Start} - {Ende})
{Beschreibung der Tests, Anpassungen und Übergabeaktivitäten}
```

**Erforderliche Elemente:** Sprint-Nummern mit KW-Angaben, Ziel pro Sprint, Lieferergebnisse
**Muster:** KW-Notation verwenden (Kalenderwochen).

---

## 3. Funktionen und Arbeitsabläufe

**Vorlage:**

Ein Unterabschnitt pro Hauptfunktion:

```
### {Funktionsname}
{Was es macht — 1-2 Sätze mit technischen Details}
{Wie es funktioniert — Prozessablauf oder Integrationspunkte}
{Mehrwert — messbarer Nutzen oder freigeschaltete Fähigkeit}
```

Bei API-basierten Lösungen:
- Endpunkt-URL-Muster
- Request/Response-Format-Zusammenfassung
- Authentifizierungsmethode

---

## 4. Geistiges Eigentum und rechtliche Aspekte

**Vorlage:**

```
### IP-Eigentum
{Status des IP-Eigentums — wem gehört der Code, die Modelle, die Datenausgaben}
{Verweis auf Vertragsklausel falls verfügbar}
Kundenbestätigung: {Bestätigt von [Name] am [Datum] / [Noch zu bestätigen]}

### Lizenzeinhaltung
| **Komponente** | **Lizenz** | **Typ** | **Compliance-Status** |
| --- | --- | --- | --- |
| {Bibliotheksname} | {MIT/Apache/GPL/etc.} | {Permissiv/Copyleft} | {Konform/Prüfung erforderlich} |

### Vertragliche Klauseln
- **Wettbewerbsverbot:** {Einzeilige Zusammenfassung oder "Siehe Vertrag §X" / [Noch zu bestätigen]}
- **Bevorzugter Partner:** {Einzeilige Zusammenfassung oder [Noch zu bestätigen]}
- **Code-Weitergabebeschränkungen:** {Zusammenfassung / [Noch zu bestätigen]}
- **Kundenfreigabe-Status:** {Bestätigt per E-Mail am [Datum] / [Noch zu bestätigen]}

### Datenschutz
- {DSGVO-Maßnahmen}
- {Anonymisierungsansatz}
- {Datenaufbewahrungsrichtlinie}
- {AVV-Status: unterzeichnet/ausstehend/nicht zutreffend}
```

**Erforderliche Elemente:** IP-Eigentumsstatus, Lizenztabelle, Klauselzusammenfassungen, Datenschutzstatus
**Muster:** `[Noch zu bestätigen]` großzügig verwenden. Die Struktur ist wichtiger als die Vollständigkeit.
**KRITISCH:** NIEMALS rechtliche Details erfinden. Auf Verträge verweisen oder als `[Noch zu bestätigen]` markieren.

---

## 5. Beschreibung der verwendeten Datenquellen

**Vorlage:**

```
### {Datenquellenname}
- **Typ:** {PDF, CSV, API, Datenbank, etc.}
- **Umfang:** {Anzahl oder Bereich}
- **Format:** {Formatdetails, Variationen}
- **Qualität:** {Qualitätsbeobachtungen, bekannte Probleme}
- **Zugang:** {Wie Daten bereitgestellt wurden/werden}
```

**Muster:** Spezifisch über Formatvariationen sein (z.B. "53 historische Stundenzettel mit stark variierenden Layouts")

---

## 5. Historie der Projektentwicklung

**Vorlage pro Sprint:**

```
## Sprint {N} (KW {Daten})
{Sprint-Ziel}

### Details
{Narrativ was gebaut/verbessert wurde}

**{Komponente/Feature}** {Verb: verfeinert, implementiert, entwickelt}
- **Entscheidung:** {Was entschieden wurde und warum}
- **Resultate:** {Metriken — Vorher/Nachher wo verfügbar}

{Auf nächsten Sprint verschobene Items und Begründung}
```

**Erforderliche Elemente:** Pro-Sprint-Aufschlüsselung, Entscheidungen mit Begründung, Metrik-Verlauf
**Muster:** Metrik-Verbesserung über Sprints verfolgen. `**Entscheidung:**` Präfix für alle Entscheidungen.

---

## 6. Systemarchitektur

**Vorlage:**

```
## Architekturdiagramm
{Eingebettetes Bild}

## Beschreibung der Systemarchitektur und ihrer Komponenten

### Hauptarbeitslauf
1. {Schritt 1 — z.B. "Eine Client-App sendet eine HTTPS-Anfrage mit JSON-Payload an den Azure App Service über dessen privaten Endpunkt."}
2. {Schritt 2}
3. {Schritt 3}

### Zentrale Komponenten
| **Name** | **Typ** | **Beschreibung** |
| --- | --- | --- |
| {Komponentenname} | {Azure App Service / etc.} | {Was es macht} |

### Verbindungen (optional)
| **Quelle** | **Ziel** | **Methode** | **Authentifizierung** | **Protokoll** |
| --- | --- | --- | --- | --- |
| {Quelle} | {Ziel} | {Privater Endpunkt / VPN / etc.} | {Bearer Token / API Key / etc.} | {HTTPS} |
```

---

## 7. Abhängigkeiten und Bibliotheken

**Vorlage:**

```
### Hauptabhängigkeiten
- OS {Name} {Version}
- {Sprache} {Version} oder neuer
- {IaC-Tool} {Version} oder neuer

### OS-Level-Pakete
- {Paket1}
- {Paket2}

### {Sprache}-Module
\```{sprache}
"{Paket1} == {Version}",
"{Paket2} == {Version}",
\```
```

**Erforderliche Elemente:** ALLE Abhängigkeiten aus Quellen mit exakten Versionen

---

## 8. Anleitung zur Bereitstellung

**Vorlage:**

```
### Cloud Infrastruktur
{IaC-Ansatz Beschreibung}

{Voraussetzungen — Installationsschritte mit Befehlen}

{Änderungen prüfen}
\```
{exakter Befehl}
\```

{Änderungen anwenden}
\```
{exakter Befehl}
\```

### Code-Bereitstellung
{Bereitstellungsmethode Beschreibung}

{Setup-Schritte (nummeriert)}
1. {Schritt mit Befehl}
2. {Schritt mit Befehl}
```

**Erforderliche Elemente:** Exakte Befehle (kopierbar), Portal-URLs, Credential-Standorte
**Muster:** Erwartete Eingabeaufforderungen und ignorierbare Warnungen einschließen

---

## 9. Bekannte Einschränkungen und offene Punkte

**Vorlage:**

```
- {Einschränkung 1 — spezifisch und ehrlich}
- {Einschränkung 2 — mit Kontext falls nötig}
- {Geplantes aber nicht implementiertes Feature — mit Grund}
- {Bekannter Grenzfall — mit Workaround falls verfügbar}
```

---

## 10. Codepaket

**Vorlage:**

```
### Bereitstellungsmethode
{Wie Code geteilt wird: ZIP-Datei auf SharePoint / GitHub Repo / etc.}

### Zugang
{Link oder URL}
Zugang gewährt für: {Liste der E-Mail-Adressen}

### Inhalt
{Was enthalten ist}
{Was ausgeschlossen ist}

### Umgebungsvariablen
{Wie .env-Datei zu erhalten — 1Password-Link, E-Mail, etc.}
```

---

## 11. Zugangsdaten

**Vorlage pro System:**

```
### {System-/Servicename}
1. Sicherer Link: {1Password Share-URL}
2. Zugriff gewährt für: {Liste der E-Mail-Adressen}
3. Ablaufdatum: {Datum}
```

**KRITISCH:** NIEMALS echte Passwörter, Tokens oder API-Keys im Dokument. Nur Links zu sicheren Speichern.

---

## 12. Empfehlungen und nächste Schritte

**Vorlage:**

```
### Kurzfristig
- {Sofortige Verbesserung}
- {Bugfix oder Optimierung}

### Mittelfristig
- {Feature-Erweiterung}
- {Zusätzliche Integration}

### Langfristig
- {Strategische Vision}
- {Plattform-Evolution}

### Wartung
{Wer übernimmt den laufenden Support}
{SLA oder Support-Vereinbarung Details}
```
