---
layout: default
title: Amantadine
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 10
---

# Amantadine
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

# Amantadine: From Parkinson's Disease / Influenza A to Rasmussen Subacute Encephalitis

---

## One-Sentence Summary

Amantadine is a long-established drug used for Parkinson's disease symptom management and influenza A prophylaxis and treatment, acting via NMDA receptor antagonism and M2 channel blockade.
The TxGNN model predicts it may be effective for **Rasmussen Subacute Encephalitis**,
with **0 clinical trials** and **0 publications** currently supporting this direction — the prediction rests entirely on knowledge graph topology, with no empirical evidence identified.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease / Influenza A (established international indications; not registered in Australia) |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Amantadine acts through two principal mechanisms: (1) antiviral activity by blocking the M2 ion channel of influenza A virus, thereby inhibiting viral uncoating; and (2) neurological effects via non-competitive antagonism of NMDA (N-methyl-D-aspartate) receptors and promotion of dopamine release from presynaptic terminals. These properties form the basis of its approved uses in influenza A treatment/prophylaxis and Parkinson's disease motor symptom management.

Rasmussen subacute encephalitis is a rare, progressive unihemispheric autoimmune inflammatory condition characterised by antibodies targeting ionotropic glutamate receptor subunits GluA3 and GluN2B. Given that Amantadine is an NMDA receptor antagonist, a theoretical mechanistic rationale exists: blocking NMDA receptors could theoretically dampen the excitotoxic neuronal injury that drives progressive cortical destruction in this condition.

In practice, however, this link remains entirely hypothetical. There are currently no basic science studies, animal model data, or any published clinical experience supporting Amantadine for Rasmussen encephalitis. The elevated TxGNN score (99.48%) most likely reflects topological proximity of the NMDA receptor node within the knowledge graph — a structural artefact rather than a validated biological signal. This prediction should be treated as a potential false positive at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Australia Market Information

Amantadine is **not currently listed on the Australian Register of Therapeutic Goods (ARTG)**. No product licences were identified in this search. Any clinical use in Australia would require access via the Special Access Scheme (SAS) or Authorised Prescriber pathway under TGA regulations.

---

## Safety Considerations

Please refer to published international Product Information (e.g., FDA PI or EMA SmPC) for full safety information, as no TGA-approved Australian PI exists.

Based on established pharmacological knowledge: Amantadine carries well-recognised CNS adverse effects including confusion, hallucinations, dizziness, insomnia, and — at higher doses — agitation and seizure risk. It requires dose adjustment in renal impairment. Dopaminergic activity may exacerbate psychosis in susceptible individuals. Use with other NMDA antagonists, anticholinergics, or dopaminergic agents may increase adverse effect burden.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial, preclinical study, or published literature directly supporting the use of Amantadine in Rasmussen subacute encephalitis. This is a pure model prediction (L5), and mechanistic plausibility via NMDA antagonism remains speculative without any supporting evidence chain.

**To proceed, the following is needed:**
- Preclinical studies (in vitro or animal models of Rasmussen encephalitis) assessing the impact of NMDA antagonism on disease progression
- Mechanistic clarification of the role of glutamate excitotoxicity versus autoimmune-mediated injury in disease pathogenesis
- Case reports or case series documenting any off-label clinical use in Rasmussen encephalitis or closely related autoimmune encephalitides
- TGA Special Access Scheme eligibility assessment, given the absence of any Australian ARTG registration
- Full safety profile review relevant to paediatric and adolescent populations (Rasmussen encephalitis predominantly affects children)
- Review of existing immunotherapy-based treatment approaches to determine whether Amantadine could serve a complementary rather than stand-alone role

> ⚠️ **Research Disclaimer:** This report is for research purposes only and does not constitute medical advice. Repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

