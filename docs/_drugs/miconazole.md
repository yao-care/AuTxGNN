---
layout: default
title: Miconazole
parent: Moderate Evidence (L3-L4)
nav_order: 475
evidence_level: L3
indication_count: 10
---

# Miconazole
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Miconazole: From Superficial Fungal Skin Infections to Acne

## One-Sentence Summary

Miconazole is a topical imidazole antifungal originally used for tinea (athlete's foot, ringworm), cutaneous candidiasis, pityriasis versicolor and vulvovaginal candidiasis.
The TxGNN model predicts it may be effective for **acne**, but there are **no registered clinical trials** and only **4 publications** (one review, two small cohort studies and one in vitro study), so the evidence remains early-stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, cutaneous candidiasis, pityriasis versicolor, vulvovaginal candidiasis and related superficial fungal infections (the ARTG entry in the data compiled for this report has no indication text; these come from the knowledge graph) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L3 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on known information, miconazole is an imidazole antifungal. Imidazoles generally inhibit fungal ergosterol synthesis (CYP51), and the literature also describes a second action on fungal peroxidases (PMID 16597199). Its efficacy in superficial fungal skin infections is well established.

The link to acne is indirect, with three supporting threads:

- **Antibacterial activity:** An in vitro study found that azole antifungals have activity against *Propionibacterium acnes* (*Cutibacterium acnes*), the bacterium implicated in acne vulgaris (PMID 20045949).
- **Misdiagnosed acne:** *Pityrosporum* (*Malassezia*) folliculitis is often mistaken for acne vulgaris. Antifungal treatment, including azoles, may help in these cases (PMID 8593718).
- **Anti-inflammatory effects:** A review reports that miconazole has multiple effects on skin disorders, including possible anti-inflammatory activity (PMID 18627330). A split-face assessment in mild inflammatory catamenial acne gives limited human data (PMID 15536660).

Overall, the plausible benefit is mainly in fungal-associated acne-like eruptions rather than classic acne. The evidence is small and heterogeneous.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Review | Expert Opin Pharmacother | Overview of miconazole's multiple effects on skin disorders |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Cohort | Skin Res Technol | Split-face clinical and bioinstrumental assessment in mild inflammatory catamenial acne |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Cohort | Clin Exp Dermatol | 62 patients with Pityrosporum folliculitis, a condition often misdiagnosed as acne vulgaris; diagnosis and therapeutic trials |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro | Biol Pharm Bull | In vitro activity of azole antifungals against *P. acnes* isolated from acne patients |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 9027D | Daktarin | Cream containing miconazole nitrate 20 mg per g, 30 g | Not stated in the data compiled for this report |

---

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text):** Liver disease and gallbladder disease are listed as contraindicated conditions.
- **Drug Interactions:** 100 interactions were identified in the interaction databases. The listed ones are mostly Moderate, for example paclitaxel, fentanyl, alfentanil, hydrocodone, acalabrutinib, nifedipine, amlodipine, amiodarone, amitriptyline, alprazolam, alfuzosin, aliskiren, alosetron, ethinylestradiol and estradiol. Minor interactions include dolutegravir, loratadine, amphotericin B and ambrisentan. These are typically relevant to systemic exposure, and the significance for topical use is likely lower.

For label warnings and precautions, please refer to the TGA-approved Product Information (PI).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but support for acne is limited to one review, two small cohort studies and an in vitro study, with no registered trials. The most plausible benefit is in Malassezia-related folliculitis that mimics acne, not classic acne. Label safety information and mechanism data are also missing from the data compiled for this report.

**To proceed, the following is needed:**
- Obtain the TGA-approved PI for Daktarin to confirm the approved indications, warnings and contraindications
- Mechanism of action data (for example from DrugBank)
- A well-designed randomised controlled trial comparing topical miconazole with standard acne therapy, ideally stratifying for Malassezia involvement
- A review of how the liver and gallbladder disease contraindication signals apply to topical use

---

## Other Predicted Indications (Brief Notes)

These are ranked lower and shown for context only.

| Predicted Indication | TxGNN Score | Evidence Level | Note |
|------|------|------|------|
| Superficial mycosis | 97.05% | L3 | Largely within existing approved uses. Supported by a comparative study versus clotrimazole (PMID 2632381) and multiple reviews. Candidate for Proceed with Guardrails, but it is not true repurposing. |
| Tinea profunda / Majocchi granuloma | 97.20% / 97.08% | L4 | Case reports and preclinical analogue chemistry only. Topical penetration into follicular and dermal infection is likely inadequate. |
| Dermatophytosis of scalp or beard | 96.92% | L4 | Literature is general. Systemic agents are standard, and topical agents are adjunctive. |
| Blastomycosis | 95.17% | L3 | Old uncontrolled reports of IV or oral miconazole. Superseded by itraconazole and amphotericin B. |
| Gastrin secretion abnormality, papillary conjunctivitis, ectothrix and endothrix infections | 97.0–98.7% | L5 | Model prediction only, with no supporting literature. Hold. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

