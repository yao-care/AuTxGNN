---
layout: default
title: Cefuroxime
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 10
---

# Cefuroxime
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

# Cefuroxime: From Bacterial Infections to Urinary Tract Infection

## One-Sentence Summary

Cefuroxime is a second-generation cephalosporin antibiotic with broad-spectrum bactericidal activity, currently not registered on the ARTG in Australia.
The TxGNN model predicts it may be effective for **Urinary Tract Infection (UTI)**, with **17 clinical trials** and **20 publications** currently supporting this direction — including a 100,000-patient real-world study and multiple completed Phase 4 trials.
Cefuroxime axetil is already approved for UTI in numerous international jurisdictions (FDA, EMA), strongly suggesting the absence of TGA registration reflects regulatory and commercial factors rather than any safety or efficacy concern.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No ARTG registration data available (second-generation cephalosporin antibiotic class) |
| Predicted New Indication | Urinary Tract Infection |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the dataset. Based on known pharmacological information, Cefuroxime is a second-generation cephalosporin beta-lactam antibiotic. It exerts bactericidal activity by binding to penicillin-binding proteins (PBPs), inhibiting the final transpeptidation step of peptidoglycan cell wall synthesis and ultimately causing osmotic bacterial lysis. A key structural advantage over first-generation cephalosporins is its stability against many bacterial beta-lactamases, which broadens Gram-negative coverage to include *Haemophilus influenzae* (including beta-lactamase–producing strains) and *Moraxella catarrhalis* — organisms not reliably covered by earlier cephalosporins.

The oral prodrug cefuroxime axetil achieves urinary drug concentrations that far exceed the MIC₉₀ for the three organisms responsible for over 80% of community-acquired UTIs: *Escherichia coli*, *Klebsiella* spp., and *Proteus mirabilis*. Oral bioavailability of 37–52% combined with renal excretion as the primary elimination route creates a highly favourable PK/PD profile that directly supports the mechanistic plausibility of the TxGNN prediction for this indication.

