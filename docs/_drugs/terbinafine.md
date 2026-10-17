---
layout: default
title: Terbinafine
parent: Model Prediction Only (L5)
nav_order: 708
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Terbinafine: predicted new indication Creeping myiasis (evidence level L5). Approved use: Tinea pedis, tinea corporis, tinea infection, tinea unguium…"
monitor_inn: "Terbinafine"
predicted_indications: ["creeping myiasis", "furuncular myiasis", "wound myiasis", "myiasis", "toxoplasmosis", "blastomycosis", "echinococcus granulosus infectious disease"]
---

# Terbinafine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Terbinafine: From Dermatophyte Skin and Nail Infections to Creeping Myiasis

## One-Sentence Summary

Terbinafine is an oral allylamine antifungal, originally used for dermatophyte infections such as tinea pedis, tinea corporis and tinea unguium.
The TxGNN model predicts it may be effective for **creeping myiasis** (a fly-larvae infestation), but this is a graph-based prediction only, with **no clinical trials** and **no supporting publications** behind it.
Other predictions for this drug, particularly **tinea manuum** and **superficial mycosis**, are far better supported, but they largely overlap with the existing approved use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, tinea infection, tinea unguium, pityriasis versicolor, dermatophytosis of the groin and perianal area (the Australian licence entry has no indication text, so these come from the knowledge graph) |
| Predicted New Indication | Creeping myiasis |
| TxGNN Prediction Score | 96.74% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Terbinafine is generally understood to inhibit fungal squalene epoxidase, blocking ergosterol synthesis, and this fungicidal action underpins its efficacy against dermatophytes.

Myiasis is an infestation by fly larvae, which are animal parasites rather than fungi. No shared target or pathway with fungal ergosterol synthesis has been established, so the mechanistic case for creeping myiasis is weak. The high score (0.967) most likely reflects proximity in the knowledge graph to skin infections, not a pharmacological rationale. The same score was assigned to furuncular myiasis and wound myiasis, and the broader category of myiasis scored 0.962.

For context, the other predictions fall into three groups:
- **Plausible and largely within existing use:** tinea manuum (0.901) and superficial mycosis (0.845) involve the same dermatophytes and the same mechanism as the approved indications.
- **Biologically plausible but weakly evidenced:** cutaneous candidiasis (0.950) and blastomycosis (0.918) are fungal, but evidence is in vitro, review-level or case-report only.
- **Unsupported:** myiasis variants, toxoplasmosis (0.948) and *Echinococcus granulosus* infection (0.861) involve non-fungal parasites with no mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered for creeping myiasis, and none were identified for any of the other top-ranked predictions.

## Literature Evidence

No publications are linked directly to creeping myiasis. The closest available items relate to the other myiasis predictions and do not demonstrate efficacy:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25016125](https://pubmed.ncbi.nlm.nih.gov/25016125/) | 2014 | Case report | Turkiye Parazitol Derg | A 12-year-old boy with furuncular myiasis had received terbinafine among several unsuccessful treatments over 2 months. This is a diagnostic report and does not show terbinafine efficacy. |
| [39081689](https://pubmed.ncbi.nlm.nih.gov/39081689/) | 2024 | Case report | Front Med | Chromoblastomycosis occurring together with myiasis in a kidney transplant recipient. Myiasis was a concurrent condition, and any antifungal use targeted the fungal infection. |

For the better-supported related predictions, key sources include:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1911319](https://pubmed.ncbi.nlm.nih.gov/1911319/) | 1991 | Clinical study | Br J Dermatol | Two-week oral terbinafine versus placebo in moccasin tinea pedis and tinea manuum |
| [1372222](https://pubmed.ncbi.nlm.nih.gov/1372222/) | 1992 | Review | Drugs | Mycological and overall efficacy of about 90% and 80% in tinea corporis/cruris and tinea pedis |
| [10439936](https://pubmed.ncbi.nlm.nih.gov/10439936/) | 1999 | Review | Drugs | Oral terbinafine achieves mycological cure in over 80% of patients with superficial dermatophyte infections; fungistatic against *Candida albicans* |
| [9593126](https://pubmed.ncbi.nlm.nih.gov/9593126/) | 1998 | In vitro study | Antimicrob Agents Chemother | In vitro activity against cutaneous *Candida* isolates |
| [10886159](https://pubmed.ncbi.nlm.nih.gov/10886159/) | 2000 | Case report | Br J Dermatol | Paracoccidioidomycosis treated successfully with terbinafine (a different organism from *Blastomyces*) |
| [39114868](https://pubmed.ncbi.nlm.nih.gov/39114868/) | 2024 | Review | Expert Rev Anti Infect Ther | *Trichophyton indotineae* is usually poorly responsive to terbinafine |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2285G | Terbinafine-DRLA | Tablet 250 mg (as hydrochloride) | Not recorded in the data compiled for this report |

All marketed presentations are oral. Whether the indication, dose or duration would suit a parasitic skin infestation has not been assessed.

## Safety Considerations

- **Disease associations from the knowledge graph (not label text):** kidney disease, pyoureter, liver disease, gallbladder disease, systemic lupus erythematosus (including paediatric), and substance abuse/dependence. These should be checked against the TGA-approved Product Information.
- **Drug Interactions:** 100 interactions were identified. Of those listed, **eliglustat** is rated Major. Moderate interactions include morphine, naltrexone, ondansetron, dexfenfluramine and fenfluramine. Cimetidine is rated Minor. Others, such as metformin, omeprazole, prednisone and doxycycline, have no severity rating.
- **Resistance:** terbinafine-resistant dermatophytes (notably *T. indotineae*, also reported in Japan and China) are a stewardship concern for the dermatophyte-related predictions. One Australian laboratory study (PMID 40514259) examined detection of *T. indotineae*.

Please refer to the TGA-approved Product Information (PI) for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for creeping myiasis rests on a model score alone (evidence level L5). There are no trials or supporting literature, and no plausible mechanism links a fungal squalene epoxidase inhibitor to fly-larvae infestation. Standard care for myiasis (larval removal and local management) is unaffected by this prediction.

**To proceed, the following is needed:**
- Any mechanistic or in vitro evidence of terbinafine activity against fly larvae, which currently appears unlikely
- Detailed mechanism of action data from DrugBank
- Warnings and contraindications from the TGA-approved PI (the ARTG entry has no indication text)
- Redirecting effort to **tinea manuum** and **superficial mycosis** (both rated Proceed with Guardrails, L3). Both are essentially within-class extensions of existing use. Guardrails would include susceptibility testing and antifungal stewardship given emerging resistance.
- **Cutaneous candidiasis** and **blastomycosis** (both L4) could be framed as research questions, as terbinafine is generally fungistatic against *Candida* and azoles or amphotericin B remain standard.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

