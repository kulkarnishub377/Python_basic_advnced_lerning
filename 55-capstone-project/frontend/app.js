/**
 * app.js - Vanilla JS Frontend logic for Capstone Task Manager
 */

const API_BASE = 'http://127.0.0.1:8000/api';

// DOM Elements
const views = document.querySelectorAll('.view-section');
const navItems = document.querySelectorAll('.nav-item');
const apiStatusIndicator = document.querySelector('.status-indicator');
const apiStatusText = document.getElementById('api-status-text');

// Modals
const taskModal = document.getElementById('task-modal');
const modalTitle = document.getElementById('modal-title');
const btnNewTask = document.getElementById('btn-new-task');
const btnCloseModal = document.getElementById('btn-close-modal');
const btnCancelModal = document.getElementById('btn-cancel-modal');
const btnSaveTask = document.getElementById('btn-save-task');

// Form inputs
const formId = document.getElementById('task-id');
const formTitle = document.getElementById('task-title');
const formDesc = document.getElementById('task-desc');
const formPriority = document.getElementById('task-priority');
const formStatus = document.getElementById('task-status');
const formAssignee = document.getElementById('task-assignee');

// Init
document.addEventListener('DOMContentLoaded', () => {
    checkApiHealth();
    loadDashboardStats();
    loadRecentTasks();
    loadAllTasks();

    // Setup navigation
    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = item.getAttribute('data-tab');
            
            navItems.forEach(n => n.classList.remove('active'));
            item.classList.add('active');
            
            views.forEach(v => v.classList.remove('active'));
            document.getElementById(`view-${targetId}`).classList.add('active');

            if(targetId === 'tasks') {
                loadAllTasks();
            } else {
                loadDashboardStats();
                loadRecentTasks();
            }
        });
    });

    document.getElementById('link-view-all').addEventListener('click', (e) => {
        e.preventDefault();
        document.querySelector('[data-tab="tasks"]').click();
    });

    // Filtering
    document.getElementById('filter-status').addEventListener('change', loadAllTasks);
    document.getElementById('filter-priority').addEventListener('change', loadAllTasks);
    document.getElementById('btn-clear-filters').addEventListener('click', () => {
        document.getElementById('filter-status').value = '';
        document.getElementById('filter-priority').value = '';
        loadAllTasks();
    });

    // Search
    let searchTimeout;
    document.getElementById('search-input').addEventListener('input', (e) => {
        clearTimeout(searchTimeout);
        const keyword = e.target.value.trim();
        searchTimeout = setTimeout(() => {
            if(keyword) {
                searchTasks(keyword);
                document.querySelector('[data-tab="tasks"]').click(); // switch to tasks view
            } else {
                loadAllTasks();
            }
        }, 500);
    });

    // Modal behavior
    btnNewTask.addEventListener('click', () => openModal());
    btnCloseModal.addEventListener('click', closeModal);
    btnCancelModal.addEventListener('click', closeModal);
    btnSaveTask.addEventListener('click', saveTask);
});

// --- API Functions ---

async function checkApiHealth() {
    try {
        const res = await fetch(`${API_BASE}/health`);
        if (res.ok) {
            apiStatusIndicator.className = 'status-indicator online';
            apiStatusText.textContent = 'API Online';
        } else {
            throw new Error('API degraded');
        }
    } catch (err) {
        apiStatusIndicator.className = 'status-indicator offline';
        apiStatusText.textContent = 'API Offline';
        console.error("Health check failed:", err);
    }
}

async function loadDashboardStats() {
    try {
        const res = await fetch(`${API_BASE}/dashboard`);
        const data = await res.json();
        
        document.getElementById('stat-total').textContent = data.total_tasks;
        document.getElementById('stat-pending').textContent = data.pending_tasks;
        document.getElementById('stat-completed').textContent = data.completed_tasks;
        document.getElementById('stat-high-priority').textContent = data.high_priority_count;
    } catch (err) {
        console.error("Failed to load stats", err);
    }
}

async function loadRecentTasks() {
    try {
        const res = await fetch(`${API_BASE}/tasks?limit=5`);
        const tasks = await res.json();
        const tbody = document.getElementById('recent-tasks-body');
        tbody.innerHTML = '';
        
        tasks.forEach(task => {
            tbody.appendChild(createTaskTableRow(task, false));
        });
    } catch (err) {
        console.error("Failed to load recent tasks", err);
    }
}

async function loadAllTasks() {
    const status = document.getElementById('filter-status').value;
    const priority = document.getElementById('filter-priority').value;
    
    let url = `${API_BASE}/tasks?limit=100`;
    if (status) url += `&status=${status}`;
    if (priority) url += `&priority=${priority}`;

    try {
        const res = await fetch(url);
        const tasks = await res.json();
        renderAllTasksTable(tasks);
    } catch (err) {
        console.error("Failed to load all tasks", err);
    }
}

