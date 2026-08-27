---
layout: default
title: Ondansetron
parent: 僅模型預測 (L5)
nav_order: 493
evidence_level: L5
indication_count: 10
---

# Ondansetron
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

# Ondansetron: From Chemotherapy-Induced Nausea and Vomiting to Tourette Syndrome

## One-Sentence Summary

Ondansetron is a selective 5-HT3 receptor antagonist originally developed as an antiemetic for chemotherapy- and anaesthesia-induced nausea and vomiting. The TxGNN model's highest-scoring prediction (nephrogenic syndrome of inappropriate antidiuresis) has no supporting evidence and is assessed as a likely false positive; the strongest evidence-backed candidate is **Tourette syndrome**, supported by **1 completed Phase 4 RCT** and **11 publications**, including two additional randomised controlled trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antiemetic — chemotherapy- and anaesthesia-induced nausea and vomiting (derived from literature evidence; not confirmed against a local product label) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 97.96% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed (no entries returned in the available regulatory dataset) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for ondansetron is not available in the structured drug record for this evaluation. Based on the literature evidence retrieved for this pack (e.g. PMID 11474424), ondansetron is a selective 5-HT3 (serotonin) receptor antagonist, originally used clinically as an antiemetic for cancer chemotherapy- and anaesthesia-related nausea and vomiting.

5-HT3 receptors are also expressed along striatal and mesolimbic dopaminergic pathways implicated in tic generation and in obsessive-compulsive symptoms that commonly co-occur with Tourette syndrome. This provides a biologically plausible bridge between the drug's established antiemetic mechanism and its potential effect on tic severity. Several independent research groups have tested this hypothesis over more than two decades (Toren et al. 1999 open-label pilot; Toren et al. 2005 placebo-controlled RCT; Stern et al. 2025 high-dose RCT with brain connectivity imaging), and a completed Phase 4 trial (NCT03239210, n=110) specifically evaluated ondansetron in patients with Tourette/tic disorders and OCD.

The mechanistic case is not fully settled, however: a genetic association study (PMID 16314763) found no association between HTR3A/HTR3B receptor gene variants and Tourette syndrome susceptibility, suggesting the clinical effect — if real — may not operate through direct receptor-gene-level causation. This is why the evidence level is rated L2 (supportive but not yet confirmatory) rather than higher.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03239210](https://clinicaltrials.gov/study/NCT03239210) | Phase 4 | Completed | 110 | Randomised, placebo-controlled trial of 4 weeks of ondansetron 24 mg/day vs placebo in OCD and tic disorder patients, assessing symptom change and brain function via MRI |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39876680](https://pubmed.ncbi.nlm.nih.gov/39876680/) | 2025 | RCT | American Journal of Psychiatry | High-dose ondansetron vs placebo tested for effects on sensory phenomena severity and interoceptive-sensorimotor brain connectivity in OCD/Tourette's disorder |
| [15816793](https://pubmed.ncbi.nlm.nih.gov/15816793/) | 2005 | RCT | Journal of Clinical Psychiatry | 3-week randomised, double-blind, placebo-controlled trial evaluating ondansetron efficacy in Tourette's disorder |
| [40489853](https://pubmed.ncbi.nlm.nih.gov/40489853/) | 2025 | Review | Medicine | Narrative review of Phase III/IV pharmacological trials for Tourette syndrome across age groups |
| [21183132](https://pubmed.ncbi.nlm.nih.gov/21183132/) | 2010 | Review | Seminars in Pediatric Neurology | Review of RCTs for pharmacotherapy of tics/Tourette syndrome and stereotypies in autism |
| [11474424](https://pubmed.ncbi.nlm.nih.gov/11474424/) | 2001 | Review | CNS Drug Reviews | Overview of ondansetron as a selective 5-HT3 antagonist, including applications in CNS-related disorders |
| [10565805](https://pubmed.ncbi.nlm.nih.gov/10565805/) | 1999 | Open-label/Case series | International Clinical Psychopharmacology | Open-label pilot study of ondansetron in 6 haloperidol-resistant Tourette's syndrome patients, showing symptom improvement |
| [16314763](https://pubmed.ncbi.nlm.nih.gov/16314763/) | 2005 | Genetic association study | Psychiatric Genetics | HTR3A/HTR3B gene sequencing found no association with Tourette syndrome, tempering the receptor-level mechanistic claim |
| [21568361](https://pubmed.ncbi.nlm.nih.gov/21568361/) | 2011 | Review | Drugs | Review of overlapping features and treatments across OCD, impulse control disorders, and addiction |
| [18184945](https://pubmed.ncbi.nlm.nih.gov/18184945/) | 2008 | Case report | Journal of Child Neurology | Case of a boy with leukaemia and Tourette syndrome whose tics improved on ondansetron given for chemotherapy-induced nausea |
| [16434179](https://pubmed.ncbi.nlm.nih.gov/16434179/) | 2006 | Case report | International Journal of Obstetric Anesthesia | Anaesthetic management case report for caesarean delivery in a patient with Tourette's syndrome (not a treatment study) |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

---

## Other Candidates Reviewed but Not Progressed

TxGNN generated nine further predictions for ondansetron (ranks 1, 3–10, scores 96.6–98.7%). Notably, the **highest-scoring** prediction — nephrogenic syndrome of inappropriate antidiuresis (98.65%) — has zero supporting clinical trials or literature and no known mechanistic link to 5-HT3 antagonism; it is assessed as a knowledge-graph embedding artefact rather than a genuine signal. The remaining candidates (trichotillomania, four personality disorders scoring identically, common cold, allergic urticaria, acute intermittent porphyria) similarly returned no clinical trial or relevant literature support and are held at evidence level L5. Tourette syndrome is the only candidate in this set with meaningful clinical and mechanistic support, which is why it is the focus of this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A completed Phase 4 RCT and two further published RCTs give a biologically plausible, moderately supported signal for ondansetron in Tourette syndrome (L2), but no confirmatory Phase 3 trial exists, genetic data have not confirmed a direct receptor-level mechanism, and safety/product information needed for an initial safety assessment is currently unavailable (a blocking data gap).

**To proceed, the following is needed:**
- TGA-approved Product Information (warnings, contraindications, drug interactions) — currently blocking safety review
- Confirmation of current ARTG registration status and marketed formulations for ondansetron in Australia
- A larger, confirmatory Phase 3 RCT in the Tourette syndrome population
- Drug interaction data, particularly for QT-prolongation risk with concomitant serotonergic or QT-prolonging agents, common with 5-HT3 antagonists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

