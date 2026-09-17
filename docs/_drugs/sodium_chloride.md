---
layout: default
title: Sodium Chloride
parent: Model Prediction Only (L5)
nav_order: 636
evidence_level: L5
indication_count: 10
---

# Sodium Chloride
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

# Sodium Chloride: From Generic Electrolyte/Irrigation Use to Vulvovaginitis (Adjunctive Irrigation)

## One-Sentence Summary

Sodium chloride (DrugBank DB09153) has no single defined original indication or MOA recorded in this Evidence Pack — it is a generic isotonic salt solution used broadly for fluid/electrolyte replacement and irrigation. TxGNN's *highest-scoring* hit, **breast fibrocystic disease** (96.8%), was assessed by the evidence review as a likely artifact of semantic overlap with "saline breast implant" rather than a real pharmacological signal, so it is not carried forward. The best-supported candidate is instead **vulvovaginitis** (score **96.7%**), backed by **5 clinical trials** and **7 publications**, though only one study directly examines saline irrigation as an intervention.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in this Evidence Pack — sodium chloride is a generic electrolyte/irrigation solution with no single defined "original indication" or TGA license record captured here |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 96.69% |
| Evidence Level | L3 (observational) |
| Australia Market Status | Not marketed (under this DrugBank entry) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available for this candidate (`original_moa: [Data Gap]`). Based on general pharmacological knowledge, sodium chloride solutions act as isotonic irrigation/cleansing agents — they mechanically flush and dilute mucosal secretions and pathogen load rather than exerting a pharmacological antimicrobial or anti-inflammatory effect.

For vulvovaginitis, this generic irrigation action is plausible as an **adjunctive, non-curative** measure: rinsing the vaginal mucosa with saline can reduce discharge and irritant burden alongside standard antimicrobial therapy, but it does not treat the underlying infective or inflammatory cause. This is consistent with the evidence pack's own assessment: *"生理食鹽水為等滲透壓沖洗液，機械性清潔+稀釋陰道分泌物/病原負荷，非藥理性殺菌，僅輔助性、非治癒性機轉"* (isotonic saline irrigation provides mechanical cleansing/dilution, not pharmacological killing — an adjunctive, non-curative mechanism only). The same rationale applies near-identically to the related candidate **vulvitis** (rank 3, score 96.3%), which reflects the same underlying signal rather than an independent finding.

By contrast, the top TxGNN-ranked candidate — breast fibrocystic disease — was explicitly flagged in the pack's own rationale as likely arising from vocabulary confusion with "saline breast implant" in the literature corpus, not a genuine mechanistic link. The remaining ranked candidates (postmenopausal atrophic vaginitis, ulceration of vulva, vulvar neoplasm, blunt duct/apocrine adenosis of breast, benign mammary dysplasia, breast abscess) were all scored **L4–L5 / Hold** by the pack's own analysis, with no supporting trial or literature evidence directly implicating sodium chloride.

---

## Clinical Trial Evidence

