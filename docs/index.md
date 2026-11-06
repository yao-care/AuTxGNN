---
layout: default
title: AuTxGNN - Australia Drug Repurposing Predictions
description: "TxGNN drug repurposing reports for 749 medicines listed on the PBS Schedule (Australia), with evidence levels L1–L5 from clinical trials and literature."
last_modified_at: 2026-11-04
---

# AuTxGNN

Drug repurposing predictions for Australia using the TxGNN graph neural network.

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Australia: what this site covers

This site publishes reports for **{{ site.data.drug_stats.total_drugs }}** medicines listed on the [PBS Schedule](https://data.pbs.gov.au/api/api-public.html) (Australia).

### This site's local data

| Item | Detail |
|------|--------|
| Dataset | PBS Schedule items (current schedule, CSV) |
| Publisher | Australian Department of Health, PBS public API |
| Download | <https://data-api.health.gov.au/pbs/api/v3/items> (API documentation: <https://data.pbs.gov.au/api/api-public.html>) |
| Item identifier | PBS item code |
| Updates | Automatic weekly download (every Monday) of the schedule currently in effect; an item that drops off the list keeps its previous status |

Details: [Data Sources]({{ '/sources/' | relative_url }}).

Reports by evidence level:

| Evidence level | Reports | Share |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

4 predicted drug–disease pairs on this site appear on no other of the 30 TxGNN sites.

### Highest evidence levels on this site

| Medicine | Evidence level |
|---|---|
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Peginterferon Alfa-2A](/drugs/peginterferon-alfa-2a/) | L1 |
| [Clomipramine](/drugs/clomipramine/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |
| [Ranitidine](/drugs/ranitidine/) | L1 |
| [Potassium](/drugs/potassium/) | L1 |
| [Atorvastatin](/drugs/atorvastatin/) | L1 |
| [Tacrolimus](/drugs/tacrolimus/) | L1 |
| [Dapsone](/drugs/dapsone/) | L1 |

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

- **Drug Data**: [PBS Schedule](https://data.pbs.gov.au/api/api-public.html) (Pharmaceutical Benefits Scheme)
- **Knowledge Graph**: TxGNN biomedical knowledge graph
- **Clinical Trials**: ClinicalTrials.gov, ANZCTR (Australian New Zealand Clinical Trials Registry)
- **Literature**: PubMed, Google Scholar

## API Access

### FHIR R4 API

Access prediction data via FHIR R4 resources:

- **Base URL**: `https://autxgnn.yao.care/fhir`
- **Capability Statement**: [/fhir/metadata](/fhir/metadata)

#### Available Resources

| Resource Type | Description |
|--------------|-------------|
| MedicationKnowledge | Drug information from the PBS Schedule |
| ClinicalUseDefinition | Predicted drug-disease indications |

## Disclaimer

**Research Use Only**: The predictions provided by AuTxGNN are for research purposes only and do not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.

This is not a TGA-approved tool. Always consult healthcare professionals for medical decisions.

## Contact

- Website: [yao.care](https://yao.care)
- GitHub: [yao-care/AuTxGNN](https://github.com/yao-care/AuTxGNN)

---

*Last updated: {{ page.last_modified_at | date: "%Y-%m-%d" }}*

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care). See the
<a href="{{ '/about/' | relative_url }}">About</a> page for the full company and methodology background.
