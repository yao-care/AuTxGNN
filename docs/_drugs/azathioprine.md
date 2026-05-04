---
layout: default
title: Azathioprine
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine: From Immunosuppressive Therapy to Inflammatory Bowel Disease

## One-Sentence Summary

Azathioprine is a well-established thiopurine immunosuppressant used globally for organ transplant rejection prevention and autoimmune disease management, though it currently holds no Australian Register of Therapeutic Goods (ARTG) registration.
The TxGNN model predicts it may be effective for **Inflammatory Bowel Disease (IBD)** — encompassing Crohn's disease and ulcerative colitis —
with **50 clinical trials** and **20 publications** supporting this direction, including multiple completed Phase 3 RCTs and Cochrane systematic reviews updated as recently as 2025.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Australia; globally used for organ transplant rejection prevention and autoimmune disease management |
| Predicted New Indication | Inflammatory Bowel Disease (Crohn's Disease and Ulcerative Colitis) |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on the published literature, azathioprine is a thiopurine prodrug that is metabolised in vivo to 6-thioguanine nucleotides (6-TGN). These active metabolites competitively inhibit HPRT-mediated purine biosynthesis, inducing apoptosis of activated T-lymphocytes and disrupting Rac1 GTPase signalling pathways. This multi-modal immunosuppressive mechanism has been further characterised and validated through TPMT and NUDT15 pharmacogenomic research, enabling precision dosing strategies to maximise efficacy while minimising haematological toxicity.

Inflammatory bowel disease is driven by aberrant Th1/Th17 immune responses against intestinal commensal flora, resulting in chronic mucosal inflammation of the gastrointestinal tract. Azathioprine's 6-TGN metabolites directly suppress this dysregulated mucosal immunity by targeting activated lymphocytes at the site of disease, providing a mechanistically coherent rationale for its use in IBD. Both Crohn's disease and ulcerative colitis share this immune-dysregulation pathophysiology, explaining why azathioprine shows efficacy across both conditions.

The clinical evidence supporting this prediction is exceptionally robust. Multiple Cochrane systematic reviews — most recently updated in 2025 — confirm azathioprine's superiority over placebo for maintenance of remission in ulcerative colitis, while Phase 3 RCTs demonstrate efficacy in preventing postoperative recurrence in Crohn's disease. The combination of azathioprine with anti-TNF biologics (infliximab, adalimumab) has become a cornerstone of moderate-to-severe IBD management internationally, underpinned by landmark comparative trial data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Phase 3 | Completed | 83 | Multicentre, double-blind RCT directly comparing Azathioprine vs Mesalazine for prevention of postoperative recurrence in Crohn's disease — highest direct relevance |
| [NCT01235689](https://clinicaltrials.gov/study/NCT01235689) | Phase 3 | Completed | 252 | Tight disease control vs conventional management using AZA-containing algorithms in moderate-to-severe CD; mucosal healing assessed at 48 weeks |
| [NCT00946946](https://clinicaltrials.gov/study/NCT00946946) | Phase 3 | Completed | 78 | Double-blind, double-dummy RCT: Azathioprine vs Mesalazine for prevention of clinical relapse in postoperative CD with moderate or severe endoscopic recurrence |
| [NCT00094458](https://clinicaltrials.gov/study/NCT00094458) | Phase 3 | Completed | 508 | Three-arm RCT: Infliximab monotherapy vs Infliximab + Azathioprine vs Azathioprine monotherapy in biologic- and immunomodulator-naive Crohn's disease patients |
| [NCT02852694](https://clinicaltrials.gov/study/NCT02852694) | Phase 4 | Completed | 192 | Risk-stratified RCT in paediatric CD: Methotrexate vs Azathioprine for maintenance of remission in low-risk patients; 1-year steroid-free remission as primary endpoint |
| [NCT03719118](https://clinicaltrials.gov/study/NCT03719118) | N/A | Completed | 215 | RCT evaluating genotype-guided (TPMT/NUDT15) vs standard thiopurine dosing in IBD to reduce myelosuppression incidence and optimise clinical outcomes |
| [NCT02929706](https://clinicaltrials.gov/study/NCT02929706) | N/A | Unknown | 400 | RCT exploring NUDT15 R139C-guided azathioprine dose optimisation to reduce thiopurine-induced leucopenia in IBD; implications for precision dosing |
| [NCT00537316](https://clinicaltrials.gov/study/NCT00537316) | Phase 3 | Terminated | 242 | Three-arm RCT: Infliximab monotherapy, IFX + AZA combination, vs AZA monotherapy in moderate-to-severe active UC; AZA was a primary comparator arm |
| [NCT07235904](https://clinicaltrials.gov/study/NCT07235904) | Phase 4 | Recruiting | 300 | MIRACLE trial: Top-down mirikizumab vs standard-of-care azathioprine in newly diagnosed moderate-to-severe UC (52-week, multicenter, open-label RCT) |
| [NCT05584228](https://clinicaltrials.gov/study/NCT05584228) | N/A | Not yet recruiting | 150 | SMART trial: Azathioprine + subcutaneous infliximab vs ileocecal resection for symptomatic small bowel Crohn's disease — directly compares medical therapy to surgery |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Cochrane Systematic Review | Cochrane Database Syst Rev | Most recent update confirming AZA/6-MP superiority over placebo for UC maintenance of remission; incorporates newer therapeutic comparisons |
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE trial: Top-down infliximab + AZA vs AZA alone following steroid-responsive acute severe UC — direct head-to-head evaluation of combination strategy |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Cochrane Systematic Review | Cochrane Database Syst Rev | Cochrane review confirming AZA/6-MP as effective maintenance therapy in UC; established evidence platform for subsequent updates |
| [22972046](https://pubmed.ncbi.nlm.nih.gov/22972046/) | 2012 | Cochrane Systematic Review | Cochrane Database Syst Rev | Earlier Cochrane review establishing AZA/6-MP evidence base for UC remission maintenance |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Meta-analysis | Aliment Pharmacol Ther | Meta-analysis confirming efficacy of AZA and mercaptopurine in UC, resolving prior uncertainty about efficacy differences between UC and CD |
| [22072847](https://pubmed.ncbi.nlm.nih.gov/22072847/) | 2011 | Systematic Review | World J Gastroenterol | Clinical optimisation guide for 6-MP and AZA in IBD; covers metabolite monitoring, TPMT genotyping, and precision dosing strategies |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Review | J Crohn's Colitis | State-of-the-art expert review of thiopurine treatment in IBD; pharmacogenomics, safety monitoring, and current clinical practice perspectives |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Review | Expert Rev Gastroenterol Hepatol | Molecular mechanisms of AZA in IBD; 45 years of clinical experience synthesised with trial data and meta-analyses |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Cohort Study | Cell Reports Medicine | Gut microbiome species Blautia wexlerae identified as a driver of AZA therapy failure in IBD via reduced 6-MP bioavailability; implications for personalised treatment |
| [34913108](https://pubmed.ncbi.nlm.nih.gov/34913108/) | 2021 | Systematic Review | Curr Gastroenterol Rep | Comprehensive safety review of immunomodulatory agents in IBD including AZA/6-MP, anti-TNF, JAK inhibitors, and biologics; practical prescribing guidance |

---

## Australia Market Information

Azathioprine currently has **no ARTG registration** in Australia, with zero product entries on record.

Clinicians seeking to use azathioprine in Australia should explore:
- **TGA Special Access Scheme (SAS)** — for individual patient access to unregistered therapeutic goods
- **Authorised Prescriber pathway** — for clinicians regularly treating patients who may benefit
- Product information from internationally approved formulations (TGA, EMA, or FDA-approved PI) for safety and dosing guidance

---

## Cytotoxicity

Azathioprine is a thiopurine purine analogue with recognised cytotoxic properties. Although primarily used as an immunosuppressant rather than a direct antineoplastic agent, it shares pharmacological characteristics with cytotoxic drugs and requires appropriate cytotoxic handling precautions in all clinical settings.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Immunosuppressant / Cytotoxic antimetabolite (Thiopurine class — purine analogue) |
| Myelosuppression Risk | High — dose-dependent leucopenia, thrombocytopenia, and anaemia; risk markedly amplified in patients with TPMT or NUDT15 deficiency |
| Emetogenicity Classification | Low |
| Monitoring Items | Full blood count (with differential) weekly for the first month, then fortnightly for 3 months, then monthly; liver function tests; renal function; TPMT and NUDT15 pharmacogenomic testing strongly recommended prior to initiation |
| Handling Protection | Must be handled in accordance with cytotoxic drug handling regulations; gloves and appropriate PPE required; tablets should not be crushed or split |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> **Note**: Azathioprine is currently not registered in Australia (0 ARTG entries). Safety data should be sourced from the manufacturer's product information or an equivalent internationally approved document. Key known safety concerns include myelosuppression, hepatotoxicity, increased susceptibility to opportunistic infections, and elevated long-term lymphoma risk (particularly with extended use). Pharmacogenomic testing for TPMT and NUDT15 variants is strongly recommended before initiating therapy to guide dose selection and minimise serious adverse events.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base supporting azathioprine for IBD maintenance therapy is among the most extensively validated in gastroenterology, anchored by multiple completed Phase 3 RCTs (including large-scale studies up to n=508), serial Cochrane systematic reviews updated through 2025, and over four decades of international clinical experience. The primary barrier to use in Australia is the complete absence of ARTG registration, which must be resolved before routine clinical deployment can proceed.

**To proceed, the following is needed:**
- Assessment of TGA regulatory pathways (Special Access Scheme, Authorised Prescriber, or full ARTG registration submission)
- Review of complete product information for Australian-specific safety warnings and contraindications
- Implementation of a pre-treatment TPMT and NUDT15 pharmacogenomic testing protocol
- Institutional cytotoxic drug handling compliance review
- A defined haematological and hepatic function monitoring schedule aligned with Australian standards
- Drug interaction assessment, with particular attention to allopurinol (which markedly amplifies AZA toxicity by inhibiting xanthine oxidase), warfarin, and other co-administered immunosuppressants

> **Disclaimer**: This report is intended for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation prior to therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

