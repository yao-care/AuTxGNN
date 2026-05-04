---
layout: default
title: Budesonide
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
---

# Budesonide
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

# Budesonide: From Asthma and Inflammatory Airway Disease to Atopic Eczema

## One-Sentence Summary

Budesonide is a potent synthetic glucocorticoid corticosteroid with established use in asthma, allergic rhinitis, and inflammatory bowel conditions such as Crohn's disease and microscopic colitis.
The TxGNN model predicts it may also be effective for **Atopic Eczema**, with **2 clinical trials** and **20 publications** identified in the current evidence search.
Evidence is currently at Level L3 (observational and preclinical studies), and the prediction warrants further clinical investigation before development is recommended.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Asthma, allergic rhinitis, inflammatory bowel disease (TGA registration data not available in current dataset) |
| Predicted New Indication | Atopic Eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Australia Market Status | Not registered (TGA ARTG data unavailable — likely a data gap; see note below) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Research Question (Hold) |

---

## Why is This Prediction Reasonable?

Budesonide is a potent glucocorticoid receptor (GR) agonist with broad anti-inflammatory properties. Although detailed mechanism of action data was not available in this evidence pack, budesonide is well-established in the pharmacological literature as a suppressor of Th2-dominant cytokine signalling — specifically IL-4 and IL-13 — and eosinophil chemotaxis. These pathways sit at the core of atopic eczema pathogenesis, providing a plausible mechanistic basis for the TxGNN model's high prediction score.

Atopic eczema (atopic dermatitis) is characterised by skin barrier dysfunction, Th2/Th22 immune dysregulation, and chronic eosinophilic inflammation. Conventional topical corticosteroids such as hydrocortisone and betamethasone are already established as first-line therapy, confirming that GR agonism is a validated therapeutic strategy. The key scientific question for budesonide repurposing is therefore not *whether* this mechanism is relevant, but *whether budesonide offers clinical differentiation* over existing topical steroids — for example, through superior anti-inflammatory potency, improved skin penetration, or reduced systemic side effects.

A promising answer may lie in novel drug delivery. A 2024 study (PMID 38275852) demonstrated that budesonide-loaded Eudragit L100 polymeric nanoparticles formulated into pH-sensitive hydrogels can exploit the characteristic acidic microenvironment of atopic lesions for targeted, site-specific release. This approach could potentially overcome the physicochemical barriers that limit conventional topical budesonide and position it as a next-generation topical agent. However, this remains at a preclinical/formulation stage and human clinical trials have not yet been conducted.

---

## Clinical Trial Evidence

