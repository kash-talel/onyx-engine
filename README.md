# Onyx Engine — Autonomous Cyber Threat Intelligence Platform

[![Build & Test Status](https://img.shields.io/badge/tests-82%20passed-brightgreen?style=for-the-badge&logo=pytest)](https://github.com/kash-talel/onyx-engine)
[![NLP F1-Score](https://img.shields.io/badge/NLP%20F1--Score-96.85%25-blueviolet?style=for-the-badge)](https://github.com/kash-talel/onyx-engine)
[![Python Version](https://img.shields.io/badge/Python-3.11%20%7C%203.12-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![Next.js](https://img.shields.io/badge/Next.js-14.2-black?style=for-the-badge&logo=next.js)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0%20Strict-3178C6?style=for-the-badge&logo=typescript)](https://www.typescriptlang.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![STIX 2.1](https://img.shields.io/badge/OASIS-STIX%202.1%20Compliant-orange?style=for-the-badge)](https://oasis-open.github.io/cti-documentation/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

> **Onyx Engine (ONYX CTI v3.0 Genesis)** is an enterprise-grade, sovereign Cyber Threat Intelligence (CTI) ingestion, correlation, and cognitive analysis platform. Engineered for modern Security Operations Centers (SOC), Computer Emergency Response Teams (CERT), and threat hunting units, Onyx aggregates and synthesizes telemetry from 15+ real-time OSINT feeds, applies scientific NLP (SciBERT) for unstructured intelligence extraction, executes automated half-life decay modeling on Indicators of Compromise (IoCs), and provides an immersive 3D/geospatial tactical operating picture.

---

## Visual Tactical Overview

| Operational Interface | Key Functional Capability | Engineering & Visual Stack |
|---|---|---|
| ![SOC Cockpit Overview](docs/assets/cockpit_overview.gif) | **Interactive SOC Operational Cockpit**<br/>Aggregated telemetry feeds, live threat metrics, global threat risk index computation, and prioritized incident cards. | Next.js 14 (App Router), Tailwind CSS, Zustand reactive store, SSE real-time stream. |
| ![3D Global Threat Map](docs/assets/threat_map_3d.png) | **Geospatial Battleground Matrix (ThreatMap3D)**<br/>3D hardware-accelerated globe tracing dynamic Bezier attack trajectories between adversary ASNs and monitored assets. | WebGL, deck.gl ArcLayer, MapLibre GL, MaxMind GeoLite2 City localization. |
| ![Cytoscape Threat Graph](docs/assets/cytoscape_graph.png) | **Relational Adversary Graph (ThreatGraph)**<br/>Multi-hop graph topology displaying causal links between threat actors, malware strains, CVEs, and targeted industries. | Cytoscape.js (`cose-bilkent` physics layout), Neo4j Cypher pathfinding engine. |

> *Visual assets archived in [`docs/assets/`](docs/assets/).*

---

## Table of Contents

- [Executive Summary](#executive-summary)
- [System Architecture](#system-architecture)
- [Visual Tactical Overview](#visual-tactical-overview)
- [Core Engineering Pillars](#core-engineering-pillars)
  - [1. Multi-Source OSINT Harvester & TAXII Ingestion](#1-multi-source-osint-harvester--taxii-ingestion)
  - [2. SciBERT NLP & Named Entity Recognition](#2-scibert-nlp--named-entity-recognition)
    - [Quantitative ML Benchmark Evaluation](#quantitative-ml-benchmark-evaluation)
    - [Scientific Justification: SciBERT vs. Generic Base BERT](#scientific-justification-scibert-vs-generic-base-bert)
  - [3. Mathematical IoC Decay & Confidence Engine](#3-mathematical-ioc-decay--confidence-engine)
  - [4. Polyglot Persistence & Graph Synthesis](#4-polyglot-persistence--graph-synthesis)
    - [Architectural Justification & Consistency Guarantees (ADR-001)](#architectural-justification--consistency-guarantees-adr-001)
  - [5. Cognitive Copilot & RAG Pipeline](#5-cognitive-copilot--rag-pipeline)
  - [6. Tactical 3D Geospatial & Graph Visualizer](#6-tactical-3d-geospatial--graph-visualizer)
- [Technology Stack](#technology-stack)
- [Directory Structure](#directory-structure)
- [Prerequisites & Environment Configuration](#prerequisites--environment-configuration)
- [Installation & Deployment](#installation--deployment)
  - [Option A: Production Deployment (Docker Compose)](#option-a-production-deployment-docker-compose)
  - [Option B: Local Development (Bare Metal / Standalone)](#option-b-local-development-bare-metal--standalone)
  - [Option C: One-Click Windows Launchers](#option-c-one-click-windows-launchers)
- [Verification & Automated Test Suite](#verification--automated-test-suite)
- [Standards & Interoperability](#standards--interoperability)
- [Academic & Engineering Context](#academic--engineering-context)
- [License](#license)

---

## Executive Summary

Modern cybersecurity operations face an acute signal-to-noise crisis: threat feeds bombard defensive infrastructure with hundreds of thousands of ephemeral, uncurated indicators daily. Traditional Threat Intelligence Platforms (TIPs) suffer from indicator rot, static scoring models, vendor lock-in, and sluggish correlation capabilities.

**Onyx Engine** addresses these systemic challenges through four architectural breakthroughs:
1. **Dynamic Mathematical Decay**: Instead of treating IoCs as binary blacklists, Onyx implements half-life decay algorithms ($S(t) = S_0 \cdot 2^{-t / t_{1/2}}$) categorized by indicator resilience (IPv4, Domains, Hashes, C2 infrastructure, and YARA rules), ensuring active indicators receive priority while obsolete entries degrade automatically.
2. **Autonomous Multi-Source Triangulation**: Live feeds from Abuse.ch, AlienVault OTX, CISA KEV, GDELT, and MITRE ATT&CK are continuously ingested, deduplicated, scored, and cross-correlated.
3. **Deep Linguistic Entity Extraction**: An offline-capable SciBERT transformer pipeline transforms unstructured intelligence documents, pastebin dumps, and dark web transcripts into structured STIX 2.1 bundles with TTP mappings.
4. **Zero-Latency Telemetry & Polyglot Graphs**: High-speed Redis Pub/Sub events stream intelligence directly to a WebGL/deck.gl tactical globe and Cytoscape/3D relational graph within milliseconds.

---

## System Architecture

```mermaid
flowchart TD
    subgraph INGESTION ["1. Ingestion Layer"]
        OSINT["OSINT Feeds (15+ Sources)<br/>URLhaus, ThreatFox, OTX, CISA KEV"]
        TAXII["TAXII 2.1 Ingestor / Feeds"]
        CRAWLER["Darkweb & Clearweb Spiders<br/>(Tor Circuit Rotation)"]
    end

    subgraph PROCESSING ["2. Processing & Analysis Engine"]
        NLP["SciBERT NLP Engine<br/>Named Entity Recognition (NER)"]
        DECAY["Mathematical Decay Engine<br/>Half-Life Decay & Confidence Composite"]
        CORRELATION["Behavioral Convergence<br/>& Alias Disambiguation"]
        STIX["STIX 2.1 Normalization Engine"]
    end

    subgraph STORAGE ["3. Polyglot Persistence Layer"]
        PG[("PostgreSQL 15<br/>Relational Schemas & Auth")]
        MONGO[("MongoDB 7<br/>STIX Bundles & Raw Telemetry")]
        NEO4J[("Neo4j 5<br/>Threat Actor Knowledge Graph")]
        ES[("Elasticsearch 8<br/>Distributed Full-Text & Analytics")]
        REDIS[("Redis 7<br/>Pub/Sub Event Bus & Caching")]
        QDRANT[("Qdrant Vector DB<br/>RAG Semantic Embeddings")]
    end

    subgraph GATEWAY ["4. Application Gateway & API"]
        FASTAPI["FastAPI 0.115 Core Server<br/>REST Endpoints + WebSockets + GraphQL"]
        GUARDRAILS["AI Security Filter & Guardrails"]
        COPILOT["Onyx Copilot (RAG + Gemini 2.5)"]
    end

    subgraph PRESENTATION ["5. Presentation Layer (Next.js 14 SOC Cockpit)"]
        DASH["Executive Dashboard (KPIs & Risk Matrix)"]
        MAP3D["ThreatMap3D (deck.gl / MapLibre)"]
        GRAPH3D["ThreatGraph (Cytoscape / Orbital 3D)"]
        SIEM["SIEM Rule Generator (SIGMA / YARA / Snort)"]
        STIXVIEW["OASIS STIX 2.1 Bundle Inspector"]
    end

    INGESTION --> PROCESSING
    PROCESSING --> STORAGE
    STORAGE --> GATEWAY
    GATEWAY --> PRESENTATION
```

---

## Core Engineering Pillars

### 1. Multi-Source OSINT Harvester & TAXII Ingestion
Onyx Engine integrates with **15+ high-fidelity intelligence feeds** natively:
- **Zero-Key Operational Sources**:
  - **CISA KEV** (Known Exploited Vulnerabilities catalog)
  - **GDELT Project 2.0** (Global geopolitical cyber incident streams)
  - **MITRE ATT&CK Enterprise v14** (Adversary profiles, tactics, techniques)
  - **OpenPhish** (Real-time zero-day phishing telemetry)
  - **Tor Exit Node Directory** (Active anonymization relay lists)
  - **NVD / NIST CVE Stream** (National Vulnerability Database)
  - **CIRCL OSINT** (Computer Incident Response Center Luxembourg feeds)
- **API Key Enhanced Feeds**:
  - **Abuse.ch Ecosystem**: URLhaus, ThreatFox, MalwareBazaar, Feodo Tracker
  - **AlienVault OTX**: Pulses, targeted adversaries, indicator indicators
  - **AbuseIPDB**: High-velocity crowd-sourced IP reputation verification
  - **VirusTotal**: Multi-engine static/dynamic payload inspection

All outbound external requests pass through a consolidated server-side proxy route (`/api/proxy/[source]`) with built-in cache layers, rate limiting, and defensive header sanitization.

---

### 2. SciBERT NLP & Named Entity Recognition
The NLP subsystem (`onyx-nlp`) leverages specialized transformer models (`allenai/scibert_scivocab_uncased` and spaCy pipelines) to process unstructured threat advisories:
- **Automated Entity Disambiguation**: Extracts threat actors, malware strains, IPv4/v6 addresses, domains, registry keys, and CVE identifiers.
- **TTP Alignment**: Discovers tactic/technique descriptions in prose and maps them to MITRE ATT&CK technique IDs (e.g., Process Hollowing $\to$ `T1055.012`).
- **Defanging / Refanging Logic**: Automatically sanitizes malicious URLs and indicators (`hxxp[://]bad[.]com` $\to$ `http://bad.com`) during lexical parsing.

#### Quantitative ML Benchmark Evaluation
To validate extraction efficacy under production CTI constraints, the pipeline was quantitatively benchmarked against a curated ground-truth dataset (`onyx-nlp/data/eval_benchmark.json`) comprising 50 dense threat reports (CISA advisories, Unit42 telemetry, Microsoft Defender intelligence):

| Entity Category | Precision | Recall | F1-Score | True Positives (TP) | False Positives (FP) | False Negatives (FN) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **ThreatActor** | 96.97% | 100.00% | **98.46%** | 32 | 1 | 0 |
| **Malware** | 96.67% | 100.00% | **98.31%** | 29 | 1 | 0 |
| **CVE_ID** | 100.00% | 100.00% | **100.00%** | 17 | 0 | 0 |
| **IPv4_IoC** | 100.00% | 100.00% | **100.00%** | 36 | 0 | 0 |
| **MITRE_TTP** | 77.78% | 100.00% | **87.50%** | 21 | 6 | 0 |
| **Macro Average** | **94.28%** | **100.00%** | **96.85%** | **135** | **8** | **0** |

- **Mean Inference Latency**: **0.12 ms/document** (sub-millisecond streaming extraction)
- **Evaluation Throughput**: **>8,200 documents/second** (deterministic CPU execution)
- **Reproducibility**: Run `python onyx-nlp/evaluate_benchmarks.py` or `python scripts/benchmark_nlp.py`.

#### Scientific Justification: SciBERT vs. Generic Base BERT
Standard general-purpose language models (such as `bert-base-uncased` trained on Wikipedia/BookCorpus) fail systematically on dense cybersecurity telemetry due to vocabulary mismatch:
1. **Tokenization Pathology**: Generic WordPiece tokenizers shatter domain-specific cryptographic hashes, CVE strings, and zero-day identifiers into fragmented subwords (`cve-2023-38831` becomes `['cv', '##e', '-', '202', '##3', '-', '38', '##83', '##1']`), diluting self-attention weights and crippling boundary detection.
2. **SciBERT In-Domain Pre-training**: `allenai/scibert_scivocab_uncased` is pre-trained on a corpus of 1.14M scientific and computer science papers. Its specialized WordPiece vocabulary preserves dense technical nomenclature intact.
3. **Hybrid Neuro-Symbolic Architecture**: While deep neural transformers excel at contextual semantic disambiguation (differentiating between *Bear* as an animal vs. *Cozy Bear* as an APT), they lack deterministic guarantees on formal network syntaxes. Onyx couples SciBERT with validated regular expression grammars and RFC-compliant defangers, ensuring mathematical zero false-positive extraction for IPv4/IPv6, CIDR blocks, and CVE identifiers while retaining state-of-the-art transformer contextual entity tagging.

---

### 3. Mathematical IoC Decay & Confidence Engine
Indicators in Onyx undergo mathematical degradation modeled as an exponential half-life curve:

$$S(t) = S_0 \cdot 2^{-\frac{\Delta t}{t_{1/2}}}$$

Where:
- $S_0 \in [0, 1]$: Initial confidence score assigned at ingestion.
- $\Delta t$: Elapsed time since last corroboration or observation.
- $t_{1/2}$: Domain-specific half-life period:
  - **Fast-Flux / Cloud IPs**: $t_{1/2} = 24\text{ hours}$
  - **Standard IPv4 / Domains**: $t_{1/2} = 168\text{ hours (7 days)}$
  - **Bulletproof Hosters / C2**: $t_{1/2} = 720\text{ hours (30 days)}$
  - **Cryptographic File Hashes (SHA256)**: $t_{1/2} = \infty$ (Floor $S_{\text{min}} = 0.90$, immutable artifact)

#### Composite Confidence Formulation:
The platform calculates a Bayesian composite confidence score:

$$C_{\text{composite}} = w_{\text{source}} \cdot R_{\text{source}} + w_{\text{corroboration}} \cdot \Phi(N) + w_{\text{temporal}} \cdot S(t) - P_{\text{contested}}$$

Where $\Phi(N) = 1 - e^{-\lambda N}$ models multi-source corroboration asymptotic saturation.

---

### 4. Polyglot Persistence & Graph Synthesis
Onyx Engine implements a tailored polyglot storage architecture:
- **PostgreSQL 15**: Relational integrity, user roles (RBAC), authentication tokens, and audit logs.
- **MongoDB 7**: High-throughput STIX 2.1 JSON document persistence with compound indices.
- **Neo4j 5**: Native graph database executing Cypher queries for deep graph traversal:
  $$\text{(ThreatActor)} \xrightarrow{\text{USES}} \text{(TTP)} \xrightarrow{\text{TARGETS}} \text{(Sector)} \xleftarrow{\text{OBSERVED\_IN}} \text{(IoC)}$$
- **Elasticsearch 8**: Real-time distributed search across millions of telemetry events.
- **Redis 7**: Sub-millisecond pub/sub message bus, rate limit tracking, and session cache.

#### Architectural Justification & Consistency Guarantees (ADR-001)

Admissions and enterprise architectural reviews frequently query why a distributed threat intelligence platform utilizes **six distinct storage engines**. The answer lies in strict **Workload Isolation** and **Distributed Consistency Semantics**:

```mermaid
flowchart LR
    A["Raw Ingest Telemetry"] --> B["Deterministic STIX UUIDv5"]
    B --> C["PostgreSQL<br/>(ACID: Auth & RBAC)"]
    B --> D["MongoDB<br/>(Base Document Store)"]
    B --> E["Neo4j<br/>(Index-Free Adjacency Graph)"]
    B --> F["Elasticsearch<br/>(Inverted-Index Full Text)"]
    B --> G["Qdrant<br/>(Dense Vector Embeddings)"]
    B --> H["Redis<br/>(Sub-ms In-Memory Pub/Sub)"]
```

##### 1. Workload Isolation Matrix
No single storage paradigm can simultaneously optimize for transactional ACID operations, multi-hop graph pathfinding, inverted full-text search, and dense vector embeddings without incurring severe performance degradation:

| Engine | Storage Paradigm | Primary Invariant | Justification vs. Alternatives |
|---|---|---|---|
| **PostgreSQL 15** | Relational (RDBMS) | Strict ACID Transactions | Guarantees non-repudiation and strict consistency for multi-tenant RBAC, JWT revocation lists, and compliance audit logs. |
| **MongoDB 7** | Document (BSON) | Schema Flexibility | OASIS STIX 2.1 entities feature deeply nested polymorphic JSON payloads. Document-level sharding allows ingesting heterogeneous feed schemas without costly schema migrations. |
| **Neo4j 5** | Native Graph (LPG) | Index-Free Adjacency | Relational $N$-table joins degrade exponentially ($O(k^d)$) on 4-hop adversary queries (`Actor → Tool → Technique → Vulnerability → Target`). Neo4j traverses relationships in $O(1)$ constant time per hop. |
| **Elasticsearch 8** | Inverted Index | Sub-second Free-Text & BM25 | Enables fuzzy lexical search across tens of millions of raw threat logs, regex indicator matching, and real-time aggregations (e.g. top targeted ASNs in last 24h). |
| **Qdrant** | Approximate Nearest Neighbor | Cosine Similarity in $\mathbb{R}^{768}$ | Powers the Cognitive Copilot's RAG pipeline, matching analyst queries with historical incident post-mortems via high-dimensional vector embeddings. |
| **Redis 7** | In-Memory Key-Value | Sub-millisecond Latency | Decouples async ingestion from WebSocket broadcast via Redis Streams & Pub/Sub, while serving as a distributed rate-limiter and decay score cache. |

##### 2. Distributed Consistency & Idempotent Ingestion
In a distributed event-driven pipeline, worker retries and overlapping OSINT feeds inevitably produce duplicate telemetry. Onyx Engine enforces cross-engine consistency through **Deterministic Identity Formulation**:

- **OASIS STIX 2.1 UUIDv5 Generation**: Every indicator ID is derived using RFC 4122 UUIDv5 hashing over a fixed STIX namespace:
  $$\text{ID} = \text{"indicator--" } + \text{UUIDv5}(\text{NAMESPACE\_STIX}, \text{"canonical\_type:canonical\_value"})$$
- **Idempotent Upsert Semantics**:
  - In **MongoDB**: Uses `{upsert: true}` indexed uniquely on `id`.
  - In **Neo4j**: Uses Cypher `MERGE (i:Indicator {id: $id}) ON CREATE SET ... ON MATCH SET ...`.
  - In **Elasticsearch**: Uses doc ID `_id = stix_id` with versioning, preventing document duplication.
- Even if Celery workers retry an ingestion task multiple times or disparate feeds (e.g., both URLhaus and ThreatFox) report the identical malicious IP, no duplicate nodes or records are created across the storage topology.

---

### 5. Cognitive Copilot & RAG Pipeline
- **Large Language Model Integration**: Google Gemini 2.5 Flash integrated with temperature modulation and strict cybersecurity prompt engineering.
- **Retrieval-Augmented Generation (RAG)**: Connects to a Qdrant Vector Store indexing threat profiles and historical incident reports with dense vector embeddings.
- **Security Guardrails**: Input/output lexical sanitizers, prompt injection mitigation, and automated SIEM rule verification.

---

### 6. Tactical 3D Geospatial & Graph Visualizer
- **ThreatMap3D**: Built on **deck.gl** and **MapLibre GL**, rendering global 3D Bezier arcs connecting adversary infrastructure (origin ASN/country) to targeted SOC assets with real-time particle animation.
- **ThreatGraph Orbital Matrix**: Built on **Cytoscape.js** with `cose-bilkent` and `dagre` physics layout algorithms, visualizing multi-tiered relationships between nation-state actors, malware families, CVEs, and affected industries.

---

## Technology Stack

| Domain | Technology / Library | Version | Purpose |
|---|---|---|---|
| **Frontend Framework** | [Next.js](https://nextjs.org/) (App Router) | `14.2` | Production React SSR & edge API routing |
| **Frontend Language** | [TypeScript](https://www.typescriptlang.org/) | `5.0+` | Strict-mode type safety throughout |
| **Styling** | [Tailwind CSS](https://tailwindcss.com/) | `3.4` | Cyberpunk / SOC dark-mode theme system |
| **Geospatial 3D** | [deck.gl](https://deck.gl/) + [MapLibre GL](https://maplibre.org/) | `9.2 / 5.2` | WebGL hardware-accelerated globe & arcs |
| **Network Graphs** | [Cytoscape.js](https://js.cytoscape.org/) | `3.33` | Directed threat topologies & graph physics |
| **State Management**| [Zustand](https://github.com/pmndrs/zustand) | `5.0` | High-frequency telemetry state stores |
| **Backend API** | [FastAPI](https://fastapi.tiangolo.com/) | `0.115` | Async ASGI REST, WebSocket & GraphQL API |
| **Backend Language** | [Python](https://www.python.org/) | `3.11 / 3.12` | Core computing runtime |
| **ASGI Server** | [Uvicorn](https://www.uvicorn.org/) | `0.29+` | High-concurrency worker event loop |
| **NLP & AI Engine** | [SciBERT](https://github.com/allenai/scibert) + [spaCy](https://spacy.io/) | Transformers | Deep textual entity extraction & TTP tagging |
| **GenAI & Vector** | [Gemini 2.5 Flash](https://ai.google.dev/) + [Qdrant](https://qdrant.tech/) | Latest | Autonomous Copilot & RAG vector search |
| **Relational DB** | [PostgreSQL](https://www.postgresql.org/) | `15-alpine` | Users, authentication, persistent configurations |
| **Document Store** | [MongoDB](https://www.mongodb.com/) | `7.0` | STIX 2.1 entities, dynamic reports, raw telemetry |
| **Graph Database** | [Neo4j](https://neo4j.com/) | `5-community` | Relational threat actor graph intelligence |
| **Search Engine** | [Elasticsearch](https://www.elastic.co/) | `8.13` | Distributed multi-field IoC search & aggregation |
| **Event Broker** | [Redis](https://redis.io/) | `7-alpine` | WebSocket hub, pub/sub streams, distributed cache |
| **Task Queue** | [Celery](https://docs.celeryq.dev/) | `5.3+` | Asynchronous OSINT ingestors & decay loops |
| **Anonymization** | [Tor](https://www.torproject.org/) + Privoxy | Latest | Darkweb crawler proxy with circuit rotation |

---

## Directory Structure

```text
onyx-engine/
├── .github/
│   └── workflows/
│       └── ci.yml                   # Automated GitHub Actions test & type-check pipeline
├── .env.example                     # Environment configuration template
├── .gitignore                       # Production gitignore (security hardened)
├── docker-compose.yml               # Multi-service container orchestration
├── Dockerfile.backend               # Multi-stage production Python ASGI build
├── Makefile                         # Unified operations and build targets
├── requirements.txt                 # Flat backend dependency specification
├── start_ONYX_demo.bat              # Zero-config Windows demo launcher
├── start_ONYX_full.bat              # Full-stack Windows orchestration launcher
│
├── onyx-api/                        # FastAPI REST, WebSocket & GraphQL Engine
│   ├── onyx_api/
│   │   ├── auth/                    # JWT token management & RBAC security
│   │   ├── routers/                 # Modular API endpoints (iocs, actors, taxii, etc.)
│   │   ├── services/                # Business logic (Gemini, GeoIP, RAG, OSINT)
│   │   ├── utils/                   # Guardrails and defensive filters
│   │   └── workers/                 # Background workers (Decay, OSINT poller, RSS)
│   ├── migrations/                  # Database migration scripts
│   ├── data/                        # Offline MaxMind GeoLite2 City database
│   ├── tests/                       # API endpoint verification test suite
│   └── pyproject.toml               # Python package configuration
│
├── onyx-core/                       # Shared Domain Core & Mathematical Engines
│   ├── onyx_core/
│   │   ├── models/                  # OASIS STIX 2.1, Threat Actor, IoC schemas
│   │   └── services/                # Database clients (Mongo, ES, PG, Neo4j, Redis)
│   │       ├── decay_engine.py      # Half-life exponential decay implementation
│   │       └── confidence_composite.py # Bayesian multi-factor confidence scoring
│   ├── tests/
│   │   ├── unit/                    # 81 property-based tests (Hypothesis + Pytest)
│   │   └── integration/             # Database-backed integration scenarios
│   └── pyproject.toml               # Core package specifications
│
├── onyx-nlp/                        # Scientific NLP & Machine Learning Engine
│   ├── onyx_nlp/
│   │   ├── extractors/              # SciBERT IoC & TTP extraction pipelines
│   │   └── processors/              # Document preprocessing & defanging
│   ├── data/
│   │   └── eval_benchmark.json      # 50-document empirical ground-truth benchmark set
│   ├── evaluate_benchmarks.py       # Reproducible quantitative NLP evaluation script
│   └── pyproject.toml
│
├── onyx-crawlers/                   # Intelligence Harvesters & Darkweb Spiders
│   ├── onyx_crawlers/
│   │   ├── clearweb/                # GitHub and Pastebin secret & leak monitors
│   │   └── darkweb/                 # Tor-proxied .onion crawlers & ransomware blogs
│   └── pyproject.toml
│
├── onyx-dashboard/                  # Next.js 14 SOC Cockpit (App Router)
│   ├── src/
│   │   ├── app/                     # Next.js routes & server-side API proxies
│   │   ├── components/              # 35+ React SOC operational components
│   │   │   ├── ThreatMap3D.tsx      # deck.gl WebGL tactical globe
│   │   │   ├── ThreatGraph.tsx      # Cytoscape.js threat network graph
│   │   │   ├── ExecutiveDashboard.tsx # SOC KPI matrix & alert feeds
│   │   │   ├── OnyxCopilot.tsx      # Interactive AI tactical advisor
│   │   │   └── SIEMRuleConverter.tsx # SIGMA / YARA / Snort automated exporter
│   │   ├── lib/                     # 15+ OSINT client connectors & state stores
│   │   └── styles/                  # Tailwind CSS variables & tokens
│   ├── Dockerfile.frontend          # Multi-stage optimized Node.js Alpine build
│   └── package.json                 # Dashboard frontend dependencies
│
├── infra/                           # Infrastructure configurations
│   ├── elasticsearch/               # Index lifecycle & mapping settings
│   ├── mongodb/                     # Init scripts & collection indices
│   └── tor/                         # Tor daemon, Privoxy & circuit rotator
│
├── docs/
│   └── assets/                      # UI screenshots and visual media directory
│
└── scripts/                         # Operational & stress-testing utilities
    ├── benchmark_nlp.py             # Convenience wrapper for NLP benchmark evaluation
    ├── exhibition_injector.py       # Realistic APT29 / LockBit STIX injector
    └── verify_flow.py               # Zero-latency GeoIP Redis validation script
```

---

## Prerequisites & Environment Configuration

### System Prerequisites
- **Node.js**: $\ge 18.18$ (Node 20 LTS recommended)
- **Python**: $\ge 3.11$ (Python 3.12 verified)
- **Docker & Docker Compose**: Docker Desktop 4.25+ or Docker Engine with `compose` plugin
- **Memory**: Minimum 8 GB RAM (16 GB recommended for full Docker polyglot stack)

### Environment Configuration
Copy the configuration template to `.env`:
```bash
cp .env.example .env
```

Key environment parameters in `.env`:
```ini
# General Settings
ONYX_ENV=development
ONYX_DEBUG=true
ONYX_SECRET_KEY=<64-char-random-hex>

# API & Networking
ONYX_API_HOST=0.0.0.0
ONYX_API_PORT=8000
ONYX_API_CORS_ORIGINS=["http://localhost:3000"]

# Database Credentials
POSTGRES_USER=onyx_admin
POSTGRES_PASSWORD=onyx_pg_secret_2026
REDIS_PASSWORD=onyx_redis_secret_2026
NEO4J_PASSWORD=onyx_graph_secret_2026
MONGODB_PASSWORD=onyx_mongo_secret_2026
ELASTICSEARCH_PASSWORD=onyx_elastic_secret_2026

# AI & RAG Subsystem (Optional - Platform provides graceful mock fallbacks)
GEMINI_API_KEY=<your-google-ai-studio-api-key>
GEMINI_MODEL=gemini-2.5-flash
QDRANT_URL=
QDRANT_API_KEY=

# OSINT Feed Keys (Optional - Free-tier feeds operate out of the box)
URLHAUS_API_KEY=
THREATFOX_API_KEY=
OTX_API_KEY=
OSINT_ABUSEIPDB_API_KEY=
OSINT_VIRUSTOTAL_API_KEY=
```

---

## Installation & Deployment

### Option A: Production Deployment (Docker Compose)
To launch the complete distributed stack with all databases, backend, and dashboard containerized:

```bash
# 1. Clone the repository
git clone https://github.com/kash-talel/onyx-engine.git
cd onyx-engine

# 2. Build and launch all services in detached mode
docker compose up -d --build

# 3. Inspect running services
docker compose ps

# 4. Tail aggregated logs
docker compose logs -f
```

The services will be available at:
- **SOC Cockpit (Dashboard)**: `http://localhost:3000`
- **Backend API & Swagger Docs**: `http://localhost:8000/docs`
- **Neo4j Browser**: `http://localhost:7474`
- **Elasticsearch Cluster**: `http://localhost:9200`

---

### Option B: Local Development (Bare Metal / Standalone)
Onyx Engine features an autonomous **Standalone Fallback Mode**: if external database containers are not running, the backend seamlessly initializes in-memory caches, offline GeoLite2 localization, and live OSINT fallback feeds.

```bash
# Terminal 1: Backend API
cd onyx-api
pip install -r ../requirements.txt
pip install -e ../onyx-core
pip install -e .
python -m uvicorn onyx_api.main:app --host 0.0.0.0 --port 8000 --reload

# Terminal 2: Dashboard Frontend
cd onyx-dashboard
npm install
npm run dev
```

Navigate to `http://localhost:3000` to interact with the platform.

---

### Option C: One-Click Windows Launchers
For Windows workstations, automated batch scripts manage path resolution, process health, and multi-window startup:
- **`start_ONYX_full.bat`**: Comprehensive launcher that kills orphan processes, builds paths, starts backend and frontend, and launches the browser.
- **`start_ONYX_demo.bat`**: Quick launcher that boots backend in standalone mode and fires the SciBERT stress test.

---

## Verification & Automated Test Suite

Onyx Engine includes an extensive, enterprise-grade test suite covering mathematical decay invariants, Bayesian confidence weights, source reliability matrix properties, API contract validity, and empirical NLP extraction accuracy.

To run the complete test suite:
```bash
# Unit & Contract Tests (82 passed)
make test

# Or directly with pytest
python -m pytest onyx-core/tests/unit -v
python -m pytest onyx-api/tests -v

# Quantitative NLP Benchmark Evaluation
python onyx-nlp/evaluate_benchmarks.py
```

### Test Results Breakdown:
- **`test_decay_engine.py`**: Validates exponential half-life properties, half-life exactness at $t = t_{1/2}$, monotonicity, boundary adherence in $[0, 1]$, and state classification (`valid`, `degrading`, `stale`, `obsolete`).
- **`test_confidence_composite.py`**: Verifies Bayesian source reliability matrices, contextual relevance sector bounds, contestation penalties, and analyst override idempotence.
- **`test_api_health.py`**: Validates HTTP 200 liveness probes and telemetry payload schema integrity.
- **`evaluate_benchmarks.py`**: Measures empirical Precision (94.28%), Recall (100.00%), and Macro F1 (96.85%) across 5 core CTI entity categories.

**Status**: `82 passed, 0 failures` (100% pass rate).

---

## Standards & Interoperability

| Standard | Specification | Implementation in Onyx |
|---|---|---|
| **STIX 2.1** | OASIS Standard | Full serialization & parsing (`ThreatActor`, `Indicator`, `Malware`, `AttackPattern`, `Relationship`, `Report`) |
| **TAXII 2.1** | OASIS Standard | Endpoints for discovery (`/taxii2/`), API roots, collections, and envelope ingest |
| **MITRE ATT&CK** | Enterprise Matrix v14 | Automatic technique mapping and kill-chain phase alignment |
| **TLP 2.0** | FIRST Standards | Traffic Light Protocol markings (`WHITE`, `GREEN`, `AMBER`, `AMBER+STRICT`, `RED`) |
| **SIGMA** | Generic SIEM Rule Format | Automated conversion of detected IoCs to production SIGMA rules |
| **YARA** | Pattern Matching | Automated compilation of file and byte sequence signatures |
| **Snort / Suricata**| Network IDS Rules | Automatic IDS rule generation from IPv4 and domain indicators |

---

## Academic & Engineering Context

This platform represents the culmination of advanced engineering and academic research in **Cyber Threat Intelligence, Applied Deep Learning in Defense Systems, and High-Performance Distributed Computing**.

### Academic Heritage & Foundation
Onyx Engine originated as an undergraduate Bachelor's Capstone Project (*Projet de Fin d'Études — PFE*) at the **Faculté des Sciences de Sfax (FSS), Tunisia**, where it was evaluated by a faculty jury and awarded the exceptional grade of:

$$\mathbf{18.75 / 20 \quad \text{—} \quad \text{First Class Honors with Highest Distinction}}$$

Following this academic achievement, the project underwent a comprehensive architectural overhaul, evolving from an academic prototype into a production-grade, distributed cyber threat intelligence platform featuring polyglot persistence, formal STIX 2.1/TAXII 2.1 protocol engines, SciBERT neural extraction, and mathematical decay models.

### Key Research Contributions:
1. **Empirical Indicator Life-Cycle Modeling**: Formulation and implementation of algorithmic decay for threat indicators to eliminate defensive telemetry saturation.
2. **Cognitive Triangulation**: Fusion of deterministic threat feeds with transformer-based NLP and Large Language Model reasoning under strict safety guardrails.
3. **Hardware-Accelerated Situational Awareness**: Bringing military-grade 3D geospatial intelligence visualization to standard browser environments via WebGL shaders and deck.gl.
4. **Idempotent Polyglot Architecture**: Deterministic RFC 4122 UUIDv5 identity formulation ensuring cross-engine consistency across 6 isolated data stores.

### Author & Engineering Lead:
- **Mahdi Ghozzi** ([@kash-talel](https://github.com/kash-talel))  
  *M.Sc. Candidate in Systems, Networks, and Cloud Computing*  
  **Faculté des Sciences de Sfax (FSS)**, Université de Sfax, Tunisia  
  Email: [ghozzim770@gmail.com](mailto:ghozzim770@gmail.com) | GitHub: [@kash-talel](https://github.com/kash-talel)

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for complete details.
