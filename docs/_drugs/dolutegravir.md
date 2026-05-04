---
layout: default
title: Dolutegravir
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
---

# Dolutegravir
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

# Dolutegravir: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Dolutegravir (DTG) is a second-generation integrase strand transfer inhibitor (INSTI), used globally as the preferred first-line antiretroviral for HIV-1 infection in adults and children — though not currently registered in Australia.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**, supported by greater than 80% integrase enzyme sequence homology between SIV and HIV-1, with **1 clinical trial** and **15 publications** providing context for this direction.
This prediction reflects a veterinary and translational research application rather than a novel human clinical indication; the most actionable human repurposing signals in this Evidence Pack are **AIDS Related Complex (ARC)** and **Congenital HIV** (both Evidence Level L1, "Proceed with Guardrails").

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (not registered in Australia; globally approved) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold (Research Context Only) |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data was not available from the data sources accessed in this Evidence Pack. Based on established pharmacological knowledge, Dolutegravir inhibits HIV-1 replication by competitively blocking the integrase-catalysed strand transfer reaction — chelating two catalytic magnesium ions within the integrase active site to prevent viral DNA integration into the host genome. This mechanism confers a high genetic barrier to resistance, requiring multiple simultaneous integrase mutations for treatment failure, and is associated with favourable CNS penetration relative to earlier-generation INSTIs.

The mechanistic basis for the SIV prediction is well-founded. SIV integrase shares greater than 80% amino acid sequence homology with HIV-1 integrase, and the DDE catalytic triad — the binding motif targeted by all INSTIs including DTG — is fully conserved across primate lentiviruses. Multiple in vitro and non-human primate (NHP) studies have confirmed that DTG inhibits SIV integrase with comparable potency to HIV-1 integrase, and that DTG-containing combination ART (cART) effectively suppresses SIVmac239 and SIVmac251 replication to clinically relevant levels in rhesus macaques and other species. DTG has accordingly become the standard background antiretroviral in SIV-based HIV translational research.

It is important to contextualise this prediction appropriately for Australian clinicians. SIV infection is a disease of non-human primates, not humans. DTG's established role in SIV models is as a validated research tool — used to study viral reservoir dynamics, CNS penetration, immune reconstitution, and resistance mechanisms — rather than a novel human therapeutic indication. The more clinically meaningful repurposing signals in this Evidence Pack for human patient care are **AIDS Related Complex (ARC, rank 5, L1 evidence)** and **Congenital/Perinatal HIV (rank 6, L1 evidence)**, both supported by completed Phase 3 RCTs and consistent with current WHO 2023 and DHHS 2024 treatment guidelines.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Vedolizumab (gut-selective integrin inhibitor) combined with ART in HIV-infected, ART-naïve subjects — DTG is used as background ART, not the primary investigational agent; trial evaluates impact of vedolizumab on viral reservoir and remission post-ART interruption; no direct SIV-specific therapeutic intervention |

