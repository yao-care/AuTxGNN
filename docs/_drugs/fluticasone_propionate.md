---
layout: default
title: Fluticasone Propionate
parent: Model Prediction Only (L5)
nav_order: 311
evidence_level: L5
indication_count: 10
---

# Fluticasone Propionate
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

# Fluticasone Propionate: From Allergic and Inflammatory Conditions to Atopic Dermatitis

## One-Sentence Summary

Fluticasone propionate is a corticosteroid originally used for allergic and inflammatory conditions such as allergic rhinitis, asthma, atopic eczema and contact dermatitis.
The TxGNN model's top-ranked prediction is **2-hydroxyethyl methacrylate sensitization** (no supporting studies). The best-evidenced prediction is **atopic dermatitis**, with **5 clinical trials** and **20 publications**. However, atopic dermatitis is already an established use of this drug, so it confirms existing use rather than a new repurposing opportunity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic and inflammatory conditions (atopic eczema, contact dermatitis, allergic rhinitis, asthma, seborrheic dermatitis and others); the Australian licence record contains no indication text |
| Predicted New Indication | 2-hydroxyethyl methacrylate sensitization (rank 1). The best-evidenced prediction is atopic dermatitis (rank 7), which is already an original indication |
| TxGNN Prediction Score | 98.56% (rank 1); 95.32% for atopic dermatitis |
| Evidence Level | L5 for the rank 1 prediction; L1 for atopic dermatitis (per the supplied scoring, although the trials listed are Phase 4, Phase 2 or not applicable) |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold for the rank 1 prediction; Proceed with Guardrails for atopic dermatitis (existing use) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fluticasone propionate is a synthetic corticosteroid. Pharmacology records show it binds the glucocorticoid receptor (NR3C1), the mineralocorticoid receptor (NR3C2) and the progesterone receptor (PGR). Glucocorticoid receptor activation suppresses inflammatory cytokine signalling and T-cell activation.

For the rank 1 prediction, allergic contact sensitisation to 2-hydroxyethyl methacrylate is a T-cell mediated type IV hypersensitivity. Topical corticosteroids are an established treatment for allergic contact dermatitis, which is already an original indication. The class-level link is plausible, but no trial or publication specific to this drug and this condition was found. The high score is a model prediction only.

Several other top predictions have weak mechanistic support:
- **Alopecia areata** (rank 5): plausible, since it is autoimmune and corticosteroids are used clinically, but no drug-specific evidence was supplied.
- **Alopecia mucinosa** (rank 3): plausible as an inflammatory dermatosis, but no evidence was supplied.
- **Vulvar inverted follicular keratosis, telogen effluvium, vocal cord polyp and hereditary hypotrichosis** (ranks 2, 4, 8, 9): little mechanistic rationale for a corticosteroid.
- **Folliculitis decalvans** (rank 6): corticosteroids may reduce inflammation but do not address the infectious driver.
- **Polyp of middle ear** (rank 10): supported only indirectly by nasal polyp studies.

The detailed evidence below covers atopic dermatitis, the only prediction with substantial data.

## Clinical Trial Evidence

