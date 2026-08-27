---
layout: default
title: Etanercept
parent: 僅模型預測 (L5)
nav_order: 252
evidence_level: L5
indication_count: 10
---

# Etanercept
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

# Etanercept: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Etanercept is a TNF-α receptor fusion protein originally developed for the treatment of rheumatoid arthritis (RA) and later extended to other TNF-α-driven inflammatory conditions. TxGNN's top-ranked prediction for this drug is **Rheumatoid Vasculitis**, but the underlying evidence base is contradictory: the only controlled trial in a related vasculitis (ANCA-associated vasculitis) was negative and flagged an increased malignancy signal, while the majority of the supporting literature actually documents etanercept **inducing or worsening** vasculitis rather than treating it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid Arthritis (per literature; TGA/ARTG-specific labelling data not available — see below) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.71% (rank 4064) |
| Evidence Level | L3 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

*Note: Etanercept is not currently marketed in Australia (0 ARTG entries), so the "original indication" above is drawn from the supporting literature in this evidence pack (e.g. PMID 24980068) rather than an Australian product label.*

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for etanercept is not available in this evidence pack (Data Gap: MOA). Based on generally known pharmacology, etanercept is a soluble p75 TNF receptor–Fc fusion protein that binds and neutralises TNF-α, a cytokine central to synovial and vascular inflammation in rheumatoid disease. On this basis, TxGNN's hypothesis is mechanistically plausible: TNF-α is implicated in the endothelial inflammatory pathway of rheumatoid vasculitis (RV), a severe extra-articular manifestation of RA, so a TNF blocker could theoretically be beneficial.

However, the clinical evidence gathered for this candidate points the other way. The only Phase 1/2 RCT in a mechanistically related vasculitis — the WGET trial (NCT00001901) in Wegener's granulomatosis/ANCA-associated vasculitis — showed **no added efficacy from etanercept and an increased risk of solid-organ malignancy**. In parallel, a large body of case reports and case series in this pack describe etanercept as a **cause** of cutaneous vasculitis, accelerated nodulosis, and lupus-like vasculitis in RA patients, rather than a treatment for it. This is a well-recognised paradoxical class effect of TNF inhibitors.

In short, the mechanistic rationale is reasonable in theory, but the actual evidence base for using etanercept to *treat* rheumatoid vasculitis is weak, and the safety signal points toward the opposite effect.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00001901](https://clinicaltrials.gov/study/NCT00001901) | Phase 2 | Completed | 60 | WGET trial — etanercept in Wegener's granulomatosis (ANCA-associated vasculitis); **negative for added efficacy, and associated with increased solid-tumour risk**. Most directly relevant trial, but result is a warning signal, not supportive evidence. |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Observational study of RA patients — evaluates tocilizumab (Actemra), **not etanercept**; only indirectly relevant via shared RA population. |
| [NCT01557322](https://clinicaltrials.gov/study/NCT01557322) | N/A | Completed | 1754 | Real-world RA treatment-pathway study comparing etanercept vs non-biologic therapy; not designed around vasculitis endpoints. |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Cross-sectional study of biological DMARD treatment patterns in RA (China); background epidemiology only. |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Registry study of incident immune-mediated inflammatory disease risk in biologic-treated patients; relevance not yet assessed. |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty; not vasculitis-specific. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | Systematic review of biological therapy in rheumatoid vasculitis; most directly on-topic evidence source. |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Review | Nephrol Dial Transplant | Reviews the rationale and evidence for TNF-α blockade in ANCA-associated vasculitis and glomerulonephritis. |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort (BSRBR-RA registry) | RMD Open | Compares risk of lupus-like and vasculitis-like events in TNFi-treated vs non-biologic-treated RA patients — a drug-specific safety signal study. |
| [15468348](https://pubmed.ncbi.nlm.nih.gov/15468348/) | 2004 | Commentary/Review | Journal of Rheumatology | Discusses TNF-α blockade and the risk of vasculitis as an adverse effect. |
| [25544845](https://pubmed.ncbi.nlm.nih.gov/25544845/) | 2014 | Case Report | Case Reports in Medicine | Large-vessel vasculitis occurring in an RA patient under anti-TNF therapy. |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | Case Report | Arthritis and Rheumatism | Accelerated nodulosis and vasculitis following etanercept therapy for RA (drug-induced). |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | Case Series | Scandinavian Journal of Immunology | Immunology of cutaneous vasculitis associated with etanercept and infliximab. |
| [11792895](https://pubmed.ncbi.nlm.nih.gov/11792895/) | 2002 | Case Report | Rheumatology (Oxford) | Etanercept and infliximab associated with cutaneous vasculitis. |
| [15801034](https://pubmed.ncbi.nlm.nih.gov/15801034/) | 2005 | Case Report | Journal of Rheumatology | Proliferative lupus nephritis and leukocytoclastic vasculitis during etanercept treatment. |
| [19648728](https://pubmed.ncbi.nlm.nih.gov/19648728/) | 2009 | Case Report | Dermatology | Disseminated herpes zoster mimicking rheumatoid vasculitis in an etanercept-treated patient — an important diagnostic pitfall. |

---

## Australia Market Information

Etanercept has **0 ARTG entries** and is currently **not marketed** in Australia according to this evidence pack. No product-level dosage form or approved-indication data is available for the Australian market.

---

## Safety Considerations

No structured safety data (key warnings, contraindications, or drug interactions) was returned from the primary safety query for this drug (DDI query: not found).

However, the clinical evidence gathered for this specific indication contains a directly relevant safety signal worth flagging to prescribers: multiple case reports and one registry cohort study (PMID 28123776) describe etanercept **inducing or accelerating vasculitis, nodulosis, and lupus-like reactions** in RA patients, and the only related controlled trial (WGET, NCT00001901) found an **increased risk of solid-organ malignancy** with etanercept. This paradoxical autoimmune reaction is a recognised class effect of TNF inhibitors and should be treated as a safety consideration specific to this repurposing candidate.

Please refer to the TGA-approved Product Information (PI), once available, for the complete and authoritative safety profile.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for TNF blockade in rheumatoid vasculitis is theoretically sound, but the actual evidence base argues against efficacy and raises a distinct safety concern — the only related controlled trial was negative with an increased malignancy signal, and most of the literature describes etanercept as a cause of vasculitis rather than a treatment. Combined with the drug's current non-marketed status in Australia, this candidate does not support progression at this time.

**To proceed, the following is needed:**
- TGA-approved Product Information / warnings and contraindications (currently a blocking data gap)
- Confirmed mechanism-of-action data from DrugBank
- A dedicated, prospective study of etanercept specifically in rheumatoid vasculitis (rather than inference from RA or ANCA-vasculitis trials)
- Clarification of how "rheumatoid vasculitis" is defined as a TxGNN knowledge-graph node, to rule out conflation with drug-induced vasculitis reporting

---

**Note for reviewers:** This evidence pack contains several other TxGNN-predicted indications for etanercept with materially stronger evidence than rheumatoid vasculitis — notably **inflammatory spondylopathy** and **polyarticular juvenile rheumatoid arthritis** (both scored Evidence Level L1, decision stage S3, "Proceed with Guardrails"), which align with etanercept's internationally approved indications (ankylosing spondylitis, JIA). If the goal is to identify the most defensible repurposing opportunity for etanercept in this pack, those candidates warrant a separate, dedicated report rather than rank-1 by TxGNN score alone.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

