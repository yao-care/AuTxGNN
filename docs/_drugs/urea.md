---
layout: default
title: Urea
parent: High Evidence (L1-L2)
nav_order: 709
evidence_level: L2
indication_count: 10
---

# Urea
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Urea: From No Approved Indication to Dermatitis

## One-Sentence Summary

> Urea (DrugBank ID: DB03904) has no approved indication recorded in this evidence pack and is not currently marketed in Australia.
> The TxGNN model predicts it may be effective for **Dermatitis**,
> with **50 clinical trials** and **20 publications** currently supporting this direction —
> though the underlying pharmacology (urea as a keratolytic/humectant) is already well established rather than newly discovered.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded — no approved indication is captured in this evidence pack, and urea is not currently marketed in Australia |
| Predicted New Indication | Dermatitis |
| TxGNN Prediction Score | 98.21% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for urea is not available in the structured DrugBank field (flagged as a High-severity data gap). Based on the evidence collected for this candidate, urea's relevant pharmacology is well characterised in the literature: it acts as a **keratolytic agent and humectant**, disrupting hydrogen bonding within keratin in the stratum corneum, which increases the skin's water-binding capacity and supports repair of the epidermal barrier.

This mechanism is the long-standing pharmacological basis for using urea-containing preparations (typically 3–20%) in dry-skin and dermatitis-related conditions, including atopic dermatitis, xerosis cutis, and radiation- or chemotherapy-induced skin reactions (e.g. hand-foot syndrome). The clinical trial and literature evidence gathered for this candidate overwhelmingly reflects this existing use pattern rather than a mechanistically novel application.

**Important caveat for reviewers:** the internal repurposing rationale for this candidate explicitly notes that this is an **already-established use, not a genuinely novel discovery** by TxGNN. The model has essentially reconstructed a well-known indication from the knowledge graph rather than identifying a new therapeutic hypothesis. This should temper expectations about the "repurposing" value of this candidate, even though the supporting evidence base is comparatively strong.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02247830](https://clinicaltrials.gov/study/NCT02247830) | Phase 3 | Completed | 48 | Compared chamomile gel and urea cream for prevention of radiodermatitis in breast/head-and-neck cancer patients undergoing radiotherapy |
| [NCT04127513](https://clinicaltrials.gov/study/NCT04127513) | Phase 3 | Completed | 40 | Double-blind RCT comparing 12% ammonium lactate vs 10% urea cream for xerosis cutis in geriatric patients |
| [NCT06553417](https://clinicaltrials.gov/study/NCT06553417) | N/A | Completed | 60 | Compared an "emollient plus" formulation with urea 10% in mild-moderate atopic dermatitis |
| [NCT05939726](https://clinicaltrials.gov/study/NCT05939726) | Phase 2 | Completed | 145 | Three-arm RCT of urea-based cream ± vitamin E vs urea-based cream alone for capecitabine-associated palmar-plantar erythrodysesthesia |
| [NCT05348278](https://clinicaltrials.gov/study/NCT05348278) | Phase 2/3 | Unknown | 214 | Evaluated urea-based cream for prevention of capecitabine-associated hand-foot skin reactions |
| [NCT02251392](https://clinicaltrials.gov/study/NCT02251392) | Phase 3 | Unknown | 100 | Evaluated chamomile gel/infusion and urea cream for radiodermatitis in breast/head-and-neck cancer patients |
| [NCT03173365](https://clinicaltrials.gov/study/NCT03173365) | Phase 2 | Terminated | 2 | Compared topical brimonidine gel vs standard-care urea 10% lotion for hand-foot syndrome prevention during antineoplastic therapy |
| [NCT07360639](https://clinicaltrials.gov/study/NCT07360639) | Phase 1/2 | Completed | 64 | Compared a coffee-bean/patchouli extract cream with urea cream for dry skin |
| [NCT05641246](https://clinicaltrials.gov/study/NCT05641246) | Phase 2 | Completed | 86 | Evaluated urea-based cream (Carbamide®) combined with topical diclofenac for prevention of hand-foot syndrome in capecitabine-treated breast cancer patients |

*Note: The full evidence set includes 50 registered trials; the remainder largely evaluate unrelated investigational agents in dermatitis populations and were graded low-relevance to urea specifically.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39973079](https://pubmed.ncbi.nlm.nih.gov/39973079/) | 2025 | RCT/Comparative | Journal of Cosmetic Dermatology | Emollient-plus formulation vs urea 10% in mild-to-moderate atopic dermatitis |
| [32985288](https://pubmed.ncbi.nlm.nih.gov/32985288/) | 2020 | RCT | Integrative Cancer Therapies | Chamomile gel vs urea cream to prevent acute radiation dermatitis in head-and-neck cancer patients |
| [20367668](https://pubmed.ncbi.nlm.nih.gov/20367668/) | 2010 | RCT (double-blind) | Journal of Cosmetic Dermatology | Double-blind study of a urea-containing moisturiser in atopic dermatitis |
| [36719406](https://pubmed.ncbi.nlm.nih.gov/36719406/) | 2023 | Clinical Study | Italian Journal of Dermatology and Venereology | Repairing moisturising cream with amino-inositole + urea 10% for chronic hand eczema |
| [1099032](https://pubmed.ncbi.nlm.nih.gov/1099032/) | 1975 | Clinical Trial | International Journal of Dermatology | Randomised double-blind studies of urea creams for dry skin and hand dermatitis |
| [35655045](https://pubmed.ncbi.nlm.nih.gov/35655045/) | 2022 | Review (meta-analysis) | Supportive Care in Cancer | Meta-analysis of RCTs on prophylactic strategies (including urea cream) for hand-foot syndrome/reaction |
| [40265493](https://pubmed.ncbi.nlm.nih.gov/40265493/) | 2025 | Review | International Journal of Dermatology | Review of basic emollients (including urea) for xerosis cutis in atopic dermatitis |
| [35167133](https://pubmed.ncbi.nlm.nih.gov/35167133/) | 2022 | Comparative Study | Clinical and Experimental Dermatology | Physiological effects of different emollient creams on the skin barrier in atopic dermatitis |
| [33934477](https://pubmed.ncbi.nlm.nih.gov/33934477/) | 2021 | Clinical Study | Journal of Cosmetic Dermatology | Clinical and instrumental evaluation of 10% urea cream in senile xerosis |
| [20080470](https://pubmed.ncbi.nlm.nih.gov/20080470/) | 2010 | Clinical Study | Clinical & Translational Oncology | Prophylactic urea-containing cream reduced incidence and severity of radiation-induced dermatitis |

---

## Australia Market Information

Urea currently has **no ARTG entries** and is **not marketed** in Australia based on this evidence pack. No product-level dosage form or approved-indication data is available to tabulate.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No structured key warnings, contraindications, or drug interaction data were available in this evidence pack (all flagged as data gaps).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for urea in dermatitis-related conditions is reasonably substantial (L2, multiple relevant RCTs and a supporting meta-analysis), but it largely confirms an already-established therapeutic use rather than a novel repurposing signal. Combined with the absence of Australian market presence and safety documentation, this candidate should proceed only with additional safeguards, not as a standalone new-indication opportunity.

**To proceed, the following is needed:**
- TGA-approved Product Information for urea preparations (safety warnings, contraindications, DDI) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action data from DrugBank API — currently a High-severity data gap (DG002)
- Clarification of urea's original/approved indication(s), since none are captured in this evidence pack
- If registration in Australia is being considered, a regulatory pathway assessment given zero current ARTG entries
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

