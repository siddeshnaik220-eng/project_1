# Student Academic Task Manager

## Overview

A simple application for students to maintain a list of academic tasks. Each
task has a unique ID, title, description, due date, priority, and completion
status. Students can create, view, update, and delete tasks.

This document records the product requirements. Items in **Assumptions** are
not confirmed requirements; decisions in **Open questions** need input from the
college or intended users.

## Functional requirements

- **FR-1 — Create:** Students can create an academic task.
- **FR-2 — Task details:** Each task has a unique ID, title, description, due
  date, priority, and completion status.
- **FR-3 — View:** Students can view their task list and see each task's ID and
  details.
- **FR-4 — Update:** Students can update an existing task by its ID.
- **FR-5 — Delete:** Students can delete an existing task by its ID.
- **FR-6 — Error handling:** The application distinguishes unknown task IDs
  from existing tasks, reports invalid input or failed operations, and does not
  report a failed operation as successful.
- **FR-7 — ID integrity:** An ID identifies at most one task at a time. Updating
  a task retains its ID. Deleting a task removes it from subsequent views.

## Non-functional requirements

- **NFR-1 — Usability:** Actions and task fields have clear labels and the
  application gives understandable feedback.
- **NFR-2 — Data integrity:** An operation does not silently corrupt or
  misidentify a task. Invalid input and failed saves are reported.
- **NFR-3 — Reliability:** If persistence is required, successfully saved
  tasks remain available after restart. The storage and recovery expectations
  are not yet specified.
- **NFR-4 — Performance:** Viewing and updating a normal student-sized list
  should feel responsive. A measurable response-time target and maximum list
  size are not yet specified.
- **NFR-5 — Privacy:** Task data is not exposed beyond its intended audience.
  The audience, access controls, and deployment model must be decided before
  specific safeguards can be defined.

## User stories

1. As a student, I want to create a task with its academic details so that I
   can keep track of work I need to do.
2. As a student, I want each task to have a unique ID so that I can refer to
   the exact task I intend to view, update, or delete.
3. As a student, I want to view my tasks and their details so that I can review
   my academic workload and deadlines.
4. As a student, I want to update a task so that I can correct its details or
   reflect a change in completion status.
5. As a student, I want to delete a task I no longer need so that it is removed
   from my task list.
6. As a student, I want clear feedback when a task cannot be found or its
   details are invalid so that I can correct the problem.

## Acceptance criteria

### Create

- **AC-C1:** Given valid task details, when a student creates a task, the
  application creates one task with those details and confirms success.
- **AC-C2:** The new task receives an ID unique among existing tasks. The ID is
  available when viewing and when performing later CRUD operations.
- **AC-C3:** If required details are missing or invalid under the agreed
  validation rules, the application explains the problem and does not create a
  partial task.

### View

- **AC-R1:** Given one or more tasks, when the student requests the list, each
  task is shown with its ID, title, description, due date, priority, and
  completion status.
- **AC-R2:** Given an empty list, the application indicates that there are no
  tasks.
- **AC-R3:** Viewing tasks does not modify or delete them.

### Update

- **AC-U1:** Given an existing task ID and valid revised details, updating the
  task changes that same task.
- **AC-U2:** An update retains the task's ID. Fields not changed by the student
  remain unchanged.
- **AC-U3:** The student can change completion status to either complete or
  incomplete.
- **AC-U4:** For an unknown ID or invalid revised details, the application
  reports an error and leaves the stored task data unchanged.

### Delete

- **AC-D1:** Given an existing task ID, submitting the delete action removes
  that task and the application confirms success.
- **AC-D2:** A deleted task no longer appears in the task list.
- **AC-D3:** For an unknown ID, the application reports that no matching task
  exists and does not delete another task.

## Edge cases to handle or decide

- Empty or whitespace-only title; empty description.
- Invalid, ambiguous, or past due date; date format and timezone expectations.
- Missing priority or a priority outside the allowed set.
- Missing or unrecognized completion status; default status for new tasks.
- Unknown, malformed, duplicate, or stale task ID.
- Tasks with identical titles or other details must still be distinguishable
  by their IDs.
- Updating only one field, submitting unchanged values, or submitting no
  changes.
- Viewing an empty list or deleting the final task.
- Concurrent changes from more than one device or application instance.
- Storage unavailable, full, or containing malformed data.
- Very long text, special characters, and multiline descriptions.

## Assumptions (not confirmed requirements)

- A student is the intended user. No login, authentication, role, or identity
  provider is specified or assumed.
- “Maintain a list” may imply retaining tasks across restarts, but persistence
  is not explicitly required. The storage mechanism and backup behavior are
  unspecified.
- IDs are assumed to be generated by the application and stable for the
  lifetime of a task. ID format and whether IDs may ever be reused are
  undecided.
- Sorting, filtering, reminders, notifications, task sharing, collaboration,
  recurring tasks, and subtasks are not included as requirements.

## Open questions

1. Is a task list personal to each student, shared by a class, or something
   else? How is the intended student or list identified without assuming
   authentication?
2. Must tasks persist after exit or restart? What storage, backup, and recovery
   behavior is expected?
3. Which priority values and ordering are required (for example, Low, Medium,
   High), and is there a default?
4. What date format, locale, timezone, and past-date rules should apply?
5. Are title and description required? What are their maximum lengths and
   allowed content?
6. What is the initial completion status for a new task?
7. Should deletion require confirmation, and can a deleted task be restored?
8. Should viewing support a particular order, search, or filtering?
9. Which platforms and interface are required (command line, web, mobile, or
   desktop), and what accessibility requirements apply?
10. What are the expected numbers of students and tasks, response-time targets,
    concurrent-use needs, and privacy/security constraints?