async function searchTasks(keyword) {
    try {
        const res = await fetch(`${API_BASE}/tasks/search/${encodeURIComponent(keyword)}`);
        const tasks = await res.json();
        renderAllTasksTable(tasks);
    } catch (err) {
        console.error("Search failed", err);
    }
}

async function saveTask() {
    if (!formTitle.value.trim()) {
        alert("Title is required");
        return;
    }

    const payload = {
        title: formTitle.value.trim(),
        description: formDesc.value.trim(),
        priority: formPriority.value,
        assigned_to: formAssignee.value.trim() || null
    };

    const id = formId.value;
    let url = `${API_BASE}/tasks`;
    let method = 'POST';

    // If ID exists, it's an update
    if (id) {
        url = `${API_BASE}/tasks/${id}`;
        method = 'PUT';
        payload.status = formStatus.value;
    }

    try {
        const res = await fetch(url, {
            method: method,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (res.ok) {
            closeModal();
            loadDashboardStats();
            loadRecentTasks();
            if (document.getElementById('view-tasks').classList.contains('active')) {
                loadAllTasks();
            }
        } else {
            const data = await res.json();
            alert("Error saving: " + JSON.stringify(data));
        }
    } catch (err) {
        console.error("Save failed", err);
    }
}

async function deleteTask(id) {
    if (!confirm("Are you sure you want to delete this task?")) return;

    try {
        const res = await fetch(`${API_BASE}/tasks/${id}`, { method: 'DELETE' });
        if (res.ok || res.status === 204) {
            loadDashboardStats();
            loadRecentTasks();
            loadAllTasks();
        }
    } catch (err) {
        console.error("Delete failed", err);
    }
}

function editTask(task) {
    openModal(task);
}

// --- UI Helpers ---

function renderAllTasksTable(tasks) {
    const tbody = document.getElementById('all-tasks-body');
    tbody.innerHTML = '';
    
    if (tasks.length === 0) {
        tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;color:#6b7280;">No tasks found</td></tr>';
        return;
    }

    tasks.forEach(task => {
        tbody.appendChild(createTaskTableRow(task, true));
    });
}

function createTaskTableRow(task, showDesc = false) {
    const tr = document.createElement('tr');
    
    // Formatting badges
    const pBadge = `<span class="badge badge-${task.priority.toLowerCase()}">${task.priority}</span>`;
    const sBadge = `<span class="badge badge-${task.status.toLowerCase()}">${task.status.replace('_', ' ')}</span>`;
    // Assignee
    const assigneeHtml = task.assigned_to ? 
        `<div style="display:flex;align-items:center;gap:6px;"><div style="width:24px;height:24px;border-radius:50%;background:#e5e7eb;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:bold">${task.assigned_to.charAt(0).toUpperCase()}</div> ${task.assigned_to}</div>` 
        : '<span style="color:#9ca3af">Unassigned</span>';

    // Description (truncate if long)
    let descHtml = '';
    if (showDesc) {
        const truncated = task.description.length > 50 ? task.description.substring(0, 50) + '...' : task.description;
        descHtml = `<td style="color:#6b7280;font-size:0.9rem">${truncated}</td>`;
    }

    tr.innerHTML = `
        <td style="font-weight:500">${task.title}</td>
        ${descHtml}
        <td>${pBadge}</td>
        <td>${sBadge}</td>
        <td>${assigneeHtml}</td>
        <td>
            <div class="action-btns">
                <button class="btn-icon edit" onclick='editTask(${JSON.stringify(task).replace(/'/g, "&#39;")})'><i class="fa-solid fa-pen-to-square"></i></button>
                <button class="btn-icon delete" onclick='deleteTask(${task.id})'><i class="fa-solid fa-trash"></i></button>
            </div>
        </td>
    `;
    return tr;
}

function openModal(task = null) {
    taskModal.classList.add('active');
    if (task) {
        modalTitle.textContent = "Edit Task";
        formId.value = task.id;
        formTitle.value = task.title;
        formDesc.value = task.description || '';
        formPriority.value = task.priority.toLowerCase();
        formStatus.value = task.status.toLowerCase();
        formStatus.parentElement.style.display = 'block'; // Show status on edit
        formAssignee.value = task.assigned_to || '';
    } else {
        modalTitle.textContent = "Create New Task";
        formId.value = '';
        formTitle.value = '';
        formDesc.value = '';
        formPriority.value = 'medium';
        formStatus.value = 'pending';
        formStatus.parentElement.style.display = 'none'; // Hide status on create
        formAssignee.value = '';
    }
}

function closeModal() {
    taskModal.classList.remove('active');
}
