---
layout: default
title: Isosorbide Mononitrate
parent: 僅模型預測 (L5)
nav_order: 278
evidence_level: L5
indication_count: 10
---

# Isosorbide Mononitrate
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

# Isosorbide Mononitrate: From Angina Pectoris to Hypertrichosis

## One-Sentence Summary

Isosorbide mononitrate (ISMN) is a long-acting organic nitrate traditionally used for the prevention and treatment of angina pectoris, acting through nitric oxide (NO)-mediated vasodilation of coronary and systemic vessels.
The TxGNN model ranks **Hypertrichosis** as its top predicted new indication (score 99.99%), yet there are **no clinical trials and no supporting literature** — making this a likely knowledge graph clustering artefact rather than a genuine signal.
Across all 10 predicted indications, **Pulmonary Arterial Hypertension (PAH)** (rank 10) is the only indication with genuine mechanistic plausibility, backed by **6 pharmacology publications** including preclinical PAH model studies.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Angina pectoris — prevention and treatment of angina attacks |
| Predicted New Indication (Rank 1) | Hypertrichosis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

ISMN is an organic nitrate and a NO donor. After oral absorption, it spontaneously releases nitric oxide (NO), which diffuses into vascular smooth muscle cells and activates soluble guanylate cyclase (sGC). This raises intracellular cyclic GMP (cGMP) levels, triggering smooth muscle relaxation and vasodilation — reducing cardiac preload and relieving angina. The same NO/sGC/cGMP pathway also underlies its off-label use in portal hypertension.

The rank 1 prediction of **hypertrichosis** (excessive hair growth) is almost certainly a **knowledge graph clustering artefact**. The only conceivable mechanistic bridge is: ISMN → NO → vasodilation of follicular microvasculature → theoretically enhanced nutrient delivery to hair follicles. This logic is extrapolated from minoxidil, but minoxidil is a potassium channel opener — a fundamentally different mechanism from NO donation. No direct experimental or clinical evidence links ISMN to hair follicle physiology. Ranks 2–9 are similarly dominated by hair and congenital developmental conditions (alopecia areata, hypotrichosis, hair shaft abnormalities, Dandy-Walker malformation), none of which have any supporting evidence and most represent structural or genetic disorders where vasodilation has no therapeutic rationale.

The singular exception across all 10 predictions is **Pulmonary Arterial Hypertension (PAH)** at rank 10. ISMN's NO-sGC-cGMP pathway directly overlaps with two approved PAH drug classes: sGC stimulators (riociguat) and PDE5 inhibitors (sildenafil, tadalafil, which maintain cGMP by blocking its degradation). A 2018 preclinical study (PMID 29705351) confirmed that NO/sGC pathway modulation reduces pulmonary artery pressure in monocrotaline-induced PAH rats. However, three substantial barriers limit ISMN's PAH utility: (1) **nitrate tolerance** develops within 24–48 hours of continuous use; (2) a **severe, potentially fatal drug interaction** with PDE5 inhibitors — the current PAH first-line agents — makes combination therapy unsafe; and (3) early clinical data in portal hypertension (PMID 2759546) suggested inconsistent haemodynamic responses across vascular beds, raising questions about pulmonary-specific efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for isosorbide mononitrate in hypertrichosis.

---

## Literature Evidence

Currently no related literature available directly linking isosorbide mononitrate to hypertrichosis.

---

### Supporting Literature: Pulmonary Arterial Hypertension (Rank 10 — Most Biologically Plausible Indication)

