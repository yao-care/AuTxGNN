---
layout: default
title: Clonidine
parent: 僅模型預測 (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
---

# Clonidine
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

# Clonidine: From Hypertension to Tourette Syndrome

---

## One-Sentence Summary

Clonidine is a centrally acting alpha-2 adrenergic agonist with established international use in hypertension and ADHD, but it is not currently registered with the TGA in Australia.
The TxGNN model predicts it may be effective for **Tourette Syndrome** — a neurodevelopmental disorder characterised by chronic motor and vocal tics —
with **3 clinical trials** and **19 publications** (including a 2024 multicentre RCT, a network meta-analysis published in *The Lancet Child & Adolescent Health*, and the 2022 European ESSTS clinical guidelines) supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered with TGA; established international uses include hypertension and ADHD (FDA-approved Kapvay® ER) |
| Predicted New Indication | Tourette Syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Australia Market Status | Not marketed |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the regulatory dataset reviewed for Clonidine. Based on the published literature, Clonidine acts as a selective agonist at presynaptic α2A-adrenergic receptors in the prefrontal cortex and at the locus coeruleus — the brain's primary norepinephrine (noradrenaline) nucleus. By stimulating these auto-receptors, Clonidine reduces norepinephrine release throughout the central nervous system, suppressing sympathetic outflow. This is the basis for its antihypertensive effect and, separately, its utility in neurodevelopmental conditions involving dysregulated arousal, impulse control, and motor inhibition.

Tourette Syndrome (TS) involves dysfunction of the cortico-striato-thalamo-cortical (CSTC) circuit, with both dopaminergic and noradrenergic dysregulation implicated in tic generation. Elevated norepinephrine tone in the prefrontal-striatal pathway is thought to disinhibit the thalamo-cortical motor loop, facilitating involuntary tic expression. By reducing presynaptic NE release via α2A-receptor agonism, Clonidine can modulate this circuit directly. In addition, Clonidine indirectly attenuates dopamine signalling — the primary pharmacological target for tic suppression — through cross-circuit inhibitory mechanisms. Emerging preclinical evidence (2025) also suggests Clonidine may exert anti-neuroinflammatory effects in the basal ganglia, a region showing elevated IL-2 in post-mortem TS tissue.

This pharmacological rationale has been validated across more than 40 years of clinical research. Clonidine has been used for TS tic suppression since the landmark 1979 *Lancet* report by Cohen et al., and is now explicitly recommended in the 2022 ESSTS European Clinical Guidelines (v2.0) as a first-line pharmacological option — particularly valued in patients with comorbid ADHD, where it offers dual benefit on both tic suppression and attentional regulation. A 2024 multicentre, randomised, double-blind, placebo-controlled trial of the clonidine adhesive patch further substantiates its efficacy and tolerability.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|---------|------|------|------|---------|
| [NCT00370838](https://clinicaltrials.gov/study/NCT00370838) | Phase 4 | Completed | 12 | Double-blind, 15-week crossover RCT directly comparing Clonidine vs levetiracetam (Keppra) for tic suppression in children with TS; tests whether levetiracetam is superior in efficacy and tolerability to Clonidine |
| [NCT00152750](https://clinicaltrials.gov/study/NCT00152750) | Phase 4 | Status Unknown | 32 | Evaluated whether Clonidine-treated night-time sleep improvement reduces daytime aggression in children with TS and comorbid ADHD; Clonidine used as a pharmacological intervention for sleep |
| [NCT01172288](https://clinicaltrials.gov/study/NCT01172288) | Phase 2 | Completed | 31 | Double-blind, placebo-controlled RCT of N-acetylcysteine (NAC) for TS in children; Clonidine identified as a currently used active tic treatment; provides comparative safety context for Clonidine in paediatric TS |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39258554](https://pubmed.ncbi.nlm.nih.gov/39258554/) | 2024 | RCT | *Clinical Neuropharmacology* | Multicentre, randomised, double-blind, placebo-controlled trial of clonidine adhesive patch in TS; evaluated tic reduction efficacy and safety profile |
| [36528030](https://pubmed.ncbi.nlm.nih.gov/36528030/) | 2023 | Network Meta-Analysis | *The Lancet Child & Adolescent Health* | Compared efficacy, tolerability and acceptability of all pharmacological interventions for TS in children and young adults; provides rigorous evidence base for clinical guideline development |
| [34757514](https://pubmed.ncbi.nlm.nih.gov/34757514/) | 2022 | Clinical Guideline | *European Child & Adolescent Psychiatry* | Updated ESSTS European clinical guidelines v2.0 for TS pharmacological treatment; Clonidine recommended as first-line option, particularly for ADHD-comorbid presentations |
| [31061209](https://pubmed.ncbi.nlm.nih.gov/31061209/) | 2019 | Systematic Review | *Neurology* | AAN-commissioned comprehensive review of efficacy and risk of tic treatments; Clonidine systematically assessed across multiple study designs |
| [40489853](https://pubmed.ncbi.nlm.nih.gov/40489853/) | 2025 | Narrative Review | *Medicine* | Review of Phase III/IV pharmacological trials for TS across children, adults and older adults; positions alpha-2 agonists within the current treatment landscape |
| [38695046](https://pubmed.ncbi.nlm.nih.gov/38695046/) | 2024 | Clinical Study | *Psychiatry Investigation* | Assessed efficacy and safety of clonidine adhesive patch specifically in TS patients with comorbid ADHD — a common and clinically challenging subgroup |
| [40392363](https://pubmed.ncbi.nlm.nih.gov/40392363/) | 2025 | Animal Study | *J Neuroimmune Pharmacology* | Clonidine ameliorates neuroinflammation (reduced IL-2) in basal ganglia in a rat TS model; supports a novel anti-inflammatory mechanism complementary to noradrenergic agonism |
| [22728760](https://pubmed.ncbi.nlm.nih.gov/22728760/) | 2013 | Review | *Neuropharmacology* | Comprehensive synthesis of pharmacological treatment options for tic disorders and TS; Clonidine evidence evaluated within a multimodal framework |
| [1414629](https://pubmed.ncbi.nlm.nih.gov/1414629/) | 1992 | Clinical Trial | *Advances in Neurology* | Clinical evaluation of Clonidine and clonazepam for TS tic suppression; early comparative evidence |
| [89558](https://pubmed.ncbi.nlm.nih.gov/89558/) | 1979 | Clinical Study | *Lancet* | Landmark original report: small doses of Clonidine improved TS in children unresponsive to haloperidol; first evidence establishing central noradrenergic involvement in TS pathophysiology |

---

## Australia Market Information

Clonidine is **not currently registered with the TGA** and has no ARTG entries. No TGA-approved Product Information is available through this regulatory dataset.

Clinicians seeking to use Clonidine in Australia for Tourette Syndrome should explore the following regulatory pathways:

- **TGA Special Access Scheme (SAS) — Category B**: for individual patients on a case-by-case basis
- **TGA Authorised Prescriber pathway**: for specialists prescribing regularly to a defined patient population

International reference products include **Catapres®** (immediate-release tablet and transdermal patch; antihypertensive indication) and **Kapvay®** (extended-release tablet; FDA-approved for ADHD in children and adolescents aged 6–17 years).

---

## Safety Considerations

Safety data was not available in the TGA regulatory dataset, as Clonidine is not currently registered in Australia. No drug-drug interaction data was retrieved for this assessment.

> Please refer to international Product Information documents (FDA Catapres®/Kapvay® package inserts or EMA-equivalent) for comprehensive safety information before any clinical use. Based on published literature, key safety considerations include: sedation and fatigue (particularly at initiation), hypotension, bradycardia, and risk of rebound hypertension on abrupt discontinuation — structured tapering is required.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clonidine has L1 evidence supporting its use in Tourette Syndrome — including a 2024 multicentre placebo-controlled RCT, a 2023 network meta-analysis in *The Lancet Child & Adolescent Health*, and explicit inclusion in the 2022 ESSTS European Clinical Guidelines. The noradrenergic mechanistic rationale is well-established over four decades of research. The primary barrier to clinical use in Australia is the absence of TGA registration, which requires a special access or authorised prescriber pathway rather than standard prescription.

**To proceed, the following is needed:**

- **Regulatory pathway**: Apply for TGA Special Access Scheme (SAS Category B) or Authorised Prescriber status for Clonidine in Tourette Syndrome
- **Safety documentation**: Conduct a formal safety review using FDA Catapres®/Kapvay® package inserts in the absence of an Australian PI
- **Formulation selection**: Determine appropriate formulation (immediate-release vs. extended-release vs. transdermal patch) and dosing regimen for the target patient population (predominantly paediatric)
- **Cardiovascular monitoring plan**: Baseline and follow-up blood pressure and heart rate measurements; particular vigilance required in patients on other antihypertensives or CNS depressants
- **Tapering protocol**: Structured dose-reduction plan to mitigate rebound hypertension risk on discontinuation
- **Comorbidity consideration**: Evaluate Clonidine's additional utility in TS patients with comorbid ADHD, where L2 evidence supports dual benefit — this may strengthen the case for an Authorised Prescriber application
- **Related priority indication**: Also consider evaluating **specific developmental disorder (ADHD)**, which carries L2 evidence and reflects an FDA-approved use of Clonidine ER — a complementary regulatory precedent that could support the Australian access application

---

*This report is intended for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before therapeutic application. All clinical decisions should be made in accordance with current TGA guidelines and individual patient circumstances.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

