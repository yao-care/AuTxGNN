---
layout: default
title: Guanfacine
parent: 僅模型預測 (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
---

# Guanfacine
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

# Guanfacine: From ADHD to Tourette Syndrome

## One-Sentence Summary

Guanfacine is a selective alpha-2A adrenergic agonist, internationally approved for ADHD and hypertension (US FDA), though it is not currently registered in Australia.
The TxGNN model predicts it may be effective for **Tourette Syndrome** — the highest-evidence prediction among 10 candidate indications — supported by **2 directly relevant completed clinical trials** (including 1 Phase 3 RCT) and **over 20 publications**.
Notably, the 2022 European clinical guidelines have already formally incorporated guanfacine as a pharmacological treatment option for Tourette Syndrome, elevating this prediction from model-generated hypothesis to guideline-endorsed clinical practice.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ADHD and hypertension — based on internationally recognised regulatory approvals (US FDA); no TGA registration exists and original indication text is unavailable in this dataset |
| Predicted New Indication | Tourette Syndrome |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack. Based on internationally known information, guanfacine is a selective alpha-2A adrenergic receptor agonist. Its primary action is to strengthen inhibitory signalling in the dorsolateral prefrontal cortex (DLPFC) by binding alpha-2A receptors and closing cAMP-HCN channels, which enhances working memory, impulse control, and attention regulation. Compared with the non-selective alpha-2 agonist clonidine, guanfacine's subtype selectivity provides greater neuroanatomical precision and a more favourable side effect profile.

Tourette Syndrome arises from dysfunction in the cortico-striato-thalamo-cortical (CSTC) circuit, driven by hyperactivation of dopaminergic and noradrenergic signalling pathways. Guanfacine targets two complementary nodes in this circuit: (1) alpha-2A receptor activation in the prefrontal cortex and striatum strengthens top-down DLPFC inhibitory control over subcortical tic-generating circuits; and (2) suppression of norepinephrine (NE) release from the locus coeruleus reduces the sympathetic drive that amplifies tic expression. This mechanistic rationale is neuroanatomically precise, biologically plausible, and has been tested in controlled clinical settings.

The clinical bridge is further strengthened by the well-established ADHD–Tourette comorbidity: approximately 50–60% of individuals with Tourette Syndrome have concurrent ADHD, the very indication for which guanfacine has proven efficacy. The 2022 European Society for the Study of Tourette Syndrome (ESSTS) guidelines have formally incorporated guanfacine as a recommended pharmacological option, providing the highest level of clinical consensus support available for this repurposing direction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00004376](https://clinicaltrials.gov/study/NCT00004376) | Phase 3 | Completed | 35 | Randomised, double-blind, placebo-controlled trial directly evaluating guanfacine for Tourette Syndrome and ADHD in children and adolescents; primary basis for L1 evidence classification. The trial title explicitly names guanfacine for Tourette Syndrome, making this the anchor study for this indication. |
| [NCT01547000](https://clinicaltrials.gov/study/NCT01547000) | Phase 4 | Completed | 34 | Multi-site pilot study assessing tolerability and efficacy of extended-release guanfacine (Intuniv) in children with Tourette Disorder; provides confirmatory real-world safety and effectiveness data complementing the Phase 3 findings. |

> **Note:** A third trial (NCT01172288) appeared in the dataset for this indication but investigated N-acetylcysteine (NAC) as the active intervention — not guanfacine. It has been excluded from evidence calculations as a data-matching mismatch.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [34757514](https://pubmed.ncbi.nlm.nih.gov/34757514/) | 2022 | Guidelines | European Child & Adolescent Psychiatry | 2022 ESSTS European clinical guidelines for Tourette Syndrome — updated pharmacological treatment section; formally lists guanfacine as a recommended treatment option based on a systematic review of new evidence and expert consensus |
| [31061209](https://pubmed.ncbi.nlm.nih.gov/31061209/) | 2019 | Systematic Review | Neurology | Comprehensive systematic review of treatments for tics in Tourette Syndrome and chronic tic disorders; evaluates guanfacine's efficacy and risk profile alongside other pharmacological agents |
| [34286606](https://pubmed.ncbi.nlm.nih.gov/34286606/) | 2021 | Systematic Review | Journal of Psychopharmacology | Critical appraisal of evidence quality for pharmacological treatments in Tourette Syndrome in children and adults; specifically addresses alpha-2 agonist evidence base |
| [40489853](https://pubmed.ncbi.nlm.nih.gov/40489853/) | 2025 | Narrative Review | Medicine | Narrative review of Phase III and IV clinical trials for pharmacological treatment of Tourette Syndrome across all age groups; most recent synthesis available |
| [23473832](https://pubmed.ncbi.nlm.nih.gov/23473832/) | 2013 | Review | European Journal of Paediatric Neurology | Pharmacological management of comorbid Tourette Syndrome and ADHD; positions guanfacine as a preferred non-stimulant option for this high-prevalence comorbidity |
| [29335879](https://pubmed.ncbi.nlm.nih.gov/29335879/) | 2018 | Review | CNS Drugs | Current pharmacological approaches to Tourette Syndrome; places guanfacine within the modern treatment algorithm with discussion of dosing and monitoring |
| [28807495](https://pubmed.ncbi.nlm.nih.gov/28807495/) | 2018 | Review | Parkinsonism & Related Disorders | Comprehensive overview of medical, surgical, and behavioural therapies for Tourette Syndrome; alpha-2 agonists including guanfacine discussed as first-line options for milder presentations |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Review | Paediatric Drugs | Clinical characteristics and management strategies for Tourette Syndrome; guanfacine identified as a first-line alpha-2 agonist with advantages over clonidine for tic suppression |
| [37378108](https://pubmed.ncbi.nlm.nih.gov/37378108/) | 2023 | Case Series | Cureus | Three patients with Tourette Syndrome treated with guanfacine and aripiprazole combination (2011–2022); all experienced significant improvement in motor and vocal tics, supporting combination strategy in refractory cases |
| [7559307](https://pubmed.ncbi.nlm.nih.gov/7559307/) | 1995 | Clinical Study | Journal of the American Academy of Child and Adolescent Psychiatry | Early clinical experience report for guanfacine in comorbid ADHD and Tourette Syndrome; established the foundational rationale that guanfacine can address both tic and attentional symptoms simultaneously |

---

## Australia Market Information

Guanfacine is **not currently registered** on the Australian Register of Therapeutic Goods (ARTG). No TGA-approved products exist and no ARTG entries are available.

For Australian healthcare professionals considering access to guanfacine, the following regulatory pathways through the TGA are available:

- **Special Access Scheme (SAS) — Category B**: For individual patient access; requires clinical justification and TGA notification
- **Authorised Prescriber**: For practitioners regularly treating patients with Tourette Syndrome who require a longer-term access solution
- **Clinical Trial (CTN/CTA)**: If formally investigating guanfacine for Tourette Syndrome in an Australian research context

Prescribers should refer to the US FDA-approved Product Information for **Intuniv** (guanfacine extended-release, 1 mg/2 mg/3 mg/4 mg tablets) or **Tenex** (guanfacine immediate-release) as the primary prescribing reference until Australian documentation is available.

---

## Safety Considerations

Please refer to the US FDA Product Information (PI) for complete safety information, as no TGA-approved PI currently exists. The dataset did not contain TGA-sourced warning or contraindication data.

The following safety signals are drawn from clinical trial and literature summaries within this dataset and should be treated as preliminary — formal PI review is mandatory before prescribing:

- **Cardiovascular effects**: Bradycardia, hypotension, and syncope have been reported in paediatric patients treated with guanfacine for Tourette Syndrome (PMID [16229000](https://pubmed.ncbi.nlm.nih.gov/16229000/)). Heart rate and blood pressure monitoring is recommended at baseline, during dose titration, and periodically during maintenance.
- **Possible mania induction**: Case reports describe guanfacine-triggered manic reactions in children (PMID [10467976](https://pubmed.ncbi.nlm.nih.gov/10467976/), [9730081](https://pubmed.ncbi.nlm.nih.gov/9730081/), [27228067](https://pubmed.ncbi.nlm.nih.gov/27228067/)). Caution is warranted in patients with a personal or family history of bipolar disorder before initiating treatment.
- **Sedation**: Commonly reported in paediatric populations; dose-dependent and typically diminishes with continued use.
- **Overdose risk**: A case report documented significant autonomic dysfunction (sinus pause) following combined olanzapine and guanfacine overdose in a 17-year-old (PMID [31447925](https://pubmed.ncbi.nlm.nih.gov/31447925/)), highlighting the need for careful co-prescription oversight in young patients.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 randomised double-blind placebo-controlled trial (NCT00004376) directly evaluates guanfacine for Tourette Syndrome, supported by a Phase 4 multi-site confirmatory study (NCT01547000) and formal incorporation into the 2022 European clinical guidelines — constituting L1 evidence sufficient to support clinical consideration. The primary barrier to use in Australia is the absence of TGA registration, not a lack of clinical evidence.

**To proceed, the following is needed:**

- **TGA access pathway**: Submit an SAS Category B application or apply for Authorised Prescriber status; consult TGA guidance for Tourette Syndrome as a rare/specialist indication
- **Full PI review**: Obtain and review US FDA Product Information (Intuniv or Tenex) for complete contraindications, drug interactions, and special population dosing before prescribing
- **Baseline cardiovascular assessment**: Measure heart rate and blood pressure prior to initiation; establish monitoring protocol during dose titration
- **Bipolar risk screening**: Assess personal and family psychiatric history before initiating treatment, given case reports of guanfacine-induced mania in paediatric patients
- **MOA documentation**: Query DrugBank API (DB01018) to retrieve and document full mechanism of action data for institutional reporting and safety assessment purposes
- **Drug interaction review**: Formal DDI screening was not completed in this dataset; conduct a comprehensive interaction check, particularly for CNS depressants, antihypertensives, and CYP3A4 substrates
- **Paediatric-specific considerations**: Confirm age-appropriate dosing protocols from the Intuniv PI, as clinical trial populations in this dataset were predominantly children and adolescents (aged 6–17 years)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

