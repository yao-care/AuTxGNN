---
layout: default
title: Avanafil
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 10
---

# Avanafil
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

# Avanafil: From Erectile Dysfunction to Amenorrhea

## One-Sentence Summary

Avanafil is a selective PDE5 (phosphodiesterase type 5) inhibitor, internationally approved for the treatment of erectile dysfunction in adult males.
The TxGNN model predicts it may be effective for **Amenorrhea** (rank 1, score 94.59%), however there are currently **0 clinical trials** and **0 publications** directly supporting this repurposing direction.
Notably, within the full prediction set, **Raynaud disease** (rank 5) presents a substantially stronger mechanistic and class-effect rationale and is flagged as the more clinically actionable candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Erectile dysfunction (internationally approved; not registered in Australia) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 94.59% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Avanafil is a selective inhibitor of PDE5 — the same drug class as sildenafil, tadalafil, and vardenafil. Its core mechanism involves blocking PDE5-mediated degradation of cyclic GMP (cGMP), thereby elevating intracellular cGMP concentrations. This results in smooth muscle relaxation and vasodilation, primarily in vascular and cavernosal smooth muscle.

The theoretical link to amenorrhea rests on an indirect and speculative pathway. PDE5 inhibitors may enhance uterine endometrial perfusion via the NO/cGMP axis, and sildenafil has been explored off-label for thin endometrium to improve implantation outcomes. However, amenorrhea has highly heterogeneous aetiologies — including hypothalamic-pituitary-ovarian axis dysfunction, anatomical abnormalities (e.g., Asherman's syndrome), prolactinoma, premature ovarian insufficiency, and thyroid disorders — none of which are directly addressed by PDE5 inhibition. The mechanistic case for amenorrhea is therefore assessed as highly indirect and insufficient to support further development at this stage.

In contrast, **Raynaud disease** (rank 5, score 88.54%, evidence level L4) carries a direct and well-supported mechanistic rationale: episodic vasospasm is the core pathology, and cGMP-mediated smooth muscle relaxation via PDE5 inhibition directly counters it. Sildenafil has demonstrated efficacy in multiple RCTs (Cochrane Review 2012) and tadalafil has Phase 2 trial data in Raynaud's. Avanafil would be expected to share this class effect. Healthcare professionals reviewing this report should prioritise Raynaud disease as the most clinically credible repurposing opportunity within this prediction set.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Avanafil in amenorrhea.

---

## Literature Evidence

Currently no related literature available for Avanafil in amenorrhea.

---

## Australia Market Information

Avanafil is not currently registered on the Australian Register of Therapeutic Goods (ARTG). There are no ARTG entries for this drug. It is approved in the United States as **Stendra®** (Metuchen Pharmaceuticals) and in the European Union as **Spedra®** (Menarini) for the treatment of erectile dysfunction. Clinicians seeking prescribing information should consult the FDA-approved label or EMA Summary of Product Characteristics (SmPC) in the absence of a TGA-approved Product Information document.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. As Avanafil is not currently registered in Australia, prescribers should consult the FDA label (Stendra®) or EMA SmPC (Spedra®) for complete safety, contraindication, and drug interaction data.

Based on PDE5 inhibitor class characteristics, the following are established considerations:

- **Key Contraindications**: Concurrent use with any organic nitrates (risk of severe, potentially life-threatening hypotension); use in patients for whom sexual activity is inadvisable due to underlying cardiovascular status
- **Drug Interactions**: Strong CYP3A4 inhibitors (e.g., ketoconazole, itraconazole, ritonavir) substantially increase avanafil plasma exposure; alpha-blockers and antihypertensives may potentiate hypotensive effects

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN model score (94.59%), the mechanistic basis for avanafil in amenorrhea is highly indirect, and there is currently zero clinical trial or published literature evidence to support this indication (evidence level L5). The prediction score alone is insufficient to justify clinical development or further resource allocation for this specific indication.

**To proceed with further evaluation, the following is needed:**

- Obtain complete MOA data from DrugBank API (data gap DG002) to characterise molecular targets and pathway interactions relevant to reproductive endocrinology
- Obtain TGA PI or international equivalents (FDA label / EMA SmPC) to complete S1 safety pre-assessment (data gap DG001)
- **For Raynaud disease (rank 5 — recommended priority):** Initiate a structured literature review of class-effect evidence from sildenafil and tadalafil RCTs; assess feasibility of a small pilot study with avanafil given its rapid onset of action (approximately 15 minutes), which may offer a practical advantage in on-demand vasospasm management
- If amenorrhea is to be pursued further despite current evidence gaps, commission a targeted preclinical review examining PDE5 expression in endometrial and ovarian tissue, and evaluate sildenafil data in thin endometrium as the closest available proxy
- Regulatory pathway assessment via TGA for any Australian clinical use would be required prior to trials, given current non-registered status

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