*(for vulvovaginitis — note none of these trials test sodium chloride as the primary intervention; all are graded "C" relevance in the source pack)*

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01230814](https://clinicaltrials.gov/study/NCT01230814) | Phase 2 | Completed | 234 | Tests topical metronidazole/miconazole vaginal suppositories vs. placebo to prevent recurrent vaginal infections; saline not the study drug |
| [NCT01926028](https://clinicaltrials.gov/study/NCT01926028) | Phase 1/2 | Completed | 188 | NDV-3A/NDV-3 vaccine for recurrent vulvovaginal candidiasis; unrelated to sodium chloride |
| [NCT05649735](https://clinicaltrials.gov/study/NCT05649735) | N/A | Completed | 91 | Compares Logusgyn/Candidep vaginal ova/lavage products against a **sterile saline-based vaginal irrigation** comparator arm in non-specific vulvovaginitis — the most directly relevant trial, though saline is the control, not the tested intervention |
| [NCT00616330](https://clinicaltrials.gov/study/NCT00616330) | Phase 3 | Completed | 1443 | Compares vaginal infection treatment products; specific intervention not identified as sodium chloride |
| [NCT05795491](https://clinicaltrials.gov/study/NCT05795491) | N/A | Completed | 60 | Blue LED light therapy for recurrent vulvovaginal candidiasis; unrelated to sodium chloride |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22301569](https://pubmed.ncbi.nlm.nih.gov/22301569/) | 2012 | Cohort | Gynecologic and Obstetric Investigation | Compares clinical/microbiological outcomes of standard antibiotic therapy with vs. without adjunctive saline vaginal irrigation in infectious vaginitis — the primary evidence anchor for this candidate |
| [9839258](https://pubmed.ncbi.nlm.nih.gov/9839258/) | 1998 | Review | The Journal of Reproductive Medicine | Describes normal saline as a culture medium to aid rapid *Candida* detection — a diagnostic, not therapeutic, use |
| [19643525](https://pubmed.ncbi.nlm.nih.gov/19643525/) | 2009 | Review | European Journal of Obstetrics, Gynecology, and Reproductive Biology | Assesses accuracy of vaginal pH measurement from wet-mount slides; tangential to treatment |
| [33860751](https://pubmed.ncbi.nlm.nih.gov/33860751/) | 2021 | Case Report | International Journal of Clinical Pharmacology and Therapeutics | Adverse systemic reaction to terconazole vaginal suppository; saline used only for vaginal washout, not the study intervention |
| [40925571](https://pubmed.ncbi.nlm.nih.gov/40925571/) | 2026 | Case Report | New Zealand Veterinary Journal | Outbreak of infectious pustular vulvovaginitis in dairy heifers — veterinary, not human, and unrelated to sodium chloride |
| [27423947](https://pubmed.ncbi.nlm.nih.gov/27423947/) | 2016 | Cohort | Journal of Dairy Science | Oral calcium chloride/sulfate supplementation in postpartum dairy cows; veterinary and not sodium-chloride specific |
| [39598463](https://pubmed.ncbi.nlm.nih.gov/39598463/) | 2024 | Review | Pharmaceuticals (Basel) | SGLT2-inhibitor-associated diabetic ketoacidosis — appears to be an unrelated keyword-match artifact, not relevant to vulvovaginitis or sodium chloride |

---

## Australia Market Information

No ARTG entries were returned for this DrugBank record (`market_status: Not marketed / Not marketed`, `total_licenses: 0`). This does not necessarily mean saline products are unavailable in Australia generally (isotonic saline is widely marketed under other product listings for IV fluids, irrigation and nasal use), but no product-level ARTG data for this specific evidence pack entry was captured.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. Note that this Evidence Pack recorded a **Blocking-severity data gap (DG001)** — TFDA product warnings/contraindications were unavailable, which prevents a formal S1 safety pre-assessment for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The featured candidate (vulvovaginitis) reaches only L3 (observational) evidence, anchored by a single cohort study on adjunctive saline irrigation — no trial tests sodium chloride as a primary intervention.
- A Blocking data gap (DG001: missing TFDA warnings/contraindications) prevents safety pre-assessment (S1), and MOA data is also missing (DG002).
- The drug has no current ARTG-registered product under this evidence-pack entry, and the model's top-scored candidate (breast fibrocystic disease) was assessed as a likely spurious signal rather than a genuine lead.

**To proceed, the following is needed:**
- Resolve DG001: obtain TFDA/TGA Product Information warnings and contraindications for saline products
- Resolve DG002: obtain a documented mechanism-of-action summary from DrugBank or equivalent
- Confirm current ARTG listings for saline irrigation/topical products relevant to gynaecological use
- A targeted search for controlled trials testing saline vaginal irrigation specifically (rather than as a comparator/washout step) in vulvovaginitis or vulvitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

