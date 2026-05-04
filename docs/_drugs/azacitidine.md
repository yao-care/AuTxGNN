---
layout: default
title: Azacitidine
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 10
---

# Azacitidine
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

# Azacitidine: From Myelodysplastic Syndrome to Bulbar Polio

## One-Sentence Summary

Azacitidine is a DNA hypomethylating agent internationally approved for myelodysplastic syndromes (MDS) and acute myeloid leukaemia (AML), though it is not currently registered in Australia.
The TxGNN model predicts it may be effective for **Bulbar Polio**, however there are currently **no clinical trials** and **no published literature** supporting this direction.
With an evidence classification of Level 5 (model prediction only) and no mechanistic rationale, this candidate is not recommended for further investigation at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Australia; internationally approved for MDS and AML |
| Predicted New Indication | Bulbar Polio |
| TxGNN Prediction Score | 98.59% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the evidence pack. Based on established medical literature, Azacitidine (5-azacytidine) is a pyrimidine nucleoside analogue that inhibits DNA methyltransferases (DNMT1, DNMT3a, DNMT3b). By incorporating into DNA and RNA, it induces global DNA hypomethylation, reactivating transcriptionally silenced tumour-suppressor genes and promoting differentiation of dysplastic haematopoietic progenitor cells. This mechanism is directly relevant to myeloid malignancies characterised by pathological epigenetic silencing.

Bulbar poliomyelitis is an acute neurological disease caused by poliovirus — an RNA enterovirus that preferentially destroys lower motor neurons in the brainstem and spinal cord, producing bulbar palsy, respiratory failure, and cranial nerve deficits. The underlying pathology is one of viral cytolysis and neuroinflammation. There is no established biological connection between aberrant CpG methylation and poliovirus infection or replication.

The high TxGNN score almost certainly reflects topological proximity within the knowledge graph — for example, shared node connections relating to "motor neuron disease" or "neuromuscular compromise" — rather than genuine pharmacological causality. No preclinical models, mechanistic studies, or clinical observations support a role for Azacitidine in the treatment of poliomyelitis or related neurotropic viral infections.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Hypomethylating agent (pyrimidine nucleoside analogue) |
| Myelosuppression Risk | High — neutropenia, thrombocytopenia, and anaemia are among the most commonly reported adverse effects; dose-limiting in clinical practice |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Full blood count (FBC) with differential (at minimum before each cycle), liver function tests, serum creatinine and eGFR, serum electrolytes |
| Handling Protection | Must be prepared and administered in accordance with cytotoxic drug handling guidelines; appropriate PPE (gloves, gown, eye protection) required |

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) are available in the current evidence pack. As Azacitidine is not registered with the TGA, there is no Australian Product Information document. Please refer to the approved Product Information from international regulatory agencies (FDA label for Vidaza®; EMA summary of product characteristics) for comprehensive safety information, including warnings regarding embryo-foetal toxicity, renal impairment dosing, and hepatic disease.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Bulbar polio arises from RNA virus-mediated destruction of motor neurons — a pathophysiological mechanism with no established relationship to Azacitidine's DNMT inhibition activity. The complete absence of supporting clinical trials or published literature, combined with a sound biological counter-argument, renders this prediction a likely artefact of knowledge graph topology rather than a genuine repurposing opportunity.

**To proceed, the following would be needed:**
- Credible pre-clinical evidence (in vitro or animal model) demonstrating any mechanistic link between DNMT inhibition and poliovirus infection, replication, or neuronal protection
- Biological plausibility review by specialists in virology, infectious disease, and neurology
- Resolution of current data gaps: MOA confirmation, full safety profile, and TGA regulatory pathway assessment (noting Azacitidine has no current ARTG registration)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

