---
layout: default
title: Naproxen
parent: Model Prediction Only (L5)
nav_order: 461
evidence_level: L5
indication_count: 10
---

# Naproxen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Naproxen: From Arthritis/Pain Treatment to Brachydactyly-Syndactyly Syndrome (Low-confidence Prediction)

## Executive Summary

Naproxen is a traditional non-steroidal anti-inflammatory drug (NSAID) and is clinically widely used for arthritis, pain, and inflammatory symptoms. The TxGNN model's highest-scoring new indication is **Brachydactyly-Syndactyly Syndrome**, but there is currently **no clinical trial or literature support for this connection**, and the mechanistic rationale clearly indicates that this disease is a congenital skeletal developmental abnormality with no direct pathological association with NSAID anti-inflammatory mechanisms.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indications | This evidence package does not provide TFDA/ARTG approved indication wording (Naproxen is currently not marketed in Australia); based on publicly available pharmacological knowledge, Naproxen is a traditional NSAID widely used for pain, inflammation, and arthritis treatment |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature support) |
| Australian Market Status | Not marketed |
| ARTG Registry Count | 0 |
| Recommended Decision | Hold |

---

## Why is this prediction reasonable?

Currently, there is no detailed mechanistic data available. Based on known information, Naproxen is a traditional non-selective COX-1/COX-2 inhibitor class NSAID, whose efficacy in pain and inflammation-related indications has been widely clinically proven, with the mechanism primarily through inhibition of prostaglandin synthesis to produce anti-inflammatory, analgesic, and antipyretic effects.

However, Brachydactyly-Syndactyly Syndrome is a congenital acral skeletal developmental abnormality (caused by skeletal formation gene defects), with the pathological core being anomalous bone formation mechanisms during embryonic development, rather than an inflammatory mediator-driven pathological process. According to the `repurposing_rationale` provided in this evidence package, this prediction "has no direct pathological association with NSAID's COX inhibition/anti-inflammatory mechanism", suggesting the high score primarily originates from indirect proximity of bone-related nodes in the knowledge graph (graph-proximity false positive), rather than authentic mechanistic association.

In other words, this prediction currently lacks reasonable mechanistic support and represents a low-confidence candidate that should be excluded through manual review.

---

## Clinical Trial Evidence

Currently, there are no relevant clinical trials registered.

## Literature Evidence

Currently, there is no relevant literature.

---

## Australian Market Information

Naproxen is currently **not marketed in Australia** (ARTG registry count: 0), and this evidence package does not provide any ARTG entry data.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information (key warnings, contraindications, and drug interaction data are missing from this evidence package).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate achieves only L5 evidence level (model prediction alone with no clinical trial or literature support), and the mechanistic rationale itself has clearly indicated no direct pathological association with the original indication's pharmacological mechanism; the high score is likely a knowledge graph structural false positive. It is not recommended to invest further resources.

**If proceeding further is desired, the following must be supplemented:**
- At least 1 in vitro/in vivo mechanistic study to confirm the association between COX inhibition pathway and Brachydactyly-Syndactyly Syndrome pathology
- TFDA/TGA Product Information (product labeling warnings, contraindications) to complete S1 safety initial assessment
- Complete DrugBank MOA data
- If mechanistic support is weak, it is recommended to directly exclude this candidate

---

**Appendix:** This evidence package (TW-DB00788-multi) contains 10 TxGNN-predicted indications, of which rank 8 (inflammatory spondylopathy) and rank 10 (polyarticular juvenile rheumatoid arthritis) achieve evidence level L2, decision stage S2, and recommendation "Proceed with Guardrails", but the `repurposing_rationale` for both indicates they are confirmations of existing clinical practice uses, not novel mechanistic hypotheses. If the purpose is to identify evidence-supported candidates, it is recommended to generate a separate report based on these two indications as the main body, rather than the rank 1 candidate evaluated in this document.

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

