---
layout: default
title: Griseofulvin
parent: Model Prediction Only (L5)
nav_order: 346
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-13
monitor_inn: "Griseofulvin"
predicted_indications: ["myiasis", "wound myiasis", "creeping myiasis", "furuncular myiasis", "echinococcus granulosus infectious disease"]
description: "Griseofulvin: predicted new indication Myiasis (evidence level L5). Approved use: Not recorded in the local data"
---

# Griseofulvin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Griseofulvin: Myiasis
{: .text-alpha }

## One-Sentence Summary

Griseofulvin is an oral antifungal originally used for dermatophyte infections of the skin, hair and nails, such as tinea pedis, tinea corporis, tinea unguium and tinea barbae.
The TxGNN model predicts it may be effective for **myiasis** (a fly larvae infestation), but **no clinical trials and no publications** currently support this prediction.
This is a model-only signal with no demonstrated mechanistic basis, so it should be treated as a hypothesis rather than a lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| Australia Market Status | Marketed (valid licences: 1 of 1) |
| Number of ARTG Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, griseofulvin is an oral antifungal that disrupts fungal microtubules and mitosis, and it is deposited in keratinised tissue. Its efficacy in dermatophyte infections is well established.

For myiasis, however, no plausible mechanistic link can be established. Myiasis is an infestation of tissue by fly larvae (dipterans), not a fungal disease. Griseofulvin has no known antiparasitic or insecticidal activity. Standard management relies on removal of the larvae, not on an antifungal. The high score (0.9941) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The same applies to the other top-ranked predictions (wound myiasis, creeping myiasis, furuncular myiasis, toxoplasmosis and Bacteroidaceae infection), which have no trials, no literature and no credible mechanism.

Among lower-ranked predictions, **cutaneous candidiasis** is biologically closer because it is fungal. Griseofulvin is generally not effective against *Candida*. The retrieved literature for this indication is indirect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for myiasis.

For context, the literature retrieved for the lower-ranked prediction of cutaneous candidiasis (20 records, 10 shown) was indirect. It consists mainly of reviews of superficial fungal infections and other antifungals (terbinafine, itraconazole, ketoconazole, tolnaftate), with griseofulvin mentioned as a comparator or a treatment for tinea capitis. It does not show that griseofulvin treats candidiasis.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8763460](https://pubmed.ncbi.nlm.nih.gov/8763460/) | 1996 | Review | Br J Dermatol | Cutaneous mycoses in children; griseofulvin has been the main treatment in children but is only fungistatic, may cause interactions and needs prolonged dosing |
| [15571501](https://pubmed.ncbi.nlm.nih.gov/15571501/) | 2004 | Review | Dermatol Ther | Therapy of superficial fungal infections; onychomycosis often needs systemic griseofulvin, itraconazole or terbinafine |
| [34898894](https://pubmed.ncbi.nlm.nih.gov/34898894/) | 2021 | Review | J Obstet Gynaecol India | Risks and precautions of common antifungal drugs in pregnancy |
| [10439936](https://pubmed.ncbi.nlm.nih.gov/10439936/) | 1999 | Review | Drugs | Terbinafine in superficial mycoses; mycological cure above 80% in dermatophyte infections |
| [1372222](https://pubmed.ncbi.nlm.nih.gov/1372222/) | 1992 | Review | Drugs | Terbinafine pharmacology and efficacy in tinea corporis, cruris and pedis |
| [8706596](https://pubmed.ncbi.nlm.nih.gov/8706596/) | 1996 | Review | Drugs | Itraconazole in superficial fungal infections, including dermatophytosis and vaginal candidiasis |
| [8077517](https://pubmed.ncbi.nlm.nih.gov/8077517/) | 1994 | Review | J Am Acad Dermatol | Treatment of tropical mycoses (retrieved for the blastomycosis prediction); general, not griseofulvin-specific |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 1460W | Grisovin | Tablet 125 mg (oral) | Not recorded in the data compiled for this report |

---

## Safety Considerations

No product-label warnings or contraindications were available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for full safety information.

**Contraindication signals from the knowledge graph** (these are not label text and need verification against the PI):
- Liver failure
- Porphyria (including inherited porphyria and other porphyrin metabolism disorders)
- Systemic lupus erythematosus (including the paediatric form)
- Substance abuse/dependence
- Neutropenia and agranulocytosis (including congenital and idiopathic forms)

**Drug interactions** (100 interactions were identified; examples are below, with the most frequent level being Moderate):
- **Anticoagulants and antiplatelets:** warfarin, apixaban, rivaroxaban, dicoumarol, ticagrelor (Moderate); acetylsalicylic acid (Minor)
- **Antidiabetic agents:** saxagliptin, linagliptin, repaglinide (Moderate); liraglutide (Minor)
- **Antiemetics:** aprepitant, rolapitant (Moderate)
- **Antimalarials and antiparasitics:** artemether, mefloquine, praziquantel (Moderate)
- **Others:** eliglustat, naloxegol, nitisinone, macimorelin, fostamatinib (Moderate)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The myiasis prediction is a computational output only (evidence level L5). There are no registered trials, no supporting literature, and no biologically plausible mechanism linking an antifungal to fly larvae infestation. The knowledge-graph contraindication signals (hepatic, haematological and porphyria-related) and the large number of interactions add risk without any demonstrated benefit.

**To proceed, the following is needed:**
- A credible mechanistic or preclinical rationale for activity against dipteran larvae (none currently exists)
- Mechanism of action data for griseofulvin from DrugBank
- The TGA Product Information (warnings, contraindications and approved indication text), as this was not available for the Australian listing
- If a repurposing direction is still wanted, consider a review of the fungal prediction instead (cutaneous candidiasis). It has a more plausible biological basis but still needs direct comparative evidence, since standard therapies (azoles, nystatin, terbinafine, itraconazole) are already established.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

