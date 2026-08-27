---
layout: default
title: Nevirapine
parent: 僅模型預測 (L5)
nav_order: 465
evidence_level: L5
indication_count: 10
---

# Nevirapine
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

# Nevirapine: From HIV-1 Antiretroviral Therapy to Prevention of Mother-to-Child HIV Transmission

## One-Sentence Summary

Nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) established for HIV-1 antiretroviral therapy, currently **not registered in the Australian ARTG**. Of the ten TxGNN-predicted indications reviewed for this drug, most top-scoring candidates (feline immunodeficiency virus, simian immunodeficiency virus, a rare neurodevelopmental disorder, and several benign tumours) have no human clinical relevance and are flagged "Hold" in the evidence pack itself. The best-supported candidate — extending nevirapine's established mechanism to **prevention of mother-to-child (perinatal) HIV transmission**, i.e. congenital HIV — is backed by **10+ completed Phase 3 trials** and **20 publications**, reflecting decades of real-world perinatal use rather than a genuinely novel repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (antiretroviral therapy) — not listed in an Australian ARTG entry; known internationally as an approved NNRTI |
| Predicted New Indication | Prevention of Mother-to-Child (Perinatal) HIV Transmission — Congenital HIV |
| TxGNN Prediction Score | 98.52% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data was not available from the evidence pack (`original_moa: [Data Gap]`). However, the literature evidence retrieved for this candidate repeatedly and consistently describes nevirapine as a first-generation NNRTI: it binds non-competitively at a hydrophobic pocket adjacent to the active site of HIV-1 reverse transcriptase, blocking the enzyme's RNA-dependent DNA polymerase activity and halting conversion of viral RNA into proviral DNA.

The predicted "new" indication — congenital HIV / mother-to-child transmission prevention (PMTCT) — is mechanistically identical to nevirapine's original antiretroviral use, not a distinct pathway. Blocking reverse transcription in the mother reduces maternal viral load, and prophylactic dosing of the neonate blocks establishment of infection during intrapartum and early postnatal exposure. Because nevirapine is orally bioavailable, inexpensive, and has a long half-life permitting single-dose or short-course prophylaxis, it became a WHO-recommended PMTCT strategy in resource-limited settings (e.g., the HIVNET 012 regimen) — this is why the supporting evidence base is unusually large and mature compared with a typical TxGNN-only prediction.

