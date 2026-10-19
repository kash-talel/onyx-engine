"""
ONYX CTI — Convenience Wrapper for NLP Benchmark Evaluation
Run: python scripts/benchmark_nlp.py
"""

import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo_root / "onyx-nlp"))

from evaluate_benchmarks import run_benchmark, print_report

if __name__ == "__main__":
    benchmark_file = repo_root / "onyx-nlp" / "data" / "eval_benchmark.json"
    results = run_benchmark(benchmark_file)
    print_report(results)
