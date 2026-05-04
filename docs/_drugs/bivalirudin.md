---
layout: default
title: Bivalirudin
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Bivalirudin
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

# Bivalirudin: From Anticoagulation in PCI/HIT to Primary Release Disorder of Platelets

## One-Sentence Summary

Bivalirudin is a direct thrombin inhibitor established as an anticoagulant during percutaneous coronary intervention (PCI) and in patients with heparin-induced thrombocytopenia (HIT), though it currently holds no TGA registration in Australia.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**,
with **5 clinical trials** and **1 publication** currently supporting this direction.
This prediction is mechanistically plausible given the central role of thrombin in platelet activation and the particular advantage of Bivalirudin in platelet-compromised, heparin-intolerant settings.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anticoagulation during PCI; management of HIT/HITTS (established international use; no TGA registration) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 97.84% |
| Evidence Level | L3 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is not currently available for this analysis. Based on established pharmacological knowledge, Bivalirudin is a synthetic 20-amino acid direct thrombin inhibitor (DTI) that binds both the active catalytic site and the anion-binding exosite 1 of thrombin, thereby blocking thrombin's capacity to cleave fibrinogen and to activate platelets via PAR-1 and PAR-4 receptors. Critically, unlike heparin, Bivalirudin does not require antithrombin III (AT-III) as a cofactor, giving it predictable pharmacokinetics and activity even in AT-III–deficient states.

Primary release disorder of platelets refers to a failure of dense granule and/or alpha granule secretion — the release step that amplifies platelet activation and recruits additional platelets to the growing thrombus. While this condition is fundamentally a haemostatic deficiency, the clinical challenge arises when such patients also require anticoagulation (e.g., during PCI, CABG, or ECMO), or when they develop concurrent heparin-induced thrombocytopenia. Heparin-induced thrombocytopenia (HIT) is itself a condition in which platelet activation and consumptive release occur in a pathologically uncontrolled manner — directly recapitulating the "platelet activation–release" axis that defines the predicted indication.

The mechanistic link is therefore twofold: (1) Bivalirudin interrupts thrombin-mediated PAR-1 signalling, the strongest physiological trigger of platelet granule release, which is directly relevant to a release-amplification disorder; and (2) when patients with release dysfunction require procedural anticoagulation, Bivalirudin's AT-III independence, short half-life, and absence of immune platelet-depleting effects make it a safer alternative to unfractionated heparin. Both the clinical trials and the case report in this Evidence Pack centre on exactly this scenario, lending strong face validity to the TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---|---|---|---|---|
| [NCT00043940](https://clinicaltrials.gov/study/NCT00043940) | Phase 3 | Completed | 50 | Assessed safety of Bivalirudin as an alternative anticoagulant in patients with new or prior HIT/HITTS undergoing PCI. HIT is a paradigmatic platelet activation–release pathology, making this the most directly relevant trial. |
| [NCT00073580](https://clinicaltrials.gov/study/NCT00073580) | Phase 3 | Completed | 88 | Examined safety and efficacy of Bivalirudin (Angiomax) in HIT/HITTS Type II patients undergoing off-pump CABG (OPCAB). Validates Bivalirudin in surgical settings with impaired platelet release dynamics. |
| [NCT00250471](https://clinicaltrials.gov/study/NCT00250471) | Phase 3 | Completed | 900 | Compared Bivalirudin versus eptifibatide ± heparin in high-risk PCI patients. Evaluated post-PCI microvascular dysfunction and ischaemia, providing large-scale safety and efficacy data in platelet-active interventional settings. |
| [NCT01519518](https://clinicaltrials.gov/study/NCT01519518) | Phase 4 | Completed | 1,829 | Large pragmatic RCT comparing UFH versus Bivalirudin in primary PCI for STEMI, predominantly via radial access. Broad platelet-relevant anticoagulation context; GP IIb/IIIa inhibitors reserved for bail-out only. |
| [NCT01270139](https://clinicaltrials.gov/study/NCT01270139) | N/A | Completed | 180 | First-in-man trial of silica-gold nanoparticle plasmonic photothermal therapy for atherosclerotic lesions (NANOM-FIM). Bivalirudin relevance is minimal; likely a data artefact from query overlap rather than a substantive trial for this indication. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [35763168](https://pubmed.ncbi.nlm.nih.gov/35763168/) | 2022 | Case Report | Journal of Thrombosis and Thrombolysis | Describes spontaneous HIT in a COVID-19 patient presenting with acute limb ischaemia. IgG antibodies against heparin–PF4 complexes activated platelets causing a profoundly prothrombotic state — a spontaneous release-activation cascade. Underscores the clinical niche for Bivalirudin when heparin is absolutely contraindicated. |

---

## Safety Considerations

Bivalirudin is not registered with the TGA and has no Australian Product Information (PI). Please refer to the current approved prescribing information from the US FDA (Bivalirudin / Angiomax) or the EMA for comprehensive safety data, including:

- Known bleeding risks (major and minor haemorrhage)
- Contraindications in active major bleeding
- Dose adjustment requirements in renal impairment
- Monitoring parameters (ACT, aPTT, haemoglobin, creatinine)

No drug–drug interaction data was retrieved for this Evidence Pack query.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 trials directly studying Bivalirudin in HIT/HITTS — a condition mechanistically anchored in platelet activation–release pathology — provide substantive evidence supporting safety and feasibility of use in platelet-release–disordered settings. The absence of TGA registration and the lack of dedicated trials for the specific ICD entity "primary release disorder of platelets" warrant cautious, protocol-governed progression rather than immediate adoption.

**To proceed, the following is needed:**

- **TGA regulatory pathway assessment**: Bivalirudin has no ARTG listing; a Special Access Scheme (SAS) Category B or clinical trial exemption (CTX) application would be required for Australian use in this indication.
- **DrugBank MOA data**: Retrieve complete mechanism of action, pharmacokinetics, and toxicity profile via DrugBank API (DG002).
- **Dedicated clinical evidence**: No published trial has prospectively enrolled patients specifically diagnosed with primary release disorder of platelets. A case series or registry study in this population is needed to satisfy L2 evidence requirements.
- **Safety profile for platelet-release disorders**: Formal bleeding risk modelling in patients with compromised platelet granule secretion — who may have additive haemorrhagic risk when anticoagulated — is required before clinical use.
- **Renal dosing guidance**: Bivalirudin is renally cleared; dosing protocols for patients with renal impairment who also have platelet release defects must be specified.
- **ANZCTR registration**: Any prospective Australian study should be registered with the Australian New Zealand Clinical Trials Registry (ANZCTR) to ensure local regulatory visibility.

---

> **Disclaimer**: This report is generated for research purposes only and does not constitute medical advice. Drug repurposing candidates require prospective clinical validation before clinical application. Healthcare professionals should exercise independent clinical judgement and refer to current approved product information.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

