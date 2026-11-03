---
layout: default
title: Data Sources
nav_order: 93
permalink: /sources/
description: "Data sources behind AuTxGNN: the PBS Schedule (Australian Department of Health), TxGNN, ClinicalTrials.gov, PubMed and DrugBank."
---

# Data Sources

<div class="key-takeaway">
Every conclusion traces back to a public data source — nothing is a black box.
</div>

---

## Source overview

<table class="comparison-table">
<thead>
<tr><th>Type</th><th>Source</th><th>Used for</th></tr>
</thead>
<tbody>
<tr><td>Local medicines list</td><td><a href="https://data.pbs.gov.au/api/api-public.html">PBS Schedule (public API)</a></td><td>Medicines and ingredients for Australia; whether each item is listed on the current PBS Schedule</td></tr>
<tr><td>Prediction model</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Drug&ndash;disease association prediction</td></tr>
<tr><td>Clinical trials</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Evidence grading (NCT)</td></tr>
<tr><td>Literature</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Evidence grading (PMID)</td></tr>
<tr><td>Drug information</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Ingredient mapping and target data</td></tr>
<tr><td>Interactions</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Drug&ndash;drug interaction data</td></tr>
</tbody>
</table>

---

## This site's local data

Australian medicines and their market status come from the Pharmaceutical Benefits Scheme (PBS)
Schedule, published by the Australian Department of Health through the PBS public API. The PBS Schedule is
a subsidy list, **not** the TGA's ARTG register: TGA (ARTG) registration
status is not included in this data.

| Item | Detail |
|------|--------|
| Dataset | PBS Schedule items (current schedule, CSV) |
| Publisher | Australian Department of Health, PBS public API |
| Download | <https://data-api.health.gov.au/pbs/api/v3/items> (API documentation: <https://data.pbs.gov.au/api/api-public.html>) |
| Item identifier | PBS item code |
| Updates | Automatic weekly download (every Monday) of the schedule currently in effect; an item that drops off the list keeps its previous status |

---

## Licensing

Each source has its own licence — please check before citing:

- **TxGNN**: academic use; cite Huang et al. (2024)
- **ClinicalTrials.gov / PubMed**: US NIH public data
- **DrugBank**: non-commercial use subject to its licence terms
- **PBS Schedule**: subject to the Australian Department of Health's terms for the PBS public API

---

## Update frequency

| Data | Frequency |
|------|-----------|
| PBS Schedule | Weekly (every Monday) |
| Trial / literature evidence | Re-collected periodically |
| Interaction data | Reviewed quarterly |

---

## Academic citation

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care). See the
<a href="{{ '/about/' | relative_url }}">About</a> page for the full company and methodology background.

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
This report is for academic research reference only and <strong>does not constitute medical advice</strong>. Always follow your physician's instructions; never adjust medication on your own. Any drug repurposing decision requires full clinical validation and regulatory review.
<br><br>
<small>Reviewed by: 藥提醒科技有限公司 (yao.care)</small>
</div>
