---
layout: default
title: Famciclovir
parent: Model Prediction Only (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Famciclovir: predicted new indication Post-infectious neuralgia (evidence level L5). Approved use: Herpes zoster"
---

# Famciclovir
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

# Famciclovir: From Herpes Zoster to Chickenpox

## One-Sentence Summary

Famciclovir is an oral antiviral originally used to treat herpes zoster (shingles).
The TxGNN model's top-ranked prediction is post-infectious neuralgia, but the best-supported candidate in the data compiled for this report is **chickenpox**, which is caused by the same virus (varicella zoster virus, VZV).
Chickenpox has **5 linked clinical trials** (2 completed Phase 3 studies of famciclovir) and **20 publications**, although none is a confirmatory chickenpox efficacy trial.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Herpes zoster (from the TxGNN knowledge graph; no approved indication text is listed for the ARTG entry) |
| Predicted New Indication | Post-infectious neuralgia (rank 1 prediction); chickenpox (rank 7) is the best-supported candidate and is evaluated in detail below |
| TxGNN Prediction Score | 99.75% (post-infectious neuralgia); 99.11% (chickenpox) |
| Evidence Level | L4 (post-infectious neuralgia); L1 as scored for chickenpox, though no trial confirms chickenpox efficacy (see below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold for post-infectious neuralgia; Proceed with Guardrails for chickenpox |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, famciclovir is a prodrug of penciclovir. After phosphorylation by viral thymidine kinase, penciclovir inhibits VZV DNA polymerase and reduces viral replication.

**Chickenpox (rank 7):** Chickenpox and herpes zoster are both caused by VZV, so the mechanism applies directly. This is closely related to the existing zoster use rather than a truly novel indication. The evidence is largely extrapolated from zoster and paediatric pharmacokinetic data.

**Post-infectious neuralgia (rank 1):** Postherpetic neuralgia is a sequela of zoster, so early antiviral therapy could plausibly reduce its incidence or severity. This is an indirect link. The only linked trial tests oxycodone, not famciclovir.

**Other predictions:** The remaining predictions have little or no mechanistic support:
- Sequela of COVID-19, hepatitis C-induced cirrhosis, anogenital HPV infection and the mesothelioma subtypes have no clear mechanistic link. Famciclovir acts on herpesvirus DNA polymerase, and HCV and HPV lack a comparable target.
- AIDS-related disorder has only indirect support, through treatment of herpesvirus coinfections.

---

## Clinical Trial Evidence

Trials linked to chickenpox (rank 7):

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00098046](https://clinicaltrials.gov/study/NCT00098046) | Phase 3 | Completed | 76 | Pharmacokinetics and safety of a famciclovir oral paediatric formulation in children aged 1-12 years with VZV infection |
| [NCT01327144](https://clinicaltrials.gov/study/NCT01327144) | Phase 3 | Completed | 177 | Famciclovir 500 mg vs aciclovir 400 mg in herpes zoster (direct VZV evidence, not chickenpox-specific) |
| [NCT07099157](https://clinicaltrials.gov/study/NCT07099157) | Phase 4 | Recruiting | 140 | Brivudine vs famciclovir in acute herpes zoster (comparator context) |
| [NCT03120962](https://clinicaltrials.gov/study/NCT03120962) | NA | Unknown | 140 | Early oxycodone in acute zoster to prevent postherpetic neuralgia (famciclovir not the intervention; also linked to post-infectious neuralgia) |
| [NCT06798662](https://clinicaltrials.gov/study/NCT06798662) | NA | Not yet recruiting | 120 | Nerve block and pulse radiofrequency for acute zoster pain (not an antiviral study) |

No registered trials were found for the other predicted indications.

---

## Literature Evidence

Publications linked to chickenpox (up to 10 shown, drawn mainly from reviews of VZV management):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42693145](https://pubmed.ncbi.nlm.nih.gov/42693145/) | 2026 | Review | Nat Rev Dis Primers | Overview of VZV infection, including chickenpox, zoster and complications |
| [33672709](https://pubmed.ncbi.nlm.nih.gov/33672709/) | 2021 | Review | Molecules | Advances in managing VZV infections |
| [29431387](https://pubmed.ncbi.nlm.nih.gov/29431387/) | 2017 | Review | Am Fam Physician | Prevention and management of herpes zoster and postherpetic neuralgia |
| [36851652](https://pubmed.ncbi.nlm.nih.gov/36851652/) | 2023 | Review | Viruses | HSV and VZV infections in cancer patients |
| [9675639](https://pubmed.ncbi.nlm.nih.gov/9675639/) | 1997 | Review | Intervirology | Famciclovir and valaciclovir are effective in acute zoster, including zoster-associated pain |
| [12182687](https://pubmed.ncbi.nlm.nih.gov/12182687/) | 2002 | Review | Drugs Aging | Famciclovir and valaciclovir offer less frequent dosing than aciclovir in elderly zoster patients |
| [11487454](https://pubmed.ncbi.nlm.nih.gov/11487454/) | 2001 | Review | Curr Treat Options Neurol | Famciclovir, valaciclovir and high-dose aciclovir are beneficial if started within 3 days of rash |
| [21486500](https://pubmed.ncbi.nlm.nih.gov/21486500/) | 2011 | Review | BMJ Clin Evid | Chickenpox overview |
| [8809466](https://pubmed.ncbi.nlm.nih.gov/8809466/) | 1996 | Review | Clin Microbiol Rev | VZV biology, varicella and zoster |
| [10375341](https://pubmed.ncbi.nlm.nih.gov/10375341/) | 1999 | Review | Ann Intern Med | Recent advances in VZV infection |

Literature for other predictions is limited:
- **AIDS-related disorder:** six reviews and observational reports. One cohort ([21837785](https://pubmed.ncbi.nlm.nih.gov/21837785/), 2011) found that valaciclovir, famciclovir or antiretrovirals reduced HHV-8 replication in HIV-positive men.
- **Anogenital HPV infection:** an STI guideline and a review that cover famciclovir for genital herpes, not HPV.
- **Hepatitis C cirrhosis:** a 2000 review with no direct famciclovir evidence.
- **Sequela of COVID-19:** only a nanocochleate gel formulation study.
- **Post-infectious neuralgia and the mesothelioma subtypes:** no literature.

---

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 2274Q | Famvir | Tablet 250 mg (oral) | Not listed in the data compiled for this report |

---

## Safety Considerations

- **Contraindications (knowledge graph, not label text):** kidney disease and pyoureter are flagged in the TxGNN knowledge graph. These should be checked against the Product Information.
- **Drug Interactions:** 84 potential interactions were identified, all with an unclassified severity level. Examples include calcitriol, doxycycline, metformin, morphine, omeprazole, pantoprazole, prednisone, simvastatin and vancomycin.

Warnings and label contraindications were not available. Please refer to the TGA-approved Product Information (PI) for full safety information, including renal dose adjustment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (chickenpox); Hold (post-infectious neuralgia and all other predictions)**

**Rationale:**
- Chickenpox shares its causative virus and mechanism with the approved zoster use. Two completed Phase 3 trials (a paediatric PK/safety study and a zoster efficacy comparison) support the direction. However, none is a confirmatory chickenpox efficacy trial, so the evidence is extrapolated, and the L1 score should be read with that caveat.
- Post-infectious neuralgia is plausible but untested, since the only linked trial does not involve famciclovir.
- The remaining predictions rest on computation alone or on indirect evidence and should not be pursued without further justification.

**To proceed, the following is needed:**
- Approved indication text and Product Information for ARTG 2274Q, including warnings and contraindications
- Mechanism of action data from DrugBank
- A chickenpox-specific efficacy study, or a regulatory review of extrapolation from zoster and paediatric PK data
- A trial of famciclovir for preventing postherpetic neuralgia, if that indication is pursued
- Paediatric dosing and formulation availability in Australia, as the current ARTG entry is a 250 mg tablet only
- Review of the 84 interaction entries, which have no severity classification, and of the renal impairment flags
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

