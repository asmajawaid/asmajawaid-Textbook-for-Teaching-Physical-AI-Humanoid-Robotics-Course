<!--
SYNC IMPACT REPORT

- Version change: 1.1.0 → 1.2.0
- Rationale: Minor bump to clarify and strengthen the workflow standards. The 'Review' step is now explicitly defined, the 'Commit Verification' standard has been made more pragmatic by shifting it to the pull request, and a clear 'Definition of Done' for chapters has been added.
- Modified Sections:
  - Section 6: Restructured into "Workflow and Completion Standards" with explicit definitions for the development workflow, pull request standards, and the Definition of Done.
- Templates Requiring Updates:
  - ⚠ pending: `.specify/templates/tasks-template.md` (should be updated to include a final task for creating a pull request with the required verification checklist).
-->

# Constitution for "Teaching Physical AI and Humanoid Robotics"

- **Project Name**: Teaching Physical AI and Humanoid Robotics
- **Core Thesis**: Teaching physical AI and humanoid robotics requires spec-first thinking for effective, reproducible education.
- **Completion Target**: December 15, 2025
- **Constitution Version**: 1.2.0
- **Ratification Date**: 2025-12-08
- **Last Amended Date**: 2025-12-08

## 1. Purpose

This constitution defines the global quality, accuracy, and workflow standards for the "Teaching Physical AI and Humanoid Robotics" book project. It serves as the canonical source of truth and the foundation for every specification, planning, and implementation cycle executed via Spec-Kit Plus. Each chapter is to be treated as an individual "paper" within this workflow.

## 2. Core Principles

These principles are the non-negotiable pillars of the project.

- **Principle 1: Accuracy through Primary Source Verification**
  - All factual and conceptual claims must be rigorously verified against primary or authoritative secondary sources. This ensures the material is correct, reliable, and academically sound.

- **Principle 2: AI-Assisted but Human-Directed Writing**
  - AI tools (e.g., Gemini CLI, Claude) are leveraged for drafting, research, and coding, but the final expression, structure, and voice are owned and directed by the human author. Raw AI output is never acceptable.

- **Principle 3: Reproducibility and Traceability of Claims**
  - Every claim, data point, and code example must be traceable to a specific, citable source or a runnable verification script. Readers must be able to reproduce our results and follow our reasoning.

- **Principle 4: Clarity for Technical/Academic Audiences**
  - Writing must be clear, concise, and unambiguous, tailored for an audience of students, educators, and professionals in the fields of AI and robotics.

- **Principle 5: Zero-Plagiarism Tolerance**
  - All content must be original or properly attributed. Plagiarism in any form is a violation of this constitution and will result in immediate rejection of the work.

- **Principle 6: Rigor in Sourcing**
  - Preference is always given to peer-reviewed journals and conference papers. While other sources are permissible, the core arguments must be built upon a foundation of academic rigor.

- **Principle 7: Ethical and Transparent Citation Practices**
  - All borrowed ideas, text, and data must be cited using a consistent and ethical standard (APA 7th Edition). This demonstrates respect for intellectual property and academic integrity.

## 3. Testable Quality Standards

All work must meet these measurable standards before being committed.

- **Readability**: Achieve a Flesch-Kincaid grade level between 10 and 12.
- **Voice**: Maintain a minimum of 75% active voice throughout the text.
- **Technical Accuracy**: All code snippets and robotics simulations must run without errors when tested in a standard Python/ROS environment.
- **Plagiarism**: Achieve 0% similarity on a plagiarism checker (e.g., Grammarly, Turnitin), excluding properly formatted citations and the reference list.
- **Traceability**: All citations listed in the text must be present in the References section, and all sources in the References section must be traceable to a verifiable publication or artifact.
- **Visuals**: All figures, tables, and diagrams must include a source reference.

## 4. Source and Citation Requirements

- **Minimum Sources**: Each major chapter must cite a minimum of 12 peer-reviewed sources.
- **Source Quality**: At least 50% of all cited sources for a chapter must be peer-reviewed journal articles or conference papers.
- **Citation Style**: All citations and references must strictly adhere to the APA 7th Edition style guide. A complete "References" section is required at the end of each chapter.

## 5. Word Count and Format

- **Chapter Length**: Major chapters must have a target word count of 5,000–7,000 words. Introductory and concluding chapters may be shorter.
- **Final Output**: The primary output format is Markdown (`.md`), compatible with Docusaurus for web deployment. A secondary PDF export with embedded citations must also be producible.

## 6. Workflow and Completion Standards

### 6.1 Chapter Development Workflow
Each chapter must be developed following this exact, verifiable process.
1.  **For Each Chapter**:
    -   `/sp.specify`: Define the chapter's goals, scope, and requirements.
    -   `/sp.clarify`: Resolve ambiguities in the specification.
    -   `/sp.plan`: Create a detailed, step-by-step implementation plan.
    -   `/sp.tasks`: Break the plan into discrete, executable tasks.
    -   `/sp.implement`: Execute tasks to write content and code.
    -   `Review`: The non-negotiable step of formally verifying the chapter draft against every criterion listed in Section 3: Testable Quality Standards.
    -   `Commit`: Commit the draft to a feature branch.

### 6.2 Pull Request and Verification Standard
The pull request for each completed chapter must include a **Verification Checklist** in its description. This checklist must confirm that all standards in Section 3 have been met, with links to supporting evidence (e.g., plagiarism report, test results).

### 6.3 Definition of Done
A chapter is considered **'Done'** only when it:
1.  Meets all Testable Quality Standards (Section 3).
2.  Meets all Source and Citation Requirements (Section 4).
3.  Is submitted via a pull request that satisfies the Verification Standard (Section 6.2) and has been approved and merged.

## 7. Success Criteria

The project is considered successful when all criteria are met.

- All claims are verified against citable sources.
- All citations and references are APA 7th Edition compliant.
- All content passes a plagiarism check with 0% similarity (excluding references).
- The manuscript passes a final fact-checking and peer-review process.
- Each chapter meets its specified word-count and source-count targets.
- The complete book deploys successfully to GitHub Pages with full navigation, search functionality, and a responsive design.

## 8. Governance

- **Amendment Process**: Amendments to this constitution require a formal proposal and review. Changes must be documented in the Revision History section and result in a version increment.
- **Compliance Enforcement**: Work that does not comply with this constitution will not be merged. Automated checks and manual reviews will be used to enforce these standards.

## 9. Revision History

- **v1.2.0 (2025-12-08)**:
  - Clarified and strengthened workflow standards.
  - Defined the `Review` step explicitly.
  - Shifted the 'Commit Verification' standard to a more pragmatic 'Pull Request and Verification Standard'.
  - Added a formal 'Definition of Done' for chapters.
- **v1.1.0 (2025-12-08)**:
  - Updated project completion date and reinforced core thesis.
  - Made standards more testable by adding a requirement for all code examples to be runnable and error-free.
  - Strengthened source requirements, mandating at least 50% peer-reviewed sources.
  - Formalized word count, output format (Docusaurus), and workflow requirements.
- **v1.0.0 (Initial Version)**: Established the foundational principles for the project.
