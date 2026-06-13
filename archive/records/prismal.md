# Prismal (archived husk) - Design Record

> **Status:** Archived 2026-05-03; GitHub repo scheduled for deletion after absorption.
> **Original repo:** `KooshaPari/Prismal` (private, archived 2026-05-03).
> **Absorption target:** This file (in `PhenoSpecs/archive/records/`).
> **Reason for absorption:** Repo contained zero source code (`src/index.ts`
> was `// Entry point\nexport {};` - 26 bytes), zero consumers in the
> KooshaPari org (no imports of `@prism-ui/react`), and zero published
> packages. The only useful artefacts are these three design documents,
> preserved here as a historical record.
> **Audit reference:** Audit performed 2026-06-12. See
> `PhenoSpecs/specs/platform/019-private-repo-catalog/spec.md` for the
> corrected catalog entry.

---

## Why a real library was never built here

- The repo's stated purpose (minimal, accessible React component library) was
  duplicative of the `phenoDesign` / `phenodocs/packages/design/` work that
  already uses Radix UI + Tailwind + shadcn-style compound components.
- All three ADRs (Radix-UI, Tailwind-only, compound components) are now
  established org-wide decisions documented elsewhere.
- A real component library should be implemented in the canonical
  design-system home (`phenodocs/packages/design/`), not in a private
  archive husk.

---

## Preserved design documents (verbatim)

<details>
<summary><strong>PRD.md</strong> - product requirements</summary>

# PRD: prism — Minimal Accessible React Component Library

## Overview
`prism` is a minimal, accessible React component library with zero runtime CSS. It uses Tailwind classes directly for styling and meets WCAG 2.1 AA accessibility requirements. Components are tree-shakeable and fully typed with TypeScript.

## Problem Statement
Phenotype frontend applications need a shared component library. Existing libraries (MUI, Chakra) are large, opinionated on styling, and difficult to customize. Headless libraries (Radix, Headless UI) require wrapping for every use. `prism` provides ready-to-use, accessible components with zero CSS runtime overhead.

## Goals
1. WCAG 2.1 AA compliance for all interactive components
2. Zero runtime CSS (Tailwind only, no CSS-in-JS)
3. Tree-shakeable: import only what you use
4. Full TypeScript with polymorphic `as` prop support
5. Consistent, composable component API (compound component pattern)

## Epics

### E1: Form Components
- E1.1: Input (text, email, password, number, search)
- E1.2: Textarea
- E1.3: Select (native and custom)
- E1.4: Checkbox and CheckboxGroup
- E1.5: Radio and RadioGroup
- E1.6: Switch/Toggle
- E1.7: Form field wrapper (label, error, hint)

### E2: Overlay Components
- E2.1: Dialog/Modal (focus trap, scroll lock)
- E2.2: Drawer (slide-in panel)
- E2.3: Popover (positioned, with arrow)
- E2.4: Tooltip (hover + focus trigger)
- E2.5: DropdownMenu

### E3: Layout Components
- E3.1: Stack (vertical/horizontal spacing)
- E3.2: Grid (responsive grid layout)
- E3.3: Container (max-width centering)
- E3.4: Divider

### E4: Feedback Components
- E4.1: Alert/Banner (info, warning, error, success)
- E4.2: Toast notifications (with queue management)
- E4.3: Progress (bar and spinner)
- E4.4: Skeleton loader
- E4.5: Badge

### E5: Navigation Components
- E5.1: Button (primary, secondary, ghost, danger variants)
- E5.2: Link (with active state)
- E5.3: Tabs (keyboard navigable)
- E5.4: Breadcrumb
- E5.5: Pagination

### E6: Data Display
- E6.1: Table (sortable columns, row selection)
- E6.2: Avatar and AvatarGroup
- E6.3: Card
- E6.4: Tag/Chip


</details>

---

<details>
<summary><strong>FUNCTIONAL_REQUIREMENTS.md</strong> - accessibility, styling, TypeScript, dialog, forms, toasts, tree-shaking</summary>

# Functional Requirements: prism

## FR-PRS-001: Accessibility
FR-PRS-001a: All interactive components SHALL have correct ARIA roles, labels, and states.
FR-PRS-001b: All interactive components SHALL be keyboard navigable (Tab, Arrow keys, Enter, Escape).
FR-PRS-001c: Focus indicators SHALL be visible and meet WCAG 2.1 AA contrast requirements.
FR-PRS-001d: Screen reader announcements SHALL be correct for dynamic state changes (e.g., dialog open, toast added).

## FR-PRS-002: Styling
FR-PRS-002a: Components SHALL use only Tailwind utility classes for styling. No CSS-in-JS or CSS modules.
FR-PRS-002b: Components SHALL support a `className` prop for consumer overrides.
FR-PRS-002c: Components SHALL NOT inject any global styles or CSS variables at import time.
FR-PRS-002d: Tailwind classes used by prism SHALL be safe-listed in the consumer's Tailwind config via the `content` glob.