> No clinical trials directly evaluating DTG as a therapeutic intervention for SIV infection were identified. The trial above uses DTG as background ART in a HIV reservoir study; its relevance to SIV infection is indirect only.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [30381490](https://pubmed.ncbi.nlm.nih.gov/30381490/) | 2019 | Animal Study (NHP) | Journal of Virology | DTG monotherapy in SIV-infected macaques selects multiple resistance mutation patterns with variable virological outcomes — directly confirms DTG antiviral activity against SIV and characterises resistance pathways |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Animal Study (NHP) | AIDS Research and Human Retroviruses | Novel coformulated injectable cART regimens including DTG-class agents evaluated in SIVmac239-infected rhesus macaques — effective viral suppression to clinically relevant levels achieved |
| [36365101](https://pubmed.ncbi.nlm.nih.gov/36365101/) | 2022 | Animal Study (NHP) | Pharmaceutics | Pharmacological validation of long-term ART (TDF/FTC/DTG) in SIVmac251-infected NHPs — single-dose PK study confirms DTG pharmacokinetic suitability, efficacy, and tolerability in NHP SIV models |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | In vitro + NHP Model | Journal of Virology | Characterisation of INSTI resistance profiles in SIVmac239 via tissue culture selection — DTG resistance mutation pathways identified and directly compared to HIV-1, confirming conserved susceptibility genetics |
| [28576126](https://pubmed.ncbi.nlm.nih.gov/28576126/) | 2017 | Veterinary Case Study | Retrovirology | First reported effective treatment of SIVcpz-induced AIDS-like immunopathology in a captive western chimpanzee using combination ART — demonstrates translational relevance of INSTI-based regimens for primate lentiviral disease |
| [40093003](https://pubmed.ncbi.nlm.nih.gov/40093003/) | 2025 | Animal Study (NHP) | Frontiers in Immunology | FTC/TDF/DTG cART in SIV-infected rhesus macaques — evaluates timing of treatment initiation, CNS extracellular free water changes, and white matter tract integrity; highlights DTG CNS penetration relevance |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal Study (NHP) | mBio | Lentiviral infections persist in brain despite effective ART (including DTG-based regimens) in SIV-infected macaques and HIV-infected humans — highlights the CNS reservoir challenge that NHP/SIV models are used to study |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | Structural Biology / Review | FEBS Journal | Structural analysis of HIV/SIV intasome complexes via cryo-EM — explains how second-generation INSTIs (DTG, bictegravir) bind integrase, underpinning the mechanistic basis for cross-species antiviral activity and resistance |
| [32166319](https://pubmed.ncbi.nlm.nih.gov/32166319/) | 2020 | In vitro / Basic Science | Clinical Infectious Diseases | DTG and raltegravir exert pro-adipogenic and pro-fibrotic effects and induce insulin resistance in human and simian adipose tissue — important metabolic safety signal relevant to both SIV model interpretation and clinical use |
| [30161247](https://pubmed.ncbi.nlm.nih.gov/30161247/) | 2018 | Animal Study (NHP) | PLOS Pathogens | p38 MAPK inhibition combined with ART (including DTG-based regimens) reduces SIV-induced immune activation and provides additional protection from immune deterioration in macaques — supports NHP model utility for adjunctive therapy research |

---

## Australia Market Information

Dolutegravir is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. There are no ARTG entries for this drug as of the data cutoff date (April 2026).

Internationally, Dolutegravir is approved under the following brand names: **Tivicay®** (50 mg tablet, single agent), **Triumeq®** (DTG/abacavir/lamivudine fixed-dose combination), **Dovato®** (DTG/lamivudine fixed-dose combination), and **Juluca®** (DTG/rilpivirine fixed-dose combination), with regulatory approvals from the FDA (USA), EMA (Europe), and listing on the WHO Essential Medicines List for HIV treatment in adults, adolescents, and children.

Australian clinicians wishing to access Dolutegravir should consider applying through the TGA's **Special Access Scheme (SAS) Category B** for individual patients or the **Authorised Prescriber** pathway. Product information from the FDA or EMA should be consulted for prescribing guidance in the absence of a TGA-approved Australian PI.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. As Dolutegravir is not currently registered in Australia, clinicians should consult the FDA or EMA-approved Product Information for **Tivicay®** (dolutegravir).

**Pregnancy Safety Signal (Clinically Critical):** Multiple population-based cohorts and pharmacovigilance analyses have identified an approximately 2–3-fold increased risk of neural tube defects (NTDs) associated with DTG exposure at or around the time of conception (approximately 0.3% vs. background rate ~0.1% in the Botswana Tsepamo cohort). WHO 2022 updated guidelines retain DTG as the preferred first-line antiretroviral — including for women of childbearing potential — but recommend:
- Supplemental **folic acid 5 mg/day** for all women of reproductive age taking DTG
- Pre-conception counselling regarding NTD risk
- Continued monitoring via large population-based birth outcome studies (e.g., Eswatini national transition study, n = 50,075)

---

## Conclusion and Next Steps

**Decision: Hold (Research Context Only)**

**Rationale:**
The TxGNN prediction of DTG for SIV infection is mechanistically sound and consistent with a large body of NHP translational research; however, SIV is a non-human primate disease with no direct human clinical repurposing pathway. This signal confirms DTG's validity as a standard tool drug for HIV/SIV translational research rather than identifying a new human therapeutic indication.

**Most Clinically Actionable Findings for Australian Healthcare Professionals:**

The full Evidence Pack identifies two human indications with substantially stronger clinical relevance and actionability:

| Indication | Rank | Evidence Level | Recommendation | Key Basis |
|-----------|------|---------------|----------------|-----------|
| AIDS Related Complex (ARC) | 5 | L1 | Proceed with Guardrails | WHO 2023 & DHHS 2024 preferred ARV; Phase 3 RCT data; covers full HIV disease spectrum including ARC |
| Congenital / Perinatal HIV | 6 | L1 | Proceed with Guardrails | Phase 3 RCTs (NCT03048422, n=643; NCT05883761, n=50,075); paediatric PK and dosing established; NTD safety monitoring required |

**To proceed with SIV research application, the following is needed:**
- Institutional Animal Ethics Committee (IAEC) approval
- Veterinary regulatory pathway assessment (outside TGA scope)
- Species-specific DTG dosing and formulation confirmation for the NHP species of interest

**For human clinical application (ARC and Congenital HIV) in Australia:**
- TGA Special Access Scheme (SAS Category B) or Authorised Prescriber approval
- Reference to FDA/EMA-approved PI for Tivicay® for full safety and dosing guidance
- Supplemental folic acid protocol (5 mg/day) for all women of childbearing potential
- Paediatric weight-band dosing protocols for congenital/perinatal HIV treatment
- Safety monitoring plan addressing the NTD signal in pregnant women and those planning conception
- Formal mechanism of action documentation to satisfy local pharmacovigilance requirements

---

> **Disclaimer:** This report is intended for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All website pages and research outputs from this system include a YMYL disclaimer: predicted indications must be verified through clinical trials before use in patient care.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

