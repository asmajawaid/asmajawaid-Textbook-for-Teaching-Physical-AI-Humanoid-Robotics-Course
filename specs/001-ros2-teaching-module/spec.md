# Feature Specification: Module 1 - The Robotic Nervous System (ROS 2)

**Feature Branch**: `001-ros2-teaching-module`  
**Created**: 2025-12-08
**Status**: Draft  
**Input**: User description: "Chapter: Module 1 – The Robotic Nervous System (ROS 2) Target audience: Educators, curriculum designers, university instructors, and advanced students with intermediate Python and Linux skills who are teaching or learning Physical AI and humanoid robotics. Readers are familiar with basic AI concepts but may have no prior ROS 2 experience. Focus: Deliver a complete, hands-on teaching module on ROS 2 (Humble or Iron) as the core middleware for humanoid robotics. Emphasize Python/rclpy implementation, URDF/Xacro modeling of multi-DoF humanoids, and spec-first practices (defining interfaces, messages, and parameters before coding) to achieve reproducible robotic software. Success criteria (all must be testable): - Reader can install ROS 2 Humble/Iron on Ubuntu 22.04 and create a functional workspace (verified by successful colcon build and ros2 topic list). - Reader can implement and run at least 5 progressively complex, error-free examples: (1) publisher/subscriber, (2) service client/server, (3) action server/client for joint trajectories, (4) multi-node system with parameters and launch files, (5) URDF/Xacro model of a ≥12-DoF humanoid visualized and controlled in RViz. - Every code snippet executes without errors on a clean Ubuntu 22.04 + ROS 2 Humble setup; verification steps and expected output are explicitly provided. - At least 80% of technical claims (e.g., ROS 2 advantages over ROS 1, real-time capabilities, adoption rates) are backed by primary sources. - Readability scores: Flesch-Kincaid grade level 10–12 and ≥75% active voice (measured via Grammarly/Readable or equivalent before commit). - Demonstrates spec-first thinking through explicit interface definition (custom messages, srv, action files) before implementation in every major example. Constraints: - Word count: 5,500–7,000 words (excluding code blocks, figures, and references). - Format: Single Docusaurus-compatible Markdown file at docs/module-1-ros2.md with proper YAML frontmatter (id, title, sidebar_label), syntax-highlighted code blocks, and a complete APA References section at the end. - Sources: Minimum 12 peer-reviewed sources (≥50% journal articles or conference papers from the past 10 years, e.g., IEEE T-RO, IJRR, RAS letters, ROSCon proceedings); all citations in APA style with DOI links where available. - Code standards: All examples must be complete, self-contained packages; include package.xml, CMakeLists.txt snippets, and colcon build instructions. No external non-standard dependencies. - Plagiarism: 0% similarity (excluding references and code) when checked with Grammarly/Turnitin. - Timeline: Fully implemented, reviewed, and committed by December 11, 2025 (to maintain pace for book completion by December 15, 2025). Not building: - Introductory Python or Linux tutorials. - C++ (rclcpp) implementations — only brief mentions for comparison. - Advanced ROS 2 topics (DDS tuning, real-time kernels, security, lifecycle nodes). - Integration with simulation (Gazebo), perception (Isaac ROS), or LLMs — those are reserved for Modules 2–4. Weekly coverage (Weeks 3–5): - ROS 2 architecture, nodes, topics, services, actions - Parameters, launch files, and debugging tools - Building Python packages with rclpy - URDF/Xacro modeling for humanoid robots Additional notes for the AI workflow: Strictly follow the global Constitution.md: primary source verification, zero plagiarism, APA citations, active voice ≥75%, Flesch-Kincaid 10–12, all code tested and executable, all claims traceable. Treat this as an independent “paper” in Spec-Kit Plus workflow: proceed through /sp.clarify → /sp.plan → /sp.tasks → /sp.implement → fact-check/plagiarism review → commit to the Docusaurus docs/ folder and push to GitHub."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Environment Setup (Priority: P1)

A reader with intermediate Python/Linux skills follows the instructions to install ROS 2 and set up a workspace on a clean Ubuntu 22.04 system. They successfully build the workspace and verify the installation.

**Why this priority**: This is the foundational step. No reader can proceed without a working ROS 2 environment.

**Independent Test**: A user can follow only the installation and setup guide, run `colcon build` and `ros2 topic list`, and see the expected successful output without errors. This delivers the value of a verified starting point.

**Acceptance Scenarios**:

1. **Given** a clean Ubuntu 22.04 environment, **When** the reader follows the installation instructions for ROS 2 Humble/Iron, **Then** the installation completes without errors.
2. **Given** a successful ROS 2 installation, **When** the reader creates a new workspace and builds it using `colcon build`, **Then** the build succeeds and they can successfully run `ros2 topic list`.

---

### User Story 2 - Core ROS 2 Concepts (Priority: P2)

A reader implements and runs basic ROS 2 examples for publisher/subscriber, service client/server, and action server/client to understand fundamental communication patterns.

**Why this priority**: These concepts are the building blocks for any ROS 2 application.

**Independent Test**: The reader can compile and run each of the three initial examples independently. For instance, they can run the publisher/subscriber example and verify message passing, delivering a clear understanding of that specific pattern.

