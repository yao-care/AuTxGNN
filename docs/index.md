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

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care, company registration
number 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

AuTxGNN is the Australia site of the company's "TxGNN Drug Repurposing" product line.
The same system is deployed across 30 countries and regions, each named `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, and so on) at `{cc}txgnn.yao.care`.
Product overview: <https://www.yao.care/medical/txgnn/>.

The TxGNN model itself was developed by the Zitnik Lab at Harvard Medical School and published
in *Nature Medicine*. This platform is the production system 藥提醒科技有限公司 built on top of that
model, covering national drug-registration data integration, dual knowledge-graph and
deep-learning prediction, PubMed / ClinicalTrials evidence grading, and SMART on FHIR
electronic health record integration.
