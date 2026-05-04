---
layout: default
title: Eltrombopag
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
---

# Eltrombopag
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

# Eltrombopag: From Immune Thrombocytopenia to HIV Infectious Disease

## One-Sentence Summary

Eltrombopag is an oral thrombopoietin receptor (TPO-R) agonist, internationally used to treat thrombocytopenia in immune thrombocytopenic purpura (ITP), hepatitis C-associated thrombocytopenia, and aplastic anaemia. The TxGNN model predicts it may be effective for **HIV Infectious Disease** — specifically in managing HIV-associated thrombocytopenia — with **5 clinical trials** and **10 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Immune thrombocytopenia (ITP) and related thrombocytopaenic conditions (not currently TGA-registered) |
| Predicted New Indication | HIV Infectious Disease (HIV-associated thrombocytopenia) |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Eltrombopag is a small-molecule, non-peptide TPO-R agonist that binds to the transmembrane domain of the c-Mpl receptor. Unlike endogenous thrombopoietin, it activates the JAK2/STAT signalling pathway to stimulate megakaryocyte proliferation and platelet production without competing with native TPO. Detailed MOA documentation was not available in this evidence pack; however, Eltrombopag's pharmacology is extensively characterised in international literature, and its clinical efficacy in ITP and aplastic anaemia is well-established.

HIV infection drives thrombocytopenia through two overlapping mechanisms: immune-mediated platelet destruction (autoantibodies and immune complex deposition on platelet surfaces) and direct HIV-associated suppression of megakaryocyte precursors in the bone marrow. These mechanisms are biologically analogous to those seen in primary ITP — Eltrombopag's established therapeutic setting. By stimulating TPO-R to compensate for reduced platelet production and overcome immune-mediated destruction, Eltrombopag addresses the shared pathophysiological basis of both conditions. Case series and case reports (PMID 25504472, PMID 22992580, PMID 25333665) have confirmed that Eltrombopag successfully raises platelet counts in HIV-positive patients with refractory thrombocytopenia, including one case of severe aplastic anaemia associated with HIV where a trilineage haematological response and immunomodulatory benefit were observed.

