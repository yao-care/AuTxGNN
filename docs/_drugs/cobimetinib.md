---
layout: default
title: Cobimetinib
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 10
---

# Cobimetinib
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

# Cobimetinib: From BRAF-Mutated Melanoma to Amyotrophic Lateral Sclerosis

## One-Sentence Summary

Cobimetinib is a selective MEK1/2 inhibitor approved internationally (though not in Australia) in combination with vemurafenib for unresectable or metastatic melanoma harbouring a BRAF V600E or V600K mutation.
The TxGNN model predicts it may have therapeutic potential for **Amyotrophic Lateral Sclerosis (ALS)**, with **no clinical trials** and **no published literature** currently supporting this specific repurposing direction.
At this stage, the prediction is hypothesis-generating only, grounded in MAPK pathway biology, and represents an early-stage research question requiring dedicated preclinical investigation before any clinical consideration.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Australia; internationally indicated for BRAF V600E/K-mutated unresectable or metastatic melanoma (in combination with vemurafenib) |
| Predicted New Indication | Amyotrophic Lateral Sclerosis (ALS) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Cobimetinib is a potent, selective inhibitor of MEK1 and MEK2 (MAP2K1/MAP2K2) — key kinases within the RAS–RAF–MEK–ERK signalling cascade. By blocking MEK1/2 phosphorylation, cobimetinib suppresses downstream ERK activation, a pathway critically involved in cell proliferation, survival, and stress responses. Its established oncology use is in BRAF V600E/K-mutated melanoma, where constitutive ERK activation drives tumour growth.

The rationale for exploring cobimetinib in ALS centres on emerging mechanistic evidence that aberrant ERK hyperactivation contributes to motor neuron toxicity and neuroinflammation. In ALS pathology, disease-associated proteins such as TDP-43, FUS, and mutant SOD1 have been linked to dysregulation of MAPK/ERK signalling, potentially driving the neuroinflammatory microglial activation and neuronal apoptosis that characterise disease progression. MEK inhibition could theoretically interrupt this neurotoxic cascade and confer a degree of neuroprotection. Preclinical literature on MEK inhibitor class effects in neurodegeneration (beyond cobimetinib specifically) has shown some promise in oxidative stress and neuroinflammation models.

That said, the mechanistic link remains indirect and inferential. No preclinical studies specifically evaluating cobimetinib in ALS models have been identified. The TxGNN high score (0.997) likely reflects the broad topological relevance of the RAS/MAPK pathway across neurodegenerative disease networks within the knowledge graph, rather than direct experimental evidence linking cobimetinib to ALS. Importantly, cobimetinib's established safety concerns — including cardiac, ophthalmic, and hepatic toxicities — warrant careful consideration when evaluating its suitability for a non-oncology, potentially long-term neurological indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for cobimetinib in amyotrophic lateral sclerosis.

---

## Literature Evidence

Currently no related literature available for cobimetinib in amyotrophic lateral sclerosis.

---

## Australia Market Information

Cobimetinib is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. There are zero ARTG entries for any cobimetinib-containing product as of the data cut-off date (4 April 2026).

Internationally, cobimetinib (Cotellic®, Genentech/Roche) has been approved by the US FDA (November 2015) and the European Medicines Agency for BRAF V600E/K-mutated unresectable or metastatic melanoma in combination with vemurafenib. No TGA marketing approval has been granted. Any clinical access in Australia would require navigation of the Special Access Scheme (SAS) or the Authorised Prescriber pathway.

---

## Cytotoxicity

Cobimetinib is a targeted antineoplastic agent (MEK1/2 inhibitor) indicated for malignant melanoma. The cytotoxicity section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — MEK1/2 inhibitor (RAS/MAPK pathway); not a conventional cytotoxic agent |
| Myelosuppression Risk | Low (MEK inhibitors have minimal direct myelosuppressive effect; mild anaemia occasionally reported; routine FBC monitoring still recommended) |
| Emetogenicity Classification | Low to moderate (oral targeted agent; gastrointestinal effects such as diarrhoea and nausea are common but severe vomiting is uncommon) |
| Monitoring Items | LVEF (echocardiogram or MUGA scan at baseline, then periodically); LFTs (ALT, AST, bilirubin); CK and creatinine (myopathy risk); full ophthalmic assessment including retinal OCT (uveitis and retinal toxicity); dermatological review (acneiform rash, photosensitivity); serum electrolytes |
| Handling Protection | Follow institutional policy for oral targeted therapies; full cytotoxic handling precautions (as per cytotoxic drug handling guidelines) are not mandated for MEK inhibitors but should be applied if local SOPs require it |

---

## Safety Considerations

Detailed product-level safety data (TGA-specific warnings and contraindications) was not available in the current Evidence Pack. Based on the established class profile of MEK1/2 inhibitors, prescribers should be aware of the following key concerns:

- **Cardiac toxicity**: Decreased left ventricular ejection fraction (LVEF) has been reported — baseline and periodic cardiac imaging is essential
- **Ophthalmic toxicity**: Retinal vein occlusion, retinal pigment epithelial detachment, and uveitis — of particular clinical significance if cobimetinib were considered in patients with neurodegenerative disease who may already have ophthalmic comorbidities
- **Hepatotoxicity**: Elevated transaminases requiring regular LFT monitoring
- **Dermatological effects**: Acneiform rash, photosensitivity, and hand-foot skin reaction — sun protection and dermatological review advised
- **Rhabdomyolysis/myopathy**: CK elevation has been reported; relevant given potential muscle involvement in ALS

Please refer to the internationally approved Product Information (PI) for cobimetinib (Cotellic®) for comprehensive safety information. For use in Australia under unapproved access pathways, clinicians should consult the TGA's current guidance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score to cobimetinib for ALS based on MAPK pathway biology, but there is currently zero supporting clinical or dedicated preclinical evidence specific to this indication. With no ARTG registration, no clinical trials, no published literature, and no direct mechanistic studies in ALS models, this candidate remains at the earliest possible research stage (L5/S0). The biological hypothesis is coherent but indirect, and cobimetinib's known toxicity profile — particularly ophthalmic and cardiac risks — introduces additional translational hurdles for a neurological indication requiring long-term dosing.

**To proceed, the following is needed:**

- **Preclinical validation**: Dedicated in vitro and in vivo studies evaluating cobimetinib in validated ALS models (SOD1-G93A, TDP-43, C9orf72 rodent models) to assess whether MEK inhibition confers motor neuron protection
- **Class-level literature synthesis**: A systematic review of broader MEK inhibitor effects in neurodegenerative disease (Parkinson's, Huntington's, ALS) to determine whether class-level evidence supports or undermines the hypothesis
- **Safety feasibility analysis**: Assessment of cobimetinib's chronic tolerability profile in a non-oncology context — ALS patients differ significantly from melanoma patients in age, comorbidities, disease trajectory, and acceptable risk tolerance
- **Biomarker strategy**: Identification of candidate pharmacodynamic biomarkers (e.g., CSF ERK phosphorylation, neurofilament light chain) that could support proof-of-mechanism in early-phase studies
- **Stakeholder engagement**: Consultation with Australian neurology and neuromuscular disease specialists (e.g., via MND Australia clinical research network) to assess appetite for investigator-initiated research
- **Regulatory pathway planning**: TGA guidance on Special Access Scheme (Category B) or Authorised Prescriber access if a pilot study is ultimately pursued

> ⚠️ **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All information should be interpreted in conjunction with the TGA-approved Product Information and current clinical guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

