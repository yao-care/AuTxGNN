---
layout: default
title: Cyproterone Acetate
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 10
---

# Cyproterone Acetate
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

# Cyproterone Acetate: From Hyperandrogenism to Migraine Disorder

## One-Sentence Summary

Cyproterone acetate (CPA) is a synthetic steroidal anti-androgen and progestogen, widely used internationally for hyperandrogenism-related conditions such as hirsutism, acne, and polycystic ovary syndrome (PCOS), as well as high-dose androgen deprivation therapy in prostate cancer.
The TxGNN model predicts it may be effective for **Migraine Disorder** as its highest-ranked new indication (score 99.66%), though this is supported by **0 clinical trials and 0 publications**.
Across all 10 predicted indications in this evidence pack, only **amenorrhea (rank 8)** reaches clinically meaningful evidence (L3: 4 clinical trials, 14 publications); critically, multiple thrombosis-related predictions carry explicit **safety contraindications** that require immediate attention.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperandrogenism-related conditions (hirsutism, acne, PCOS); high-dose androgen deprivation in prostate cancer — based on international pharmacological profile; no TGA-approved indication on record |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature for this indication) |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Hold (for migraine) / **Proceed with Guardrails** (for amenorrhea — see below) |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this evidence pack. Based on established pharmacology, cyproterone acetate is a synthetic steroid that acts as a competitive antagonist at androgen receptors while also exerting potent progestogenic effects. At low doses (2 mg, as in Diane-35), it suppresses adrenal and ovarian androgen production; at high doses (100–300 mg), it additionally suppresses gonadotrophins (LH and FSH), resulting in marked reductions in circulating testosterone.

The proposed biological link to migraine rests on the well-established relationship between sex hormone fluctuations and migraine pathophysiology, particularly catamenial (menstrual) migraine. Oestrogen and progesterone both modulate the trigeminal vascular system, and luteal-phase progesterone withdrawal is a recognised trigger for menstrual migraine attacks. CPA's progestogenic activity could theoretically stabilise endogenous hormonal oscillations, potentially reducing this trigger.

However, this remains a speculative inference. The TxGNN model's high score (99.66%) most likely reflects knowledge graph co-occurrence between CPA and hormonal migraine pathways, rather than direct evidence of clinical benefit. No published study has specifically tested CPA as a migraine prophylactic or treatment agent, and the mechanistic hypothesis has not been experimentally validated.

---

## All Predicted Indications — Overview

This evidence pack covers 10 predicted indications. The complete picture is essential for clinical decision-making:

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Key Note |
|------|---------|-------------|----------------|----------|----------|
| 1 | Migraine disorder | 99.66% | L5 | Hold | No clinical or literature evidence |
| 2 | Migraine with brainstem aura | 99.58% | L5 | Hold | No evidence; mechanistic link to posterior circulation is very weak |
| 3 | Prinzmetal angina | 99.52% | L5 | Hold | ⚠️ CPA's prothrombotic effect may worsen coronary vasospasm events |
| 4 | Antithrombin deficiency type 2 | 99.48% | L5 | Hold | ⛔ CONTRAINDICATION: CPA increases VTE risk in inherited thrombophilia |
| 5 | Heparin cofactor 2 deficiency | 99.45% | L5 | Hold | ⛔ CONTRAINDICATION: CPA worsens coagulation imbalance |
| 6 | Factor V excess with spontaneous thrombosis | 99.45% | L5 | Hold | ⛔ CONTRAINDICATION: CPA + Factor V Leiden = synergistic VTE risk (PMID 29614525) |
| 7 | Migraine susceptibility (with/without aura) | 99.34% | L5 | Hold | 20 publications retrieved — all are epilepsy genetics papers with no CPA relevance |
| 8 | Amenorrhea | 99.28% | L3 | Proceed with Guardrails | Best evidence: 4 clinical trials + 14 publications; mechanistic basis well-established |
| 9 | Breast fibrocystic disease | 99.15% | L4 | Research Question | 4 publications; preclinical hypothesis only; dual hormonal effects uncertain |
| 10 | Thrombophilia | 99.03% | L4 | Hold | ⛔ REVERSE CAUSATION: 18 publications all document CPA as a VTE risk factor, not a treatment |

---

## Clinical Trial Evidence

### Migraine Disorder (Rank 1 — Top Prediction)

Currently no related clinical trials registered.

---

