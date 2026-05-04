---
layout: default
title: Diazepam
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 10
---

# Diazepam
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

# Diazepam: From Anxiety and Seizure Disorders to Insomnia

## One-Sentence Summary

Diazepam (Valium) is a classic benzodiazepine historically used to treat anxiety disorders, muscle spasms, seizures, and alcohol withdrawal.
The TxGNN model predicts it may be effective for **Insomnia**, with **24 clinical trials** and **18 publications** currently supporting this direction.
Evidence is drawn primarily from established benzodiazepine class use, hypnotic withdrawal management studies, and one head-to-head diazepam comparison trial, rather than large dedicated diazepam-for-insomnia RCTs.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No TGA registration data found (Diazepam is a classic benzodiazepine classically used for anxiety disorders, seizures, muscle spasms, and alcohol withdrawal) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Australia Market Status | Not Marketed (no ARTG entries found) |
| Number of ARTG Entries | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Although detailed mechanism of action data is absent from the regulatory dataset, diazepam's pharmacology is one of the most thoroughly characterised in all of medicine. Diazepam is a positive allosteric modulator (PAM) of the GABA-A receptor, binding to the benzodiazepine site at the α/γ subunit interface to increase the frequency of chloride ion channel opening. This potentiates the inhibitory neurotransmitter GABA, producing dose-dependent sedation, anxiolysis, anticonvulsant activity, and skeletal muscle relaxation across the central nervous system.

The mechanistic link to insomnia is direct and well-established. By enhancing GABA-mediated CNS inhibition, diazepam reduces sleep latency (time to fall asleep) and decreases nocturnal awakenings — the two hallmark features of insomnia. This is the same mechanism shared by the entire benzodiazepine hypnotic class (nitrazepam, temazepam, triazolam), several of which are specifically approved and marketed as sleep aids. The TxGNN prediction score of 99.99% is therefore pharmacologically unsurprising — it reflects diazepam's genuine mechanistic alignment with insomnia pathophysiology.

