// Dashboard Statistics

fetch('/dashboard-stats')
.then(response => response.json())
.then(data => {

```
    document.getElementById("totalStudents").innerText =
        data.total_students;

    document.getElementById("presentToday").innerText =
        data.present_today;

    document.getElementById("absentToday").innerText =
        data.absent_today;

    document.getElementById("emailsSent").innerText =
        data.emails_sent_today;

    createPieChart(data);

    createBarChart(data);
});
```

// Pie Chart

function createPieChart(data) {

```
const pieCtx =
    document.getElementById("attendanceChart");

new Chart(pieCtx, {

    type: "doughnut",

    data: {

        labels: [
            "Present",
            "Absent"
        ],

        datasets: [{

            data: [
                data.present_today,
                data.absent_today
            ],

            backgroundColor: [
                "#16a34a",
                "#dc2626"
            ]

        }]
    },

    options: {

        responsive: true,

        plugins: {

            legend: {
                position: "bottom"
            }
        }
    }
});
```

}

// Bar Chart

function createBarChart(data) {

```
const barCtx =
    document.getElementById("attendanceBarChart");

new Chart(barCtx, {

    type: "bar",

    data: {

        labels: [
            "Present",
            "Absent",
            "Emails"
        ],

        datasets: [{

            label: "Statistics",

            data: [

                data.present_today,

                data.absent_today,

                data.emails_sent_today

            ],

            backgroundColor: [

                "#16a34a",

                "#dc2626",

                "#f59e0b"
            ]
        }]
    },

    options: {

        responsive: true,

        maintainAspectRatio: false
    }
});
```

}

// Recent Absentees Table

fetch('/absentees')
.then(response => response.json())
.then(data => {

```
    const tableBody =
        document.querySelector(
            "#absenteesTable tbody"
        );

    data.absentees.forEach(student => {

        const row = document.createElement("tr");

        row.innerHTML = `

            <td>${student.full_name}</td>

            <td>${student.roll_number}</td>

            <td>${student.attendance_date}</td>

        `;

        tableBody.appendChild(row);
    });
});
```