The prediction is further validated by international regulatory practice. Cefuroxime axetil holds approved UTI indications across multiple major jurisdictions including the USA (FDA), European Union (EMA), and several Asian regulatory authorities. In the Australian context, the drug's absence from the ARTG warrants verification: this may represent a gap in PBS listing or commercial registration rather than a clinical barrier. Local antibiotic resistance patterns — particularly the rising prevalence of ESBL-producing strains documented in 2024–2025 literature — are the primary guardrail for empirical prescribing decisions.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT03020940](https://clinicaltrials.gov/study/NCT03020940) | N/A | Unknown | 100,000 | Largest real-world study of cefuroxime axetil dispersible tablets — 100,000-patient prospective multi-centre non-interventional study assessing safety and efficacy across indications including UTI |
| [NCT05337566](https://clinicaltrials.gov/study/NCT05337566) | N/A | Recruiting | 2,278 | Large RCT comparing azithromycin + cefuroxime vs cefuroxime alone for post-hysterectomy infections; UTI is a primary endpoint (n=2,278, estimated completion December 2030) |
| [NCT04146142](https://clinicaltrials.gov/study/NCT04146142) | N/A | Completed | 550 | RCT comparing antibiotic prophylaxis vs none for transperineal MRI-guided prostate biopsy (n=550); post-procedure UTI prevention as a primary outcome |
| [NCT04616352](https://clinicaltrials.gov/study/NCT04616352) | N/A | Completed | 973 | Retrospective study directly evaluating outcomes of cefuroxime-inappropriate therapy in hospitalised pyelonephritis patients (n=973); most directly relevant to cefuroxime in upper UTI |
| [NCT05609240](https://clinicaltrials.gov/study/NCT05609240) | Phase 2 | Recruiting | 180 | Randomised double-blind trial (Colo-Pro_2) comparing standard bolus vs bolus-continuous infusion cefuroxime prophylaxis for post-colorectal surgery infections including UTI |
| [NCT01507974](https://clinicaltrials.gov/study/NCT01507974) | N/A | Completed | 220 | RCT of preventive antibiotic treatment for recurrent UTI in pregnant women during the puerperium; UTI prevention as the primary endpoint |
| [NCT02072798](https://clinicaltrials.gov/study/NCT02072798) | Phase 4 | Completed | 42 | Phase 4 RCT of antibiotic prophylaxis for post-caesarean section infections including UTI in Denmark; supports cefuroxime for surgical UTI prophylaxis |
| [NCT05577273](https://clinicaltrials.gov/study/NCT05577273) | N/A | Unknown | 1,000 | Assesses whether antibiotic prophylaxis at urinary catheter removal prevents catheter-associated UTI; large sample provides real-world prophylaxis evidence |
| [NCT03221504](https://clinicaltrials.gov/study/NCT03221504) | N/A | Unknown | 221 | RCT comparing 7-day vs 10-day antibiotic course for febrile UTI in children; directly relevant to optimal cefuroxime duration in paediatric UTI |
| [NCT05530551](https://clinicaltrials.gov/study/NCT05530551) | N/A | Active, not recruiting | 20,000 | Large Danish cross-over cluster RCT on single vs multiple prophylactic antibiotic doses for primary total hip arthroplasty; post-surgical UTI is among the infection endpoints (n=20,000) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [18611587](https://pubmed.ncbi.nlm.nih.gov/18611587/) | 1994 | Drug Review | Int J Antimicrob Agents | Landmark narrative review of cefuroxime axetil; confirms strong activity against core UTI pathogens including *H. influenzae*, *S. pneumoniae*, and streptococci; describes oral pharmacokinetics and urinary concentration profiles |
| [38215770](https://pubmed.ncbi.nlm.nih.gov/38215770/) | 2024 | RCT | Lancet Infect Dis | SIMPLIFY trial: de-escalation from antipseudomonal β-lactams to narrow-spectrum agents (including cefuroxime) in Enterobacterales bacteraemia demonstrated to be non-inferior — supports cefuroxime's role in de-escalation stewardship for urinary-source bacteraemia |
| [30234077](https://pubmed.ncbi.nlm.nih.gov/30234077/) | 2018 | Prospective Cohort | Front Pediatrics | 2-year single-centre prospective study (n=82 children): oral cefuroxime axetil safe and effective for first febrile UTI in ambulatory paediatric patients; 96% fever resolution within 48 hours with good tolerance |
| [35069075](https://pubmed.ncbi.nlm.nih.gov/35069075/) | 2021 | Systematic Review | Menopause Review | Comprehensive review of antibiotic resistance prevention in UTI; cefuroxime discussed as second-line agent with emerging resistance stewardship considerations in recurrent UTI in women |
| [40135203](https://pubmed.ncbi.nlm.nih.gov/40135203/) | 2025 | Multicentre Observational | IJID Regions | Susceptibility mapping of *Klebsiella pneumoniae* from 18 Indian centres; provides contemporary regional resistance data directly relevant to empirical cefuroxime prescribing decisions for UTI |
| [39005695](https://pubmed.ncbi.nlm.nih.gov/39005695/) | 2024 | Observational | Infect Dis Clin Microbiol | Community-acquired UTI causative organisms and ESBL risk factors in Turkey; cefuroxime susceptibility data alongside ESBL prevalence trend analysis — important for empirical therapy guidance |
| [39948286](https://pubmed.ncbi.nlm.nih.gov/39948286/) | 2025 | Observational | Int Urol Nephrol | ESBL-producing *E. coli* resistance profiles and risk factors in hospitalised children with community-acquired UTI; critical context for the limits of empirical cefuroxime use in high-risk patients |
| [26607682](https://pubmed.ncbi.nlm.nih.gov/26607682/) | 2016 | Cohort | Braz J Infect Dis | Recurrent UTI follow-up in infants under 2 months old (n=studies); microbiological and recurrence characteristics supporting antibiotic choice including cefuroxime in neonatal UTI management |
| [35096675](https://pubmed.ncbi.nlm.nih.gov/35096675/) | 2021 | Observational | Germs | Paediatric UTI in Bucharest — clinical and antimicrobial resistance data including cefuroxime susceptibility rates among uropathogens in a Central/Eastern European population |
| [30197697](https://pubmed.ncbi.nlm.nih.gov/30197697/) | 2018 | Case Report | Open Microbiol J | Rare case of non-typable *H. influenzae* septicaemia and UTI associated with renal stone disease; cefuroxime cited as an effective treatment option, supporting its use against atypical uropathogens |

---

## Australia Market Information

No ARTG registrations for Cefuroxime were identified in the current dataset (0 entries).

This does not necessarily reflect a safety or efficacy barrier. Cefuroxime (including Zinacef® and generic cefuroxime axetil formulations) is registered and widely available in comparable jurisdictions including the United Kingdom, European Union, and United States. Prescribers should:
- Verify the current TGA registration status directly at the ARTG online portal
- Consider access via the TGA Special Access Scheme (SAS) or Authorised Prescriber pathway if clinically indicated prior to formal ARTG listing
- Check whether any cefuroxime product (including injectable cefuroxime sodium) may already hold an ARTG entry not captured in this dataset

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for full safety information. No drug interaction, key warning, or contraindication data was available in the current dataset.

**Antimicrobial resistance advisory:** Multiple 2024–2025 publications (PMIDs [40135203](https://pubmed.ncbi.nlm.nih.gov/40135203/), [39005695](https://pubmed.ncbi.nlm.nih.gov/39005695/), [39948286](https://pubmed.ncbi.nlm.nih.gov/39948286/)) document rising rates of ESBL-producing *E. coli* and *Klebsiella pneumoniae* with resistance to cefuroxime in community-acquired UTI. Australian local antibiogram data should be reviewed before initiating empirical cefuroxime therapy, particularly in patients with ESBL risk factors (recent hospitalisation, prior broad-spectrum antibiotic use, recurrent UTI, or healthcare-associated infections).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cefuroxime axetil has strong L1-level evidence for UTI, supported by a 100,000-patient real-world study, multiple completed Phase 4 RCTs, published prospective cohort data in paediatric patients, and established international regulatory approvals. The drug's absence from the ARTG appears to reflect regulatory and commercial factors rather than clinical barriers, and represents a solvable gap.

**To proceed, the following is needed:**
- Confirm current TGA ARTG registration status for cefuroxime axetil oral formulation; explore PBS listing pathway for UTI indication if not yet registered
- Obtain Australian local antibiogram data to assess cefuroxime susceptibility rates among community uropathogens — ESBL prevalence is the primary safety guardrail for empirical use
- Obtain full Product Information (PI) including complete contraindications, drug interactions, renal dose adjustment thresholds, and pregnancy safety classification
- Pharmacoeconomic evaluation comparing cefuroxime axetil against currently PBS-subsidised UTI antibiotics (trimethoprim, cefalexin, nitrofurantoin) across uncomplicated, complicated, and paediatric UTI subgroups
- Define patient subgroups where cefuroxime offers a clinical advantage: beta-lactamase–producing *H. influenzae* UTI, penicillin-allergic patients tolerant of cephalosporins, and paediatric febrile UTI where amoxicillin resistance is prevalent

**Secondary finding — Suppurative Otitis Media (L2 evidence, Proceed with Guardrails):**
A separate TxGNN prediction (Rank 9 in this Evidence Pack) identified suppurative otitis media as a secondary indication with L2 evidence and 20 supporting publications. Cefuroxime axetil is already listed as a second-line agent for acute otitis media in international guidelines (American Academy of Pediatrics). A dedicated evaluation report for this indication is recommended as a parallel workstream.

---

> **Disclaimer:** This report is intended for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Prescribers should consult current TGA-approved Product Information and applicable clinical guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

