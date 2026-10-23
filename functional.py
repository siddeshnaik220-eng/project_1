"""Requirements specification: Student Academic Task Manager

Purpose
=======
Provide students with a simple application for maintaining academic tasks.
This specification describes the requested product behavior; items under
"Explicit assumptions" are proposals, not confirmed requirements.

Functional requirements
=======================
FR-1. The application shall let a student create an academic task.
FR-2. Each task shall have a unique ID, title, description, due date, priority,
     and completion status.
FR-3. The application shall let a student view the tasks in their task list
     and the details of each task, including its ID and all FR-2 fields.
FR-4. The application shall let a student update an existing task using its ID.
FR-5. The application shall let a student delete an existing task using its ID.
FR-6. The application shall distinguish a task with a known ID from a task
     that does not exist, and shall not silently report a failed operation as
     successful.
FR-7. An ID shall identify at most one task at a time. Updating a task shall
     retain its ID; deleting a task shall remove that task from subsequent
     views.

Non-functional requirements
===========================
NFR-1. Usability: CRUD actions and task fields shall be presented with clear,
       understandable labels and feedback.
NFR-2. Data integrity: a task operation shall not silently corrupt or
       misidentify another task; invalid input and failed saves shall be
       reported to the user.
NFR-3. Reliability: successfully saved task details shall be available after
       the application is restarted, if persistence is confirmed as required.
       (Persistence mechanism and recovery expectations are undecided.)
NFR-4. Performance: viewing and updating a normal student-sized task list
       should feel responsive. A measurable response-time target and maximum
       list size have not been specified.
NFR-5. Privacy and access: the application shall not expose task data beyond
       the intended audience. The intended audience, access controls, and
       deployment model must be decided before defining specific safeguards.

User stories
============
US-1. As a student, I want to create a task with its academic details so that
     I can keep track of work I need to do.
US-2. As a student, I want every task to have a unique ID so that I can refer
     to the exact task I intend to view, update, or delete.
US-3. As a student, I want to view my tasks and their details so that I can
     review my academic workload and deadlines.
US-4. As a student, I want to update a task so that I can correct its details
     or reflect a change in its completion status.
US-5. As a student, I want to delete a task I no longer need so that it is
     removed from my task list.
US-6. As a student, I want clear feedback when a task cannot be found or task
     details are invalid so that I can correct the problem.

Acceptance criteria
===================
Create
------
AC-C1. Given valid title, description, due date, priority, and an initial
       completion status, when the student creates a task, then the application
       creates and confirms one task containing those details.
AC-C2. The new task receives an ID that is unique among existing tasks; the ID
       is available when the task is viewed and when later CRUD actions target
       it.
AC-C3. If required details are missing or invalid under the agreed validation
       rules, the application explains the problem and does not create a
       partial task.

View
----
AC-R1. Given one or more tasks, when the student requests the task list, then
       each task is shown with its ID, title, description, due date, priority,
       and completion status.
AC-R2. Given no tasks, when the student requests the task list, then the
       application indicates that the list is empty.
AC-R3. Viewing tasks does not modify or delete any task.

Update
------
AC-U1. Given an existing task ID and valid revised details, when the student
       updates the task, then the same task reflects the revised details.
AC-U2. The updated task retains its original ID, and its other fields remain
       unchanged unless the student updates them.
AC-U3. The student can change the completion status to either incomplete or
       complete.
AC-U4. Given an unknown ID or invalid revised details, the application reports
       the error and leaves the stored task data unchanged.

Delete
------
AC-D1. Given an existing task ID, when the student confirms or submits the
       delete action, then that task is removed and the application confirms
       the result.
AC-D2. After deletion, the task no longer appears in the task list.
AC-D3. Given an unknown ID, the application reports that no matching task
       exists and does not delete another task.

Edge cases to handle or decide
==============================
* Empty or whitespace-only title; empty description.
* Invalid, ambiguous, or past due date; date format and timezone expectations.
* Priority missing or outside the allowed set; allowed priority values are
  currently unspecified.
* Completion status missing or not a recognized value; initial status/default
  is currently unspecified.
* Unknown, malformed, duplicate, or stale task ID.
* Two tasks with identical titles or otherwise identical details (their IDs
  must still distinguish them).
* Updating only one field, submitting unchanged values, or submitting no
  changes.
* Deleting the final task or viewing an empty list.
* Concurrent changes from more than one device or application instance.
* Storage unavailable, full, or containing malformed data.
* Very long text, special characters, and multiline descriptions.

Explicit assumptions (not confirmed requirements)
==================================================
* A student is the person using the application. No login, authentication,
  role, or identity provider is specified or assumed.
* "Maintain a list" may imply retaining tasks across restarts, but persistence
  is not explicitly stated. The storage mechanism and backup behavior are
  unspecified.
* Unique IDs are assumed to be generated by the application and stable for a
  task's lifetime; ID format and whether IDs may ever be reused are undecided.
* This specification does not assume sorting, filtering, reminders,
  notifications, task sharing, collaboration, recurring tasks, or subtasks.

Unanswered questions
====================
1. Is the task list personal to each student, shared by a class, or something
   else? How is the intended student/list identified without assuming login?
2. Must tasks persist after exit or restart? What storage, backup, and recovery
   behavior is expected?
3. Which priority values and ordering are required (for example, Low/Medium/
   High), and is there a default?
4. What date format, locale, timezone, and past-date rules should apply?
5. Are title and description required? What are their maximum lengths and
   allowed content?
6. What is the initial completion status for a new task?
7. Should deletion require confirmation, and can a deleted task be restored?
8. Should viewing support a particular order, search, or filtering?
9. What platforms and interface are required (command line, web, mobile, or
   desktop), and what accessibility requirements apply?
10. What are the expected number of students/tasks, response-time targets,
    concurrent-use needs, and privacy/security constraints?
"""