By contrast, the raw top-ranked TxGNN predictions for this drug (feline AIDS, simian immunodeficiency virus infection, an ultra-rare neurodevelopmental disorder, prostate fibroma, Brenner tumour) either concern non-human disease models or benign neoplasms with no plausible link to an antiretroviral mechanism — the evidence pack's own rationale text flags these as likely graph noise, and this report does not pursue them further.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001135](https://clinicaltrials.gov/study/NCT00001135) | Phase 3 | Completed | 2,009 | Double-blind RCT of nevirapine (NVP) given to mother and infant vs. control to reduce maternal-fetal HIV transmission |
| [NCT00639938](https://clinicaltrials.gov/study/NCT00639938) | Phase 3 | Completed | 722 | Standard two-dose NVP regimen ± HIV immune globulin or extended infant NVP dosing for PMTCT in Uganda |
| [NCT01061151](https://clinicaltrials.gov/study/NCT01061151) | Phase 3 | Completed | 3,747 | PROMISE study — optimal antepartum, intrapartum and breastfeeding-period PMTCT interventions |
| [NCT02738502](https://clinicaltrials.gov/study/NCT02738502) | Phase 2 | Completed | 91 | PMTCT strategy without NRTIs; neonatal prophylaxis with nevirapine |
| [NCT03642704](https://clinicaltrials.gov/study/NCT03642704) | Phase 4 | Completed | 56 | Early HIV diagnosis and preventive antiretroviral treatment (incl. NVP) at birth for high-risk newborns, Guinea |
| [NCT01511237](https://clinicaltrials.gov/study/NCT01511237) | Phase 3 | Completed | 379 | PHPT-5 — perinatal antiretroviral intensification for PMTCT in women with <8 weeks antenatal HAART, Thailand |
| [NCT00164736](https://clinicaltrials.gov/study/NCT00164736) | Phase 3 | Completed | 2,369 | ARV prophylaxis (mother or infant) plus nutritional support to prevent transmission during breastfeeding |
| [NCT00197587](https://clinicaltrials.gov/study/NCT00197587) | N/A | Completed | 1,200 | "Mashi" study — prevention of milk-borne HIV-1C transmission, Botswana |
| [NCT02383849](https://clinicaltrials.gov/study/NCT02383849) | N/A (Phase 4) | Completed | 124 | IMPAACT P1106 — pharmacokinetics and safety of nevirapine (and other ARVs) in low-birth-weight infants |
| [NCT00102960](https://clinicaltrials.gov/study/NCT00102960) | Phase 3 | Completed | 377 | Strategies for antiretroviral therapy in infants shortly after primary HIV infection, resource-poor setting |

No ANZCTR-registered trials were identified for this indication in the evidence pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15249569](https://pubmed.ncbi.nlm.nih.gov/15249569/) | 2004 | RCT | JAMA | Nevirapine + zidovudine given at birth reduces perinatal HIV transmission in women presenting in labour with unknown HIV status |
| [29912896](https://pubmed.ncbi.nlm.nih.gov/29912896/) | 2018 | Systematic review / NMA | PLoS ONE | Network meta-analysis of comparative safety/effectiveness of perinatal antiretroviral regimens |
| [19236121](https://pubmed.ncbi.nlm.nih.gov/19236121/) | 2009 | Systematic review | Drug Safety | Hepatotoxicity risk with long- vs short-course prophylactic nevirapine use (RADAR project) |
| [11825335](https://pubmed.ncbi.nlm.nih.gov/11825335/) | 2001 | Review | Expert Opin Pharmacother | Overview of nevirapine's role and efficacy in HIV-1 treatment |
| [15794723](https://pubmed.ncbi.nlm.nih.gov/15794723/) | 2005 | Review | Expert Opin Drug Saf | Safety of antiretroviral drugs, incl. nevirapine, in pregnancy |
| [21711178](https://pubmed.ncbi.nlm.nih.gov/21711178/) | 2011 | Cohort | AIDS Care | Maternal HIV infection and birth outcomes under enhanced antenatal PMTCT care, Pune, India |
| [24781315](https://pubmed.ncbi.nlm.nih.gov/24781315/) | 2014 | Cohort | PLoS Medicine | French ANRS perinatal cohort — birth defect prevalence by individual ARV drug exposure |
| [21084995](https://pubmed.ncbi.nlm.nih.gov/21084995/) | 2011 | Cohort | J Acquir Immune Defic Syndr | Pregnancy outcomes compared between efavirenz- and nevirapine-exposed women |
| [35621877](https://pubmed.ncbi.nlm.nih.gov/35621877/) | 2022 | Cohort | J Acquir Immune Defic Syndr | Impact of antenatal ARV regimen on pregnancy/infant outcomes in HIV/HBV coinfection |
| [17713983](https://pubmed.ncbi.nlm.nih.gov/17713983/) | 2007 | Cohort | PLoS Medicine | Two-tiered PMTCT strategy evaluation, West Africa |

---

## Safety Considerations

Structured safety fields (key warnings, contraindications, DDI) were not available for this candidate. However, literature evidence retrieved for this indication repeatedly flags **hepatotoxicity and severe cutaneous reactions** as characteristic nevirapine risks — including a systematic review/meta-analysis specifically on short- vs. long-course prophylactic use (PMID 19236121) and a toxicogenomics study of cutaneous/hepatic adverse events across populations (PMID 21505298). As nevirapine is not currently registered in Australia, prescribers should obtain formal safety and interaction data from the TGA-approved Product Information once available, rather than relying on this evidence summary alone.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs and a large observational/systematic-review literature base (L1) support nevirapine's use in perinatal HIV transmission prevention — but this is an extension of its existing, decades-old antiretroviral mechanism rather than a novel repurposing signal, and the drug is currently unregistered in Australia (0 ARTG entries).

**To proceed, the following is needed:**
- TFDA/TGA product information — warnings and contraindications (currently a Blocking data gap; required before any S1 safety assessment)
- Formal DrugBank/PI-sourced mechanism-of-action confirmation (currently a High-severity data gap)
- Australian regulatory pathway assessment for ARTG registration, given current "not marketed" status
- A structured drug-drug interaction query (current DDI query returned "not found")
- Australian-context perinatal/neonatal dosing guidance if pursued for a PMTCT program
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