However, the prediction must be interpreted with important clinical guardrails in mind. Long-term diazepam use suppresses N3 slow-wave sleep and REM sleep, disrupts NREM oscillatory architecture (spindles and slow oscillations), and is associated with tolerance and physical dependence. A landmark 2022 *Nature Neuroscience* study (PMID 35228700) demonstrated that chronic diazepam enhances microglial synaptic engulfment via the mitochondrial translocator protein (TSPO), causing persistent cognitive impairment in animal models. Contemporary Australian and international clinical guidelines consistently recommend limiting benzodiazepine use for insomnia to short-term or intermittent courses (fewer than 4 weeks), and favour Cognitive Behavioural Therapy for Insomnia (CBT-I) and newer agents (Z-drugs, orexin receptor antagonists) as first-line treatment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrolment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT03461042](https://clinicaltrials.gov/study/NCT03461042) | Phase 4 | Completed | 17 | Placebo-controlled double-blind multicentre RCT evaluating ramelteon combined with BZD dose reduction in chronic insomnia; directly relevant design but underpowered — conclusions require cautious interpretation |
| [NCT04050176](https://clinicaltrials.gov/study/NCT04050176) | Phase 3 | Active (not recruiting) | 260 | RCT comparing blinded BZD tapering plus CBT-I versus open-label protocol for hypnotic discontinuation in insomnia patients; largest ongoing Phase 3 trial confirming BZD-insomnia clinical framework |
| [NCT02831894](https://clinicaltrials.gov/study/NCT02831894) | Phase 2 | Completed | 74 | Examines the role of tapering pace and patient traits on BZD discontinuation success in treatment-seeking insomnia patients; supports individualised tapering approach |
| [NCT04751851](https://clinicaltrials.gov/study/NCT04751851) | N/A | Completed | 128 | RCT comparing Acceptance and Commitment Therapy (ACT) versus standard psychological support adjunct to BZD withdrawal programme in adults with insomnia and hypnotic dependence |
| [NCT04364321](https://clinicaltrials.gov/study/NCT04364321) | N/A | Unknown | 74 | Directly compares single-dose clonazepam versus intermittent oral diazepam for prevention of recurrent febrile seizures in children; the only trial explicitly naming diazepam in a head-to-head comparison |
| [NCT03687086](https://clinicaltrials.gov/study/NCT03687086) | N/A | Completed | 188 | Novel mechanism-based intervention for older adults to discontinue BZD sleeping medications; highlights adverse health outcomes associated with long-term hypnotic use in the elderly |
| [NCT07417813](https://clinicaltrials.gov/study/NCT07417813) | N/A | Recruiting | 121 | Prospective observational study of lemborexant (dual orexin receptor antagonist) in psychiatric patients with comorbid insomnia; provides context for shift away from BZDs toward newer agents |
| [NCT05935553](https://clinicaltrials.gov/study/NCT05935553) | Phase 2/3 | Recruiting | 93 | Evaluating baclofen (GABA-B agonist) for improving BZD titration and withdrawal in BZD-dependent patients; indirectly supports the clinical challenge of managing BZD use in insomnia |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | RCT | J Int Med Research | Double-blind 7-day RCT (n=100): lormetazepam 1 mg significantly outperformed diazepam 5 mg in reducing sleep onset time and prolonging uninterrupted sleep in insomnia outpatients — the most directly relevant head-to-head trial for diazepam in insomnia |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | RCT | JAMA Internal Medicine | Masked BZD receptor agonist taper plus augmented CBT-I versus open-label: placebo effects are prominent in BZD insomnia trials; supports CBT-I as the primary therapeutic framework |
| [35228700](https://pubmed.ncbi.nlm.nih.gov/35228700/) | 2022 | Experimental | Nature Neuroscience | Long-term diazepam impairs dendritic spine structural plasticity via TSPO-mediated microglial engulfment, causing persistent cognitive decline in mice — a key mechanistic safety signal for chronic use |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Review | Bioorganic Chemistry | Review of GABA-A receptor small-molecule modulators: confirms diazepam as a prototypical PAM for anxiety and insomnia, noting sedation, tolerance, and dependence as principal limitations |
| [40570297](https://pubmed.ncbi.nlm.nih.gov/40570297/) | 2025 | Review | Sleep | Chronic BZD/BZRA use disrupts NREM slow oscillations, sleep spindles, and spindle–slow-oscillation coupling in older adults with chronic insomnia; implications for memory and cognitive health |
| [7525193](https://pubmed.ncbi.nlm.nih.gov/7525193/) | 1994 | Review/Guideline | Drugs | Foundational rational BZD use guidelines: benzodiazepines mainly indicated for transient or short-term insomnia; prescriptions should be limited to days or a few weeks at most |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | Pharmacokinetics of anxiolytic drugs including benzodiazepines; discusses clinical applications for anxiety and sleep disorders in the context of elimination half-life differences |
| [6114852](https://pubmed.ncbi.nlm.nih.gov/6114852/) | 1981 | Review | Drugs | Triazolam compared with longer-acting BZDs including diazepam for insomnia: shorter half-life agents preferred to minimise residual morning sedation and next-day functional impairment |

---

## Australia Market Information

No TGA-registered products for Diazepam were identified in the ARTG dataset at the time of this analysis (data cutoff: 4 April 2026). This likely reflects a data gap in the query rather than true absence of TGA registration, as Diazepam preparations have historically been available in Australia. Clinicians should verify current ARTG registration status directly via the TGA website at [https://www.tga.gov.au/resources/artg](https://www.tga.gov.au/resources/artg) before clinical use.

---

## Safety Considerations

Please refer to the TGA-approved Product Information (PI) for safety information.

> **Note:** This evidence pack has identified gaps in the safety data (TGA PI warnings, contraindications, and drug-drug interaction data were not retrieved). These are flagged as high-severity data gaps. A full safety review against the TGA PI is mandatory before any clinical use consideration.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Diazepam's GABA-A receptor mechanism directly addresses the neurobiological basis of insomnia, and there is a decades-long history of clinical use of benzodiazepines as hypnotic agents, supported by guideline-level literature and multiple clinical trials in the BZD–insomnia domain. However, contemporary evidence and clinical guidelines firmly restrict benzodiazepines to short-term insomnia management due to tolerance, dependence risk, sleep architecture disruption, and emerging cognitive safety signals. The evidence base is primarily for the BZD drug class as a whole rather than diazepam specifically; among BZDs, shorter-acting agents (temazepam, triazolam) are typically preferred as hypnotics over the long-acting diazepam.

**To proceed, the following is needed:**
- **Mandatory:** Verify current TGA ARTG registration status directly — the 0-entry query result likely reflects a data retrieval gap
- **Mandatory:** Obtain and review the full TGA-approved Product Information (PI) for warnings, contraindications, and drug interactions before any clinical use
- **Mandatory:** Conduct a drug-drug interaction risk assessment (DDI data was not retrieved in this Evidence Pack)
- Define the specific clinical niche: diazepam for insomnia is most defensible for short-term management of acute situational insomnia or insomnia with prominent anxiety features — not for chronic insomnia management
- Establish patient selection criteria and exclusion criteria (elderly patients, history of substance use disorder, respiratory disease — all represent significant risk groups)
- Develop a structured monitoring and deprescribing plan, including a planned taper schedule and maximum duration of use (recommended ≤4 weeks)
- Consider whether a shorter-acting TGA-approved benzodiazepine hypnotic (e.g., temazepam) would be more appropriate than diazepam given its long half-life and active metabolite (desmethyldiazepam)
- Ensure CBT-I referral pathway is in place as the preferred long-term insomnia management strategy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

