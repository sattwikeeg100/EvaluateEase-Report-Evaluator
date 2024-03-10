// Assuming a function `evaluateReport` exists on the server to process the report
// and return the result (replace with your actual logic)
function evaluateReport() {
    const reportText = document.getElementById('report-text').value;
  
    // Simulate sending the report text to the server for evaluation
    // (replace with actual communication with your backend)
    const evaluationResult = reportText.length % 2 === 0 ? 'PASS' : 'FAIL';
  
    // Update the displayed result on the page
    document.getElementById('result').textContent = evaluationResult;
  
    // You can update other elements based on the evaluation result (e.g., grade, score)
    // based on your logic and data received from the server
  }
  
  // Add event listener to the "Evaluate" button
  const evaluateButton = document.querySelector('.evaluation button');
  evaluateButton.addEventListener('click', evaluateReport);

  const searchInput = document.getElementById('search-topic');
const topicsList = document.querySelector('.topics-list');

searchInput.addEventListener('keyup', function() {
  const searchTerm = searchInput.value.toLowerCase(); // Make search case-insensitive
  const topicItems = topicsList.querySelectorAll('li');

  for (let i = 0; i < topicItems.length; i++) {
    const topicText = topicItems[i].textContent.toLowerCase();
    const topicLink = topicItems[i].querySelector('a');

    if (topicText.indexOf(searchTerm) !== -1) {
      topicLink.style.display = 'block'; // Show matching topics
    } else {
      topicLink.style.display = 'none'; // Hide non-matching topics
    }
  }
});

// Assuming you have data to populate the table dynamically (not included in this HTML example)
const tableBody = document.querySelector('.grade-cards tbody');

// Function to add a new grade card entry (replace with your actual data population logic)
function addGradeCard(id, authorName, topic, grade) {
  const tableRow = document.createElement('tr');

  const idCell = document.createElement('td');
  idCell.textContent = id;
  tableRow.appendChild(idCell);

  const authorNameCell = document.createElement('td');
  authorNameCell.textContent = authorName;
  tableRow.appendChild(authorNameCell);

  const topicCell = document.createElement('td');
  topicCell.textContent = topic;
  tableRow.appendChild(topicCell);

  const gradeCell = document.createElement('td');
  gradeCell.textContent = grade;
  tableRow.appendChild(gradeCell);

  tableBody.appendChild(tableRow);
}

// Sample usage (replace with your data source)
addGradeCard(7, 'Priya Das', 'Electric vs. Gasoline: A Comparative Analysis', 'B');
addGradeCard(8, 'Yash Kapoor', 'The Rise of SUVs', 'A');
