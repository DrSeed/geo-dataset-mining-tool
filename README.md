# GEO Dataset Mining Tool

> Every bioinformatics meta-analysis starts the same way: manually searching GEO, downloading series matrix files one by one, fighting with platform annotations. This tool automates all of that.

## What This Tool Does

1. Searches GEO programmatically using your keywords
2. Downloads series matrix files for all matching datasets
3. Handles probe-to-gene mapping
4. Applies quantile normalisation for cross-study comparability
5. Exports clean, analysis-ready expression matrices

## Why Normalisation Matters for Meta-Analysis

Different platforms have different dynamic ranges. Quantile normalisation forces distributions to match, so cross-study differences reflect biology, not technology.

## Usage
```bash
python geo_miner.py --query "COPD alveolar macrophage" --organism "Homo sapiens" --max-datasets 20
```
