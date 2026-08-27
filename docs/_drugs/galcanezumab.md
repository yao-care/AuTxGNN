---
layout: default
title: Galcanezumab
parent: 僅模型預測 (L5)
nav_order: 304
evidence_level: L5
indication_count: 10
---

# Galcanezumab
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

# Galcanezumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Galcanezumab is a humanized anti-CGRP monoclonal antibody whose established use, based on the supporting literature in this evidence pack, is preventive treatment of episodic and chronic migraine. Of the **10 new indications** the TxGNN model predicted for this drug, only **Migraine with Brainstem Aura** — a specific migraine subtype currently excluded from most CGRP-antibody trials — has a plausible mechanistic basis and literature support; the other nine (mostly rare coagulation and skin disorders) are assessed as knowledge-graph noise with no biological link. This subtype prediction is backed by **20 publications** (including 4 pivotal Phase 3 RCTs on migraine broadly), but **0 clinical trials** specific to this subgroup.

> **Screening note:** TxGNN scored 9 of the 10 candidates for Galcanezumab higher or comparably (0.72–0.995) than this one (0.983), but each of those nine — heparin cofactor II deficiency, antithrombin deficiency type 2, factor V excess, thrombophilia, atrophoderma vermiculata, ulerythema ophryogenesis, haemorrhagic disease of the newborn, prekallikrein deficiency, and platelet-anomaly thrombotic disorder — returned zero clinical trials and zero literature hits, and the model's own rationale flags them as vector-proximity artefacts (disease nodes clustered via generic hub nodes like "haemostasis," not real CGRP-pathway biology). This report therefore focuses on the one candidate with a defensible mechanistic and evidentiary basis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in Australian regulatory data (drug not marketed, no ARTG record); literature indicates original use is migraine prevention |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 98.33% |
| Evidence Level | L2 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available from the DrugBank field in this evidence pack (flagged as a data gap). However, the supporting literature confirms the mechanism directly: Galcanezumab is a humanized monoclonal antibody that binds calcitonin gene-related peptide (CGRP) and inhibits its physiological activity (PMID 32504377). CGRP signalling is considered central to migraine pathophysiology across subtypes (PMID 30725283), which is the pharmacological basis for the drug's established efficacy in episodic and chronic migraine, demonstrated in the pivotal Phase 3 trials EVOLVE-1, EVOLVE-2, and REGAIN.

Migraine with brainstem aura (formerly "basilar-type migraine") is a subtype of migraine with aura, not a distinct disease — so the "new indication" here is a subgroup extension rather than a novel disease area. This is mechanistically coherent: several publications in this evidence pack report CGRP-antibody efficacy on aura-related symptoms and triggers specifically (PMID 36266558, PMID 36927366), and case-based literature on anti-CGRP antibodies in migraine aura and hemiplegic migraine (a related aura subtype) shows encouraging signals (PMID 35268319, PMID 37366160, PMID 39345003, PMID 41618146).

The caveat is that patients with brainstem aura are typically **excluded from pivotal RCTs** because of a theoretical concern that vasoconstrictor migraine drugs could aggravate brainstem ischaemia. Galcanezumab acts peripherally on CGRP (unlike triptans, which are direct vasoconstrictors), so this theoretical risk is considered lower — but it has not been formally tested in this subgroup, which is why no dedicated clinical trials exist despite the mechanistic plausibility.

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific subtype (Migraine with Brainstem Aura). The efficacy evidence below comes from trials on migraine broadly and case-level literature on related aura subtypes.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29813147](https://pubmed.ncbi.nlm.nih.gov/29813147/) | 2018 | RCT | JAMA Neurology | EVOLVE-1 pivotal Phase 3 trial establishing galcanezumab efficacy in episodic migraine prevention |
| [36266558](https://pubmed.ncbi.nlm.nih.gov/36266558/) | 2023 | RCT (Phase 2, Japanese cohort) | Neurology and Therapy | Reduced migraine severity and frequency of attacks associated with nausea, photophobia/phonophobia, prodromal symptoms, **or aura** |
| [36927366](https://pubmed.ncbi.nlm.nih.gov/36927366/) | 2023 | RCT (Phase 3 subgroup) | J Headache Pain | Examined effect on headache incidence after triggers, premonitory symptoms, and **aura episodes** across responder subgroups |
| [32504377](https://pubmed.ncbi.nlm.nih.gov/32504377/) | 2020 | Review | Drugs | Overview of galcanezumab efficacy across EVOLVE-1/2 (episodic) and REGAIN (chronic) migraine trials |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | Handbook Exp Pharmacol | Foundational review of CGRP's role in migraine pathophysiology (mechanistic basis) |
| [40341526](https://pubmed.ncbi.nlm.nih.gov/40341526/) | 2025 | Review (case-based) | Headache | Genetic migraine disorders, including a case with visual/aura features, responsive to CGRP-antagonist treatment |
| [35268319](https://pubmed.ncbi.nlm.nih.gov/35268319/) | 2022 | Case reports & literature review | J Clin Medicine | Directly examines whether anti-CGRP monoclonal antibodies (incl. galcanezumab) are effective in preventing migraine **aura** itself |
| [37366160](https://pubmed.ncbi.nlm.nih.gov/37366160/) | 2023 | Case series | Headache | Anti-CGRP monoclonal antibodies in hemiplegic migraine (a related aura subtype), tertiary headache centre |
| [39345003](https://pubmed.ncbi.nlm.nih.gov/39345003/) | 2025 | Case series | Headache | Galcanezumab efficacy in PRRT2-associated familial hemiplegic migraine |
| [41618146](https://pubmed.ncbi.nlm.nih.gov/41618146/) | 2026 | Individual patient analysis | J Headache Pain | Effectiveness and safety of anti-CGRP monoclonal antibodies in hemiplegic migraine (patients systematically excluded from RCTs) |

## Australia Market Information

Galcanezumab is **not currently registered on the ARTG** (Australian Register of Therapeutic Goods) per this evidence pack — there are no listed products for the Australian market.

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information — no key warnings, contraindications, or drug-interaction data were retrievable in this evidence pack (DDI query returned no results, and the TGA-equivalent label data is flagged as a blocking data gap, DG001).

Two isolated case reports in the supporting literature are worth noting for clinical awareness, though they do not constitute systematic safety data:
- Reversible cerebral artery vasoconstriction observed after a galcanezumab loading dose in one patient (PMID 39365416)
- Two cases of continued galcanezumab use into the first/second trimester of pregnancy without adverse delivery outcomes (PMID 41760025)

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The CGRP mechanism is well established for migraine broadly (4 pivotal Phase 3 RCTs), and literature specifically links CGRP-antibody activity to aura-related symptoms — but no clinical trial has directly tested galcanezumab in patients with brainstem aura, a subgroup routinely excluded from RCTs over theoretical vasoconstriction concerns.

**To proceed, the following is needed:**
- Dedicated efficacy/safety data in patients with migraine with brainstem aura (currently excluded from all cited RCTs)
- TFDA/TGA-equivalent Product Information and formal contraindication/DDI data (currently unavailable — DG001, blocking)
- Primary-source MOA confirmation from DrugBank (currently a data gap — DG002)
- ARTG registration status confirmation, since the drug is not currently marketed in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

