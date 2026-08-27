---
layout: default
title: Golimumab
parent: 僅模型預測 (L5)
nav_order: 318
evidence_level: L5
indication_count: 10
---

# Golimumab
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

# Golimumab: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Golimumab is a fully human anti-TNF-α monoclonal antibody internationally approved for rheumatoid arthritis, psoriatic arthritis, and ankylosing spondylitis. The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis** (score 99.73%), but the supporting evidence is weak and partly **contradictory** — none of the 3 clinical trials study vasculitis specifically, and one of the 6 literature reports documents anti-TNF therapy *inducing* vasculitis (Takayasu's arteritis) rather than treating it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (internationally approved; no formal registry record in this evidence pack — see Data Gap DG002) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as Data Gap DG002). Based on known information, golimumab is a fully human IgG1κ monoclonal antibody that neutralises tumour necrosis factor-alpha (TNF-α), and its efficacy in TNF-α–driven inflammatory arthritis (rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis) is well established internationally.

Rheumatoid vasculitis is a severe extra-articular manifestation of rheumatoid arthritis, and TNF-α is implicated in its pathogenesis, which is the surface-level rationale for this prediction — golimumab already treats the parent disease (RA), so treating a complication of RA is mechanistically plausible.

However, this evidence pack itself surfaces an important counter-signal: anti-TNF therapy has also been reported to **induce** vasculitis as a paradoxical adverse effect (see PMID 22999907, Takayasu's arteritis occurring under anti-TNF therapy). None of the retrieved clinical trials study golimumab specifically in rheumatoid vasculitis. This should be treated as a safety signal requiring clarification, not confirmed treatment evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A (observational) | Completed | 184 | Non-interventional RA study — **note: evaluates tocilizumab (Actemra), not golimumab**; general RA population, not vasculitis-specific |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Registry study on risk of a second immune-mediated inflammatory disease (IMID) developing in patients with an existing IMID; not a golimumab efficacy trial |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty; unrelated to vasculitis treatment |

**None of the identified trials directly study golimumab in rheumatoid vasculitis.**

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23557513](https://pubmed.ncbi.nlm.nih.gov/23557513/) | 2013 | Review | BMC Medicine | General review of biologic therapy (incl. anti-TNF agents) for autoimmune rheumatic diseases |
| [31491879](https://pubmed.ncbi.nlm.nih.gov/31491879/) | 2019 | Network Meta-Analysis | Int J Mol Sci | 36 RCTs comparing 5 TNF inhibitors (incl. golimumab) for reducing joint destruction in RA vs methotrexate; no vasculitis endpoint |
| [27591827](https://pubmed.ncbi.nlm.nih.gov/27591827/) | 2017 | Observational | Semin Arthritis Rheum | Frequency and causes of end-stage renal disease in RA patients; not vasculitis- or golimumab-specific |
| [22999907](https://pubmed.ncbi.nlm.nih.gov/22999907/) | 2013 | Case Report | Joint Bone Spine | **Two cases of Takayasu's arteritis (large-vessel vasculitis) occurring during anti-TNF therapy** — a paradoxical adverse effect, opposite to the treatment hypothesis |
| [23252659](https://pubmed.ncbi.nlm.nih.gov/23252659/) | 2013 | Case Report | Ocul Immunol Inflamm | Golimumab used successfully for Behçet disease-associated uveitis (a different vasculitic/inflammatory eye condition, not rheumatoid vasculitis) |
| [29075910](https://pubmed.ncbi.nlm.nih.gov/29075910/) | 2018 | Case Report | Rheumatol Int | Pyoderma gangrenosum and septic arthritis in an RA patient on golimumab; discusses rheumatoid vasculitis as a background disease feature, not as a treatment outcome |

---

## Australia Market Information

No product currently registered (0 entries; market status: Not marketed).

---

## Safety Considerations

No structured warnings, contraindications, or drug-interaction data were retrieved for this candidate (TFDA/PI extraction pending — see Data Gap DG001, classified as Blocking). Please refer to the TGA-approved Product Information (PI) for safety information.

**Literature-derived signal worth noting:** one case report in this evidence pack (PMID 22999907) describes anti-TNF therapy inducing large-vessel vasculitis (Takayasu's arteritis) as a paradoxical adverse effect. This should be treated as a safety consideration for any vasculitis-related use, pending formal PI review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L4 with no trials specific to rheumatoid vasculitis, and one retrieved case report describes anti-TNF therapy inducing vasculitis rather than treating it — a direction that conflicts with the repurposing hypothesis. Combined with the Blocking-severity gap in TFDA safety data, this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- TFDA/PI-equivalent warnings and contraindications (Data Gap DG001, Blocking)
- Confirmed mechanism of action data from DrugBank (Data Gap DG002)
- A dedicated safety review clarifying whether anti-TNF-associated vasculitis is a class-wide paradoxical risk for golimumab specifically
- Consider whether other candidates in this evidence pack with stronger, non-contradictory support — e.g. inflammatory spondylopathy (L1, Proceed with Guardrails) and polyarticular juvenile RA (L1, Proceed with Guardrails), both aligned with golimumab's approved anti-TNF mechanism — represent better-prioritised repurposing targets than rheumatoid vasculitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

