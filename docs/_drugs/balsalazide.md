---
layout: default
title: Balsalazide
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 10
---

# Balsalazide
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

# Balsalazide: From Ulcerative Colitis to Gout

## One-Sentence Summary

Balsalazide is a prodrug of 5-aminosalicylic acid (5-ASA), originally used for the treatment of mild-to-moderate active ulcerative colitis.
The TxGNN model predicts it may be effective for **Gout** (prediction score: 99.75%),
however, there are currently **no registered clinical trials** and **no supporting publications** for this indication — this represents a model prediction only (Evidence Level L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ulcerative colitis (mild-to-moderate active disease) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 (Model prediction only — no supporting studies identified) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Balsalazide is an oral prodrug of 5-aminosalicylic acid (5-ASA, mesalamine). After ingestion, the drug is delivered intact to the colon, where colonic bacteria cleave the azo bond to release 5-ASA locally at the site of mucosal inflammation. 5-ASA is understood to act primarily through inhibition of NF-κB signalling and suppression of prostaglandin synthesis, reducing inflammation of the colonic mucosa. Detailed mechanism of action data was not available in the current Evidence Pack; however, Balsalazide's efficacy in ulcerative colitis has been well established in international clinical practice and regulatory approvals.

Gout is driven by monosodium urate crystal deposition in joints, which triggers NLRP3 inflammasome activation and a subsequent neutrophil-mediated acute inflammatory cascade. While 5-ASA does possess some NF-κB inhibitory activity, there is no published evidence that it targets xanthine oxidase (the enzyme responsible for uric acid synthesis), directly inhibits the NLRP3 inflammasome, or meaningfully affects uric acid metabolism or renal urate excretion. The mechanistic link between Balsalazide and gout therefore remains indirect inference rather than a well-characterised biological pathway.

The TxGNN knowledge graph prediction likely arises from shared inflammatory pathway nodes connecting inflammatory bowel disease and crystal arthropathy within the graph structure, rather than a direct pharmacological relationship. In the absence of any supporting preclinical or clinical evidence, this prediction cannot be considered a viable repurposing candidate at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Balsalazide in Gout.

---

## Literature Evidence

Currently no related literature available for Balsalazide in Gout.

---

## Australia Market Information

Balsalazide is not currently registered with the Therapeutic Goods Administration (TGA) and holds no ARTG entries. It is not available as a marketed product in Australia.

> **Note for clinicians:** Balsalazide is approved and marketed in a number of other jurisdictions (including the United States, where it is available as Colazal® for ulcerative colitis). Australian clinicians seeking access would need to pursue Special Access Scheme (SAS) pathways. For prescribing information, refer to the FDA-approved label or equivalent international Product Information (PI), as no TGA-approved PI is currently available.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. As no TGA PI exists at this time, the following international class-level considerations apply to Balsalazide as a 5-ASA-containing agent:

- **Salicylate hypersensitivity:** Contraindicated or use with extreme caution in patients with known salicylate or aminosalicylate hypersensitivity.
- **Renal impairment:** 5-ASA products carry a class warning for nephrotoxicity with prolonged use; renal function monitoring is recommended.
- **Hepatic impairment:** Use with caution; hepatic reactions have been reported with aminosalicylate class drugs.

> Formal TGA safety data (key warnings, contraindications, drug interactions) was not available in this Evidence Pack. Full safety assessment requires access to an approved international PI.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.75%), the mechanistic basis for Balsalazide in gout is weak — 5-ASA's anti-inflammatory activity does not target the key drivers of gout pathophysiology (xanthine oxidase, NLRP3 inflammasome activation, or uric acid handling), and no clinical or preclinical evidence has been identified to support this repurposing hypothesis.

**To proceed, the following would be needed:**

- **Preclinical evidence** demonstrating that 5-ASA or Balsalazide directly inhibits NLRP3 inflammasome activation or reduces serum uric acid levels in relevant models
- **Mechanistic clarity** on whether NF-κB inhibition alone provides clinically meaningful benefit in acute or chronic gout
- **TGA registration pathway** — Balsalazide is not available in Australia; any clinical investigation would require either TGA registration or SAS Category B/C approval
- **Full safety data** — obtain and review an international PI (FDA, EMA) to complete safety gap assessment before advancing to any clinical consideration
- **Knowledge graph audit** — consider whether this prediction reflects a true biological signal or a graph connectivity artefact linking IBD and inflammatory arthritis nodes

---

> ⚠️ **Disclaimer:** This report is intended for research purposes only and does not constitute medical advice. Drug repurposing candidates require formal clinical validation before therapeutic application. All predictions should be interpreted in the context of established clinical evidence and regulatory requirements.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

