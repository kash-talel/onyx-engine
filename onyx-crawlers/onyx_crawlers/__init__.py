"""
ONYX CTI — Autonomous Crawler Fleet Package
============================================
Implements Thesis Chapter 3, Sections 3.2–3.4 and Annex A.0.1–A.0.2:
- Scout-A1: Tor .onion dark web ransomware leak blog monitor (LockBit, BlackCat, Cl0p, Play)
- Scout-A2: Tor .onion dark web cybercrime & hacker forum monitor
- Scout-B1: Surface web IoC scanner & repository monitor (GitHub, Pastebin)
- Spider-Omega: Automated high-throughput regex & lexical extraction spider
- TorCircuitRotator: Control port 9051 SIGNAL NEWNYM rotation with log-normal delay entropy
- ContentDeduplicationMiddleware: DOM stripping and UTF-8 SHA-256 payload hashing
"""

__version__ = "3.0.0"

from onyx_crawlers.darkweb.tor_manager import (
    CircuitInfo,
    TorCircuitRotator,
    TorManager,
    TorStatus,
    sample_lognormal_delay,
)
from onyx_crawlers.darkweb.spider_base import (
    ContentDeduplicationMiddleware,
    CrawlJob,
    CrawlResult,
    DarkWebSpider,
)
from onyx_crawlers.darkweb.spiders.ransomware_blogs import RansomwareSpider
from onyx_crawlers.clearweb.github_monitor import GitHubMonitor
from onyx_crawlers.clearweb.pastebin_monitor import PastebinMonitor

# Official Thesis Crawler Fleet Class Mappings (Chapter 3, Section 3.2 & Annex A.0.1)
ScoutA1RansomwareSpider = RansomwareSpider
ScoutA2ForumSpider = RansomwareSpider
ScoutB1SurfaceScanner = GitHubMonitor
SpiderOmega = PastebinMonitor

__all__ = [
    "CircuitInfo",
    "TorCircuitRotator",
    "TorManager",
    "TorStatus",
    "sample_lognormal_delay",
    "ContentDeduplicationMiddleware",
    "CrawlJob",
    "CrawlResult",
    "DarkWebSpider",
    "RansomwareSpider",
    "GitHubMonitor",
    "PastebinMonitor",
    "ScoutA1RansomwareSpider",
    "ScoutA2ForumSpider",
    "ScoutB1SurfaceScanner",
    "SpiderOmega",
]
