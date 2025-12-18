# Tasks: Docusaurus RAG Chatbot UI

**Input**: Design documents from `specs/010-docusaurus-chatbot-ui/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Manual verification as per spec.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Install frontend dependencies (axios, react-markdown, remark-gfm, clsx, lucide-react) in `website/package.json`
- [x] T002 Create `.env` file with `BACKEND_URL` in `website/.env`
- [x] T003 Create component directory structure `website/src/components/Chatbot/`

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Configure FastAPI CORS middleware in `backend/main.py`
- [x] T005 Create Global Root wrapper in `website/src/theme/Root.tsx`
- [x] T006 Define shared TypeScript interfaces (ChatMessage, Citation) in `website/src/components/Chatbot/types.ts`
- [x] T007 Create basic CSS module in `website/src/components/Chatbot/styles.module.css`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

## Phase 3: User Story 1 - Interactive Knowledge Retrieval (Priority: P1) 🎯 MVP

**Goal**: Users can ask questions and receive Markdown answers.

**Independent Test**: Launch Docusaurus, open chat, type message, receive mock/real response.

### Implementation for User Story 1

- [x] T008 [US1] Implement API client function in `website/src/components/Chatbot/api.ts`
- [x] T009 [US1] Create ChatBubble component with Markdown rendering in `website/src/components/Chatbot/ChatBubble.tsx`
- [x] T010 [US1] Create ChatWindow component (input + list) in `website/src/components/Chatbot/ChatWindow.tsx`
- [x] T011 [US1] Assemble Chatbot container in `website/src/components/Chatbot/index.tsx`
- [x] T012 [US1] Mount Chatbot component in `website/src/theme/Root.tsx`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

## Phase 4: User Story 2 - Source Verification (Priority: P2)

**Goal**: Users see clickable citations in responses.

**Independent Test**: Ask a question, verify response contains "Sources" section with clickable links.

### Implementation for User Story 2

- [x] T013 [US2] Update ChatBubble to render Citation list in `website/src/components/Chatbot/ChatBubble.tsx`
- [x] T014 [US2] Style citations in `website/src/components/Chatbot/styles.module.css`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

## Phase 5: User Story 3 - Integrated Experience (Priority: P3)

**Goal**: Chatbot is seamless, persistent, and matches theme.

**Independent Test**: Navigate between pages, verify chat state persists. Toggle chat open/close.

### Implementation for User Story 3

- [x] T015 [US3] Implement floating toggle button logic in `website/src/components/Chatbot/index.tsx`
- [x] T016 [US3] Update styles to use Docusaurus theme variables (colors) in `website/src/components/Chatbot/styles.module.css`
- [x] T017 [US3] Verify persistence across navigation (Manual Check)

**Checkpoint**: All user stories should now be independently functional

## Phase 6: Final Review and Pull Request

**Purpose**: Verify the completed feature against all constitutional standards.

- [x] T018 **Run All Technical Checks**:
    - [x] Verify End-to-End flow (Frontend -> Backend -> LLM -> Frontend).
    - [x] Build Docusaurus project (`npm run build`) to ensure no SSR errors.
- [x] T019 **Update Documentation**:
    - [x] Ensure `specs/010-docusaurus-chatbot-ui/quickstart.md` is accurate.
- [x] T020 **Create Pull Request**:
    - [x] Create a pull request to merge `010-docusaurus-chatbot-ui`.
    - [x] Fill out verification checklist.

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies
- **Foundational (Phase 2)**: Depends on Phase 1
- **User Stories (Phase 3+)**: Depend on Phase 2
- **Polish (Phase 6)**: Depends on all implementation phases

### User Story Dependencies

- **US1 (P1)**: Independent after Foundation.
- **US2 (P2)**: Extends US1 (depends on ChatBubble).
- **US3 (P3)**: Extends US1 (depends on Chatbot container).

---

## Parallel Example: User Story 1

```bash
# Launch UI components and API logic in parallel
Task: "Implement API client function in website/src/components/Chatbot/api.ts"
Task: "Create ChatBubble component... in website/src/components/Chatbot/ChatBubble.tsx"
```