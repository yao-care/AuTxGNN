---
layout: default
title: Nitrofurantoin
parent: 僅模型預測 (L5)
nav_order: 473
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis

## One-Sentence Summary

Nitrofurantoin is a nitrofuran-class antibacterial agent whose established use (referenced throughout the underlying literature, though not present in a formal Australian regulatory record) is treatment of urinary tract infection. The TxGNN model assigns a high prediction score for **Rheumatoid Arthritis**, but no clinical trials support this link, and all 12 identified publications describe nitrofurantoin's known pulmonary, hepatic, and haematological toxicity risks — several occurring specifically in rheumatoid arthritis patients — rather than any therapeutic benefit for the disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (inferred from literature context; no formal ARTG/regulatory record available — see Data Gap below) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for nitrofurantoin in this evidence pack (flagged as a High-severity data gap). Based on general pharmacology referenced in the literature, nitrofurantoin acts by damaging bacterial DNA and ribosomal function — an antibacterial mechanism with no known anti-inflammatory or immunomodulatory activity that would plausibly treat rheumatoid arthritis, an autoimmune disease.

The relationship between the original indication (urinary tract infection) and the predicted indication (rheumatoid arthritis) is not mechanistically coherent, and the literature evidence bears this out: rather than describing therapeutic use in RA, the 12 retrieved publications overwhelmingly describe nitrofurantoin-induced pulmonary fibrosis/interstitial lung disease — a known adverse effect — occurring in or alongside RA patients (who are independently predisposed to lung fibrosis as part of their underlying disease). One case report specifically documents a harmful drug interaction (methotrexate + nitrofurantoin causing irreversible pulmonary fibrosis) in an RA patient.

**This prediction should be treated as a low-confidence, unconfirmed model output.** The high TxGNN score does not correspond to supportive biological or clinical evidence; if anything, the retrieved literature points toward increased risk rather than benefit in this population.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort (self-controlled case series) | Scientific Reports | In 31,992 RA patients, examined association between antibiotic exposure (including nitrofuran-class agents) and timing of RA flares — an epidemiological safety signal, not treatment evidence |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | RA patients hospitalised for interstitial pulmonary fibrosis had poor prognosis; nitrofurantoin is a recognised cause of drug-induced pulmonary fibrosis relevant to this population |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Reviews drugs causing pulmonary fibrosis, listing nitrofurantoin alongside bleomycin/amiodarone; notes RA itself predisposes to pulmonary fibrosis |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du praticien | Review of drug-induced interstitial lung disease listing nitrofurantoin among causative antibiotics |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | Irreversible pulmonary fibrosis in a 94-year-old RA patient from combined methotrexate + nitrofurantoin therapy — a drug interaction/safety warning |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Case report | Revue de pneumologie clinique | Gold-salt-induced pneumonitis in an RA patient (RA-treatment toxicity, referenced via lung-toxicity co-occurrence, not nitrofurantoin itself) |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case report | Cureus | Autoimmune hepatitis case in which nitrofurantoin was among the drugs excluded as a cause of drug-induced liver injury |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case report | Annales de dermatologie et de vénéréologie | Phenylbutazone-induced sialadenitis; nitrofurantoin mentioned only as another drug reported to cause sialadenitis |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Cohort | Acta Medica Scandinavica | Short-term nitrofurantoin therapy for bacteriuria — reflects the drug's established UTI use, unrelated to RA |

---

## Australia Market Information

Nitrofurantoin currently has no ARTG entries recorded (market status: not marketed). No product-level information is available to summarise.

---

## Safety Considerations

No structured TGA Product Information data (warnings, contraindications, or drug interactions) was available for this evaluation — this is flagged as a **Blocking** data gap (DG001), meaning a formal safety assessment cannot proceed without it.

That said, the literature evidence gathered for this candidate itself surfaces known nitrofurantoin safety signals worth noting for any clinician reviewing this report:
- **Pulmonary toxicity**: repeated association with drug-induced pulmonary fibrosis / interstitial lung disease, including a case of irreversible fibrosis when co-administered with methotrexate.
- **Hepatotoxicity**: nitrofurantoin is a recognised cause of drug-induced liver injury/autoimmune hepatitis.
- **Methemoglobinemia**: separate TxGNN predictions in this evidence pack (methemoglobinemia, ranks 8 and 10) independently confirm this as an established adverse effect, not a treatment target.

Please refer to the TGA-approved Product Information (PI) once available for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is no mechanistic rationale, no clinical trial evidence, and the literature that does exist describes toxicity risks (particularly pulmonary and hepatic) rather than any therapeutic signal for rheumatoid arthritis — in some cases occurring specifically in RA patients. Combined with the drug's unmarketed status in Australia (0 ARTG entries), this candidate does not meet the bar to advance.

**To proceed, the following is needed:**
- Formal TFDA/TGA Product Information (warnings, contraindications, DDI) — currently a Blocking data gap
- Verified mechanism of action data to assess biological plausibility for an immune-mediated indication
- Any preclinical or mechanistic study directly testing nitrofurantoin (or its metabolites) in autoimmune/inflammatory models, rather than relying on incidental co-occurrence in RA-population safety literature
- Reassessment of whether the underlying literature match reflects a genuine biological signal or a co-occurrence artefact (e.g. RA patients being treated for concurrent UTIs)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

