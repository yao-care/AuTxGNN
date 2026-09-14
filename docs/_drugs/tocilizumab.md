---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 682
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab: From Rheumatoid Arthritis to Ankylosing Spondylitis

## One-Sentence Summary

Tocilizumab is a humanised anti-IL-6 receptor monoclonal antibody whose established use is Rheumatoid Arthritis (and juvenile idiopathic arthritis).
The TxGNN model predicts it may be effective for **Ankylosing Spondylitis**, with **8 clinical trials** and **20 publications** currently identified —
however, the two dedicated Phase 2/3 trials in this indication were both **terminated for lack of efficacy**, making this a case where a high prediction score is contradicted by direct clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid Arthritis (per literature/trial context in evidence pack; not formally captured in regulatory fields) |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on known information, Tocilizumab is an IL-6 receptor antagonist, and its efficacy in Rheumatoid Arthritis (and juvenile idiopathic arthritis) is well established, as reflected in multiple trials and reviews in the evidence base (e.g. PMID 28841363).

Rheumatoid Arthritis and Ankylosing Spondylitis are both chronic inflammatory arthritides, which is likely why the TxGNN knowledge-graph model flagged a strong similarity. However, IL-6's pathogenic role in AS is considered less central than TNF-α or IL-17A, and this mechanistic uncertainty is borne out clinically: two purpose-built Phase 2/3 randomised, placebo-controlled trials (NCT01209689 and NCT01209702) were terminated because tocilizumab did not meet its efficacy endpoints in AS patients — including those with inadequate response to prior TNF antagonists and those who were TNF-antagonist naïve.

This is therefore a case where the mechanistic hypothesis is plausible but has already been **directly tested and refuted** in dedicated RCTs, rather than a scenario of "insufficient evidence." The high TxGNN score should be interpreted with this context in mind.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | Terminated | 113 | RCT of tocilizumab (8mg/kg or 4mg/kg IV) vs placebo in AS patients with inadequate response to prior TNF antagonist therapy — terminated |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 (seamless) | Terminated | 306 | RCT of tocilizumab vs placebo in TNF-naïve AS patients who failed NSAIDs; assessed signs/symptoms and structural damage — terminated |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Completed | 60 | Mechanistic study of tocilizumab's effect on T follicular helper cells in RA patients; not an AS efficacy endpoint |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Recruiting | 10,000 | Korean nationwide registry monitoring safety of biologics/targeted DMARDs in RA, AS and PsA |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | Recruiting | 2,500 | Multi-centre biomarker/cytokine profiling study across systemic inflammatory diseases |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Population study of risk of developing a second immune-mediated inflammatory disease |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Completed | 1,431 | Real-world observational registry for infliximab (Inflectra), not tocilizumab-specific |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients undergoing shoulder arthroplasty |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT (BUILDER-1/2) | Annals of the Rheumatic Diseases | Randomised, placebo-controlled trials assessing short-term symptomatic efficacy of tocilizumab in AS |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Systematic Review/Network Meta-analysis | Medicine | Comparative effectiveness of biologic regimens (including IL-6 blockade) for AS |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Meta-analysis | Clinical Rheumatology | Risk of serious infections with biologics in AS and non-radiographic axial spondyloarthritis |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Review | Seminars in Arthritis and Rheumatism | Second-line biologic therapy optimisation strategies in RA, PsA and AS |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflammation & Allergy Drug Targets | Short review of IL-6 antagonism as a therapeutic strategy in AS |
| [27789989](https://pubmed.ncbi.nlm.nih.gov/27789989/) | 2009 | Review | Open Access Rheumatology | Comprehensive review of biologics (incl. IL-6 blockers) in RA, AS and PsA |
| [19822066](https://pubmed.ncbi.nlm.nih.gov/19822066/) | 2009 | Review | Clinical and Experimental Rheumatology | Biologics in RA and AS treatment, noting pathogenic differences between the two diseases |
| [20959960](https://pubmed.ncbi.nlm.nih.gov/20959960/) | 2011 | Review | Osteoporosis International | Systemic bone effects of biologic therapies in RA and AS |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Case reports + literature review | Frontiers in Medicine | Successful treatment of AA amyloidosis secondary to AS using tocilizumab (2 cases) |
| [20851032](https://pubmed.ncbi.nlm.nih.gov/20851032/) | 2010 | Case report | Joint Bone Spine | Tocilizumab used in a patient with AS and Crohn's disease refractory to TNF antagonists |

## Australia Market Information

Tocilizumab is currently **not marketed** in Australia under this evidence pack (0 ARTG entries recorded). No product-level ARTG data is available for review.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score is very high (99.99%) and the mechanism is biologically plausible, the two dedicated Phase 2/3 RCTs conducted specifically in AS (NCT01209689, NCT01209702) were terminated for failure to meet efficacy endpoints. This constitutes direct negative clinical evidence rather than a simple evidence gap, and outweighs the model's prediction score.

**To proceed, the following is needed:**
- Detailed mechanism of action (MOA) data confirming IL-6 pathway relevance to axial disease activity
- TGA-approved Product Information for full warnings, contraindications and interaction data (currently unavailable)
- Re-evaluation of whether biomarker-defined AS subgroups (e.g. elevated IL-6/CRP) were more responsive in the terminated trials, to determine if a narrower patient population could still be considered
- Confirmation that no newer trials have reopened this indication since the 2011 terminations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

