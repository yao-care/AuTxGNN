---
layout: default
title: Erythromycin
parent: 僅模型預測 (L5)
nav_order: 202
evidence_level: L5
indication_count: 10
---

# Erythromycin
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

# Erythromycin: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Erythromycin is a macrolide antibiotic with broad-spectrum activity against Gram-positive organisms, historically used for respiratory, skin, and sexually transmitted bacterial infections, including ophthalmic surface infections.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
with **0 clinical trials** and **2 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (macrolide antibiotic — no TGA-approved indication currently on file for Australia) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on well-established pharmacological knowledge, erythromycin belongs to the macrolide antibiotic class and exerts its antibacterial effect by binding to the 50S ribosomal subunit of susceptible bacteria, thereby inhibiting protein synthesis. It demonstrates activity against Gram-positive cocci (*Staphylococcus*, *Streptococcus*), *Haemophilus influenzae*, and intracellular pathogens including *Chlamydia trachomatis* and *Mycoplasma pneumoniae*. A 0.5% ophthalmic ointment formulation has been approved by the US FDA for the prevention and treatment of superficial ocular bacterial infections, supporting its plausibility as an ocular therapeutic agent.

Punctate epithelial keratoconjunctivitis (PEK) is characterised by superficial punctate epithelial defects distributed across the cornea and conjunctiva, and is associated with a broad and heterogeneous range of aetiologies — including adenoviral infection, herpes simplex virus, *Chlamydia trachomatis*, toxic or medication-induced injury, dry eye disease, blepharitis, and immune-mediated inflammation. The mechanistic link between erythromycin and PEK is therefore narrow: erythromycin could plausibly address PEK presentations driven by susceptible bacterial or chlamydial pathogens (e.g., blepharitis-related or inclusion conjunctivitis-associated PEK), but the majority of PEK cases involve non-bacterial mechanisms that are not amenable to macrolide therapy.

The TxGNN prediction likely reflects erythromycin's established ophthalmic antibacterial profile and its connectivity to ocular surface infection nodes within the knowledge graph, rather than a direct or specific mechanistic relationship with punctate epithelial keratoconjunctivitis as a distinct clinical entity. Neither of the two identified publications directly evaluates erythromycin for this indication, and the overall evidence base is insufficient to support clinical translation at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11495307](https://pubmed.ncbi.nlm.nih.gov/11495307/) | 2001 | Case series / Review | Journal of Pediatric Ophthalmology and Strabismus | Describes the history, symptoms, clinical signs, and treatment approaches for chronic blepharokeratoconjunctivitis in children; provides indirect context for inflammatory keratoconjunctivitis management |
| [32826651](https://pubmed.ncbi.nlm.nih.gov/32826651/) | 2021 | Case report | Cornea | Reports a case of microsporidia (*Encephalitozoon hellem*) keratoconjunctivitis in an immunocompetent adult diagnosed by metagenomic deep sequencing; illustrates rare infectious causes of keratoconjunctivitis but does not evaluate erythromycin |

> **Note:** Neither publication directly evaluates erythromycin for punctate epithelial keratoconjunctivitis. Both are tier 3 evidence and are considered indirectly relevant at best.

---

## Australia Market Information

Erythromycin is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. No ARTG entries were identified in this dataset.

> Any clinical use of erythromycin in Australia would need to occur through appropriate regulatory pathways (e.g., Special Access Scheme or Authorised Prescriber pathways via the TGA), depending on clinical circumstances.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> No safety data — including key warnings, contraindications, or drug-drug interaction information — was retrievable from the current dataset. Clinicians should consult the TGA website and relevant product documentation prior to any clinical consideration involving erythromycin.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the TxGNN model assigns a high algorithmic prediction score (99.89%) to erythromycin for punctate epithelial keratoconjunctivitis, the evidence base is at Level L4 (preclinical and mechanistic inference only), with no registered clinical trials and only 2 indirectly related publications. The mechanistic link is weak given PEK's predominantly non-bacterial aetiology. Compounding this, erythromycin has no current ARTG registration in Australia, creating a regulatory gap that must be addressed before any clinical pathway is considered.

**To proceed, the following is needed:**
- Full mechanism of action (MOA) data retrieved from DrugBank (DrugBank ID: DB00199) to confirm pharmacological basis
- Identification of specific PEK subtypes with confirmed bacterial or *Chlamydia*-related aetiology, which may represent more tractable sub-indications
- Complete safety profile: TGA-approved or equivalent Product Information including key warnings, contraindications, and drug interactions (especially QT-prolongation risk and CYP3A4 interactions known for macrolides)
- ARTG registration pathway assessment if any clinical development or import for use is planned in Australia
- Prospective review of higher-evidence predictions from this same dataset before committing resources to this indication — particularly:
  - **Lymphogranuloma Venereum** (Rank 4 · Evidence Level L3 · "Proceed with Guardrails") — supported by historical CDC guideline listing and Phase 4 macrolide class trial evidence
  - **Necrotising Ulcerative Gingivitis** (Rank 5 · Evidence Level L3 · "Research Question") — supported by historical clinical reports of erythromycin (Ilotycin) use in fusospirochetal oral infections
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

