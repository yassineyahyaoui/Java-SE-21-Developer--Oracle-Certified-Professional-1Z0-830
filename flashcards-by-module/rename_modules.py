"""Rename module-NN.md to module-NN-slug.md. Run from flashcards-by-module/ or course root."""
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
SLUGS = {
    "01": "introduction-to-java-se-21-certification",
    "02": "introduction-to-java-and-environment-setup",
    "03": "basics-of-java",
    "04": "operators",
    "05": "array",
    "06": "control-flow-statements",
    "07": "methods",
    "08": "java-object-oriented-concept",
    "09": "java-object-oriented-programming",
    "10": "wrapper-classes-autoboxing-unboxing",
    "11": "strings",
    "12": "collections",
    "13": "exception-handling",
    "14": "enum-types",
    "15": "lambda-expression",
    "16": "stream-api",
    "17": "date-time",
    "18": "java-io",
    "19": "overview-of-threads",
    "20": "thread-creation-and-management",
    "21": "synchronization-and-concurrency-control",
    "22": "high-level-concurrency-apis",
    "23": "thread-coordination",
    "24": "locks-and-advanced-synchronization",
    "25": "concurrent-collections",
    "26": "performance-and-scalability",
    "27": "jvm-and-threads",
    "28": "best-practices-and-advanced-topics",
    "29": "case-studies-and-practical-scenarios",
    "30": "tools-and-testing",
    "31": "mock-exam-java-se-21-developer",
    "32": "practice-exam",
    "33": "extra",
}

def main():
    for nn, slug in SLUGS.items():
        old_name = f"module-{nn}.md"
        new_name = f"module-{nn}-{slug}.md"
        old_path = os.path.join(BASE, old_name)
        new_path = os.path.join(BASE, new_name)
        if os.path.isfile(old_path) and not os.path.isfile(new_path):
            os.rename(old_path, new_path)
            print(f"Renamed {old_name} -> {new_name}")
        elif os.path.isfile(new_path):
            print(f"Skip (exists): {new_name}")

if __name__ == "__main__":
    main()
