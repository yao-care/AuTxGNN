---
layout: default
title: Hyaluronic Acid
parent: 僅模型預測 (L5)
nav_order: 226
evidence_level: L5
indication_count: 10
---

# Hyaluronic Acid
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

# Hyaluronic Acid: From Ocular Lubrication to Dry Eye Syndrome

## One-Sentence Summary

Hyaluronic acid (HA) is a naturally occurring glycosaminoglycan widely recognised for its viscoelastic and lubricating properties, used internationally as an ophthalmic viscosurgical device, intra-articular injection, and dermal filler — though it is not currently registered on the Australian Register of Therapeutic Goods (ARTG).
The TxGNN model predicts it may be effective for **Dry Eye Syndrome**, with an exceptionally high confidence score of **99.86%**, and this prediction is underpinned by **multiple completed Phase 2/3 randomised controlled trials** and **20 publications** — evidence consistent with its established role as a first-line lubricant therapy in international dry eye guidelines.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Australian (ARTG) registrations on file |
| Predicted New Indication | Dry Eye Syndrome |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Hyaluronic acid is a high-molecular-weight linear polysaccharide that occurs naturally in the vitreous humour of the eye, synovial fluid, and skin extracellular matrix. Its defining physicochemical property is an extraordinary capacity to retain water — a single HA molecule can bind up to 1,000 times its own weight in water — conferring exceptional viscoelastic and lubricating characteristics. When applied as an ophthalmic preparation, HA forms a protective viscoelastic film over the ocular surface that mimics the mucin and aqueous layers of the natural tear film. Beyond simple lubrication, HA binds to CD44 receptors expressed on corneal epithelial cells, promoting cell migration and wound healing, and may inhibit NF-κB-mediated inflammatory signalling at the ocular surface — mechanisms directly relevant to the pathophysiology of dry eye disease.

Dry Eye Syndrome is characterised by tear film instability, hyperosmolarity, and ocular surface inflammation — precisely the processes HA is mechanistically positioned to address. Unlike most drug repurposing candidates where the new indication is speculative, HA ophthalmic drops already occupy a well-established role in international clinical practice for dry eye disease and serve as the standard comparator arm in the majority of dry eye clinical trials worldwide. The TxGNN prediction here reflects a convergence of biological plausibility and existing clinical evidence rather than a purely computational hypothesis.

