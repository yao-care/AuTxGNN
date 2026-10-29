---
layout: default
title: AuTxGNN - Australia Drug Repurposing Predictions
---

# AuTxGNN

Drug repurposing predictions for Australia using the TxGNN graph neural network.

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Australia: what this site covers

This site publishes reports for **{{ site.data.drug_stats.total_drugs }}** medicines listed in the registration data of [TGA](https://www.tga.gov.au/) (Australia).

Reports by evidence level: L1 {{ site.data.drug_stats.level_counts.L1 }} · L2 {{ site.data.drug_stats.level_counts.L2 }} · L3 {{ site.data.drug_stats.level_counts.L3 }} · L4 {{ site.data.drug_stats.level_counts.L4 }} · L5 {{ site.data.drug_stats.level_counts.L5 }}

### Highest evidence levels on this site

| Medicine | Evidence level |
|---|---|
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Hyaluronic Acid](/drugs/hyaluronic-acid/) | L1 |
| [Lanadelumab](/drugs/lanadelumab/) | L1 |
| [Rifabutin](/drugs/rifabutin/) | L1 |
| [Triptorelin](/drugs/triptorelin/) | L1 |
| [Candesartan](/drugs/candesartan/) | L1 |
| [Hydrocortisone](/drugs/hydrocortisone/) | L1 |
| [Hydrocortisone Acetate](/drugs/hydrocortisone-acetate/) | L1 |
| [Peginterferon Alfa-2A](/drugs/peginterferon-alfa-2a/) | L1 |

### Medicines covered only by this site among the 30 TxGNN sites

| Medicine | Evidence level |
|---|---|
| [Perhexiline](/drugs/perhexiline/) | L5 |
| [Alogliptin](/drugs/alogliptin/) | N/A |
| [Aluminium](/drugs/aluminium/) | N/A |
| [Bivalirudin](/drugs/bivalirudin/) | N/A |
| [Castor Oil](/drugs/castor-oil/) | N/A |
| [Chloroform](/drugs/chloroform/) | N/A |
| [Citrulline](/drugs/citrulline/) | N/A |
| [Dicloxacillin](/drugs/dicloxacillin/) | N/A |
| [Dornase Alfa](/drugs/dornase-alfa/) | N/A |
| [Ibandronate](/drugs/ibandronate/) | N/A |
| [Idarubicin](/drugs/idarubicin/) | N/A |
| [Lanthanum Carbonate](/drugs/lanthanum-carbonate/) | N/A |
| [Lercanidipine](/drugs/lercanidipine/) | N/A |
| [Phenelzine](/drugs/phenelzine/) | N/A |
| [Pizotifen](/drugs/pizotifen/) | N/A |

<!-- local-home:end -->

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
model, covering national drug-registration data integration, deep-learning prediction that excludes uses already recorded in the knowledge graph, PubMed / ClinicalTrials evidence grading, and SMART on FHIR
electronic health record integration.
