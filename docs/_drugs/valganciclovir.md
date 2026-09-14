---
layout: default
title: Valganciclovir
parent: 僅模型預測 (L5)
nav_order: 713
evidence_level: L5
indication_count: 10
---

# Valganciclovir
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

# Valganciclovir: From Cytomegalovirus (CMV) Infection to Rheumatoid Arthritis

## One-Sentence Summary

Valganciclovir is an antiviral prodrug (hydrolysed to ganciclovir) established for cytomegalovirus (CMV) infection/retinitis, most notably in immunocompromised patients. The TxGNN model assigns a high score for **Rheumatoid Arthritis**, but on review the supporting literature describes CMV infection occurring **in** RA patients who are immunosuppressed by other drugs (methotrexate, anti-TNF, tofacitinib, JAK inhibitors) — not valganciclovir treating RA itself. No clinical trials support this indication, and the evidence assessment flags this as a likely knowledge-graph co-occurrence artefact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in Australian regulatory data (drug not marketed). Literature confirms valganciclovir's established use is cytomegalovirus (CMV) retinitis/infection in immunocompromised patients. |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 98.97% |
| Evidence Level | L5 (model prediction only, no supportive studies) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is currently unavailable from DrugBank (data gap). Based on the literature retrieved, valganciclovir's known mechanism is inhibition of CMV DNA polymerase, blocking viral replication — it has no known immunomodulatory or anti-inflammatory activity relevant to rheumatoid arthritis pathophysiology (synovial inflammation, cytokine-driven joint destruction).

The literature evidence pack consistently shows the opposite causal direction to what would be needed to support this indication: RA patients treated with immunosuppressive therapies (methotrexate, anti-TNF agents, tofacitinib, upadacitinib) are at increased risk of CMV reactivation (colitis, retinitis, gastritis, pericardial effusion), and valganciclovir is used to **treat that CMV complication**, not the underlying RA. This is a well-recognised "guilt by association" pattern in knowledge-graph-based prediction: high textual co-occurrence between "valganciclovir" and "rheumatoid arthritis" in case reports, without any genuine mechanistic or therapeutic link.

On this basis, the high TxGNN score for this indication should be treated as a probable false positive rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18068874](https://pubmed.ncbi.nlm.nih.gov/18068874/) | 2008 | Review | La Revue de médecine interne | No consensus guidelines exist for antiviral use in CMV infection complicating immunosuppressive therapy for RA/SLE |
| [26150269](https://pubmed.ncbi.nlm.nih.gov/26150269/) | 2015 | Case Report | Reumatismo | CMV ileocolitis in an RA patient on immunosuppressive therapy |
| [28389165](https://pubmed.ncbi.nlm.nih.gov/28389165/) | 2017 | Case Report | J Infect Chemother | CMV retinitis followed by immune recovery uveitis in an RA patient on methotrexate + tofacitinib |
| [25697299](https://pubmed.ncbi.nlm.nih.gov/25697299/) | 2015 | Case Report | BMJ Case Reports | CMV bowel perforation in a frail RA patient, complicated by Enterobacter pericardial effusion |
| [41779881](https://pubmed.ncbi.nlm.nih.gov/41779881/) | 2025 | Case Report | Retinal Cases & Brief Reports | CMV retinitis in non-HIV RA patients on tofacitinib |
| [15494900](https://pubmed.ncbi.nlm.nih.gov/15494900/) | 2004 | Case Report | Clin Infect Dis | CMV retinitis in an RA patient treated with anti-TNF-α antibody therapy |
| [23904414](https://pubmed.ncbi.nlm.nih.gov/23904414/) | 2013 | Case Report | BMJ Case Reports | RA patient on methotrexate with concurrent CMV gastritis and H. pylori infection |
| [20711100](https://pubmed.ncbi.nlm.nih.gov/20711100/) | 2010 | Case Report | Acta Reumatologica Portuguesa | CMV hepatitis in an inflammatory arthritis patient, treated with valganciclovir |
| [23247975](https://pubmed.ncbi.nlm.nih.gov/23247975/) | 2013 | Case Report | Jpn J Ophthalmol | CMV/HHV-6 corneal endotheliitis (RA mentioned as comorbid context) |
| [15155152](https://pubmed.ncbi.nlm.nih.gov/15155152/) | 2004 | Review | Expert Opin Drug Saf | General review of drug-related retinal toxicity, mentions hydroxychloroquine use in RA (limited relevance) |

---

## Australia Market Information

No ARTG entries found. Valganciclovir is not currently marketed in Australia based on the data available in this evidence pack.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level for this candidate is L5 — no clinical trials, no reviews or observational studies directly supporting valganciclovir as a treatment for rheumatoid arthritis. The available literature indicates a reverse relationship (CMV infection as a *complication* of RA immunosuppressive therapy, treated with valganciclovir), consistent with a knowledge-graph co-occurrence false positive rather than a genuine mechanistic signal. The drug is also not currently marketed in Australia (0 ARTG entries), and key regulatory safety data (TFDA/PI warnings, contraindications) remain an unresolved **Blocking** data gap (DG001) that must be closed before any S1 safety evaluation can proceed.

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, DDI) — currently a Blocking data gap
- Confirmed mechanism of action from DrugBank (currently a High-severity data gap)
- Re-classification/reclassification of the "pending" literature entries to confirm none represent stronger evidence than currently assessed

**Note for reviewers:** Rank 2 in this evidence pack (bronchitis, L3, decision stage S1, "Research Question") has materially stronger evidence — multiple cohort studies show valganciclovir prophylaxis reduces CMV-related bronchiolitis obliterans syndrome (BOS) after lung transplantation. However, the indication label "bronchitis" is a mismatch for the actual patient population (lung transplant recipients) and disease entity (BOS, not acute bronchitis) and would need separate, corrected evaluation rather than being taken at face value.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

