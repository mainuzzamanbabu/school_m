# CRUD Guide (Members + Notices)

This project now uses Django class-based generic views and simple Bootstrap templates
to provide full CRUD (Create, Read, Update, Delete) for the members and notice apps.

## 1) URLs and Routing

- All CRUD routes are listed directly in `core/urls.py` (no `include()`).
- You can see the paths for list, create, detail, update, delete in one file.

## 2) Members CRUD

- Model: `members/models.py` defines `Member`.
- Views: `members/views.py`
  - List: shows table + filter by `?type=teacher` or `?type=admin`
  - Create/Update: uses the same form template
  - Detail: shows one member
  - Delete: confirmation page
- Templates:
  - `templates/members.html` (list)
  - `templates/member_form.html` (create/update)
  - `templates/member_detail.html` (detail)
  - `templates/member_confirm_delete.html` (delete)

## 3) Notice CRUD

- Model: `notice/models.py` defines `Notice`.
- Views: `notice/views.py`
  - List, Create, Detail, Update, Delete (same pattern as members)
- Templates:
  - `templates/notice_list.html`
  - `templates/notice_form.html`
  - `templates/notice_detail.html`
  - `templates/notice_confirm_delete.html`

## 4) Database and Migrations

- A new migration exists: `notice/migrations/0001_initial.py`
- Apply it once:
  - `python manage.py migrate`

## 5) How to Use (Quick Demo)

- Members:
  - List: `/members/`
  - Create: `/members/create/`
  - Detail: `/members/1/`
  - Edit: `/members/1/edit/`
  - Delete: `/members/1/delete/`
- Notices:
  - List: `/notices/`
  - Create: `/notices/create/`
  - Detail: `/notices/1/`
  - Edit: `/notices/1/edit/`
  - Delete: `/notices/1/delete/`
