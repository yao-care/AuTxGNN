---
layout: default
title: Sulfasalazine
parent: Model Prediction Only (L5)
nav_order: 691
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-13
description: "Sulfasalazine: predicted new indication Brachydactyly-syndactyly syndrome (evidence level L5). Approved use: Rheumatoid arthritis, ulcerative colitis, inflammatory bowel disease…"
monitor_inn: "Sulfasalazine"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "osteoarthritis susceptibility", "congenital hypotrichosis with juvenile macular dystrophy", "osteoarthritis", "WHIM syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis"]
---

# Sulfasalazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Sulfasalazine: From Rheumatoid Arthritis and Inflammatory Bowel Disease to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Sulfasalazine is an anti-inflammatory drug originally used for rheumatoid arthritis, ulcerative colitis and other inflammatory bowel and joint diseases.
The TxGNN model gives its highest-ranked prediction as **brachydactyly-syndactyly syndrome**, a rare congenital limb malformation, but there are **no clinical trials and no publications** supporting this prediction.
It is a purely computational result, and the most biologically plausible candidate in the top 10 is **osteoarthritis**, supported only by preclinical data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, ulcerative colitis, inflammatory bowel disease, juvenile idiopathic arthritis, spondyloarthropathy (the ARTG entry lists no approved indication text) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Australia Market Status | Marketed |
| Number of ARTG Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Sulfasalazine is known to have anti-inflammatory activity, and the compiled preclinical literature points to inhibition of NF-kB signalling and of the cystine/glutamate antiporter (xCT).

For brachydactyly-syndactyly syndrome, no mechanistic link could be identified. It is a rare congenital limb malformation of genetic origin, and sulfasalazine's anti-inflammatory actions have no evident relevance to its pathophysiology. The high score reflects a computational pattern only, and the same applies to the other rare genetic conditions in the top 10 (for example colobomatous microphthalmia-rhizomelic dysplasia syndrome, WHIM syndrome and acromesomelic dysplasia, Hunter-Thompson type).

Two other top-10 predictions are more meaningful:
- **Osteoarthritis (rank 5):** Preclinical studies suggest sulfasalazine reduces cytokine-stimulated cartilage proteoglycan and collagen release, lowers prostaglandin and leukotriene production, and attenuates cartilage destruction in an animal model. A sulfasalazine-hyaluronic acid formulation also reduced inflammation and cartilage degradation in a rat model. This is in vitro and animal data only, with no human efficacy data.
- **Spondyloarthropathy, susceptibility to (rank 8):** This is already among sulfasalazine's original indications, so it reflects existing use rather than true repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered for brachydactyly-syndactyly syndrome, or for osteoarthritis and spondyloarthropathy in the data compiled for this report.

## Literature Evidence

Currently no related literature available for brachydactyly-syndactyly syndrome.

For the most plausible candidate, osteoarthritis, the most relevant publications are preclinical:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29548914](https://pubmed.ncbi.nlm.nih.gov/29548914/) | 2018 | Preclinical (rat model) | Int J Biol Macromol | Sulfasalazine-containing hyaluronic acid released drug for up to 60 days and reduced inflammation and cartilage degradation in a rat osteoarthritis model |
| [26466556](https://pubmed.ncbi.nlm.nih.gov/26466556/) | 2016 | Preclinical (animal model) | J Orthop Res | Sulfasalazine attenuated cartilage destruction after ACL transection and meniscectomy, via inhibition of the cystine/glutamate antiporter |
| [19690126](https://pubmed.ncbi.nlm.nih.gov/19690126/) | 2009 | Preclinical (in vitro) | Rheumatology (Oxford) | Sulfasalazine blocked proteoglycan and collagen release from cytokine-stimulated cartilage and down-regulated metalloproteinases |
| [24329131](https://pubmed.ncbi.nlm.nih.gov/24329131/) | 2014 | Preclinical (chondrocyte proteomics) | Mod Rheumatol | Examined the effects of sulfasalazine and tofacitinib on the protein profile of articular chondrocytes |
| [1673814](https://pubmed.ncbi.nlm.nih.gov/1673814/) | 1991 | Preclinical (in vitro) | Wien Klin Wochenschr | Sulfasalazine and its metabolites altered prostaglandin and leukotriene release from human synovial tissue |
| [35958605](https://pubmed.ncbi.nlm.nih.gov/35958605/) | 2022 | Review | Front Immunol | Review of ferroptosis in inflammatory arthritis, including osteoarthritis (indirect evidence) |

For spondyloarthropathy, the retrieved literature is mainly reviews, plus one pharmacogenetic study:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25413361](https://pubmed.ncbi.nlm.nih.gov/25413361/) | 2014 | Pharmacogenetic case-control | BMC Pharmacol Toxicol | NAT polymorphisms in Han Chinese patients with ankylosing spondylitis and their link to sulfasalazine adverse reactions |
| [19938189](https://pubmed.ncbi.nlm.nih.gov/19938189/) | 2009 | Review | World J Gastroenterol | Rheumatic manifestations of inflammatory bowel disease |
| [15922688](https://pubmed.ncbi.nlm.nih.gov/15922688/) | 2005 | Review | Am J Med | Update on spondyloarthritis pathogenesis and management |

## Australia Market Information

| ARTG Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 13433B | Pyralin EN | Tablet 500 mg (enteric coated) | Not stated in the data compiled for this report |

## Safety Considerations

**Contraindications and cautions (from the knowledge graph, not label text):** Sulfasalazine is associated with caution or contraindication in the following conditions:
- Porphyria (including inherited porphyria and porphyrin metabolism disease)
- Kidney disease, liver disease, gallbladder disease, urinary tract obstruction and pyoureter
- Asthma (including intrinsic and allergic asthma)
- Blood disorders: neutropenia, agranulocytosis, aplastic anaemia (including idiopathic)
- G6PD deficiency and slow acetylator status
- Metabolic disorders: glycogen storage disease, cystinuria, galactosemia

**Drug Interactions:** The interaction screen returned 100 interactions in total. The first 20 shown include:
- **Major:** prilocaine (topical), human immunoglobulin G (intravenous), methenamine
- **Moderate:** ketorolac, ibuprofen, celecoxib, acyclovir, ethinylestradiol, estradiol, alpelisib, amphotericin B, amikacin, apalutamide, azathioprine, asparaginase, bacitracin, aminolevulinic acid (topical)
- **Minor:** folic acid

Please refer to the TGA-approved Product Information (PI) for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (brachydactyly-syndactyly syndrome) has no clinical trials, no literature and no plausible mechanism, so it is a model output only (Evidence Level L5). Osteoarthritis has a plausible rationale (Evidence Level L4), but support is limited to in vitro and animal studies. It would be better treated as a research question than as a candidate for clinical use. Spondyloarthropathy is an existing indication, not a new one.

**To proceed, the following is needed:**
- Detailed mechanism of action data for sulfasalazine
- Human efficacy data for osteoarthritis, such as a pilot clinical trial, before any clinical decision
- Approved indication text and safety information from the TGA Product Information, which were not available in the data compiled for this report
- Confirmation of the route and formulation needed (the only Australian product is an oral enteric-coated tablet, whereas the preclinical osteoarthritis work used a sulfasalazine-hyaluronic acid formulation)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

