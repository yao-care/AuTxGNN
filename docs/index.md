---
layout: default
title: AuTxGNN - Australia Drug Repurposing Predictions
---

# AuTxGNN

Drug repurposing predictions for Australia using TxGNN knowledge graph.

## Overview

AuTxGNN uses graph neural networks to identify potential new therapeutic uses for existing drugs registered with the Australian Therapeutic Goods Administration (TGA).

## Data Sources

- **Drug Data**: Australian Register of Therapeutic Goods (ARTG)
- **Knowledge Graph**: TxGNN biomedical knowledge graph
- **Clinical Trials**: ClinicalTrials.gov, ANZCTR (Australian New Zealand Clinical Trials Registry)
- **Literature**: PubMed, Google Scholar

## API Access

### FHIR R4 API

Access prediction data via FHIR R4 resources:

- **Base URL**: `https://autxgnn.yao.care/fhir`
- **Capability Statement**: [/fhir/metadata](/fhir/metadata.json)

#### Available Resources

| Resource Type | Description |
|--------------|-------------|
| MedicationKnowledge | Drug information from ARTG |
| ClinicalUseDefinition | Predicted drug-disease indications |

## Disclaimer

**Research Use Only**: The predictions provided by AuTxGNN are for research purposes only and do not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.

This is not a TGA-approved tool. Always consult healthcare professionals for medical decisions.

## Contact

- Website: [yao.care](https://yao.care)
- GitHub: [yao-care/AuTxGNN](https://github.com/yao-care/AuTxGNN)

---

*Last updated: {{ site.time | date: "%Y-%m-%d" }}*
