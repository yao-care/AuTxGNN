---
layout: default
title: Burosumab
parent: 僅模型預測 (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
---

# Burosumab
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

# Burosumab: From X-linked Hypophosphatemia to Renal Osteodystrophy

## One-Sentence Summary

Burosumab (brand name: Crysvita) is a fully human anti-FGF23 monoclonal antibody approved internationally for the treatment of X-linked hypophosphatemia (XLH), a rare genetic disorder causing chronic low blood phosphate and progressive skeletal disease.
The TxGNN model predicts it may have potential in **Renal Osteodystrophy** (prediction score 96.9%), though this specific indication is currently supported by only **1 review publication** and **no clinical trials**.
Importantly, a closely related indication — **Bone Remodeling Disease** (Rank 4) — is backed by **2 completed Phase 3 trials** and represents the most clinically actionable opportunity in this drug's predicted profile.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | X-linked Hypophosphatemia (XLH) — approved by FDA, EMA, and PMDA; not registered in Australia |
| Predicted New Indication | Renal Osteodystrophy |
| TxGNN Prediction Score | 96.9% |
| Evidence Level | L4 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Burosumab is a fully human IgG1 monoclonal antibody that targets and inhibits fibroblast growth factor 23 (FGF23). In XLH — caused by loss-of-function mutations in the *PHEX* gene — FGF23 is chronically overproduced, which suppresses renal tubular phosphate reabsorption (via downregulation of NaPi-IIa and NaPi-IIc co-transporters) and inhibits CYP27B1 (1α-hydroxylase), reducing synthesis of active vitamin D (1,25(OH)₂D₃). This combined phosphate and calcitriol deficiency severely impairs bone mineralisation, causing rickets in children and osteomalacia in adults. Burosumab reverses this process by blocking FGF23, restoring both phosphate reabsorption and calcitriol synthesis — a mechanism confirmed across two pivotal Phase 3 trials in XLH.

Renal osteodystrophy is the umbrella term for bone disease arising in chronic kidney disease (CKD), driven partly by markedly elevated FGF23 levels. The shared FGF23 axis superficially links XLH and renal osteodystrophy, and the TxGNN knowledge graph captures this topological proximity (score 96.9%). However, the clinical situation in CKD is fundamentally different: FGF23 elevation in CKD is a *compensatory* mechanism designed to prevent the dangerous phosphate retention that accelerates CKD progression, vascular calcification, and cardiovascular mortality. Blocking FGF23 with Burosumab in this setting would be expected to worsen hyperphosphataemia — directly opposing the goals of CKD-MBD (mineral and bone disorder) management.

Currently, only one broad review article addresses metabolic bone disease in the context relevant to this indication. No dedicated preclinical or clinical studies have evaluated Burosumab for renal osteodystrophy, and the mechanistic concern about inducing clinically significant hyperphosphataemia in CKD patients remains unresolved. The TxGNN prediction score reflects graph topology, not clinical safety or feasibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for renal osteodystrophy.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37927073](https://pubmed.ncbi.nlm.nih.gov/37927073/) | 2024 | Review | Current Pediatric Reviews | Reviews diagnosis and management of hypophosphatasia and X-linked hypophosphatemic rickets in children; highlights the challenges of rare metabolic bone disease diagnosis, overlapping phenotypes with common rickets, and emerging targeted therapies including anti-FGF23 approaches |

---

## Australia Market Information

Burosumab (Crysvita) is **not registered** on the Australian Register of Therapeutic Goods (ARTG). There are currently no ARTG entries for this drug.

> **Context for clinicians:** Burosumab has received regulatory approval in the United States (FDA, 2018), Europe (EMA, 2018), Japan (PMDA, 2019), and several other jurisdictions for X-linked hypophosphatemia in paediatric and adult patients. TGA registration in Australia had not been completed as of the data cutoff (21 June 2026). Access in Australia would currently require Special Access Scheme (SAS) or Authorised Prescriber pathway.

---

## Safety Considerations

No TGA-approved Product Information (PI) is available for Australia. Clinicians should consult the approved prescribing information from the FDA (US Prescribing Information), EMA (Summary of Product Characteristics), or PMDA as the applicable reference source.

**Key mechanistic safety concern specific to this indication:** In patients with CKD, FGF23 suppression via Burosumab carries a theoretical risk of inducing or significantly worsening **hyperphosphataemia**. Elevated serum phosphate in CKD accelerates progression to end-stage renal disease, promotes vascular and soft-tissue calcification, and is independently associated with increased cardiovascular mortality. Any exploratory use of Burosumab in CKD-related bone disease would require rigorous phosphate monitoring at minimum, and the risk-benefit assessment is currently unfavourable without dedicated safety data in this population.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction captures a genuine biological link between Burosumab's FGF23-blocking mechanism and renal osteodystrophy via shared phosphate metabolism pathways; however, in CKD the elevated FGF23 is a protective compensatory response, and blocking it risks clinically significant hyperphosphataemia that contradicts established CKD-MBD management principles. With only one peripheral review article and zero clinical trials, the evidence base is insufficient to justify further development for this specific indication at this time.

**To proceed, the following is needed:**
- Preclinical (animal model) studies evaluating the safety profile of FGF23 blockade in CKD models, with rigorous phosphate, phosphaturia, and renal function endpoints
- Identification of a defined CKD subpopulation where the risk-benefit ratio may be favourable — most plausibly patients with XLH who subsequently develop CKD (as documented in PMID 38195892 under Indication Rank 2), where the primary driver of FGF23 elevation remains genetic rather than compensatory
- Pharmacokinetic and pharmacodynamic modelling of Burosumab dosing in varying degrees of CKD (eGFR staging)
- TGA registration of Burosumab for its primary XLH indication as a regulatory prerequisite for any expanded use in Australia
- Review of the **Bone Remodeling Disease** indication (Rank 4 in this Evidence Pack, Evidence Level L1, "Proceed with Guardrails") as the priority repurposing pathway — two completed Phase 3 RCTs directly support Burosumab's efficacy in phosphate-mediated bone mineralisation disorders within this broader disease category
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