## FR-PRS-003: TypeScript
FR-PRS-003a: All components SHALL be typed with TypeScript. No `any` types in public APIs.
FR-PRS-003b: Polymorphic components (Button, Link) SHALL support an `as` prop with correct type inference.
FR-PRS-003c: Component props SHALL extend the native HTML element props they render (e.g., `InputProps` extends `React.InputHTMLAttributes<HTMLInputElement>`).

## FR-PRS-004: Dialog Component
FR-PRS-004a: `Dialog` SHALL trap focus within the dialog when open.
FR-PRS-004b: `Dialog` SHALL prevent body scroll when open.
FR-PRS-004c: `Dialog` SHALL close on Escape key press.
FR-PRS-004d: `Dialog` SHALL return focus to the trigger element on close.
FR-PRS-004e: `Dialog` SHALL have `aria-modal="true"` and `role="dialog"`.

## FR-PRS-005: Form Components
FR-PRS-005a: `Input`, `Textarea`, `Select`, `Checkbox`, `Radio`, `Switch` SHALL each have: `id`, `name`, `disabled`, `required`, `aria-invalid`, `aria-describedby` props.
FR-PRS-005b: `FormField` wrapper SHALL associate label with input via `htmlFor`/`id` linkage.
FR-PRS-005c: Error state SHALL be visually distinct and announced via `aria-live="polite"`.

## FR-PRS-006: Toast Notifications
FR-PRS-006a: `useToast()` hook SHALL return `{ toast, dismiss, dismissAll }` functions.
FR-PRS-006b: Toasts SHALL be rendered in a portal at the document root.
FR-PRS-006c: Toast queue SHALL be limited to 5 visible toasts; additional toasts replace the oldest.
FR-PRS-006d: Toasts SHALL be announced via `aria-live="assertive"` for errors and `aria-live="polite"` for others.

## FR-PRS-007: Tree-Shaking
FR-PRS-007a: Each component SHALL be importable independently: `import { Button } from "@prism-ui/react"`.
FR-PRS-007b: Importing `Button` SHALL NOT include `Dialog` in the bundle (verified by bundle analysis).
FR-PRS-007c: The library SHALL have `"sideEffects": false` in `package.json`.


</details>

---

<details>
<summary><strong>ADR.md</strong> - ADR-001 Radix UI, ADR-002 Tailwind CSS, ADR-003 compound components</summary>

# ADR: prism — React Component Library

## ADR-001: Radix UI Primitives as Accessibility Foundation

**Status**: Accepted

**Context**: Accessibility for complex components (Dialog, DropdownMenu, Popover, Tabs) requires extensive ARIA and keyboard handling. Build from scratch or use a headless primitive library?

**Decision**: Use Radix UI primitives as the unstyled, accessible foundation. prism wraps Radix primitives with Tailwind styling.

**Rationale**: Radix UI handles all ARIA patterns, focus management, and keyboard interactions correctly and is actively maintained. Building equivalent accessibility from scratch is error-prone and expensive. Wrapping is the correct pattern (aligns with Phenotype wrap-over-handroll mandate).

**Consequences**: Radix UI is a runtime dependency. prism is a styling layer over Radix, not a full reimplementation. If Radix makes breaking changes, prism adapters must be updated.

---

## ADR-002: Tailwind CSS over CSS-in-JS

**Status**: Accepted

**Context**: Styling options: CSS-in-JS (styled-components, Emotion), CSS Modules, Tailwind, vanilla-extract.

**Decision**: Tailwind utility classes exclusively. No CSS-in-JS.

**Rationale**: Zero runtime overhead (no style injection at runtime). Tailwind is already the Phenotype frontend standard. CSS-in-JS (Emotion/styled-components) adds 15-20KB runtime and SSR complexity. Tailwind classes are tree-shaken by the build tool naturally.

**Consequences**: Consumers must have Tailwind configured and must include prism's paths in their `content` config to avoid class purging.

---

## ADR-003: Compound Component Pattern

**Status**: Accepted

**Context**: Complex components (Dialog, Tabs, Select) can be designed as: (a) single monolithic component with props, (b) compound components (Dialog.Root, Dialog.Trigger, Dialog.Content).

**Decision**: Compound component pattern for multi-part components.

**Rationale**: Compound components give consumers control over DOM structure and placement. A single `<Dialog>` component cannot support every layout need. Compound components align with Radix UI's own API, reducing the conceptual gap between prism and Radix.

**Consequences**: More verbose usage for simple cases. Offset by flexibility and alignment with the underlying library.


</details>