Evidence for atopic dermatitis (rank 7). No clinical trials were registered for the rank 1 prediction.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT01915914](https://clinicaltrials.gov/study/NCT01915914) | Phase 4 | Completed | 107 | Randomised, open-label study of twice-weekly fluticasone 0.05% cream plus daily moisturiser to reduce relapse in children with stabilised atopic dermatitis |
| [NCT00546000](https://clinicaltrials.gov/study/NCT00546000) | Phase 4 | Completed | 56 | Open-label study of Cutivate (fluticasone) 0.05% lotion and its effect on the HPA axis in infants with atopic dermatitis |
| [NCT00616538](https://clinicaltrials.gov/study/NCT00616538) | Phase 4 | Completed | 121 | Investigator-blind pilot comparing a ceramide barrier cream with mid-strength topical steroid (fluticasone 0.05%) in children; fluticasone is likely the comparator |
| [NCT07537751](https://clinicaltrials.gov/study/NCT07537751) | Not applicable | Completed | 40 | Double-blind comparison of crisaborole 2% versus fluticasone 0.05% in children aged 1-12 years with mild to moderate disease; fluticasone is the comparator |
| [NCT03742414](https://clinicaltrials.gov/study/NCT03742414) | Phase 2 | Active, not recruiting | 398 | SEAL study of proactive skin care, including fluticasone cream, to prevent the allergic march; fluticasone is not the primary agent |

## Literature Evidence

Selected from the atopic dermatitis publications, plus the two nasal polyp papers retrieved for polyp of middle ear. No literature was available for the rank 1 prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27543211](https://pubmed.ncbi.nlm.nih.gov/27543211/) | 2016 | RCT | J Am Acad Dermatol | Effects of fluticasone cream and adjunctive bleach baths on the skin microbiome in childhood atopic dermatitis |
| [14522623](https://pubmed.ncbi.nlm.nih.gov/14522623/) | 2003 | Double-blind comparative studies | J Dermatol Treat | Two multicentre studies of fluticasone 0.05% cream for acute and maintenance treatment in children aged 2-14 years |
| [9704834](https://pubmed.ncbi.nlm.nih.gov/9704834/) | 1998 | Comparative study | J Am Acad Dermatol | Once-daily fluticasone 0.05% cream versus twice-daily clobetasone butyrate in children |
| [12207596](https://pubmed.ncbi.nlm.nih.gov/12207596/) | 2002 | Clinical study | Br J Dermatol | Intermittent dosing of fluticasone cream to reduce relapse risk |
| [18298423](https://pubmed.ncbi.nlm.nih.gov/18298423/) | 2009 | Clinical study | Pediatr Allergy Immunol | Twice-weekly maintenance with fluticasone 0.005% ointment in 90 children after 4 weeks of acute treatment |
| [11862174](https://pubmed.ncbi.nlm.nih.gov/11862174/) | 2002 | Clinical safety study | J Am Acad Dermatol | Safety of fluticasone 0.05% cream in severe, extensive disease in children as young as 3 months |
| [21977914](https://pubmed.ncbi.nlm.nih.gov/21977914/) | 2012 | Review | J Eur Acad Dermatol Venereol | Fluticasone as intervention and maintenance therapy, supported by a high therapeutic index |
| [15608497](https://pubmed.ncbi.nlm.nih.gov/15608497/) | 2005 | Review | Skin Pharmacol Physiol | Safety and efficacy of topical fluticasone in skin diseases |
| [9604976](https://pubmed.ncbi.nlm.nih.gov/9604976/) | 1998 | Clinical study (nasal polyposis) | Arch Otolaryngol Head Neck Surg | Effect of intranasal fluticasone in severe nasal polyposis (indirect evidence for middle ear polyp) |
| [11447383](https://pubmed.ncbi.nlm.nih.gov/11447383/) | 2001 | Mechanistic/cohort | J Allergy Clin Immunol | Glucocorticoid receptor beta expression in nasal polyp cells and its link to intranasal fluticasone's anti-inflammatory effect |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| ARTG 14347D | Flixotide | Pressurised inhalation, fluticasone propionate 125 micrograms per dose, 120 doses (CFC-free formulation) | Not recorded in the data compiled for this report |

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text):** The TxGNN knowledge graph links fluticasone propionate with the following conditions. These are associations only and should be checked against the Product Information:
  - Cardiovascular: hypertension, long QT syndrome (including the familial form)
  - Other systemic: epilepsy, liver disease, gallbladder disease, hyperglycaemia
  - Infection-related: measles, herpes simplex virus keratitis
  - Pituitary and endocrine: hypopituitarism, pituitary hormone deficiencies (including Sheehan syndrome), growth hormone deficiency, hypogonadotropic hypogonadism and Kallmann syndrome
- **Drug interactions:** No drug-drug interaction records were returned. The pharmacology records show binding to the glucocorticoid, mineralocorticoid and progesterone receptors.
- **Guardrails from the atopic dermatitis evidence:** Monitor for HPA axis suppression and skin atrophy with extensive or prolonged use, particularly in children. Use intermittent or maintenance regimens as studied.

Please refer to the TGA-approved Product Information (PI) for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold (rank 1 prediction, 2-hydroxyethyl methacrylate sensitization); Proceed with Guardrails (atopic dermatitis, existing use)**

**Rationale:**
- The rank 1 prediction has no trials or literature (L5), so the 98.56% score is a model output only. The mechanistic link through allergic contact dermatitis is plausible but unproven for this drug.
- Atopic dermatitis is already an original indication with consistent clinical support, so it confirms current use rather than a new repurposing opportunity.
- The only Australian licence, Flixotide, is an inhaled product. No topical dermatological or nasal product appears in the data compiled for this report.

**To proceed, the following is needed:**
- Product Information warnings and contraindications for the Australian product (a blocking data gap)
- Mechanism of action data from DrugBank
- Drug-specific studies for contact sensitisation to 2-hydroxyethyl methacrylate, such as patch-test or small controlled studies
- Route compatibility assessment, because the Australian product is inhaled while the predicted skin indications need topical formulations
- Review of the dermatology-focused predictions (alopecia areata, alopecia mucinosa) for literature and trial evidence before any further assessment
- Confirmation of which topical fluticasone products are registered in Australia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

