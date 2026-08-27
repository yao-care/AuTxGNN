---
layout: default
title: Oxycodone
parent: 僅模型預測 (L5)
nav_order: 502
evidence_level: L5
indication_count: 10
---

# Oxycodone
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

# Oxycodone: From Pain Management to Restless Legs Syndrome

> **Note on indication selection:** Among the 10 disease signals TxGNN returned for Oxycodone, the single highest-scoring one (*methemoglobinemia*, 92.7%) is explicitly flagged in the evidence pack as having zero supporting clinical trials or literature and no plausible pharmacological mechanism (oxidative-reduction pathology vs. mu-opioid agonism) — it is judged a likely embedding-space artefact rather than a real signal ("Hold", evidence level L5). This report instead focuses on **Restless Legs Syndrome (RLS)**, the only candidate among the ten with substantive clinical trial and literature support and a real-world regulatory precedent.

## One-Sentence Summary

Oxycodone is a semi-synthetic opioid analgesic used for the management of moderate to severe pain. The TxGNN model, together with corroborating clinical and literature evidence, points to **Restless Legs Syndrome** as a credible new indication, with **1 completed Phase 3 randomised controlled trial** and **20 supporting publications** — including a 2025 American Academy of Sleep Medicine guideline — and an existing European approval for the oxycodone/naloxone prolonged-release combination in this exact setting.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Moderate to severe pain (opioid analgesic) — specific regulatory-approved indication text not available in this evidence pack |
| Predicted New Indication | Restless Legs Syndrome |
| TxGNN Prediction Score | 90.35% |
| Evidence Level | L2 (1 completed Phase 2/3 RCT, supported by systematic reviews and a clinical practice guideline) |
| Australia Market Status | Not Marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Oxycodone is not available in this evidence pack (data gap). Based on established pharmacology, Oxycodone is a semi-synthetic **mu-opioid receptor agonist**, structurally and functionally related to morphine, used clinically for central analgesia across a broad range of pain conditions.

Restless Legs Syndrome (RLS) is a neurological movement disorder characterised by an urge to move the legs, worsening at rest and at night, with pathogenesis believed to involve **central dopaminergic dysfunction** and, more recently recognised, **endogenous opioid system involvement**. Opioid receptor agonists are known to relieve both the sensory and motor components of RLS, and interactions between the opioid and dopaminergic systems are part of the accepted pathophysiological model of the disease — this is the mechanistic bridge that plausibly connects Oxycodone's known pharmacology to a non-analgesic neurological indication.

