---
layout: default
title: Rifaximin
parent: Model Prediction Only (L5)
nav_order: 591
evidence_level: L5
indication_count: 10
---

# Rifaximin
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

# Rifaximin: From Enteric Antibacterial Use to HIV-Associated Immune Activation (Investigational)

## One-Sentence Summary

Rifaximin is a non-absorbed, gut-restricted rifamycin-class antibiotic; the source evidence pack does not contain a confirmed original TGA-approved indication text, and the drug is **not currently marketed in Australia** (0 ARTG entries). Of TxGNN's ten predicted indications, the two highest-scoring candidates (oral candidiasis, candidiasis) are **not genuine repurposing signals** — the underlying literature describes rifaximin as *increasing* Candida infection risk via gut dysbiosis, not treating it. The only candidate with a coherent, literature-supported mechanistic rationale is **HIV infectious disease** (rank 9, TxGNN score 98.23%), evaluated at decision stage S1 ("Research Question") on the strength of **1 clinical trial** and **6 publications**, though the clinical trial data (withdrawn, 0 enrolled) and RCT literature (marginal, non-significant effects) do not currently support efficacy.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no licence/indication text on record; general pharmacological class: enteric antibacterial) |
| Predicted New Indication | HIV infectious disease *(selected over the nominal top-ranked "oral candidiasis" — see note below)* |
| TxGNN Prediction Score | 98.23% |
| Evidence Level | L3 (observational/RCT evidence exists but shows no significant clinical benefit) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

> **Note on candidate selection:** TxGNN ranked "oral candidiasis" (99.75%) and "candidiasis" (99.15%) highest by score. The evidence pack's own mechanistic annotations state these are **negative associations** — rifaximin use is described in the literature as *favouring* Candida overgrowth via gut dysbiosis, not treating it. Presenting these as "predicted new indications" would be misleading, so this report focuses on the highest-ranked candidate with a genuine treatment-direction rationale and real supporting evidence (HIV infectious disease, S1/"Research Question"). Ranks 2–5, 7, 8, 10 have no clinical trial or literature support at all (evidence level L5, TxGNN score noise) and are not discussed further.

---

## Why is This Prediction Reasonable?

Detailed, drug-pack-sourced mechanism of action is flagged as a data gap (DG002), so the following draws only on the mechanistic rationale documented against the HIV candidate in the evidence pack itself. Rifaximin is a rifamycin-class antibiotic that inhibits bacterial RNA polymerase; because it is essentially non-absorbed from the gut, its action is confined to the intestinal lumen.

The proposed link to HIV infection is indirect: HIV-associated damage to the gut mucosal barrier allows bacterial products to translocate into the bloodstream, driving chronic immune activation — a recognised contributor to HIV disease progression even in patients on antiretroviral therapy. The hypothesis is that suppressing gut bacterial flora with rifaximin would reduce this microbial translocation and downstream immune activation, and/or treat HIV-associated enteric co-infections (e.g. *Cryptosporidium*, enteroaggregative *E. coli*) that are common in this population.

However, the two RCTs specifically testing this hypothesis in HIV-positive immune non-responders (ACTG A5286) found only a **marginal, non-statistically-significant** effect on microbial translocation, T-cell activation and inflammation, and **no significant change** in rectal microbial diversity. The one registered trial directly addressing rifaximin in HIV-related liver disease (NCT01654939) was withdrawn with zero enrolment. This means the mechanistic story is biologically plausible but has already been tested and has not shown a clinical benefit — this is a "negative/inconclusive trial" situation rather than an untested hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01654939](https://clinicaltrials.gov/study/NCT01654939) | Phase 4 | Withdrawn | 0 | Intended to assess rifaximin's impact on liver fibrosis in HIV-infected patients with liver disease (hepatitis C co-infection); withdrawn before enrolment, no data generated |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25214516](https://pubmed.ncbi.nlm.nih.gov/25214516/) | 2015 | RCT | J Infect Dis | ACTG A5286: rifaximin had only a **marginal impact** on microbial translocation, T-cell activation and inflammation in HIV-positive ART immune non-responders |
| [31583331](https://pubmed.ncbi.nlm.nih.gov/31583331/) | 2019 | RCT | Pathogens & Immunity | Follow-up analysis of ACTG A5286: 4 weeks of rifaximin **failed to significantly alter** rectal microbial diversity |
| [21918437](https://pubmed.ncbi.nlm.nih.gov/21918437/) | 2011 | Review | Curr Opin HIV AIDS | General review of end-stage liver disease management in HIV/HCV co-infection; no rifaximin-specific trial data |
| [36533398](https://pubmed.ncbi.nlm.nih.gov/36533398/) | 2023 | Review | Expert Rev Anti Infect Ther | Review of cryptosporidiosis treatment options; rifaximin not the primary focus |
| [17005776](https://pubmed.ncbi.nlm.nih.gov/17005776/) | 2006 | Review | J Med Microbiol | Review of enteroaggregative *E. coli* as an enteric pathogen relevant to HIV-infected patients |
| [10632386](https://pubmed.ncbi.nlm.nih.gov/10632386/) | 1999 | Cohort | J Chemother | Observational study of intestinal protozoa (*Cryptosporidium*, *Blastocystis*) in HIV patients; rifaximin effect noted but not the primary endpoint |

---

## Australia Market Information

Rifaximin has **no ARTG entries** and is **not currently marketed in Australia**. There is no TGA-approved Product Information for this product in the Australian market at present.

---

## Safety Considerations

The evidence pack contains no usable safety data — key warnings, contraindications and drug interaction records are all data gaps (DG001, flagged as **Blocking**), and the DDI query returned no results.

> As rifaximin is not TGA-registered, there is no Australian Product Information available. Safety assessment would need to draw on overseas-approved PI (e.g. US/EU rifaximin labelling) as a starting reference, pending confirmation of any Australian-specific data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only mechanistically coherent candidate (HIV infectious disease) has already been directly tested in two RCTs, both showing marginal-to-no clinical benefit, and its one registered trial was withdrawn with zero enrolment. Combined with the drug's non-marketed status in Australia and a **blocking** safety data gap (no TFDA/TGA warning or contraindication data), there is not enough support to advance this candidate.

**To proceed, the following is needed:**
- Resolve DG001 (blocking): obtain TGA/overseas Product Information for warnings and contraindications before any S1 safety screening
- Resolve DG002: confirm detailed mechanism of action from DrugBank or primary pharmacology sources
- If pursuing the HIV hypothesis further, a new trial design would need to address why prior RCTs (ACTG A5286) failed to show significant effect — e.g. different dosing, duration, or patient subgroup
- Re-run TxGNN evidence triage to exclude negative-association predictions (oral candidiasis, candidiasis) from being surfaced as "repurposing candidates" in future reports
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

