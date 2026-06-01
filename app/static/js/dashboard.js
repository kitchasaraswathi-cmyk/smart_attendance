/**
 * Smart Attendance System (SAS) - Core Shared Client Component Orchestrator
 */

document.addEventListener("DOMContentLoaded", () => {
    initGlobalSearchEngine();
    initTeacherProfileDropdown();
    initNotificationBadgePolling();
});

/**
 * Universal Client-Side Real-Time Table Row Filter Engine
 */
function initGlobalSearchEngine() {
    const searchInput = document.getElementById("dashboardSearchInput");
    if (!searchInput) return;

    searchInput.addEventListener("input", (e) => {
        const query = e.target.value.toLowerCase().trim();
        const activeTable = document.querySelector(".ui-panel table, .table-responsive table");
        if (!activeTable) return;

        const rows = activeTable.querySelectorAll("tbody tr");
        rows.forEach(row => {
            // Do not hide empty data state placeholder text rows
            if (row.cells.length === 1 && row.cells[0].getAttribute("colspan")) return;
            
            const textContent = row.innerText.toLowerCase();
            row.style.display = textContent.includes(query) ? "" : "none";
        });
    });
}

/**
 * Top Navbar Faculty Profile Component Popup Dropdown Card Controller
 */
function initTeacherProfileDropdown() {
    const trigger = document.getElementById("profilePillTrigger");
    const menu = document.getElementById("profileDropdownMenu");

    if (!trigger || !menu) return;

    trigger.addEventListener("click", (e) => {
        e.stopPropagation();
        menu.classList.toggle("show");
        trigger.classList.toggle("active");
    });

    // Dismiss popover card context when clicking on background page layouts
    document.addEventListener("click", () => {
        menu.classList.remove("show");
        trigger.classList.remove("active");
    });
}

/**
 * Real-Time Polling Engine for Header Notifications Badge Count
 */
function initNotificationBadgePolling() {
    const badge = document.getElementById("notificationBadge");
    if (!badge) return;

    const executePoll = async () => {
        try {
            const response = await fetch('/notification-count');
            const data = await response.json();
            
            if (data.status === "success" && data.count !== undefined) {
                badge.textContent = data.count;
                badge.style.display = data.count > 0 ? "flex" : "none";
            }
        } catch (error) {
            console.warn("Telemetry polling connection drop:", error);
        }
    };

    // Initialize immediate execution and establish 10-second recurrence interval loop
    executePoll();
    setInterval(executePoll, 10000);
}

/**
 * Helper Utility Engine to Format Dates Safely inside Tables
 */
function formatSystemDate(dateString) {
    if (!dateString) return "—";
    try {
        const options = { year: 'numeric', month: 'short', day: '2-digit' };
        return new Date(dateString).toLocaleDateString('en-US', options);
    } catch (e) {
        return dateString;
    }
}