No clinical trials directly evaluating budesonide as a treatment for atopic eczema were identified. The two trials retrieved involve atopic populations but are not relevant to this repurposing question.

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01028560](https://clinicaltrials.gov/study/NCT01028560) | Phase 1/2 | Completed | 58 | Allergy immunotherapy (not budesonide) for preventing asthma in atopic, wheezing children aged 18 months to 3 years; participants may have co-existing eczema but the intervention is unrelated to budesonide |
| [NCT04680117](https://clinicaltrials.gov/study/NCT04680117) | Observational | Unknown | 150 | Characterisation of severe paediatric asthma endotypes using immune, metabolomic and microbial profiling; does not evaluate budesonide treatment for atopic eczema |

> **Relevance note:** Both trials are graded C (low relevance). No Grade A or B trials were identified for this indication. This is a significant evidence gap.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Formulation/Preclinical | *Gels (Basel)* | Budesonide-loaded pH-sensitive nanoparticles in hydrogel for paediatric atopic dermatitis; exploits lesion acidity for targeted release; promising delivery platform but no human data yet |
| [8864369](https://pubmed.ncbi.nlm.nih.gov/8864369/) | 1996 | Observational | *Dermatology* | Topical glucocorticosteroids including budesonide in children with atopic dermatitis; assessed systemic effects on IGF axis, bone and collagen turnover; highlights percutaneous absorption risks in paediatric use |
| [21062310](https://pubmed.ncbi.nlm.nih.gov/21062310/) | 2010 | RCT (Veterinary) | *J Vet Pharmacol Ther* | 0.025% budesonide leave-on conditioner (Barazone) significantly reduced skin lesions and pruritus vs placebo in a crossover RCT of 29 dogs with atopic dermatitis; translational relevance is limited but mechanistically supportive |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Cross-sectional | *Contact Dermatitis* | Patch testing of budesonide across Italy (2018–2019); budesonide is the European Baseline Series marker for corticosteroid contact hypersensitivity; a decreasing sensitisation trend was observed over the past two decades |
| [35133669](https://pubmed.ncbi.nlm.nih.gov/35133669/) | 2022 | Cross-sectional | *Contact Dermatitis* | Contact sensitisation patterns at an Asian dermatology centre; atopic dermatitis patients showed similar or higher patch-test positivity rates, with corticosteroids (including budesonide) identified as relevant sensitisers |
| [24603519](https://pubmed.ncbi.nlm.nih.gov/24603519/) | 2014 | Cross-sectional | *Dermatitis* | Contact hypersensitivity to budesonide and other corticosteroids in adolescents and adults with atopic dermatitis; relevant safety signal for budesonide application in this population |
| [30053491](https://pubmed.ncbi.nlm.nih.gov/30053491/) | 2018 | Cross-sectional | *J Am Acad Dermatol* | Allergic contact dermatitis to topical medications in adults with atopic dermatitis; skin barrier disruption and immune dysregulation in AD increase risk of sensitisation to topical corticosteroids |
| [40020933](https://pubmed.ncbi.nlm.nih.gov/40020933/) | 2025 | Translational | *J Allergy Clin Immunol* | Cutaneous ceramide synthesis dysregulation in paediatric eosinophilic oesophagitis shares features with atopic dermatitis; highlights shared epithelial barrier pathomechanisms relevant to budesonide's potential multi-indication role |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | *Neuroimmunomodulation* | Intranasal corticosteroids and HPA axis suppression; relevant to systemic safety considerations when budesonide is applied across multiple atopic conditions concurrently |
| [31705907](https://pubmed.ncbi.nlm.nih.gov/31705907/) | 2020 | Review | *J Allergy Clin Immunol* | Emerging therapies for eosinophilic oesophagitis; discusses topical budesonide formulations and Th2-driven inflammatory overlap — provides context for budesonide's broader positioning in type 2 inflammatory disease |

---

## Australia Market Information

No ARTG entries were identified for Budesonide in the current dataset (0 licences; market status recorded as not registered).

> **Important note:** This is likely a data gap rather than a true absence from the Australian market. Budesonide is a globally registered medicine available under brands including **Pulmicort** (inhalation), **Rhinocort** (nasal spray), and **Entocort** (oral/rectal capsule), and is expected to have multiple ARTG registrations. Clinicians should verify current registration status and approved indications directly via the [TGA ARTG Public Summary Search](https://www.tga.gov.au/resources/artg).

---

## Safety Considerations

Specific safety data — including key warnings, contraindications, and drug-drug interactions — were not available in this evidence pack. Please refer to the **TGA-approved Product Information (PI)** for Budesonide for complete safety information.

Based on the literature identified in this evidence pack, the following safety areas are particularly relevant to the atopic eczema repurposing context and should be reviewed prior to any clinical application:

- **Contact hypersensitivity:** Budesonide is an established marker for corticosteroid contact allergy in the European Baseline Patch Test Series. Atopic dermatitis patients are at increased risk of sensitisation due to impaired skin barrier and repeated topical exposures (see PMID 33931866, 35133669, 24603519, 30053491).
- **HPA axis suppression:** Percutaneous absorption with long-term topical use can cause clinically significant adrenal suppression, particularly in children (see PMID 8864369, 19571596).
- **Skin atrophy:** A recognised risk of chronic topical corticosteroid use; relevance to budesonide formulations should be formally assessed.

---

## Conclusion and Next Steps

**Decision: Research Question (Hold)**

**Rationale:**
The TxGNN prediction is mechanistically well-founded — budesonide's GR agonism and Th2 suppression are directly relevant to atopic eczema pathology — but current human clinical evidence is absent. The only directly relevant study is a 2024 preclinical nanoparticle formulation paper, and no human RCTs have been conducted. Furthermore, conventional topical corticosteroids are already first-line for atopic eczema, meaning budesonide must demonstrate clear clinical differentiation (e.g., via novel delivery technology or superior therapeutic index) to justify development.

**To proceed, the following is needed:**

- **Confirm TGA registration status:** Retrieve current ARTG listings and review the approved Product Information for complete safety, contraindications, and approved indications.
- **Mechanism of action data:** Obtain full MOA characterisation from DrugBank (DB01222) to strengthen the biological rationale section of any clinical development submission.
- **Human proof-of-concept study:** A Phase 1/2 trial evaluating the budesonide nanoparticle hydrogel formulation (building on PMID 38275852) in adults with mild-to-moderate atopic dermatitis is the logical next step.
- **Comparative efficacy design:** Any future trial should include an active comparator arm (e.g., betamethasone valerate) to demonstrate differentiation from existing first-line topical corticosteroids.
- **Paediatric safety assessment:** Given that atopic eczema is common in children and that systemic absorption is a documented concern, dedicated paediatric safety data (HPA axis monitoring, growth assessment) will be required by the TGA.
- **Contact sensitisation risk quantification:** A systematic review or prospective cohort study to quantify budesonide contact allergy rates specifically in the atopic dermatitis population is needed before broad topical use is recommended.

---

> *This report is generated for research evaluation purposes only and does not constitute medical advice. All repurposing candidates require clinical validation before therapeutic application. Healthcare professionals should refer to current TGA-approved Product Information and clinical guidelines when making prescribing decisions.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

