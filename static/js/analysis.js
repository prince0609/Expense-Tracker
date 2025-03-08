
var chart;
      function displayChart() {
        // Sample data for Budget, Expense, and Savings (for 6 months)

        let year = document.getElementById("year").value;

        let profiles = JSON.parse(document.getElementById("data").innerText);

        let budgetData = [];
        let expenseData = [];
        let savingsData = [];
        let months = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
        let averageSpent = 0,
          averageSavings = 0;

        for (let profile of profiles) {
          if (profile.year == year) {
            budgetData.push(profile.budget);
            expenseData.push(profile.expense);
            savingsData.push(profile.savings);
            months[profile.month - 1] = 1;
            averageSpent += profile.expense;
            averageSavings += profile.savings;
          }
        }

        document.getElementById("averageSpent").innerText = (
          averageSpent / expenseData.length
        ).toFixed(0);
        document.getElementById("averageSavings").innerText = (
          averageSavings / savingsData.length
        ).toFixed(0);

        const months_name = [
          "Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "July",
          "Aug",
          "Sep",
          "Oct",
          "Nov",
          "Dec",
        ];
        labels = [];
        for (let month in months) {
          if (months[month]) {
            labels.push(months_name[month]);
          }
        }

        // Chart.js data object
        const data = {
          labels: labels, // Labels representing months
          datasets: [
            {
              type: "line", // Bar chart for Budget
              label: "Budget",
              backgroundColor: "#ffc107", // Blue
              borderColor: "#ffc107", // Blue border
              borderWidth: 1,
              data: budgetData,
            },
            {
              type: "line", // Bar chart for Expense
              label: "Expense",
              backgroundColor: "#dc3545", // Red
              borderColor: "#dc3545", // Red border
              borderWidth: 1,
              data: expenseData,
            },
            {
              type: "line", // Line chart for Savings
              label: "Savings",
              backgroundColor: "#198754", // Green
              borderColor: "#198754", // Green border
              borderWidth: 1,
              data: savingsData,
            },
          ],
        };

        // Chart.js configuration
        const config = {
          type: "line", // The main chart type (could be 'line' since we have both line and bar types)
          data: data,
          options: {
            responsive: false,
            plugins: {
              title: {
                text: `Budget vs Expense vs Savings (Monthly) - ${year}`,
                display: true,
              },
              legend: {
                position: "top",
              },
            },
            scales: {
              y: {
                beginAtZero: true, // Ensure the primary y-axis starts at 0
                title: {
                  display: true,
                  text: "Amount (₹)", // y-axis label for Budget and Expense
                },
              },
            },
          },
        };

        // Render the chart
        let area = document.getElementById("myChart");

        if (chart instanceof Chart) {
          chart.destroy();
        }

        chart = new Chart(area, config);
      }

      displayChart();