The following publications were retrieved for the PAH indication and are presented for reference, as PAH represents the only mechanistically grounded signal in this report.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [29377691](https://pubmed.ncbi.nlm.nih.gov/29377691/) | 2018 | Experimental (Medicinal Chemistry) | J Med Chem | ISMN–bardoxolone methyl hybrid (CDDO-NO) released NO in rat lungs and reduced mean pulmonary artery pressure and right ventricular systolic pressure — suggesting ISMN as a NO-donor scaffold for PAH drug design |
| [29705351](https://pubmed.ncbi.nlm.nih.gov/29705351/) | 2018 | Preclinical (Animal) | Life Sciences | Disruption of NO-sensitive sGC balance demonstrated in monocrotaline PAH rats; NO-enhancing agents restored sGC signalling and halted disease progression |
| [16422873](https://pubmed.ncbi.nlm.nih.gov/16422873/) | 2005 | Clinical Study (Crossover/RCT) | J Sex Med | Isosorbide mononitrate produced significant haemodynamic effects in men with coronary artery disease; critically highlighted severe hypotensive interaction with sildenafil — a key DDI concern in PAH patients |
| [2759546](https://pubmed.ncbi.nlm.nih.gov/2759546/) | 1989 | Clinical Study (RCT) | Hepatology | ISMN 20 mg reduced mean arterial and mean pulmonary arterial pressure in some but not all cirrhosis patients with portal hypertension; inconsistent response in pulmonary vasculature noted |
| [3384359](https://pubmed.ncbi.nlm.nih.gov/3384359/) | 1988 | Pharmacology Review | Gut | Mechanistic review of ISMN in portal hypertension — confirms NO-mediated reduction in vascular resistance; establishes pharmacological basis for vascular bed effects |
| [9673832](https://pubmed.ncbi.nlm.nih.gov/9673832/) | 1998 | Pharmacokinetics Review | Clin Pharmacokinet | Comprehensive PK profile of ISMN and other vasodilators — confirms oral bioavailability and systemic distribution relevant to pulmonary dosing considerations |

---

## Australia Market Information

Isosorbide mononitrate is currently **not registered on the Australian Register of Therapeutic Goods (ARTG)**. There are no ARTG entries for this drug. Any clinical use in Australia would require access through the TGA's **Special Access Scheme (SAS)** or **Authorised Prescriber (AP)** pathway. This absence from the ARTG is a material barrier to any repurposing programme within Australia and would necessitate a regulatory strategy prior to clinical investigation.

---

## Safety Considerations

No formal TGA Product Information or Drug Interaction data were available in this analysis. The following safety considerations are based on established pharmacological knowledge of ISMN as an organic nitrate:

- **Critical DDI — PDE5 inhibitors**: Concomitant use with sildenafil, tadalafil, or vardenafil is **contraindicated** due to the risk of severe, potentially life-threatening hypotension. This is directly relevant to PAH management, where PDE5 inhibitors are first-line therapy.
- **Nitrate tolerance (tachyphylaxis)**: Haemodynamic effects diminish within 24–48 hours of continuous exposure. Eccentric dosing schedules with nitrate-free intervals are required.
- **Hypotension**: Particularly in volume-depleted patients, the elderly, or those on concurrent antihypertensives.
- **Headache**: The most common adverse effect, due to cerebral vasodilation.

Please refer to the TGA-approved Product Information (PI) and Australian Prescriber resources for comprehensive safety information before considering any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (hypertrichosis, L5 evidence) has no clinical trials, no supporting literature, and no credible mechanistic link to ISMN's pharmacology. The same applies to ranks 2–9, which cluster around hair disorders and congenital structural anomalies — consistent with a knowledge graph node-proximity artefact rather than genuine drug-disease biology. With ISMN also absent from the ARTG, there is no pathway to clinical application in Australia without substantial further work.

**The only actionable signal in this report is Pulmonary Arterial Hypertension (rank 10):**
ISMN's NO/sGC/cGMP mechanism directly overlaps with approved PAH drug targets, and preliminary preclinical data support pulmonary vasodilation via this route. However, nitrate tolerance and the critical DDI with first-line PAH agents (PDE5 inhibitors) represent major barriers that must be resolved before this warrants clinical investigation.

**To progress further, the following would be required:**

1. **Safety data gap closure**: Obtain TGA PI equivalent documentation and perform a formal DDI assessment — particularly the ISMN × sildenafil/tadalafil interaction in the PAH context
2. **Nitrate tolerance mitigation strategy**: Evaluate intermittent or eccentric dosing regimens compatible with PAH management protocols
3. **PAH-specific preclinical programme**: Dedicated in vivo studies in established PAH models (e.g., monocrotaline, SU5416/hypoxia) using ISMN monotherapy
4. **Novel scaffold consideration**: The ISMN–bardoxolone methyl hybrid (PMID 29377691) showed dual vasodilation and vascular remodelling inhibition — this hybrid strategy may offer superior PAH efficacy and merit independent investigation
5. **ARTG registration pathway**: A full TGA registration strategy is required before any Australian clinical trial or therapeutic use can proceed
6. **Hypertrichosis predictions (ranks 1–9)**: No further investment recommended — reclassify as KG clustering noise pending contradictory mechanistic evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

