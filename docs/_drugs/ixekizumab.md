---
layout: default
title: Ixekizumab
parent: 僅模型預測 (L5)
nav_order: 374
evidence_level: L5
indication_count: 10
---

# Ixekizumab
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

# Ixekizumab: From Inflammatory Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Ixekizumab (Taltz®) is a high-affinity monoclonal antibody that selectively targets interleukin-17A (IL-17A), approved globally for psoriatic arthritis, axial spondyloarthritis, and plaque psoriasis — though not currently registered in Australia.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis** (Rank 1, TxGNN score 97.53%), with only **1 indirectly related clinical trial** and **no published literature** directly supporting this specific indication.
Notably, the model separately identifies **Inflammatory Spondylopathy** (Rank 6) as the highest-evidence prediction at L1, backed by 26 clinical trials and 20 publications including multiple completed Phase 3 RCTs.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Psoriatic arthritis; axial spondyloarthritis; plaque psoriasis (global approvals — not registered in Australia) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 97.53% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Ixekizumab in this Evidence Pack. Based on known information, Ixekizumab is a humanised IgG4κ monoclonal antibody that selectively binds and neutralises IL-17A — a key pro-inflammatory cytokine central to the immunopathogenesis of spondyloarthritis, psoriasis, and psoriatic arthritis. By blocking IL-17A signalling, Ixekizumab reduces neutrophil recruitment, keratinocyte hyperactivation, and entheseal/joint inflammation across the spondyloarthritis spectrum.

Rheumatoid vasculitis (RV) is a rare but serious extra-articular complication of longstanding, high-titre seropositive rheumatoid arthritis (RA), characterised by immune complex–mediated inflammation of small-to-medium blood vessel walls. This can manifest as digital ischaemic ulcers, mononeuritis multiplex, and systemic vasculitis with significant morbidity. IL-17A has been detected in the synovial and perivascular microenvironment of RA, providing a theoretical basis for IL-17A blockade to attenuate vascular wall inflammation — which is where the TxGNN model's prediction derives its mechanistic plausibility.

However, this theoretical link does not currently translate to clinical evidence. RV is pathophysiologically distinct from spondyloarthritis, and standard-of-care remains high-dose glucocorticoids combined with cyclophosphamide or rituximab. The high TxGNN prediction score (97.53%) most likely reflects the proximity of RA and spondyloarthritis nodes within the knowledge graph — where Ixekizumab is heavily represented — rather than a direct biological connection to RV. This prediction should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Perioperative immunosuppressant management in rheumatology patients (including those on Ixekizumab) undergoing elective total shoulder arthroplasty — assesses flare incidence and functional outcomes around surgery, not RV treatment efficacy |

> **Note**: This trial has Grade C relevance only. It concerns the management of immunosuppressants perioperatively and does not evaluate Ixekizumab's therapeutic effect in rheumatoid vasculitis.

---

## Literature Evidence

Currently no related literature available for Ixekizumab in rheumatoid vasculitis.

---

## Australia Market Information

Ixekizumab is not currently registered on the Australian Register of Therapeutic Goods (ARTG). No ARTG product entries are available.

> Australian healthcare professionals wishing to access Ixekizumab may consider the TGA's Special Access Scheme (SAS Category B) or Authorised Prescriber pathway. Globally, Ixekizumab (Taltz®, Eli Lilly) holds approvals from the FDA (USA), EMA (Europe), and other regulatory bodies for psoriatic arthritis, radiographic and non-radiographic axial spondyloarthritis, and moderate-to-severe plaque psoriasis. Any future Australian indication would require a full TGA submission.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. As Ixekizumab is not currently registered in Australia, Australian healthcare professionals should consult the Eli Lilly global Product Information for Taltz® and TGA guidance on the use of biological DMARDs for relevant safety data, including considerations around infection risk, inflammatory bowel disease exacerbation, and injection-site reactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or peer-reviewed publications directly evaluate Ixekizumab in rheumatoid vasculitis. The L5 TxGNN prediction reflects knowledge graph topology rather than validated clinical benefit, and there is no preclinical or mechanistic evidence to justify clinical investigation at this stage. Established therapies for RV (rituximab, cyclophosphamide) remain the standard of care.

**To proceed with rheumatoid vasculitis as a repurposing target, the following is needed:**
- Preclinical studies establishing IL-17A's causal role in rheumatoid vasculitis pathogenesis (e.g., biopsy-based IL-17A quantification in RV lesions)
- Phase 1/2 exploratory trial in RV patients refractory to standard therapies
- Biomarker strategy to identify an IL-17A–high RV subgroup most likely to respond
- Full MOA documentation from DrugBank query (currently a data gap)
- TGA registration for established indications (PsA, axSpA) as a foundational prerequisite for any future Australian clinical development programme

---

> **Broader context for Australian prescribers**: While Rheumatoid Vasculitis (Rank 1) currently lacks supporting clinical evidence, the TxGNN model's most actionable predictions are:
>
> | Rank | Indication | TxGNN Score | Evidence Level | Decision |
> |------|------------|-------------|---------------|----------|
> | 6 | Inflammatory Spondylopathy | 97.67% | **L1** | Proceed with Guardrails |
> | 9 | Vertebral Disease | 95.13% | **L1** | Proceed with Guardrails |
>
> Both are supported by completed Phase 3 RCTs (COAST-V, COAST-W, COAST-X, SPIRIT-P1/P2) and represent clinically established indications for Ixekizumab in other jurisdictions. These should be the focus of any TGA registration strategy.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

