# Muster-Auszüge — Deutsch

**WARNUNG:** Diese Auszüge zeigen NUR STRUKTUR und TON. ALLE domänenspezifischen Inhalte (Firmennamen, Systemnamen, Metriken, URLs) müssen AUSSCHLIESSLICH aus den bereitgestellten Quelldokumenten stammen. NIEMALS Begriffe oder Details aus diesen Beispielen in das tatsächliche Dokument übernehmen.

---

## Beispiel: Projektübersicht und Hintergrund

> Die **Beispiel GmbH**, ein führender Dienstleister im Personal- und Projektmanagement, steht aktuell vor der Herausforderung, monatlich rund 600 Stundenzettel in unterschiedlichen Formaten manuell zu bearbeiten. Dieser Prozess ist nicht nur zeitintensiv, sondern auch fehleranfällig und bindet wertvolle Kapazitäten, die an anderer Stelle besser eingesetzt werden könnten.
>
> Vor diesem Hintergrund wurde ein Projekt durchgeführt, mit dem Ziel, relevante Daten aus digitalisierten Stundenzetteln automatisch zu extrahieren, in strukturierte JSON-Dateien zu konvertieren und für die Integration in das Zielsystem vorzubereiten. In enger Zusammenarbeit und durch iterative Entwicklung konnte ein funktionsfähiges MVP realisiert werden.
>
> Konkret werden Felder wie Datum, gearbeitete Stunden sowie Abwesenheiten zuverlässig erkannt und standardisiert. Dadurch werden Fehler minimiert, der manuelle Aufwand reduziert und wertvolle Zeitressourcen freigesetzt.
>
> Die Lösung umfasst eine API, über die Stundenzettel eingereicht, automatisch ausgelesen und im JSON-Format zurückgegeben werden. Ergänzend bewertet ein Ampelsystem (grün, gelb, rot) die Qualität der Extraktion und macht potenzielle Probleme transparent sichtbar.

**Beachte den Ton:** Sachlich, spezifisch, problemorientiert. Beginnt mit dem Kundenproblem, nicht mit der Partnerschaft.

---

## Beispiel: Historie der Projektentwicklung (ein Sprint)

> ## Sprint 2 (KW 34 & 35)
>
> Verfeinerung der Validierungslogik und Klassifikation (Ampelsystem: Grün/Gelb/Rot).
>
> ### Details
>
> **Validierungslogik** und Klassifikation weiterentwickelt.
>
> - **Resultate:** Die Validierung haben wir in diesem Sprint von 46% auf 79% gesteigert.
>
> **VPN-Anbindung** der Infrastruktur eingerichtet. Diese Anbindung wurde erstmal für einen Nutzer eingerichtet.
>
> **Entscheidung:** Die VPN-Anbindung unserer Infrastruktur an die Kundenumgebung erwies sich als komplex. Gemeinsam mit dem Kunden haben wir deren notwendige Einrichtungsschritte erfolgreich umgesetzt.
>
> Zusätzlich musste die Validierung auf 90% erhöht werden. Da die Ergebnisse des Hackathons unter strengeren Regeln stark zurückgingen (von 63% auf 14%), haben wir mehr Aufwand investiert, um die Validierungsrate zu steigern.
>
> Um den Fokus klar zu halten, wurde die Generierung des PNG-Bildes auf Sprint 3 verschoben.

**Beachte die Muster:**
- `**Entscheidung:**` Präfix für Entscheidungen
- `**Resultate:**` Präfix für Metriken
- Metrik-Verlauf über Sprints (14% → 46% → 79%)
- Verschobene Items mit Begründung

---

## Beispiel: Systemarchitektur

> ### Hauptarbeitslauf
>
> 1. Eine Client-App sendet eine HTTPS-Anfrage mit JSON-Payload an den **Azure App Service** über dessen privaten Endpunkt. Die Anfrage enthält Daten wie PDF-/Dokumenten-Binärdaten, Dateiname, Beraterliste usw.
>
> 2. Der **Azure App Service** nutzt **Azure OpenAI** und Azure **Document Intelligence**, um die Zeiterfassungsdetails aus der angegebenen Datei zu extrahieren.
>
> 3. Der **Azure App Service** sendet Telemetrie und Protokolle an **Application Insights** und den **Log Analytics-Arbeitsbereich** zu Überwachungszwecken.
>
> 4. Der **Azure App Service** ruft die Anmeldeinformationen aus dem **Azure Key Vault** ab, um auf die verschiedenen Dienste zuzugreifen.
>
> 5. Der **Azure App Service** sendet die HTTPS-Antwort mit JSON-Payload zurück, die Daten wie extrahierte Felder, den zugeordneten Berater und einen optionalen Bericht enthält.
>
> ### Zentrale Komponenten
>
> | **Name** | **Typ** | **Beschreibung** |
> | --- | --- | --- |
> | example-webapp | Azure App Service | API-Endpunkt |
> | example-openai | Azure OpenAI | LLM-Endpunkt für Datenextraktion |
> | example-docint | Azure AI Services | Document-Intelligence-Endpunkt |
> | example-vault | Azure Key Vault | Verwaltete Anmeldeinformationen |
> | example-appi | Azure Application Insights | Überwachung |
> | example-law | Azure Log Analytics | Protokollspeicherung |

**Beachte die Muster:**
- Nummerierte Schritte für den Arbeitsablauf
- Fettgedruckte Systemnamen bei erster Erwähnung
- Tabellenformat für Komponenten (Name | Typ | Beschreibung)

---

## Beispiel: Anleitung zur Bereitstellung

> ### Cloud Infrastruktur
>
> Die Cloud-Infrastruktur ist als Infrastructure-as-Code in Terraform deklariert (siehe Ordner /terraform).
>
> Bevor Änderungen vorgenommen werden, muss folgendes geschehen:
>
> 1. Terraform installieren: https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli
> 2. terraform.tfstate und terraform.tfvars über einen sicheren Kanal herunterladen und im terraform Ordner ablegen.
> 3. In den Terraform-Ordner wechseln und das Terraform-Projekt initialisieren:
>
> ```
> cd terraform
> terraform init
> ```
>
> Nachdem der Infrastruktur-Code geändert wurde:
>
> ```
> terraform plan -var-file="terraform.tfvars"
> ```
>
> Die Liste der Änderungen überprüfen. Sobald bestätigt:
>
> ```
> terraform apply -var-file="terraform.tfvars"
> ```

**Beachte die Muster:**
- Nummerierte Schritte mit exakten Befehlen
- Code-Blöcke für ALLE Befehle
- Voraussetzungen zuerst, dann Ausführung
- Portal-Links wo relevant

---

## Beispiel: Zugangsdaten

> ### Terraform-Zustand und Variablen
>
> 1. Sicherer Link: https://share.1password.com/s#EXAMPLE
> 2. Zugriff auf den Link ist den folgenden E-Mail-Adressen gewährt: name1@client.com, name2@client.com
> 3. Der Link läuft am 10.11.2025 ab.
>
> ### API-Endpunkt und Bearer-Token
>
> 1. Sicherer Link: https://share.1password.com/s#EXAMPLE
> 2. Zugriff auf den Link ist den folgenden E-Mail-Adressen gewährt: name1@client.com, name2@client.com
> 3. Der Link läuft am 10.11.2025 ab.

**Beachte die Muster:**
- Konsistente Struktur pro System (Link, Zugriff, Ablauf)
- NIEMALS echte Credentials im Dokument
- 1Password Share-Links als bevorzugte Methode