A secondary exploratory hypothesis is raised by a 2020 in vitro pharmacological screen (PMID 32977702), which identified Eltrombopag as a potential modulator of HIV-1 proviral transcription. This antiviral mechanism remains entirely unvalidated in clinical settings and should not be considered a primary therapeutic rationale. The clinically meaningful application of Eltrombopag in HIV is therefore best positioned as **management of HIV-associated thrombocytopenia**, which is mechanistically and clinically analogous to its core ITP indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01636778](https://clinicaltrials.gov/study/NCT01636778) | Phase 2 | Completed | 45 | SB-497115-GR (Eltrombopag early designation) raised platelet counts in HCV-thrombocytopenic patients with compensated cirrhosis to levels sufficient for antiviral therapy initiation; most directly relevant trial, most likely to have enrolled HIV co-infected subjects |
| [NCT00529568](https://clinicaltrials.gov/study/NCT00529568) | Phase 3 | Completed | 759 | Largest completed trial — Eltrombopag maintained platelet counts to facilitate Peg-IFN/RBV therapy initiation and minimise dose reductions; SVR measured as primary clinical benefit endpoint (ENABLE series) |
| [NCT00516321](https://clinicaltrials.gov/study/NCT00516321) | Phase 3 | Completed | 687 | Companion ENABLE trial using Peg-IFN alfa-2a; provides paired indirect evidence for infection-induced immune thrombocytopenia mechanistic analogy |
| [NCT00678587](https://clinicaltrials.gov/study/NCT00678587) | Phase 3 | Terminated | 292 | Randomised double-blind placebo-controlled trial in chronic liver disease thrombocytopenia undergoing invasive procedures; terminated early — reason not publicly disclosed, requiring investigation before extrapolation |
| [NCT00996216](https://clinicaltrials.gov/study/NCT00996216) | Phase 3 | Completed | 27 | Open-label rollover safety study assessing long-term tolerability in HCV thrombocytopenia; very small sample size limits efficacy contribution |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [25504472](https://pubmed.ncbi.nlm.nih.gov/25504472/) | 2015 | Case Series | J Int Assoc Provid AIDS Care | Eltrombopag and romiplostim effective as salvage therapy for refractory HIV-associated ITP; recommends optimising HAART before initiating TPO-RAs |
| [22185370](https://pubmed.ncbi.nlm.nih.gov/22185370/) | 2012 | Retrospective Series | Platelets | Danish real-world series of 32 patients receiving TPO-RAs; includes off-label secondary ITP use, providing context for HIV-related applications |
| [19932434](https://pubmed.ncbi.nlm.nih.gov/19932434/) | 2009 | Narrative Review | Hematol Oncol Clin N Am | Reviews infectious causes of chronic ITP (HCV, HIV, H. pylori); treating the primary infection often resolves thrombocytopenia; TPO-RAs indicated for refractory cases |
| [19245929](https://pubmed.ncbi.nlm.nih.gov/19245929/) | 2009 | Narrative Review | Semin Hematol | Reviews therapeutic strategies for infection-associated ITP; Eltrombopag discussed as an emerging option for refractory HIV-associated thrombocytopenia |
| [22992580](https://pubmed.ncbi.nlm.nih.gov/22992580/) | 2012 | Case Report | AIDS | Successful eltrombopag use in refractory HIV-related immune reconstitution thrombocytopenia without splenectomy; sustained platelet response achieved |
| [25333665](https://pubmed.ncbi.nlm.nih.gov/25333665/) | 2014 | Case Report | AIDS | First reported eltrombopag treatment for severe aplastic anaemia associated with HIV; trilineage haematological response with immunomodulatory effects (decreased Th1/Th17, increased T-regulatory cell ratio) |
| [24816314](https://pubmed.ncbi.nlm.nih.gov/24816314/) | 2014 | Narrative Review | Intern Med J | Discusses TPO-RA use in ITP of less than 6 months duration across a spectrum of secondary ITP aetiologies including infectious causes |
| [32977702](https://pubmed.ncbi.nlm.nih.gov/32977702/) | 2020 | In Vitro Screen | Viruses | Eltrombopag identified as a potential HIV-1 proviral transcription modulator in an FDA-approved drug library screen; exploratory finding only, no clinical validation to date |
| [28043314](https://pubmed.ncbi.nlm.nih.gov/28043314/) | 2016 | Case Report | J Coll Physicians Surg Pak | HBV-associated peripheral thrombocytopenia and megaloblastic anaemia; contextualises the spectrum of viral infection-induced haematological complications mechanistically relevant to this indication |
| [24128106](https://pubmed.ncbi.nlm.nih.gov/24128106/) | 2013 | Case Report | Farm Hosp | Two cases of eltrombopag in HCV-associated thrombocytopenia; provides bridging evidence from HCV to HIV thrombocytopenic context |

---

## Australia Market Information

Eltrombopag is **not currently listed on the Australian Register of Therapeutic Goods (ARTG)**. No ARTG entries were identified for this medicine (data as at 4 April 2026).

Eltrombopag is approved and marketed in several comparable international jurisdictions (e.g., United States as Promacta®, European Union and United Kingdom as Revolade®) for chronic ITP, thrombocytopenia in chronic hepatitis C, and severe aplastic anaemia. Australian prescribers wishing to access this medicine would need to apply through the TGA Special Access Scheme (SAS) or Authorised Prescriber (AP) pathway.

---

## Safety Considerations

Complete TGA-specific safety documentation (approved warnings and contraindications) is not available in this evidence pack.

Please refer to the TGA-approved Product Information (PI) for safety information. In the absence of a current ARTG listing, the international Revolade®/Promacta® Product Information should be reviewed as the primary reference.

**For prescriber awareness**, the following safety signals are widely documented in international regulatory submissions:
- **Hepatotoxicity**: Serious hepatic adverse events, including cases of hepatic failure, have been reported; liver function tests should be monitored before, during, and following treatment
- **Thromboembolic events**: Platelet count elevation above normal range increases the risk of thromboembolic complications; particular caution is warranted in immunocompromised patients (e.g., advanced AIDS with CD4 count <200/μL) where platelet-mediated thrombosis risk may be compounded
- **Bone marrow reticulin deposition**: Prolonged use may increase reticulin formation; bone marrow examination should be considered in the appropriate clinical context

*These points are provided for general awareness only and are not a substitute for formal product information review.*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The biological rationale is sound — HIV-associated thrombocytopenia shares the same underlying immune dysregulation and bone marrow suppression pathophysiology as ITP and aplastic anaemia, which are Eltrombopag's internationally approved indications. Supporting case series and case reports confirm clinical benefit in HIV-positive patients, and large-scale Phase 3 RCT data from HCV-related thrombocytopenia provide indirect controlled-trial support for the broader concept of infection-induced immune thrombocytopenia treatment. However, the absence of a dedicated randomised controlled trial in an HIV population, the lack of TGA registration in Australia, and critical gaps in safety documentation prevent a full "Go" decision at this stage.

**To proceed, the following is needed:**
- Retrieve and review the full international Revolade®/Promacta® Product Information to extract complete warnings, contraindications, and monitoring requirements relevant to the Australian clinical context
- Obtain detailed mechanism of action documentation from DrugBank API (DG002 data gap) to strengthen the mechanistic justification narrative
- Conduct a systematic literature search specifically targeting Phase 2/3 randomised controlled trials in HIV-associated thrombocytopenia populations
- Develop a haematological monitoring protocol (full blood count with differential, liver function tests, platelet count target thresholds) tailored to HIV/AIDS patients, accounting for elevated thromboembolic risk at low CD4 counts
- Engage the TGA regarding eligibility for the Special Access Scheme Category B (SAS-B) or Authorised Prescriber pathway given the absence of an ARTG listing
- Consult with infectious disease and haematology specialists to assess patient selection criteria and determine appropriate monitoring intervals in the Australian HIV-treating context

---

> **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All website content and research outputs should be read in conjunction with appropriate YMYL disclaimers.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