### Amenorrhea (Rank 8 — Best-Evidenced Prediction)

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT01103518](https://clinicaltrials.gov/study/NCT01103518) | Phase 4 | Unknown | 100 | Randomised, double-blind comparison of two EE + CPA formulations for menstrual irregularities of hyperandrogenic origin; most directly relevant CPA clinical trial for this indication |
| [NCT04831151](https://clinicaltrials.gov/study/NCT04831151) | N/A | Unknown | 42 | Comparison of CPA-containing vs drospirenone-containing combined OCP on blood metabolomics in PCOS women; provides direct pharmacological CPA data in an amenorrhoea-related population |
| [NCT02729545](https://clinicaltrials.gov/study/NCT02729545) | Phase 2 | Completed | 60 | Tung's acupuncture vs Diane-35 (CPA 2 mg/EE 35 mcg) as active comparator for improving ovarian function in PCOS; CPA arm provides real-world outcomes data |
| [NCT02744131](https://clinicaltrials.gov/study/NCT02744131) | N/A | Unknown | 100 | EE + CPA (OCP) vs Metformin for clinical, hormonal, and metabolic features of PCOS in Indian women; includes amenorrhoea management as a secondary endpoint |

---

## Literature Evidence

### Migraine Disorder (Rank 1 — Top Prediction)

Currently no related literature directly evaluating CPA for migraine treatment is available.

---

### Amenorrhea (Rank 8 — Best-Evidenced Prediction)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2946604](https://pubmed.ncbi.nlm.nih.gov/2946604/) | 1986 | Multicentre Trial | Fertility and Sterility | CPA (Diane 2 mg vs Androcur 100 mg) in 158 patients with severe hirsutism; characterises dose-dependent anti-androgen profile directly relevant to PCOS-related amenorrhoea management |
| [9130733](https://pubmed.ncbi.nlm.nih.gov/9130733/) | 1997 | Clinical Study | Human Reproduction | GnRH agonist + EE/CPA pill vs EE/CPA alone in 12 patients with PCOS-related hyperandrogenism; demonstrates hormonal efficacy of the EE/CPA combination in regulating gonadotrophin axis |
| [2528199](https://pubmed.ncbi.nlm.nih.gov/2528199/) | 1989 | Review | Revue Française de Gynécologie | CPA described as the most effective anti-androgen available; importantly notes co-prescription of oestrogen is necessary to prevent CPA-induced amenorrhoea — mechanistically central to this indication |
| [6232474](https://pubmed.ncbi.nlm.nih.gov/6232474/) | 1984 | Review | Obstetrics and Gynecology Annual | Early foundational review of polycystic ovarian disease, contextualising hormonal treatment rationale for CPA |
| [17162716](https://pubmed.ncbi.nlm.nih.gov/17162716/) | 2006 | Case Report | Gynecological Endocrinology | Recurrent catamenial pneumothorax managed with deliberate therapeutic amenorrhoea using hormonal treatment including CPA; demonstrates CPA's capacity to suppress the hypothalamic-pituitary-ovarian axis |
| [1589384](https://pubmed.ncbi.nlm.nih.gov/1589384/) | 1992 | Case Report | Postgraduate Medical Journal | Bilateral adrenocortical adenomas with polycystic ovaries in a young woman treated with CPA + EE for secondary amenorrhoea and hirsutism over 3 years; direct clinical application |
| [2137793](https://pubmed.ncbi.nlm.nih.gov/2137793/) | 1990 | Case Series | Fertility and Sterility | Familial virilisation with insulin resistance, amenorrhoea, and hirsutism treated with GnRH agonist + anti-androgen (CPA); combination reversed hirsutism while preserving fertility potential |
| [35592826](https://pubmed.ncbi.nlm.nih.gov/35592826/) | 2022 | Case Report | Annals of Medicine and Surgery | Congenital adrenal hyperplasia (21-hydroxylase deficiency) presenting with virilisation in adolescence; contextualises the hyperandrogenism–amenorrhoea pathophysiological link relevant to CPA's mechanism |

---

## Australia Market Information

Cyproterone acetate is **not currently registered on the Australian Register of Therapeutic Goods (ARTG)**. There are no active ARTG entries as of the data cutoff (4 April 2026).

> **Access pathway for Australian prescribers**: CPA is available internationally (e.g., Diane-35 in the UK, EU, Taiwan; Androcur in Europe for prostate cancer). Australian clinicians wishing to prescribe CPA would need to access it via the **TGA Special Access Scheme (SAS Category B or C)** or apply for **Authorised Prescriber** status. Given CPA's established international use for hyperandrogenism, SAS access for individual patients with PCOS-related amenorrhoea is feasible pending appropriate clinical justification and TGA submission.

---

## Safety Considerations

### ⛔ Critical Safety Finding — Prothrombotic Risk (Affects Multiple Predicted Indications)

The most clinically important finding in this evidence pack is that **four of the ten TxGNN-predicted indications are clinical contraindications to CPA**, not therapeutic opportunities. The underlying issue is CPA's well-characterised prothrombotic effect:

- CPA reduces protein S levels and increases thrombin generation, as measured by calibrated automated thrombography (PMID [15550051](https://pubmed.ncbi.nlm.nih.gov/15550051/); PMID [18064335](https://pubmed.ncbi.nlm.nih.gov/18064335/))
- CPA combined with Factor V Leiden mutation carries markedly elevated VTE risk — a synergistic interaction confirmed in two independent genetic epidemiology studies (PMID [29614525](https://pubmed.ncbi.nlm.nih.gov/29614525/); PMID [32342502](https://pubmed.ncbi.nlm.nih.gov/32342502/))
- French pharmacoepidemiological data (30 public hospitals) confirm elevated thromboembolic event rates in CPA users (PMID [24634164](https://pubmed.ncbi.nlm.nih.gov/24634164/))
- Upper extremity DVT (jugular to elbow) has been reported in CPA/EE users with co-existing thrombophilic mutations (PMID [19340712](https://pubmed.ncbi.nlm.nih.gov/19340712/))
- Cerebral venous sinus thrombosis has been reported in combined OCP users (PMID [40704263](https://pubmed.ncbi.nlm.nih.gov/40704263/))

**Predicted indications that represent explicit clinical contraindications for CPA:**

| Predicted Indication | Rank | Reason CPA is Contraindicated |
|---------------------|------|-------------------------------|
| Antithrombin deficiency type 2 | 4 | High baseline VTE risk; CPA further impairs anticoagulant pathways |
| Heparin cofactor 2 deficiency | 5 | Rare inherited thrombophilia; CPA directly worsens coagulation imbalance |
| Factor V excess with spontaneous thrombosis | 6 | CPA + Factor V Leiden = synergistic VTE risk (OR significantly elevated) |
| Thrombophilia (general) | 10 | All 18 retrieved publications document CPA as a VTE risk factor — not a treatment |

> **Model interpretation note**: TxGNN's high scores for these thrombosis-related conditions are most likely an artefact of knowledge graph co-occurrence — CPA appears frequently in thrombosis literature *as a risk factor*, not as a treatment. This is a clear example of reverse causation that graph-based models can misinterpret as therapeutic association. Human expert review is essential before acting on any CPA-thrombosis prediction.

### Key Warnings

Please refer to the TGA-approved Product Information (PI) or the applicable international prescribing information (EMA EPAR for Diane-35 / Androcur; MHRA SPC) for the full list of warnings and precautions. Specific warning data was not available in this evidence pack.

Key known warnings from published evidence:

- **Venous thromboembolism**: Avoid in patients with current or prior VTE, known thrombophilia, Factor V Leiden, or protein S/C deficiency
- **Hepatotoxicity**: High-dose CPA (≥ 100 mg/day) is associated with hepatotoxicity including rare fatal cases; liver function monitoring required
- **Cardiovascular risk**: Increased risk of cerebrovascular events, particularly with migraine with aura — note the irony that CPA is predicted for migraine but may aggravate migraine-associated stroke risk
- **Depression and mood disorders**: CPA has been associated with depressive symptoms and suicidality, particularly in gender-affirming care contexts
- **Adrenal suppression**: High-dose CPA suppresses adrenal cortex function; abrupt discontinuation can precipitate adrenal insufficiency

---

## Conclusion and Next Steps

### Migraine Disorder (Rank 1)

**Decision: Hold**

**Rationale:**
The top TxGNN-predicted indication has no supporting clinical or literature evidence (L5), and while the mechanistic hypothesis around hormonal migraine modulation is biologically plausible, it is entirely unvalidated. CPA is not TGA-registered, and its prothrombotic risk profile raises additional safety concerns for patients with migraine with aura (who are already at elevated stroke risk with combined hormonal therapy).

**To proceed, the following is needed:**
- Proof-of-concept study investigating CPA's effect on catamenial migraine frequency and severity
- Clarification of mechanistic pathway linking CPA's progestogenic activity to trigeminal vascular suppression
- Prospective safety data specifically addressing stroke risk in migraine patients on CPA

---

### Amenorrhea (Rank 8)

**Decision: Proceed with Guardrails**

**Rationale:**
The amenorrhea indication has the strongest evidence in this pack (L3): one Phase 4 RCT (NCT01103518), additional interventional trials, and 14 supporting publications. CPA's mechanism (anti-androgen + progestogen) is well-suited to PCOS-related amenorrhoea and hyperandrogenic menstrual dysfunction. The EE/CPA combination (Diane-35) is an established therapy internationally for this indication.

**To proceed, the following is needed:**
- **TGA access**: Establish SAS Category B or Authorised Prescriber arrangement; assess feasibility of formal ARTG registration application
- **Mandatory pre-prescribing screen**: Thrombophilia workup (personal/family VTE history, Factor V Leiden, prothrombin G20210A, protein S/C, antithrombin); absolute contraindication if positive
- **Complete MOA documentation**: Obtain from DrugBank API or primary pharmacology literature (currently listed as data gap)
- **Full safety profile**: Source EMA or MHRA product information for CPA as proxy for TGA prescribing guidance
- **Monitoring plan**: Baseline liver function tests (LFTs), SHBG (as surrogate thrombotic risk marker), blood pressure, and FBC at baseline and 3-monthly intervals
- **Patient selection**: Avoid in smokers over 35, women with history of cardiovascular or cerebrovascular disease, or those with migraine with aura

---

> ⚕️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require rigorous clinical validation before therapeutic application. All prescribing decisions must be made by qualified healthcare professionals in accordance with Australian regulatory requirements and TGA guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