**Acceptance Scenarios**:

1. **Given** a functional ROS 2 workspace, **When** the reader implements the publisher/subscriber example code, **Then** the nodes launch and messages are passed successfully from publisher to subscriber.
2. **Given** a functional ROS 2 workspace, **When** the reader implements the service example, **Then** the client can successfully call the server and receive a response.
3. **Given** a functional ROS 2 workspace, **When** the reader implements the action example for joint trajectories, **Then** the client can send a goal to the action server and receive feedback/results.

---

### User Story 3 - Building a Humanoid Model (Priority: P3)

A reader creates a URDF/Xacro model of a humanoid robot with at least 12 degrees of freedom and visualizes it in RViz.

**Why this priority**: This applies the learned concepts to a concrete, complex robotics task, which is the core focus of the book.

**Independent Test**: The reader can create the URDF files, use a provided launch file to start RViz, and see the 3D model of the humanoid robot correctly rendered. This delivers the value of seeing a tangible robotic representation.

**Acceptance Scenarios**:

1. **Given** a functional ROS 2 workspace, **When** the reader creates the URDF/Xacro files for a humanoid robot, **Then** the model can be parsed without errors.
2. **Given** a valid URDF model, **When** the reader uses the provided launch file, **Then** RViz opens and displays the humanoid model, which can be manipulated via the GUI.

### Edge Cases

- What happens if the reader uses a different, unsupported Linux distribution or ROS 2 version? (The text should specify that only Ubuntu 22.04 with Humble/Iron is supported).
- How does the system handle compiler errors? (The text should provide complete, error-free code and clear build instructions to minimize this).
- What if a required dependency is missing? (The installation guide must be complete and list all prerequisites).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The module MUST provide complete, step-by-step instructions to install ROS 2 (Humble or Iron) on Ubuntu 22.04.
- **FR-002**: The module MUST explain the core ROS 2 architecture, including nodes, topics, services, actions, parameters, and launch files.
- **FR-003**: The module MUST provide at least 5 complete, executable Python/rclpy examples: a simple publisher/subscriber, a service, an action, a multi-node system with parameters, and a humanoid URDF visualization.
- **FR-004**: The module MUST demonstrate how to create custom messages, services, and action definitions before they are used in code (spec-first).
- **FR-005**: The module MUST provide instructions on how to model a humanoid robot with 12+ DoF using URDF and Xacro.
- **FR-006**: The module MUST show how to visualize and interact with the robot model in RViz.
- **FR-007**: All technical claims regarding ROS 2's capabilities or adoption MUST be supported by citations to peer-reviewed sources.
- **FR-008**: All code examples MUST be self-contained within ROS 2 packages, including `package.xml` and build instructions.

### Non-Functional Requirements

- **NFR-001 (Word Count)**: The final chapter output MUST be between 5,500 and 7,000 words (excluding code, figures, references).
- **NFR-002 (Format)**: The final output MUST be a single Docusaurus-compatible Markdown file.
- **NFR-003 (Styling)**: The markdown MUST include proper YAML frontmatter (`id`, `title`, `sidebar_label`) and syntax-highlighted code blocks.
- **NFR-004 (Readability)**: The text MUST score between grade level 10-12 on the Flesch-Kincaid scale and use at least 75% active voice.
- **NFR-005 (Sources)**: The module MUST cite a minimum of 12 peer-reviewed sources, with at least 50% being recent journal/conference papers.
- **NFR-006 (Citations)**: All citations and references MUST follow APA style with DOI links.
- **NFR-007 (Plagiarism)**: The text MUST have 0% similarity score when checked, excluding code and references.
- **NFR-008 (Deadline)**: The module MUST be fully implemented and reviewed by December 11, 2025.

### Key Entities

- **ROS 2 Node**: The primary process in a ROS 2 system. Key attributes: name, namespace.
- **Topic**: A message bus for many-to-many communication. Key attributes: name, message type.
- **Service**: A request/reply communication pattern. Key attributes: name, service type.
- **Action**: A long-running task with feedback. Key attributes: name, action type.
- **URDF/Xacro**: XML formats for describing robot models. Key attributes: links, joints, visuals, collision properties.
- **ROS 2 Package**: A self-contained unit of ROS 2 code. Key attributes: name, dependencies, build files.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of readers can successfully install ROS 2 and create a functional workspace by following the guide. This is verified by a successful `colcon build` and output from `ros2 topic list`.
- **SC-002**: 100% of the 5+ provided code examples execute without error on a clean, specified environment. Verification steps and expected output are explicitly provided for each.
- **SC-003**: A reader can successfully define a custom message/service/action and use it in a Python node, demonstrating the spec-first approach.
- **SC-004**: A reader can assemble a ≥12-DoF humanoid URDF model that is successfully visualized and controlled in RViz.
- **SC-005**: At least 80% of technical claims are backed by citations from primary sources visible in the References section.
- **SC-006**: The final submitted Markdown file passes a Flesch-Kincaid (10-12) and active voice (≥75%) check.
- **SC-007**: The final submission passes a plagiarism check with a 0% similarity score (excluding code and references).