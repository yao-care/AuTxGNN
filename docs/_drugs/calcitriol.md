---
layout: default
title: Calcitriol
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Calcitriol
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

# Calcitriol: From Vitamin D Deficiency States to Hereditary Hypophosphatemic Rickets

## One-Sentence Summary

Calcitriol (1,25-dihydroxyvitamin D₃) is the biologically active form of vitamin D, internationally recognised for treating hypocalcaemia, renal osteodystrophy, and hypoparathyroidism, though it is not currently registered with the TGA in Australia.
The TxGNN model predicts it may be effective for **Hereditary Hypophosphatemic Rickets** (principally X-Linked Hypophosphatemia, XLH),
with **7 clinical trials** (including 2 trials directly testing calcitriol in XLH) and **20 publications** currently supporting this direction.

> **Editorial note on TxGNN ranking:** The model's rank #1 prediction (score 99.96%) was *"obsolete vitamin D deficiency"* — a deprecated ontology term that yields no searchable clinical or trial evidence. This finding confirms calcitriol's established role in vitamin D pathways but does not constitute an actionable new repurposing target. This report therefore focuses on the highest-evidence actionable prediction: **Hereditary Hypophosphatemic Rickets** (rank #7, Evidence Level L2, score 99.28%).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | TGA registration data not available (calcitriol is not currently registered in Australia; internationally used for renal osteodystrophy, hypocalcaemia in CKD, and hypoparathyroidism) |
| Predicted New Indication | Hereditary Hypophosphatemic Rickets (X-Linked Hypophosphatemia, XLH) |
| TxGNN Prediction Score | 99.28% (Rank #7) |
| Evidence Level | L2 |
| Australia Market Status | Not registered with TGA |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the provided dataset. Based on established pharmacology, calcitriol (1,25-dihydroxyvitamin D₃) is the hormonally active form of vitamin D. It binds to the nuclear Vitamin D Receptor (VDR), which regulates gene expression controlling intestinal calcium and phosphate absorption, renal calcium reabsorption via the TRPV5/Calbindin-D pathway, and bone mineralisation through osteoblast differentiation. Calcitriol also suppresses parathyroid hormone (PTH) secretion via a negative feedback loop, making it a pivotal regulator of whole-body mineral homeostasis.

Hereditary Hypophosphatemic Rickets (predominantly X-Linked Hypophosphatemia, XLH — caused by *PHEX* gene mutations) is characterised by excessive FGF23 production, which simultaneously drives renal phosphate wasting and suppresses the renal 1α-hydroxylase enzyme responsible for synthesising calcitriol. The resulting dual deficit — insufficient phosphate and low calcitriol — causes defective bone mineralisation, leading to rickets in children and osteomalacia in adults. Calcitriol supplementation directly bypasses FGF23-mediated 1α-hydroxylase suppression, restoring active vitamin D signalling and promoting intestinal phosphate absorption and skeletal mineralisation.

The combination of calcitriol with oral phosphate supplementation has been the established standard of care for XLH for over four decades. Foundational evidence from the *Journal of Clinical Investigation* (PMID 3839245, 1985) demonstrated that high-dose calcitriol was specifically required to heal the osteomalacia component of XLH that phosphate supplementation alone could not resolve. Current guidelines (Lancet 2024; Calcified Tissue International 2025) continue to endorse calcitriol as a core treatment option, with the anti-FGF23 monoclonal antibody burosumab representing a newer alternative where accessible. It is worth noting that ranks #8 (hypophosphatemic rickets, L2), #9 (osteomalacia, L3), and #10 (vitamin D-dependent rickets, L3) in the TxGNN predictions further reinforce this mechanistic cluster, all pointing to calcitriol's established role across phosphate/calcium mineralisation disorders.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT03748966](https://clinicaltrials.gov/study/NCT03748966) | Early Phase 1 | Active, Not Recruiting | 20 | **Highest relevance — direct calcitriol evidence:** Calcitriol monotherapy in XLH adults and children, with dose escalation over 3 months. Assesses serum phosphate, skeletal mineralisation, and nephrocalcinosis. Only trial specifically testing calcitriol alone (without phosphate) in XLH. |
| [NCT03820518](https://clinicaltrials.gov/study/NCT03820518) | Phase 4 | Unknown | 100 | High vs low dose active vitamin D (calcitriol) combined with neutral phosphate in children with XLH. Largest calcitriol dosing study in this indication; outcome data requires status confirmation. |
| [NCT06046820](https://clinicaltrials.gov/study/NCT06046820) | Phase 3 | Active, Not Recruiting | 27 | ENERGY 3 Study: INZ-701 (not calcitriol) in children with ENPP1 Deficiency (a hypophosphatemic rickets subtype). Provides disease-level evidence context; demonstrates active therapeutic development in this field. |
| [NCT04846647](https://clinicaltrials.gov/study/NCT04846647) | N/A (Observational) | Completed | 260 | Observational study of inappropriate FGF23 secretion in hospitalised hypophosphataemic patients. Completed (n=260); provides biomarker data relevant to stratifying patients for calcitriol therapy. |
| [NCT01526304](https://clinicaltrials.gov/study/NCT01526304) | N/A (Observational) | Unknown | 150 | Cross-sectional study of FGF23/Klotho/Sclerostin in kidney stone formers. Relevant as safety background: highlights hypercalciuria risk associated with calcitriol use in phosphate-wasting conditions. |
| [NCT06921720](https://clinicaltrials.gov/study/NCT06921720) | N/A (Diagnostic) | Not Yet Recruiting | 65 | ATP measurement by phosphorus-31 spectroscopy in phosphate diabetes (XLH). Diagnostic/mechanistic study; recruitment not yet commenced (planned May 2025). |

> Note: NCT00844740 (cinacalcet study for familial hypophosphatemic rickets) excluded — withdrawn prior to enrolment (n=0) and tests a different drug.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [40295317](https://pubmed.ncbi.nlm.nih.gov/40295317/) | 2025 | Clinical guideline review | Calcified Tissue International | Current XLH diagnosis and therapy: calcitriol + phosphate endorsed as standard of care; discusses transitioning to burosumab where accessible |
| [39181153](https://pubmed.ncbi.nlm.nih.gov/39181153/) | 2024 | Disease overview | Lancet | Comprehensive XLH overview; FGF23 excess suppresses calcitriol synthesis — calcitriol replacement directly addresses this pathophysiological deficit |
| [3839245](https://pubmed.ncbi.nlm.nih.gov/3839245/) | 1985 | Clinical trial (uncontrolled) | Journal of Clinical Investigation | Foundational direct evidence: high-dose calcitriol healed osteomalacia in XLH where phosphate supplementation alone had failed; established calcitriol as essential component of XLH therapy |
| [6252463](https://pubmed.ncbi.nlm.nih.gov/6252463/) | 1980 | Clinical series | New England Journal of Medicine | 11 children with vitamin D-resistant rickets; calcitriol (0.25–1 μg/day) + phosphate increased intestinal phosphate absorption and improved bone healing |
| [2157942](https://pubmed.ncbi.nlm.nih.gov/2157942/) | 1990 | Clinical trial / case series | Metabolism | Calcitriol in VDDR type I (complete remission) and XLH (significant improvement); establishes calcitriol's differential therapeutic benefit across rickets subtypes |
| [29292875](https://pubmed.ncbi.nlm.nih.gov/29292875/) | 2017 | Multicentre cohort | Pediatric Endocrinology Reviews | 127 XLH patients from 49 centres; early calcitriol + phosphate therapy associated with improved growth parameters; provides real-world evidence across multiple sites |
| [30454743](https://pubmed.ncbi.nlm.nih.gov/30454743/) | 2019 | Review | Pediatric Clinics of North America | XLH management overview: calcitriol + phosphate as standard care; active monitoring required for nephrocalcinosis and secondary hyperparathyroidism |
| [36446330](https://pubmed.ncbi.nlm.nih.gov/36446330/) | 2022 | Review | Hormone Research in Paediatrics | History and current practice in rickets: vitamin D metabolites including calcitriol remain a cornerstone therapy across multiple rickets subtypes |
| [9316301](https://pubmed.ncbi.nlm.nih.gov/9316301/) | 1997 | Review | Acta Paediatrica Japonica | Combined phosphate + calcitriol in XLH: improves growth, bone deformity, and biochemical parameters; catalogues complications including nephrocalcinosis and hyperparathyroidism |
| [2492895](https://pubmed.ncbi.nlm.nih.gov/2492895/) | 1989 | Cohort study | Calcified Tissue International | 17 children with familial hypophosphataemia; calcitriol + phosphate supplementation improved axial and appendicular bone mineral density measured at 6-month intervals |

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. As calcitriol is not currently registered with the TGA in Australia (0 ARTG entries), no local PI is available. When relying on international published evidence, clinical literature consistently identifies the following key safety signals in the context of hereditary hypophosphatemic rickets:

- **Hypercalcaemia and hypercalciuria** are the primary dose-limiting adverse effects — regular serum and urinary calcium monitoring is essential
- **Nephrocalcinosis** is a recognised long-term complication in patients (particularly children) receiving sustained calcitriol therapy; periodic renal ultrasound monitoring is recommended in clinical guidelines
- **Secondary hyperparathyroidism** may develop with prolonged combined calcitriol + phosphate therapy and should be monitored via PTH levels

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Calcitriol combined with oral phosphate supplementation is the historically established and internationally endorsed standard of care for X-Linked Hypophosphatemia and related hereditary hypophosphatemic rickets, with foundational evidence dating to 1980 (NEJM) and current endorsement in 2024–2025 clinical guidelines. Two clinical trials directly test calcitriol in XLH (NCT03748966 Early Phase 1, NCT03820518 Phase 4), supporting an L2 evidence designation. The principal barrier to Australian clinical use is the absence of TGA registration (0 ARTG entries) and a formal safety evaluation under Australian regulatory requirements.

**To proceed, the following is needed:**
- Determine the appropriate regulatory pathway for calcitriol access in Australia — TGA registration, Special Access Scheme (SAS Category B), or Authorised Prescriber pathway
- Obtain an approved international Product Information (e.g. US FDA or EMA label) as an interim safety reference pending TGA registration
- Confirm the publication status of NCT03820518 (Phase 4, n=100, status unknown) — results from this dosing study would directly inform clinical practice
- Review current PBS listing status for burosumab (anti-FGF23) in Australia to contextualise calcitriol's role as a cost-effective alternative
- Engage with the Australian Rare Diseases Network and relevant paediatric endocrinology services to determine current local management practice for XLH
- Develop a monitoring protocol addressing hypercalcaemia, hypercalciuria, and nephrocalcinosis risk within the Australian clinical setting prior to initiating therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