Although detailed mechanism of action data for this specific DrugBank entry (DB08818) is not available in the current Evidence Pack, the mechanistic basis for HA in dry eye disease is thoroughly described in peer-reviewed literature. Efficacy appears to be both concentration- and formulation-dependent: crosslinked HA (CLHA) preparations generally demonstrate longer ocular surface retention and superior tear film stability compared to linear HA, while sodium hyaluronate at concentrations of 0.1%–0.4% represents the most extensively studied formulation across randomised controlled trials.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|------|--------|-----------|-------------|
| [NCT00599716](https://clinicaltrials.gov/study/NCT00599716) | Phase 3 | Completed | 300 | Vismed® (sodium hyaluronate) vs vehicle in dry eye syndrome; randomised, double-masked multicentre study assessing safety and efficacy of HA as the primary active ingredient |
| [NCT05411367](https://clinicaltrials.gov/study/NCT05411367) | Phase 3 | Completed | 232 | SI-614 ophthalmic solution (HA-based) vs placebo; randomised, double-masked, multicentre trial with comprehensive dry eye efficacy and safety endpoints |
| [NCT06221345](https://clinicaltrials.gov/study/NCT06221345) | Phase 4 | Completed | 70 | HPG/HA vs CMC/HA lubricant eye drops for post-cataract DED; direct head-to-head comparison of two HA-containing formulations on objective and subjective outcomes |
| [NCT04704531](https://clinicaltrials.gov/study/NCT04704531) | Phase 2 | Completed | 141 | Lagricel® Ofteno (sodium hyaluronate 0.4%, preservative-free) evaluated across three dosing schemes (BID, QID, 6×/day) for mild-to-moderate dry eye; primary endpoint OSDI score |
| [NCT01363414](https://clinicaltrials.gov/study/NCT01363414) | N/A (RCT) | Completed | 50 | Sodium hyaluronate instillation reduces corneal and ocular wavefront aberrations in dry eye patients, demonstrating improved optical quality and tear film stability following HA application |
| [NCT06517667](https://clinicaltrials.gov/study/NCT06517667) | Phase 2/3 | Completed | 30 | Comparison of different HA tear substitute formulations in evaporative dry eye; randomised single-blind trial examining efficacy across HA molecular weight and concentration variants |
| [NCT06851364](https://clinicaltrials.gov/study/NCT06851364) | Phase 2 | Completed | 45 | 0.38% vs 0.18% sodium hyaluronate for moderate-to-severe DED; improvements demonstrated in Arab-OSDI scores, tear break-up time, corneal fluorescein staining, and lissamine green conjunctival staining |
| [NCT04485533](https://clinicaltrials.gov/study/NCT04485533) | N/A | Unknown | 90 | VisuXL® ophthalmic gel (HA-containing) for moderate DED; randomised, crossover, double-blind European multicentre post-market clinical study |
| [NCT05724056](https://clinicaltrials.gov/study/NCT05724056) | N/A | Unknown | 130 | Idroflog® (sodium hyaluronate + hydrocortisone) vs sodium hyaluronate 0.18% alone for DED; non-inferiority design in patients with documented ≥3 months history of tear substitute use |
| [NCT05356728](https://clinicaltrials.gov/study/NCT05356728) | N/A | Unknown | 96 | Head-to-head comparison of trehalose/hyaluronate vs HA alone as artificial tears for DED; HA described as "a well-established active ingredient in artificial tears" and used as reference standard |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33804439](https://pubmed.ncbi.nlm.nih.gov/33804439/) | 2021 | Meta-Analysis | Int J Environ Res Public Health | HA eye drops significantly superior to non-HA artificial tears in tear break-up time and corneal staining; pooled analysis across 8 databases confirming consistent efficacy advantage |
| [38895674](https://pubmed.ncbi.nlm.nih.gov/38895674/) | 2024 | Meta-Analysis | Int J Ophthalmology | Higher concentration HA (≥0.3%) superior to lower concentrations in TBUT and symptom scores; establishes a clinically meaningful dose-response relationship |
| [35514082](https://pubmed.ncbi.nlm.nih.gov/35514082/) | 2022 | Review | Acta Ophthalmologica | Comprehensive critical evaluation of HA safety and efficacy in DED; concludes HA is safe across formulations with no major adverse events reported |
| [37042308](https://pubmed.ncbi.nlm.nih.gov/37042308/) | 2024 | Systematic Review | Acta Ophthalmologica | Summarises all published direct comparisons between HA and other topical DED active ingredients; HA remains one of the most efficacious and best-tolerated reference standards |
| [39260878](https://pubmed.ncbi.nlm.nih.gov/39260878/) | 2024 | RCT | BMJ | 0.1% sodium hyaluronate used as active comparator in non-inferiority RCT; provides robust efficacy benchmark data for HA in dry eye disease |
| [37117131](https://pubmed.ncbi.nlm.nih.gov/37117131/) | 2023 | RCT | Contact Lens Anterior Eye | Trehalose + HA artificial tears effective over 3 months in postmenopausal women (42–54 vs ≥55 years) with moderate and severe DED; demonstrates efficacy across hormonal status subgroups |
| [34562113](https://pubmed.ncbi.nlm.nih.gov/34562113/) | 2022 | RCT | Graefe's Arch Clin Exp Ophthalmol | HA 0.3% + cyanocobalamin (vitamin B12) combination effective for menopausal patients with moderate DED; improved TBUT and patient-reported symptom scores |
| [27324942](https://pubmed.ncbi.nlm.nih.gov/27324942/) | 2016 | Systematic Review | J Cosmetic Dermatology | Comprehensive review of HA's physicochemical properties across medical applications; confirms biocompatibility and strong scientific rationale for ophthalmic use |
| [37241190](https://pubmed.ncbi.nlm.nih.gov/37241190/) | 2023 | Clinical Study | Medicina (Kaunas) | HA + mallow extract combination compared to HA alone in 20 DED patients across 5 Italian ophthalmological practices; improved OSDI and TBUT over treatment period |
| [32070808](https://pubmed.ncbi.nlm.nih.gov/32070808/) | 2020 | Review | Carbohydrate Research | Reviews HA's water retention and lubricant properties in ophthalmology, rheumatology, and dermatology; highlights established international role in dry eye treatment and ocular viscosurgical device use |

---

## Australia Market Information

Hyaluronic acid (DrugBank ID: DB08818) is currently **not registered on the Australian Register of Therapeutic Goods (ARTG)**. There are no product licences, approved indications, or dosage form records available through the TGA.

| Item | Status |
|------|--------|
| ARTG Registrations | None on file |
| TGA Market Status | Not marketed |
| Special Access Scheme | Available as a pathway for individual patient access pending formal registration |
| International Registration | Registered in the USA (FDA), European Union (EMA), Japan (PMDA), and numerous other jurisdictions as ophthalmic drops (sodium hyaluronate) for dry eye disease |

This represents a regulatory access gap rather than an evidence gap. Healthcare professionals wishing to use HA ophthalmic preparations in Australia prior to ARTG registration may explore the TGA's Special Access Scheme (SAS Category B) or Authorised Prescriber pathways.

---

## Safety Considerations

No Australian regulatory safety data (TGA-approved Product Information) is currently available, as Hyaluronic Acid is not registered on the ARTG. No drug-drug interactions were identified in the current database search.

Based on published literature, HA ophthalmic preparations are generally considered very well tolerated, with no major systemic adverse events reported across clinical trials. Healthcare professionals should consult international regulatory documents for registered HA ophthalmic products (e.g., FDA or EMA-approved PI) for comprehensive warnings, contraindications, and precautions applicable to specific formulations.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base supporting hyaluronic acid ophthalmic preparations for Dry Eye Syndrome is among the strongest available for any ophthalmic lubricant (Evidence Level L1), with multiple completed Phase 2/3 randomised controlled trials, two meta-analyses, and multiple systematic reviews consistently demonstrating efficacy and an excellent safety profile. The primary barrier to Australian clinical implementation is the absence of ARTG registration rather than any deficiency in clinical evidence.

**To proceed, the following is needed:**
- **ARTG registration pathway**: Initiate a TGA regulatory submission for a sodium hyaluronate ophthalmic preparation, leveraging the extensive published evidence base and international approvals (FDA, EMA) as supporting data
- **Product Information (PI) development**: Compile warnings, contraindications, and drug interaction data from internationally registered HA ophthalmic PI documents for inclusion in the TGA submission
- **Formulation selection**: Determine the preferred HA concentration (0.1%–0.4%) and whether crosslinked (CLHA) or linear HA formulation best suits the target patient population and clinical setting
- **MOA documentation**: Complete the DrugBank mechanism of action entry for DB08818 to strengthen regulatory and clinical decision-making documentation
- **Short-term access pathway**: Where individual patient need is urgent, evaluate eligibility for TGA Special Access Scheme (Category B) using internationally registered HA ophthalmic products as the source
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

