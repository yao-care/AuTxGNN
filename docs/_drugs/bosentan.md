---
layout: default
title: Bosentan
parent: Model Prediction Only (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
---

# Bosentan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Bosentan: From Pulmonary Arterial Hypertension to Rheumatoid Arthritis

## One-Sentence Summary

Bosentan is a dual endothelin receptor antagonist, originally used to treat pulmonary arterial hypertension (PAH) and systemic sclerosis-related conditions.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but there are **0 registered clinical trials** and only **animal-model studies** directly supporting this direction.
The evidence is at the model-prediction and preclinical stage, so this should be treated as a hypothesis rather than an actionable repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (the ARTG entry lists no indication text; original indications are drawn from the TxGNN knowledge graph and include pulmonary hypertension, systemic sclerosis and localised scleroderma) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 (preclinical and mechanism studies only) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for bosentan were not available in the data compiled for this report. Based on its known drug class, bosentan is a dual endothelin receptor antagonist (ETA/ETB). Its efficacy in PAH is established, and mechanistically it may be applicable to inflammatory conditions in which endothelin-1 (ET-1) plays a role.

Endothelin-1 contributes to synovial inflammation, vasculopathy and cytokine release (including TNF-alpha and LTB4). In mice, bosentan ameliorated collagen-induced arthritis, apparently through TNF-alpha-dependent mechanisms (PMID 22249931). A separate study showed that endothelins modulate the inflammatory reaction in zymosan-induced arthritis (PMID 18515326).

This is a plausible mechanism, but only animal data directly support it. The human literature identified concerns PAH associated with connective tissue disease, not treatment of rheumatoid arthritis itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22249931](https://pubmed.ncbi.nlm.nih.gov/22249931/) | 2012 | Preclinical (mouse model) | Inflamm Res | Bosentan ameliorated collagen-induced arthritis; TNF-alpha involved in inducing endothelin system genes |
| [18515326](https://pubmed.ncbi.nlm.nih.gov/18515326/) | 2008 | Preclinical (mouse model) | J Leukoc Biol | Endothelins modulate neutrophil accumulation and oedema in zymosan-induced arthritis |
| [24268012](https://pubmed.ncbi.nlm.nih.gov/24268012/) | 2014 | Review | Rheum Dis Clin North Am | Review of PAH related to connective tissue disease; high morbidity and mortality |
| [16218473](https://pubmed.ncbi.nlm.nih.gov/16218473/) | 2005 | Review | Lupus | PAH as a complication of connective tissue diseases, including (less commonly) rheumatoid arthritis |
| [19487226](https://pubmed.ncbi.nlm.nih.gov/19487226/) | 2009 | Review | Rheumatology (Oxford) | Vasculopathy and PAH in connective tissue disease |
| [19851110](https://pubmed.ncbi.nlm.nih.gov/19851110/) | 2010 | Review | Curr Opin Rheumatol | Overview of rheumatic skin disease therapies |
| [20054770](https://pubmed.ncbi.nlm.nih.gov/20054770/) | 2009 | Case report | Kardiol Pol | Child with Eisenmenger syndrome treated with bosentan who was later diagnosed with juvenile rheumatoid arthritis; coincidental, not evidence of benefit |

Several other retrieved records (for example, IL-17 and IL-15 hypernociception studies) did not involve bosentan and are not included.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 12134P | Bosentan RBX | Tablet 62.5 mg (as monohydrate) | Not stated in the data compiled for this report |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph** (these come from the TxGNN knowledge graph, not from approved label text): liver failure, liver disease, drug-induced liver injury, hyperbilirubinaemia (including hereditary forms and Gilbert syndrome), gallbladder disease, thrombocytopenia, anaemia (including macrocytic anaemia), congestive heart failure, pulmonary oedema and pulmonary veno-occlusive disease.
- **Drug Interactions**: 100 interactions were recorded in the DDInter database. The 20 reviewed were all of Moderate severity. They include corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone), antidiabetic agents (pioglitazone, acetohexamide, chlorpropamide, and the SGLT2 inhibitors canagliflozin, dapagliflozin, empagliflozin and ertugliflozin), and others such as clarithromycin, metronidazole, cimetidine, cisapride, aprepitant and clotrimazole.

Corticosteroids and other immunomodulators are commonly used in rheumatoid arthritis, so the interaction profile would be relevant in this population. Please refer to the TGA-approved Product Information (PI) for the authoritative warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the supporting evidence is limited to mouse arthritis models and reviews of connective-tissue-disease PAH. There are no registered trials and no human data on bosentan for rheumatoid arthritis, and the safety profile (liver toxicity signals, many interactions) calls for caution.

**To proceed, the following is needed:**
- Mechanism-of-action data and a clearer link between endothelin antagonism and rheumatoid arthritis pathology
- Human proof-of-concept evidence, such as an early-phase trial in rheumatoid arthritis
- The TGA-approved PI, to complete safety screening (warnings and contraindications were not available)
- A benefit-risk assessment, including liver monitoring and the interactions with drugs commonly used in rheumatoid arthritis

---

### Note on Other Predicted Indications

- **Limited systemic sclerosis (L3, research question):** This has the strongest evidence of the predictions, including a 2023 systematic review and meta-analysis of bosentan for systemic sclerosis digital ulcers (PMID 36974107) and national recommendations (PMID 38956991). However, it overlaps substantially with bosentan's existing indications, so it is not a true repurposing candidate. The L3 grade may understate the digital ulcer evidence, which should be checked against the RCT literature.
- **Gout:** The only record is a pharmacovigilance analysis of endothelin receptor antagonist adverse events, which does not support a therapeutic role.
- **Remaining predictions** (brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, pseudoxanthoma elasticum forme fruste, kyphoscoliotic heart disease, elastoma, hypertrichosis and Ambras-type hypertrichosis universalis congenita): model prediction only (L5), with no supporting trials or literature.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