Critically, this is not a purely theoretical repurposing hypothesis: a prolonged-release **oxycodone/naloxone (OXN PR)** combination (marketed in Europe as Targin/Targinact) is already **approved in Europe as second-line therapy for severe-to-very-severe idiopathic RLS** in patients who have failed first-line dopamine agonist or α2δ-ligand therapy. The naloxone component is included specifically to counteract opioid-induced bowel dysfunction without compromising central analgesic/RLS efficacy. This existing regulatory precedent, combined with a completed Phase 3 RCT and multiple independent reviews (including a Cochrane systematic review and the 2025 AASM clinical practice guideline), makes this one of the more evidence-anchored repurposing signals in the TxGNN output for this drug — a genuine step up from a purely computational association.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01112644](https://clinicaltrials.gov/study/NCT01112644) | Phase 3 | Completed | 205 | Randomised, double-blind, placebo-controlled, multicentre trial demonstrating superior efficacy of prolonged-release oxycodone/naloxone (OXN PR) over placebo in improving RLS symptom severity in moderate-to-severe idiopathic RLS with daytime symptoms |

No ANZCTR-registered trials for this indication were identified in the evidence pack.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39324694](https://pubmed.ncbi.nlm.nih.gov/39324694/) | 2025 | Practice Guideline (AASM) | J Clin Sleep Med | American Academy of Sleep Medicine clinical practice guideline for treatment of RLS and periodic limb movement disorder |
| [26966363](https://pubmed.ncbi.nlm.nih.gov/26966363/) | 2016 | Review | Neuropsychiatric Dis Treat | Reviews the role of prolonged-release oxycodone-naloxone specifically in intractable/refractory RLS after dopamine agonist or α2δ-ligand failure |
| [26135898](https://pubmed.ncbi.nlm.nih.gov/26135898/) | 2015 | Review | CNS Drugs | Dedicated review of oxycodone/naloxone PR (Targin/Targiniq) as an approved second-line treatment for severe refractory RLS in Europe |
| [27355187](https://pubmed.ncbi.nlm.nih.gov/27355187/) | 2016 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Cochrane systematic review of opioids, including oxycodone/naloxone, for RLS treatment |
| [29756335](https://pubmed.ncbi.nlm.nih.gov/29756335/) | 2018 | Evidence-based Review | Mov Disord | Updated evidence-based review confirming oxycodone/naloxone has accrued sufficient data to be considered efficacious for RLS |
| [35026088](https://pubmed.ncbi.nlm.nih.gov/35026088/) | 2022 | Review/Commentary | Tidsskr Nor Laegeforen | Commentary specifically addressing "Oxycodone to treat restless legs syndrome?" |
| [33985652](https://pubmed.ncbi.nlm.nih.gov/33985652/) | 2021 | Review | Sleep Med Clin | Discusses opioids, including oxycodone/naloxone PR, as second-line RLS treatment after alpha-2-delta ligands |
| [30244828](https://pubmed.ncbi.nlm.nih.gov/30244828/) | 2018 | Review | Lancet Neurol | Overview of RLS comorbidities, treatment, and pathophysiology, including dopaminergic and opioid pathway involvement |
| [26215616](https://pubmed.ncbi.nlm.nih.gov/26215616/) | 2015 | Review | Nat Rev Neurol | Reviews current RLS therapies including opioids where approved, and management of augmentation with dopaminergic agents |
| [33880737](https://pubmed.ncbi.nlm.nih.gov/33880737/) | 2021 | Review | Neurotherapeutics | Contemporary review of RLS diagnosis and treatment, situating opioid therapy within the broader dopaminergic pathophysiological model |

---

## Australia Market Information

Oxycodone (this candidate) is currently **not marketed** in Australia under this evidence pack's search, with **0 ARTG entries** identified. No product, dosage form, or approved-indication data is available to tabulate.

*(Note: Oxycodone in general is a well-established Schedule 8 opioid available in various registered Australian products for pain indications; the absence of ARTG entries here reflects a gap in this evidence pack's regulatory data collection rather than confirmation that no oxycodone product exists in Australia. This should be verified directly against the TGA/ARTG database before any decision is finalised.)*

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information. No structured safety warnings, contraindications, or drug interaction data were available in this evidence pack (DDI query status: not found).

This is a **critical data gap**, not merely an absence of findings — see Conclusion and Next Steps below.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The RLS signal is supported by a completed Phase 3 RCT, a Cochrane systematic review, and a current (2025) AASM clinical practice guideline, and the oxycodone/naloxone combination already holds regulatory approval in Europe for this exact second-line indication in refractory RLS. This is meaningfully stronger than a model-only signal, but two blocking-severity data gaps — missing local safety/label data and missing MOA data — mean the candidate cannot yet proceed past initial safety screening.

**To proceed, the following is needed:**
- TFDA/TGA-equivalent Product Information warnings and contraindications (data gap **DG001**, Blocking — currently prevents entry into initial safety assessment)
- Detailed mechanism-of-action data from DrugBank (data gap **DG002**, High — needed for mechanistic-plausibility review)
- Confirmed drug-drug interaction dataset (current query status: not found), particularly relevant for the typically older RLS patient population
- Verification of current Australian registration/ARTG status for oxycodone products, since 0 entries were found in this evidence pack
- Confirmation that efficacy shown for the **oxycodone/naloxone** combination applies to any oxycodone monotherapy formulation under consideration, since the supporting trial and reviews are naloxone-combination-specific
- Alignment check against Australian RLS treatment guidelines and PBS pathway, given opioids are recommended only as second-line therapy after dopamine agonist/α2δ-ligand failure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

