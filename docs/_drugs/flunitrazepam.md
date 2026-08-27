---
layout: default
title: Flunitrazepam
parent: 僅模型預測 (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
---

# Flunitrazepam
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

# Flunitrazepam: From No Registered Indication to Insomnia (Known Hypnotic Class Action)

## One-Sentence Summary

Flunitrazepam is a benzodiazepine that is **not currently registered or marketed in Australia** (no ARTG entry), and no original indication is recorded for it in this evidence pack. The TxGNN model's top prediction is **Insomnia (disease)**, supported by **1 clinical trial** and **11 publications** — but this is not truly a "new" use: flunitrazepam is pharmacologically a classic sedative-hypnotic, and insomnia is its already-known class action rather than a novel repurposing target.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Australia — no original indication on file (0 ARTG entries) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available from DrugBank in this pack. Based on known pharmacological class information, flunitrazepam is a benzodiazepine and a positive allosteric modulator (PAM) of the GABA_A receptor — the mechanism that underlies the sedative-hypnotic effect shared by all classical benzodiazepines.

This mechanism directly and unambiguously supports an insomnia indication. However, this is an important caveat for interpretation: flunitrazepam is one of the best-known hypnotic benzodiazepines internationally (marketed elsewhere as a night-time sedative), so "insomnia" is not a genuinely novel repurposing candidate — it is the drug's original, well-established pharmacological action. The evidence pack itself flags this: the drug shows an empty `original_indications` field and "not marketed" status specifically because it has no Australian regulatory history, not because insomnia is an unexpected new use.

Separately, the evidence pack's rank-6 candidate (alcohol withdrawal delirium) has a stronger genuine mechanistic case — GABA_A receptor down-regulation during alcohol withdrawal is directly compensated by benzodiazepine PAM activity — but that is outside the scope of the rank-1 candidate this report focuses on.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A | Unknown | 1,400 | Prospective cohort study at a Taiwanese academic medical centre examining hypnotic medication-use patterns, safety, and outcomes in elderly patients. Not a flunitrazepam-specific interventional trial — provides indirect, class-level (hypnotic agents) safety/efficacy signal only. |

No ANZCTR-registered trials were identified for this candidate.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40195](https://pubmed.ncbi.nlm.nih.gov/40195/) | 1979 | Clinical study | La Nouvelle presse medicale | Direct study of flunitrazepam's action on organic and functional sleep disorders. |
| [8519370](https://pubmed.ncbi.nlm.nih.gov/8519370/) | 1993 | Clinical pharmacology (acute effects) | European Respiratory Journal | Compared flunitrazepam, triazolam and zolpidem on arterial blood gases/breathing control in COPD patients with insomnia. |
| [430730](https://pubmed.ncbi.nlm.nih.gov/430730/) | 1979 | Review / clinical observation | JAMA | Sleep-lab evaluation of 5 benzodiazepines including flunitrazepam; rebound insomnia occurred after withdrawal of short/intermediate half-life agents. |
| [684426](https://pubmed.ncbi.nlm.nih.gov/684426/) | 1978 | Clinical syndrome description | Science | First description of "rebound insomnia" following withdrawal of short-acting benzodiazepine hypnotics. |
| [6114852](https://pubmed.ncbi.nlm.nih.gov/6114852/) | 1981 | Review | Drugs | Reviews triazolam against other hypnotics including flunitrazepam, nitrazepam and flurazepam for insomnia. |
| [2883822](https://pubmed.ncbi.nlm.nih.gov/2883822/) | 1986 | Review | Acta Psychiatrica Scandinavica Suppl. | Reviews benzodiazepine pharmacodynamics in the elderly, including flunitrazepam; shows increased sensitivity with age. |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Review | Acta Psychiatrica Scandinavica Suppl. | Reviews the clinical rationale for a variety of hypnotics in insomnia management. |
| [20171127](https://pubmed.ncbi.nlm.nih.gov/20171127/) | 2010 | Review | Sleep Medicine Reviews | Reviews effects of hypnotic drugs on body balance/standing steadiness and fall risk. |
| [14722706](https://pubmed.ncbi.nlm.nih.gov/14722706/) | 2004 | Animal study | Psychopharmacology | Compared three hypnotics' effects on the sleep-wake cycle in sleep-disturbed rats. |

Two literature hits returned by the search (PMID 22155391 on an herbal anxiolytic extract, and PMID 8829906 on benign recurrent intrahepatic cholestasis) were excluded as not substantively related to flunitrazepam or insomnia.

---

## Safety Considerations

**Blocking data gap:** TFDA/overseas Product Information (warnings and contraindications) could not be retrieved from the sources queried. This is flagged in the evidence pack as a **Blocking** severity gap — it explicitly prevents progression to the S1 safety initial-assessment stage.

Flunitrazepam is not registered on the ARTG, so no Australian-approved Product Information exists for this drug. A drug-drug interaction query returned no results (`not_found`). Please refer to an authoritative overseas Product Information source (e.g., country of origin regulator, DrugBank) for safety information before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Safety data is blocked at the source (DG001, Blocking severity), and the drug has no ARTG registration or Australian market history. In addition, the top-ranked "new" indication (insomnia) is not a genuine repurposing signal — it reflects flunitrazepam's already-established pharmacological class action as a hypnotic, so the repurposing value of this candidate is limited on its own merits.

**To proceed, the following is needed:**
- Product Information (warnings, contraindications, precautions) from an authoritative regulatory source — currently blocking (DG001)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- A resolved drug-drug interaction dataset (current query: not found)
- A human decision on whether "insomnia" should even be scored as a repurposing candidate, given it duplicates the drug's known class indication, or whether evaluation effort should instead focus on the mechanistically stronger alcohol-withdrawal-delirium candidate (rank 6, L3/S2) identified elsewhere in this evidence pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

