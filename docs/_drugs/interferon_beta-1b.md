---
layout: default
title: Interferon Beta-1B
parent: Model Prediction Only (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
---

# Interferon Beta-1B
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

# Interferon beta-1b: From Relapsing-Remitting Multiple Sclerosis to Autoimmune Disease of the Central Nervous System

## One-Sentence Summary

Interferon beta-1b is an immunomodulatory protein originally used to treat relapsing-remitting multiple sclerosis (RRMS).
The TxGNN model's top-ranked prediction is **hairy cell leukaemia**, which has no supporting studies. The best-supported prediction is **autoimmune disease of the central nervous system** (rank 2), with **6 clinical trials** and **18 publications**. This category is largely the same as the drug's existing indication (multiple sclerosis), so it is not a true repurposing finding.

*Note: The first-ranked prediction (hairy cell leukaemia) has no trials or literature (Evidence Level L5, Hold). This report focuses on rank 2 because it is the only top-ranked prediction with substantial evidence. Other predictions are summarised briefly below.*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsing-remitting multiple sclerosis (the ARTG entry does not list indication text) |
| Predicted New Indication | Autoimmune disease of the central nervous system (rank 2; rank 1 is hairy cell leukaemia, L5, Hold) |
| TxGNN Prediction Score | 99.02% (rank 1, hairy cell leukaemia: 99.16%) |
| Evidence Level | L1 (rank 2); note that the evidence is mostly for MS, the original indication |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. From the published literature, interferon beta-1b is understood to modulate the immune system. It reduces T-cell activation, lowers MHC class II expression on antigen-presenting cells, shifts cytokine balance toward an anti-inflammatory profile, and limits immune-cell trafficking across the blood-brain barrier. The exact mechanism in MS is not fully established.

The predicted category, "autoimmune disease of the central nervous system", is dominated by multiple sclerosis, the drug's existing indication. The prediction is therefore reasonable, but it largely reflects the original indication rather than a new use. The data compiled for this report contain no evidence for non-MS CNS autoimmune conditions. In neuromyelitis optica spectrum disorder (NMOSD), interferon beta may in fact worsen disease.

**Other predictions in the top 10:**
- **Hairy cell leukaemia (rank 1) and its variant (rank 8):** Interferon alpha has established activity in hairy cell leukaemia, and interferon beta-1b acts through the same receptor (IFNAR), so a link is plausible. However, there are no trials or literature for this drug, and the variant is generally less responsive to interferons. Evidence Level L5, Hold.
- **Progressive multiple sclerosis (rank 7):** L2. Indirect support from reviews and a 2024 network meta-analysis. The only Phase 3 trial (NCT00313976) was withdrawn with no participants enrolled. Benefit in primary progressive MS is limited.
- **Multiple sclerosis, susceptibility to (rank 4):** L3. Literature covers pharmacogenomics and adverse reactions only. It is useful for research on response prediction, not as a separate indication.
- **Fetal methylmercury syndrome, hepatic infarction, extramammary Paget disease, peliosis hepatis (ranks 5, 6, 9, 10):** No plausible mechanism and no evidence (L5, Hold). The drug carries hepatotoxicity warnings, which argues against use in the liver conditions.

---

## Clinical Trial Evidence

Trials for autoimmune disease of the central nervous system (rank 2):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00185211](https://clinicaltrials.gov/study/NCT00185211) | Phase 3 | Completed | 468 | Open-label extension of the placebo-controlled BENEFIT study; long-term data on early versus delayed interferon beta-1b in early MS |
| [NCT01333501](https://clinicaltrials.gov/study/NCT01333501) | Phase 4 | Completed | 151 | Randomised, rater-blinded comparison of fingolimod with interferon beta-1b on cognitive symptoms in RRMS |
| [NCT00893217](https://clinicaltrials.gov/study/NCT00893217) | Phase 2 | Completed | 71 | Double-blind safety and tolerability study of 500 mcg versus 250 mcg every other day in RRMS |
| [NCT01158183](https://clinicaltrials.gov/study/NCT01158183) | N/A | Completed | 226 | Real-world observational study of 12-month outcomes in relapsing MS |
| [NCT01111656](https://clinicaltrials.gov/study/NCT01111656) | Phase 2 | Completed | 28 | Follow-up of atorvastatin added to interferon beta-1b in RRMS (small combination study) |
| [NCT01701856](https://clinicaltrials.gov/study/NCT01701856) | Phase 4 | Terminated | 5 | Natalizumab de-escalation to interferon beta-1b; terminated early and uninformative |

Further trials for the closely related category "CNS demyelinating autoimmune disease" (rank 3) include [NCT00459667](https://clinicaltrials.gov/study/NCT00459667) (Phase 3b, 1,420 participants, dose comparison of 250 mcg and 500 mcg in relapsing MS) and [NCT03577977](https://clinicaltrials.gov/study/NCT03577977) (retrospective data in children and adolescents with MS, n=70). Most other trials listed for that category are observational adherence or device studies.

No ANZCTR identifiers are present in the data compiled for this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38032059](https://pubmed.ncbi.nlm.nih.gov/38032059/) | 2023 | Network meta-analysis | Cochrane Database Syst Rev | Compares the relative adverse effects of MS immunotherapies |
| [38174776](https://pubmed.ncbi.nlm.nih.gov/38174776/) | 2024 | Network meta-analysis | Cochrane Database Syst Rev | Relative benefit of immunomodulators and immunosuppressants in RRMS (update of the 2015 review) |
| [26384035](https://pubmed.ncbi.nlm.nih.gov/26384035/) | 2015 | Network meta-analysis | Cochrane Database Syst Rev | Original network meta-analysis of therapies for RRMS |
| [39254048](https://pubmed.ncbi.nlm.nih.gov/39254048/) | 2024 | Network meta-analysis | Cochrane Database Syst Rev | Immunomodulators and immunosuppressants in progressive MS |
| [21128695](https://pubmed.ncbi.nlm.nih.gov/21128695/) | 2011 | Review | CNS Drugs | Large randomised trials of 2 to 3.5 years show efficacy of 250 µg every other day in MS, including after a first clinical event |
| [18698876](https://pubmed.ncbi.nlm.nih.gov/18698876/) | 2008 | Review | CNS Drugs | In BENEFIT, relative risk of clinically definite MS was reduced by 41% over 3 years |
| [28440858](https://pubmed.ncbi.nlm.nih.gov/28440858/) | 2017 | Systematic review | Cochrane Database Syst Rev | Disease-modifying drugs after a first clinical attack suggestive of MS |
| [30610426](https://pubmed.ncbi.nlm.nih.gov/30610426/) | 2020 | Long-term follow-up | J Neurol | Long-term outcomes from early treatment of clinically isolated syndrome in BENEFIT 11 |
| [15182221](https://pubmed.ncbi.nlm.nih.gov/15182221/) | 2004 | Review | CNS Drugs | Review of use in RRMS and secondary progressive MS |
| [25482255](https://pubmed.ncbi.nlm.nih.gov/25482255/) | 2014 | Review | Neurol Neurochir Pol | Long-term follow-up of the pivotal trial and the effect of interferon beta on survival |

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 8101J | Betaferon | Injection set including 1 vial powder for injection 8,000,000 I.U. (250 micrograms) and solvent | Not listed in the data compiled for this report |

---

## Safety Considerations

Specific warnings and contraindications are not available in the data compiled for this report. Please refer to the TGA-approved Product Information (PI) for safety information.

**Drug interactions:** 100 interactions were identified in total. Examples include:
- **Major:** Bupropion
- **Moderate:** Pioglitazone, rosiglitazone, simvastatin, rosuvastatin, clarithromycin, levofloxacin, minocycline, naltrexone, orlistat, acarbose, and anabolic steroids (oxandrolone, oxymetholone, stanozolol)

Published literature also notes that interferon beta-1b can cause liver enzyme elevation, injection site reactions, flu-like symptoms, and rarely severe skin reactions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence for rank 2 is substantial (a Phase 3 extension trial, several Cochrane network meta-analyses, and many reviews), but it concerns multiple sclerosis, which is the drug's existing indication. It does not demonstrate a new use. The top-ranked prediction, hairy cell leukaemia, has no supporting evidence and should remain on Hold.

**To proceed, the following is needed:**
- Confirm the current TGA-approved indications for Betaferon, as the indication text was not available
- Retrieve the TGA Product Information to complete warnings and contraindications
- Obtain detailed mechanism of action data
- Define whether any non-MS CNS autoimmune condition is being targeted. Evidence for these is absent, and interferon beta may worsen NMOSD.
- For hairy cell leukaemia, a literature and trial review would be needed before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

