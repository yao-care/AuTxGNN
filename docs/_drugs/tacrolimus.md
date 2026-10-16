---
layout: default
title: Tacrolimus
parent: Model Prediction Only (L5)
nav_order: 695
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Tacrolimus: predicted new indication Seborrheic dermatitis (evidence level L5). Approved use: Atopic eczema / atopic dermatitis"
monitor_inn: "Tacrolimus"
predicted_indications: ["seborrheic dermatitis", "parapsoriasis", "dermatitis", "acute lichenoid pityriasis", "acrodermatitis chronica atrophicans", "rheumatoid arthritis", "acne keloid", "psoriasis", "neonatal dermatomyositis", "exanthem (disease)"]
---

# Tacrolimus
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

# Tacrolimus: From Atopic Eczema to Seborrheic Dermatitis

## One-Sentence Summary

Tacrolimus is a calcineurin inhibitor originally used to treat atopic eczema (atopic dermatitis).
The TxGNN model predicts it may be effective for **seborrheic dermatitis**,
with **2 directly relevant clinical trials** (one Phase 3 and one Phase 4, both completed) and a body of published literature, including a clinical study of maintenance therapy, supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic eczema / atopic dermatitis (source: TxGNN knowledge graph; the ARTG entry in the data compiled has no indication text) |
| Predicted New Indication | Seborrheic dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 (as scored in the data compiled; see note below) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* Strictly applying the grading rules, the seborrheic dermatitis evidence comprises one completed Phase 3 trial and one completed Phase 4 study, with no results summarised in the data. That is closer to L2 than to L1 (which needs at least two completed Phase 3 RCTs). The L1 grade comes from the scoring in the data compiled and should be confirmed.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled. Based on known pharmacology, tacrolimus inhibits calcineurin, which blocks NFAT-dependent T-cell activation and the release of pro-inflammatory cytokines. This is the mechanism behind its established use in atopic dermatitis.

Seborrheic dermatitis is a chronic, relapsing inflammatory skin disease affecting the face and scalp, and it involves an inflammatory response to *Malassezia* yeast. Atopic dermatitis and seborrheic dermatitis are both inflammatory dermatoses, so topical calcineurin inhibition is plausibly relevant. Published reviews describe topical calcineurin inhibitors as a steroid-sparing option for seborrheic dermatitis, since long-term corticosteroid use on the face carries adverse effects.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Tacrolimus ointment (Protopic) as maintenance treatment of severe seborrheic dermatitis on the adult face, aiming to reduce relapses and topical steroid use. Results not provided in the data compiled. |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Proactive once- or twice-weekly 0.1% tacrolimus ointment to keep adult facial seborrheic dermatitis in remission and reduce exacerbations. Results not provided in the data compiled. |

No ANZCTR identifiers were available in the data compiled.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic review | Am J Clin Dermatol | Reviews topical treatments for facial seborrheic dermatitis; topical therapy is the first line of treatment. |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Clinical study | Ann Dermatol | Maintenance therapy of facial seborrheic dermatitis with 0.1% tacrolimus ointment. |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Systematic review / network meta-analysis | Clin Exp Allergy | Cochrane review of topical anti-inflammatory treatments for eczema. |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Topical calcineurin inhibitors as a safe alternative for seborrheic dermatitis, since corticosteroids have limited long-term use. |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | Clinical trial | Ann Parasitol | Compared sertaconazole 2% cream with tacrolimus 0.03% cream in 60 patients with seborrheic dermatitis. |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Review | J Drugs Dermatol | Current status and therapeutic horizons for facial seborrheic dermatitis. |
| [31476936](https://pubmed.ncbi.nlm.nih.gov/31476936/) | 2019 | Review | J Cutan Med Surg | Off-label use of topical calcineurin inhibitors in dermatologic disorders. |
| [15461548](https://pubmed.ncbi.nlm.nih.gov/15461548/) | 2004 | Review | Expert Opin Pharmacother | Topical tacrolimus in atopic dermatitis and other inflammatory skin diseases. |
| [11770914](https://pubmed.ncbi.nlm.nih.gov/11770914/) | 2001 | Review | Semin Cutan Med Surg | Topical immunomodulators in psoriasis, seborrheic dermatitis, lichen planus and other conditions. |
| [20347654](https://pubmed.ncbi.nlm.nih.gov/20347654/) | 2010 | Review | Clin Dermatol | Tinea incognito can follow topical tacrolimus use and can mimic seborrheic dermatitis, so diagnosis may be delayed. |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 10859M | Tacrolimus Sandoz | Capsule 0.75 mg (oral) | Not stated in the data compiled |

The only registered product in the data compiled is an oral capsule. No topical tacrolimus product is listed, whereas the seborrheic dermatitis evidence relates to topical ointment. Availability of a suitable topical formulation in Australia should be confirmed.

## Safety Considerations

- **Contraindications (knowledge graph associations, not label text):** The TxGNN knowledge graph links tacrolimus with conditions including hypertension, long QT syndrome and torsades de pointes, liver failure, kidney disease, epilepsy, hyperglycaemia and diabetes mellitus, serious infections (including herpes simplex, herpes zoster, infectious mononucleosis and progressive multifocal leukoencephalopathy), and cancers (including lymphoma). These relate mainly to systemic use and should be checked against the TGA-approved Product Information.
- **Drug Interactions:** 100 interactions were identified. Major-level interactions in the list reviewed include amphotericin B (including the lipid complex), loperamide, mesalazine, omeprazole and balsalazide. Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), famotidine, rabeprazole, metformin, pioglitazone, aprepitant and metronidazole.
- **Cancer risk:** A 2023 systematic review and meta-analysis (PMID 36370744) examined cancer risk with topical calcineurin inhibitors in atopic dermatitis. Long-term topical use carries a boxed warning in other jurisdictions.
- **Diagnostic caution:** Topical immunomodulators can modify the appearance of fungal skin infection (tinea incognito), so infection should be excluded before treating a suspected seborrheic dermatitis.

Please refer to the TGA-approved Product Information (PI) for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is plausible, and a completed Phase 3 trial and a completed Phase 4 study evaluate tacrolimus ointment specifically in seborrheic dermatitis, supported by a published maintenance-therapy study and reviews. However, results of the registered trials are not summarised in the data compiled, and the only Australian product listed is an oral capsule.

**To proceed, the following is needed:**
- Results of NCT02004860 and NCT01591070 (efficacy, relapse rates, safety)
- Confirmation of an available topical tacrolimus product and its TGA-approved indications
- Mechanism of action data and package insert warnings and contraindications from the TGA Product Information
- A long-term safety and malignancy monitoring plan, with infection excluded before treatment
- Confirmation of the evidence level (L1 as scored versus L2 on strict application of the rules)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

